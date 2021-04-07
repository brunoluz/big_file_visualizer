import argparse
import traceback

from sys import stderr
from blessed import Terminal

from bfv_error import BigFileVisualizerError
from big_file_handler import BigFileHandler

term = Terminal()


def read_command():

    with term.cbreak():
        key = term.inkey()
        code = key.code

    if code == 259 or code == 339:  # arrow up / page up
        return "up", 11

    elif code == 258 or code == 338:  # arrow down / page down
        return "down", 11

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
        bfh = BigFileHandler(args.file)

        while True:
            command, lines = read_command()
            print(f"c {command}, l {lines}")

    except BigFileVisualizerError as custom_error:
        print(custom_error.message, file=stderr)
    except KeyboardInterrupt:
        pass
    except:
        traceback.print_exc()
