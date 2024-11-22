# Archive Compressor - ALG II
Algorithms assignment in archive compression using the LZW algorithm.

*UFMG, 2024*.

### Students
1. Ester Sara Assis 2021031785
2. Júlia Paes de Viterbo 2021032137

## Brief explanation
The present assignment implements an archive compressor which uses the LZW algorithm for Algorithms II course in Univerdade Federal de Minas Gerais. 

It takes an archive, compresses it and optionally tests the quality of this compression based on compression rate, number of elements stored and the memory space necessary for it, as well as regarding the total running time of the program. The tests made beforehand for evaluation matters are in the **report file (Relatorio.pdf)**, which also better explains the implementation of the method and gives an example of the code's functioning.


## How to use it
You will have to write a sentence like the following in the command line, where every <> represents a field to be completed:

*python3 main.py <mode> <input_file> <output_file> --max_bits <number> --variable_code --stats*

**mode**: can be either "compress" or "decompress";
**input_file**: name the input file with **.txt** (compress mode) or **.lzw** (decompress mode), there are examples *"origin0.txt"* and *"origin1.txt"*, *"origin0_compressed.lzw"* and *"origin1_compressed.lzw"*  in the directory;
**output_file**: name of the output file to be generated, **.lzw** (compress mode) or **.txt** (decompress mode);
**--max_bits <number> (opcional)**: sets the maximum number of bits, default is 12;
**--variable_code (opcional)**: enables variable number of bits during execution;
**--stats (opcional)**: exhibits the statistics after execution and saves it at the *Statistics* repository with the name <input_file>_<mode>_statistics.txt

Examples: 

1. compression: python3 main.py compress origin1.txt origin1_compressed.lzw --max_bits 12 --stats

2. decompression: python3 main.py decompress origin1_compressed.lzw origin1_decompressed.txt --max_bits 12 --stats