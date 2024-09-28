#!/usr/bin/python3

def _main() -> None:
    a, b, c = map(int,input().split())
    res = 0
    if not (a<b and b<c):
        res = 1
        if (a>c and c>b) or (b>a and a>c):
            res = 2
    print(res)

if __name__ == '__main__':
    _main()