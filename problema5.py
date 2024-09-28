#!/usr/bin/python3
import math
def _main() -> None:
    n, u, d = map(int, input().split())
    minutos = math.ceil((n-u)/(u-d))*2 + 1
    print(minutos)

if __name__ == '__main__':
    _main()