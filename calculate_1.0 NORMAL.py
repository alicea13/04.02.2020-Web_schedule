import sys


try:
    numbs = sys.argv[1:]
    a, b = int(numbs[0]), int(numbs[1])
except Exception:
    print(0)