import argparse
import traceback

from sys import stderr
from blessed import Terminal

from bfv_error import BigFileVisualizerFatalError
from big_file_handler import BigFileHandler

term = Terminal()

_lines_to_show = 11


def read_command():
    with term.cbreak():
        key = term.inkey()
        code = key.code

    if code == 259 or code == 339:  # arrow up / page up
        return "up", _lines_to_show

    elif code == 258 or code == 338:  # arrow down / page down
        return "down", _lines_to_show

    elif key == "l":
        print("which line? ")
        line_number = input()
        if line_number.isnumeric():
            return "goto", int(line_number)

    return "invalid", 0


if __name__ == '__main__':

    parser = argparse.ArgumentParser(description='Bigfile line visualizer tool')
    parser.add_argument('--file', '-f', dest='file', help='file to be opened', required=True)
    args = parser.parse_args()

    try:

        with BigFileHandler(args.file) as bfh:
            print("***big file visualizer***")
            print(f"Showing first {_lines_to_show} lines from {args.file}")

            lines_dict = bfh.get_next_lines(_lines_to_show)
            [print(f"line {i}: {lines_dict[i]}") for i in lines_dict.keys()]
            
            while True:
                command, lines = read_command()
                print(f"c {command}, l {lines}")

    except BigFileVisualizerFatalError as custom_error:
        print(custom_error.message, file=stderr)
    except KeyboardInterrupt:
        pass
    except:
        traceback.print_exc()
