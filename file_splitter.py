import os
import pandas as pd
from argparse import ArgumentParser


def splitter(file, *, size=100, output=".", sep=","):
    """Split file into <SIZE>-MB chunks to output folder."""
    with open(file) as f:
        file_rows = sum(1 for line in f)
    file_name, file_ext = file.rsplit(".", 1)
    file_size = os.stat(file).st_size / 1_000_000
    chunk_size = size * file_rows // file_size
    print(f"Splitting file into {round(file_size / size)} chunks by ~{size}MB...")

    chunks = pd.read_csv(file, sep=sep, iterator=True, chunksize=chunk_size)
    for i, chunk in enumerate(chunks, start=1):
        outname = f"{output}/{file_name}-chunk-{i}.{file_ext}"
        chunk.to_csv(outname, sep=sep, header=True, index=False)
        print(f"\t{outname} -> {chunk.size / 100_000}MB")


def parse_args():
    parser = ArgumentParser(description="Split file into <SIZE>-MB chunks to output folder.")
    parser.add_argument("-f", "--file", type=str, required=True, help="file name for splitting")
    parser.add_argument("-n", "--size", type=int, default=100, help="file chunk size in MB after splitting")
    parser.add_argument("-d", "--dir", type=str, default=".", help="directory to save chunks after splitting")
    parser.add_argument("-s", "--sep", type=str, default=",", help="file fields separator")
    return parser.parse_args()


def main():
    args = parse_args()
    splitter(args.file, size=args.size, output=args.dir, sep=args.sep)


if __name__ == '__main__':
    main()
