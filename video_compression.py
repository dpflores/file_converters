import os
import argparse
# sudo apt install ffmpeg

def convert(args):
    input_file= args.input
    output_file= args.output
    crf = 28 # higher crf reduces the file size 

    os.system(f'ffmpeg -i {input_file} -vcodec libx264 -crf {crf} {output_file}')

def main():
    parser = argparse.ArgumentParser()
    parser.add_argument('input', type=str, default='test.mp4',
                        help='What is the input file')
    parser.add_argument('output', type=str, default='test.webm',
                        help='What is the output file')

    args = parser.parse_args()

    convert(args)



if __name__ == '__main__':
    main()