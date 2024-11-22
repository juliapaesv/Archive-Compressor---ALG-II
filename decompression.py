import time

class Decompressor:
    def __init__(self, max_bits=12, variable_code=False):
        self.max_bits = max_bits
        self.variable_code = variable_code
        self.max_code_size = 2 ** max_bits
        self.dictionary = {}
        self.next_code = 256 
        self.statistics = {
            "decompression_time": 0,
            "dictionary_size": [],
        }

    def initialize_dictionary(self):
        self.dictionary = {i: chr(i) for i in range(256)}

    def decompress(self, input_file, output_file):
        start_time = time.time()

        self.initialize_dictionary()

        with open(input_file, 'rb') as infile, open(output_file, 'wb') as outfile:
            input_data = infile.read()
            code_size = (self.max_bits + 7) // 8
            codes = [
                int.from_bytes(input_data[i:i+code_size], 'big')
                for i in range(0, len(input_data), code_size)
            ]

            previous_string = ""
            for code in codes:
                if code in self.dictionary:
                    current_string = self.dictionary[code]
                elif code == self.next_code:
                    current_string = previous_string + previous_string[0]
                else:
                    raise ValueError("Código inválido na entrada")

                # saída
                outfile.write(current_string.encode('latin1'))

                if previous_string and self.next_code < self.max_code_size:
                    self.dictionary[self.next_code] = previous_string + current_string[0]
                    self.next_code += 1

                previous_string = current_string

        self.statistics["decompression_time"] = time.time() - start_time
        self.statistics["dictionary_size"] = len(self.dictionary)

    def get_statistics(self):
        return self.statistics
