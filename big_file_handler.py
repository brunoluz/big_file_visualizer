import os
from bfv_error import BigFileVisualizerFatalError, BigFileVisualizerCustomError


class BigFileHandler:

    def __init__(self, file, debug=False):
        if not os.path.isfile(file):
            raise BigFileVisualizerFatalError(f"Specified file is not valid file: {file}")

        self._debug = debug
        self._file = file  # file name
        self._opened_file = open(self._file, 'rt')  # opened file instance
        self._current_line = 1  # which line we are in
        self._skip_lines = 11  # page up/down
        self._buffer = dict()  # line number, line content
        self._buffer_reads = 0
        self._buffer_size = 100
        self._total_lines = None  # if we reached end of file, we will save the last line number

        self.load_buffer(self._current_line)

    # enable working with "with" statement
    def __enter__(self):
        return self

    # destructor - releases the opened file
    def __exit__(self, exc_type, exc_value, exc_traceback):
        if not self._opened_file.closed:
            self._opened_file.close()

    def get_current_line(self):
        return self._current_line

    def get_file(self):
        return self._file

    def get_buffer_min_value(self):
        return min(self._buffer.keys())

    def get_buffer_max_value(self):
        return max(self._buffer.keys())

    def get_total_lines(self):
        return self._total_lines

    def get_buffer_reads(self):
        return self._buffer_reads

    def up(self):
        # we move up only if possible
        if self._current_line > 1:
            self._current_line -= 1

    def down(self):
        self._current_line += 1

    def page_up(self):

        if self._current_line < self._skip_lines:
            self._current_line = 1
        else:
            self._current_line -= self._skip_lines

    def page_down(self):
        self._current_line += self._skip_lines

    def goto(self, line):
        if line > 0:
            self._current_line = line

    # will read first 100 lines if requested line less than 100.
    # will read last 100 file lines if requested line is 100 lines near the end
    # will read 40 lines before and 60 lines after requested line case two options above weren't satisfied.
    def load_buffer(self, requested_line):

        self._buffer.clear()
        self._opened_file.seek(0)
        self._buffer_reads += 1

        last_position = None

        for position, line in enumerate(self._opened_file):
            eof = True
            last_position = position
            self._buffer[position + 1] = line.rstrip(os.linesep)

            # clear previous lines outside buffer
            if position + 1 < requested_line - ((self._buffer_size / 2) - 1):
                self._buffer.pop(position + 1)

            # read next 50 lines from requested position
            if position >= requested_line + ((self._buffer_size / 2) - 1):
                eof = False  # not the end of file yet
                break

        if last_position is None:
            self._opened_file.close()
            raise BigFileVisualizerFatalError(f"Empty file: {self._file}")

        if eof:
            # we reached end of file
            # current line must be the last line minus lines to be shown.
            self._total_lines = last_position + 1
            self._current_line = self._total_lines - self._skip_lines

    def get_lines(self):

        # if requested line range is outside buffer, we need to load another buffer range.
        if self._current_line < min(self._buffer.keys()) or \
                self._current_line + self._skip_lines > max(self._buffer.keys()):
            self.load_buffer(self._current_line)

        return_value = dict()
        for i in range(self._current_line, self._current_line + self._skip_lines, 1):
            return_value[i] = self._buffer[i]

        return return_value
