#!/usr/bin/python3

def _main() -> None:
    c, p, h = map(int,(input().split()))
    repartir = c-p
    repartidos = repartir//(h+1)
    sin_repartir = repartir-(repartidos*(h+1))
    print(p+sin_repartir)

if __name__ == '__main__':
    _main()