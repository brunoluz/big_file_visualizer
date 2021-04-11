# big file visualizer
A tool for visualize lines in big files.

## Prerequisites
1. Python 3.X installed.
2. Internet access to pypi.org to install dependencies.

## To configure environment
1. Download the code
2. Create virtual environment
3. Install packages

There are shells that will do the hard work for you.
- Windows: configure.bat
- Linux/MacOS: configure.sh

## To execute the application
- Windows (inside cmd)
1. Activate virtualenv: venv/Scripts/activate.bat
2. Run the application: python app.py -f [filename]
- Linux/MacOS: 
1. Activate virtualenv: source venv/bin/activate
2. Run the application: python app.py -f [filename]

## Usage and commands
1. Arrow Up - move one position up.
2. Arrow Down - move one position down.
3. Page Up - move eleven positions up.
4. Page Down - move eleven positions down.
5. l - goto line.
6. Ctrl+C - quit.

## Project Details
1. big_file_handler.py: Contains all the file navigation algorithm and logic.
2. app.py: provides a command line interface to use the big_file_handler.py.
3. file_creator.py: file creation tool used to test this application.
4. tests/test_*.py: unit tests to ensure the expected results from this application.

## Further considerations - Next steps
- Trying to make the 100 lines buffer work for small files (99 lines or less) has increased the code complexity and has no real value. This code could become more simpler if the buffer were used only for files bigger than 100 lines.
- The buffer is "feeded" while the pointer navigates through the file. To increase performance, the next version of this code could arrive in the wanted line and only after that feed the buffer. This approach will increase performance.
- To have great gains on performance, when the program starts, a background process could be started to map the line breaks on an index. Using an index would prevent reading the file from beginning every time a buffer is needed to load.