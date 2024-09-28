#!/usr/bin/python3

def _main() -> None:
    try:
        n = int(input())
        if n<1 or n>100:
            raise Exception
        numeros = (list(map(int, input().split())))
        n_max = max(numeros)
        print(numeros.count(n_max))
    except:
        print("0")

if __name__ == '__main__':
    _main()