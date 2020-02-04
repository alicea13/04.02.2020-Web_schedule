import sys


class NumbException(Exception):
    pass


class EmptyError(NumbException):
    pass


s = [int(i.strip()) for i in sys.argv[1:] if i.strip().isdigit()]
try:
    if not s:
        raise EmptyError
    summ = 0
    count = 0
    for i in s:
        if int(i) == i:
            if count % 2 == 0:
                summ += i
            else:
                summ -= i
    print(summ)
except EmptyError:
    print("NO PARAMS")
except Exception as err:
    print(err)
