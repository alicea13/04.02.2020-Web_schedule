import sys


try:
    numbs = sys.argv[1:]
    n1 = int(numbs[0])
    n2 = int(numbs[1])
    print(n1 + n2)
except Exception:
    print(0)