import sys


def solution(numb):
    n1, n2 = numb[1], numb[2]
    try:
        print(n1 + n2)
    except Exception:
        print(0)


numb = [int(i.strip()) for i in sys.argv()]
solution(numb)