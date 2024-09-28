#!/usr/bin/python3

def _main() -> None:
    try:
        n = int(input())
        if n>= 0 and n<=10_000:
            total = 0
            n = int(n)
            for i in range(n):
                cantidad, precio = map(int, input().split())
                total = total + cantidad*precio
            print(total)
    except:
        print("Salida")

if __name__ == '__main__':
    _main()
    
# 1 3
# 2 5
# 3 15
# 8 45
# 2 31