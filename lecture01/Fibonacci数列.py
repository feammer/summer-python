mem_fibo = [0, 1]
def fibo(n):
    if n == 0:
        return mem_fibo[0]
    elif n == 1:
        return mem_fibo[1]
    else:
        if len(mem_fibo) <= n:
            mem_fibo.extend([0 for i in range(n + 1 - len(mem_fibo))])
        if mem_fibo[n] == 0:
            mem_fibo[n] = fibo(n - 1) + fibo(n - 2)
        return mem_fibo[n]


if __name__ == '__main__':
    print("fibo(100)=" + str(fibo(100)))
