import os
import argparse



def convert(args):
    input_file= args.input
    output_file= args.output

    os.system(f'ffmpeg -i {input_file} -vf "fps=10,scale=620:-1:flags=lanczos,split[s0][s1];[s0]palettegen[p];[s1][p]paletteuse" -loop 0 {output_file}')

def main():
    parser = argparse.ArgumentParser()
    parser.add_argument('input', type=str, default='test.webm',
                        help='What is the input file')
    parser.add_argument('output', type=str, default='test.gif',
                        help='What is the output file')

    args = parser.parse_args()
    convert(args)

if __name__ == '__main__':
    main()