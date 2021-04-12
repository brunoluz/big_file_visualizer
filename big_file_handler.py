import os
from bfh_error import BigFileVisualizerFatalError


class BigFileHandler:

    def __init__(self, file):
        if not os.path.isfile(file):
            raise BigFileVisualizerFatalError(f"Specified file is not valid file: {file}")

        self._file = file  # file name
        self._opened_file = open(self._file, 'rt')  # opened file instance
        self._current_line = 1  # which line we are in
        self._skip_lines = 11  # page up/down or lines to be retrieved
        self._buffer = dict()  # line number, line content
        self._buffer_reads = 0  # how many times the buffer was "fed"
        self._buffer_size = 100
        self._total_lines = None  # if we reached end of file, we will save the last line number

        self.load_buffer()

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
        # safety checks to safely move down
        if self._total_lines is None:
            self._current_line += 1
        elif self._current_line <= self._total_lines - self._skip_lines:
            self._current_line += 1

    def page_up(self):
        if self._current_line < self._skip_lines:
            self._current_line = 1
        else:
            self._current_line -= self._skip_lines

    def page_down(self):
        # safety checks to safely move down
        if self._total_lines is None:
            self._current_line += self._skip_lines
        elif self._current_line + self._skip_lines < self._total_lines:
            self._current_line += self._skip_lines
        elif self._current_line + self._skip_lines >= self._total_lines:
            self._current_line = self._total_lines - self._skip_lines + 1

    def goto(self, line):
        if self._skip_lines < 11:
            self._current_line = 1
            return

        if line < 1:
            self._current_line = 1
        else:
            if self._total_lines is None:
                self._current_line = line
            else:
                if self._total_lines == 1:
                    self._current_line = 1
                elif line <= self._total_lines - self._skip_lines + 1:
                    self._current_line = line
                else:
                    self._current_line = self._total_lines - self._skip_lines
                    if self._current_line < 1:
                        self._current_line = 1

    def load_buffer(self):

        self._buffer.clear()
        self._opened_file.seek(0)  # start from file beginning
        self._buffer_reads += 1

        last_position = None
        for position, line in enumerate(self._opened_file):
            eof = True
            last_position = position
            self._buffer[position + 1] = line.rstrip(os.linesep)

            # clear previous lines outside buffer
            if position + 1 < self._current_line - (int(self._buffer_size / 2) - 1):
                self._buffer.pop(position + 1)

            # read next 50 lines from requested position
            if position >= self._current_line + (int(self._buffer_size / 2) - 1):
                eof = False  # not the end of file yet
                break

        if last_position is None:
            # we tried to open an empty file
            self._opened_file.close()
            raise BigFileVisualizerFatalError(f"Empty file: {self._file}")

        if eof:
            # we reached end of file
            # current line must be the last line minus lines to be shown.
            self._total_lines = last_position + 1

            # handling small files
            if self._buffer_size > self._total_lines:
                self._buffer_size = self._total_lines
            if self._skip_lines > self._total_lines:
                self._skip_lines = self._total_lines
            if self._buffer_size == self._skip_lines or self._total_lines - self._current_line < self._skip_lines:
                self._current_line = self._total_lines - self._skip_lines + 1

    def get_lines(self):

        if self._skip_lines == 11:
            # only load buffer if lines to show are equal to 11. If it is different, it
            # means we are trying to open a less than 11 lines file.

            if self._current_line < self.get_buffer_min_value() or \
                    self._current_line + self._skip_lines - 1 > self.get_buffer_max_value():
                # if requested line range is outside buffer, we need to load another buffer range.
                self.load_buffer()

        # retrieve lines from buffer
        return_value = dict()
        i = self._current_line
        while True:
            return_value[i] = self._buffer[i]
            i += 1
            if i >= self._current_line + self._skip_lines or i not in self._buffer:
                break

        return return_value
