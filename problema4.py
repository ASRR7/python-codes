#!/usr/bin/python3

def _main() -> None:
    d = []
    for i in range(3):
        n1, n2 = map(int, input().split())
        d.append(abs(n1 - n2))
    print(d[0]+d[1]+d[2])

if __name__ == '__main__':
    _main()