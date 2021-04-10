import sys

if __name__ == '__main__':
    path = sys.argv[0]
    lines = sys.argv[1]

    with open(path, 'w') as f:
        for i in range(1, lines):
            f.write(f"line {i}")
