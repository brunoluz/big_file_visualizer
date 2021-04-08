class BigFileVisualizerFatalError(Exception):
    """Fatal exception class for big file visualizer exceptions"""

    def __init__(self, message):
        self.message = message


class BigFileVisualizerCustomError(Exception):
    """Custom exception class for big file visualizer exceptions"""

    def __init__(self, message):
        self.message = message
