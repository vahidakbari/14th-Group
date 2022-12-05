

def factorial(n):
    cur,nex = 1, 1
    while nex <= n:
        cur = cur*nex
        nex = nex+1
    print(cur)


if __name__ == '__main__':
    factorial(100)