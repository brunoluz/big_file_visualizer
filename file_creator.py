import random
import string
import sys
from ipython_genutils.py3compat import xrange

if __name__ == '__main__':
    path = sys.argv[1]
    lines = sys.argv[2]

    # 20GB file: 1431655765 lines
    # 10GB file: 715827882 lines

    with open(path, 'w') as f:
        for i in range(1, int(lines) + 1):
            f.write(f"line {i} - xxxx\n")
            f.flush()
