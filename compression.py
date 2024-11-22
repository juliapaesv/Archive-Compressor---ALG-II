import os
import time
from trie import Trie

class Compressor:
    def __init__(self, max_bits=12, variable_code=False):
        self.max_bits = max_bits
        self.variable_code = variable_code
        self.max_code_size = 2 ** max_bits
        self.trie = Trie()
        self.next_code = 256  # usa-se o padrão
        self.statistics = {
            "compression_ratio": [],
            "dictionary_size": [],
            "execution_time": 0
        }

    def initialize_trie(self):
        for i in range(256):
            self.trie.insert(chr(i), i)

    def compress(self, input_file, output_file):
        start_time = time.time()

        self.initialize_trie()

        with open(input_file, 'rb') as infile, open(output_file, 'wb') as outfile:
            data = infile.read()
            current_string = ""
            output_codes = []

            for byte in data:
                symbol = chr(byte)
                new_string = current_string + symbol

                if self.trie.search(new_string) is not None:
                    current_string = new_string
                else:
                    
                    output_codes.append(self.trie.search(current_string))

                    if self.next_code < self.max_code_size:
                        self.trie.insert(new_string, self.next_code)
                        self.next_code += 1

                    current_string = symbol

            if current_string:
                output_codes.append(self.trie.search(current_string))

            # saída
            for code in output_codes:
                outfile.write(code.to_bytes((self.max_bits + 7) // 8, 'big'))

        # estatísticas
        self.statistics["execution_time"] = time.time() - start_time
        self.statistics["compression_ratio"] = len(data) / len(output_codes)
        self.statistics["dictionary_size"] = self.next_code

    def get_statistics(self):
        return self.statistics
