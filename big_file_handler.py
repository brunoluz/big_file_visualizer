import os
from bfv_error import BigFileVisualizerError

class BigFileHandler:

    def __init__(self, file):

        if not os.path.isfile(file):
            raise BigFileVisualizerError(f"Specified file is not valid file: {file}")

        self.file = file




