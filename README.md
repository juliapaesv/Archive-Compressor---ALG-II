# Archive-Compressor---ALG-II
Algorithms assignment in archive compression using the LZW algorithm.

*UFMG, 2024*.

### Students
1. Ester Sara Assis 2021031785
2. Júlia Paes de Viterbo 2021032137

## Breaf explanation
The present assignment implements an archive compressor which uses the LZW algorithm for Algorithms II course in Univerdade Federal de Minas Gerais. 

It takes an archive, compresses it and optionally tests the quality of this compression based on compression rate, number of elements stored and the memory space necessary for it, as well as regarding the total running time of the program. The tests made beforehand for evaluation matters are in the **report file (Relatorio.pdf)**, which also better explains the implementation of the method and gives examples of the code's functioning.


## How to use it
The program receives *three parameters after "python3 main.py"* to work properly: 
1. binary: *1* if the compression is to be tested regarding statistic performance (results are aggregated in the Statistics directory), *0* otherwise;
2. text: the name of one of the following archives in the Archives directory: *"origin0.txt" (text)*, *"origin1.txt" (text)*, *"" (bitmap image)*, *"" (bitmap image)*;
3. number (optional): number of bits used in the encoding *(9-12)*, *12 is the default value*.