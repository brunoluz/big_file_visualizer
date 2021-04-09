import argparse
import traceback

from sys import stderr
from blessed import Terminal

from bfv_error import BigFileVisualizerFatalError
from big_file_handler import BigFileHandler

term = Terminal()

def read_command():

    with term.cbreak():
        key = term.inkey()
        code = key.code

    if code == 339:
        return "page_up", None

    elif code == 259:
        return "up", None

    elif code == 338:
        return "page_down", None

    elif code == 258:
        return "down", None

    elif key == "l":
        print("which line?")
        line_number = input()
        if line_number.isnumeric():
            return "goto", int(line_number)

    return "invalid", 0

def print_lines():
    lines_dict = bfh.get_lines()
    print("showing lines...")
    [print(f"line {i}: {lines_dict[i]}") for i in lines_dict.keys()]

if __name__ == '__main__':

    parser = argparse.ArgumentParser(description='Bigfile line visualizer tool')
    parser.add_argument('--debug', action='store_true')
    parser.add_argument('--file', '-f', dest='file', help='file to be opened', required=True)
    

    args = parser.parse_args()

    try:

        with BigFileHandler(args.file, args.debug) as bfh:
            print("***big file visualizer***")
            print_lines()

            while True:
                command, line = read_command()

                if command == "up":
                    bfh.up()
                elif command == "down":
                    bfh.down()
                elif command == "page_up":
                    bfh.page_up()
                elif command == "page_down":
                    bfh.page_down()
                elif command == "goto":
                    bfh.goto(line)

                if command != "invalid":
                    print_lines()

    except BigFileVisualizerFatalError as custom_error:
        print(custom_error.message, file=stderr)
    except KeyboardInterrupt:
        pass
    except:
        # traceback.print_exc()
        raise
