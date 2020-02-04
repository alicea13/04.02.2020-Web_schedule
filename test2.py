import sys


print(f"my name is {sys.argv[0]}")
if len(sys.argv) > 1:
    print(f"first par {sys.argv[0]}, last par {sys.argv[-1]}")
else:
    print('NO PARAMENTRS')