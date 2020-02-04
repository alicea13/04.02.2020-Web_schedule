import sys


summ = 0
par = sys.argv[1:]
if not par:
    print("NO PARAMS")
else:
    k = 1
    for i in range(len(par)):
        try:
            number = int(par[i]) * k
            summ += number
        except Exception as err:
            print(err.__class__.__name__)
            sys.exit(0)
        k *= -1
    print(summ)

