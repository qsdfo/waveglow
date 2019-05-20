import argparse
import os
import subprocess

from mel2samp import files_to_list

if __name__ == "__main__":
    # Get defaults so it can work with no Sacred
    parser = argparse.ArgumentParser()
    parser.add_argument('-f', "--filelist_path", required=True)
    parser.add_argument('-o', '--output_dir', type=str,
                        help='Output directory')
    args = parser.parse_args()

    filepaths = files_to_list(args.filelist_path)

    for filepath in filepaths:
        source_wav = filepath
        filename = os.path.basename(filepath)
        dest_wav = f'{args.output_dir}/{filename}'
        command = f'sox {source_wav} {dest_wav} remix 1,2 rate 22050'
        subprocess.run(command, shell=True)