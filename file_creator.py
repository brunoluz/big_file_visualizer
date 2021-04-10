import os
import random
import string
import sys

from ipython_genutils.py3compat import xrange

if __name__ == '__main__':
    path = sys.argv[1]
    lines = sys.argv[2]

    with open(path, 'w') as f:
        for i in range(1, int(lines)):
            f.write(f"line {i} - {''.join(random.choice(string.ascii_lowercase) for _ in xrange(4))}\n")
