import argparse
import os
from compression import Compressor
from decompression import Decompressor

def save_statistics(stats, filename, mode):
    os.makedirs("Statistics", exist_ok=True) 
    filepath = os.path.join("Statistics", f"{filename}_{mode}_stats.txt")
    with open(filepath, 'w') as f:
        for key, value in stats.items():
            f.write(f"{key}: {value}\n")
    print(f"Estatísticas salvas em {filepath}")

def main():
    # opções de linha de comando
    parser = argparse.ArgumentParser(description="Algoritmo LZW para compressão e descompressão.")
    parser.add_argument("mode", choices=["compress", "decompress"], help="Modo de operação")
    parser.add_argument("input_file", help="Arquivo de entrada")
    parser.add_argument("output_file", help="Arquivo de saída")
    parser.add_argument("--max_bits", type=int, default=12, help="Número máximo de bits (padrão: 12)")
    parser.add_argument("--variable_code", action="store_true", help="Usar tamanho de código variável")
    parser.add_argument("--stats", action="store_true", help="Exibir estatísticas do processo")

    args = parser.parse_args()

    file_extension = os.path.splitext(args.input_file)[1].lower()
    base_filename = os.path.basename(args.input_file).split('.')[0]

    if args.mode == "compress":
        compressor = Compressor(max_bits=args.max_bits, variable_code=args.variable_code)
        compressor.compress(args.input_file, args.output_file)
        if args.stats:
            save_statistics(compressor.get_statistics(), base_filename, "compress")
    elif args.mode == "decompress":
        decompressor = Decompressor(max_bits=args.max_bits, variable_code=args.variable_code)
        decompressor.decompress(args.input_file, args.output_file)
        if args.stats:
            save_statistics(decompressor.get_statistics(), base_filename, "decompress")

if __name__ == "__main__":
    main()