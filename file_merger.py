import os
import argparse


def merge_files(input_paths, output_path, separator="\n---\n"):
    with open(output_path, "w", encoding="utf-8") as outfile:
        for i, path in enumerate(input_paths):
            if not os.path.exists(path):
                print(f"Warning: {path} not found, skipping.")
                continue
            with open(path, "r", encoding="utf-8") as infile:
                outfile.write(infile.read())
            if i < len(input_paths) - 1:
                outfile.write(separator)
    print(f"Merged {len(input_paths)} files into {output_path}")


def main():
    parser = argparse.ArgumentParser(description="Merge multiple text files into one.")
    parser.add_argument("inputs", nargs="+", help="Input file paths")
    parser.add_argument("-o", "--output", required=True, help="Output file path")
    parser.add_argument("-s", "--separator", default="\n---\n", help="Separator between files")
    args = parser.parse_args()

    merge_files(args.inputs, args.output, args.separator)


if __name__ == "__main__":
    main()
