import os
from bfv_error import BigFileVisualizerFatalError, BigFileVisualizerCustomError


class BigFileHandler:

    def __init__(self, file):
        if not os.path.isfile(file):
            raise BigFileVisualizerFatalError(f"Specified file is not valid file: {file}")

        self._file = file
        self._opened_file = open(self.get_file(), 'rt')
        self._current_line = 1

        self._buffer = dict()  # line number, line content
        self._buffer_size = 100
        self._buffer_min_value = 0
        self._buffer_max_value = 0

    # enable working with "with" statement
    def __enter__(self):
        return self

    # destructor - releases the opened file
    def __exit__(self, exc_type, exc_value, exc_traceback):
        self._opened_file.close()

    def get_file(self):
        return self._file

    def load_buffer(self, line_start):

        self._buffer.clear()
        for position, line in enumerate(self._opened_file):

            if position in range(line_start - 1, line_start + self._buffer_size - 1, 1):
                self._buffer[position + 1] = line.rstrip(os.linesep)

            if position >= line_start + self._buffer_size - 1:
                break

        lines_in_buffer = self._buffer.keys()
        self._buffer_min_value = min(lines_in_buffer)
        self._buffer_max_value = max(lines_in_buffer)

    def get_next_lines(self, number_of_lines):

        if number_of_lines < 1 or number_of_lines > 100:
            raise BigFileVisualizerCustomError("Invalid request")

        if self._buffer_min_value <= self._current_line and \
                self._current_line + number_of_lines <= self._buffer_max_value:
            # values are in buffer
            pass
        else:
            self.load_buffer(self._current_line)

        return_value = dict()
        for i in range(self._current_line, self._current_line + number_of_lines, 1):
            return_value[i] = self._buffer[i]

        return return_value
