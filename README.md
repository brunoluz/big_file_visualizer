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