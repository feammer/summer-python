def isPrime(num):
    from math import sqrt
    for i in range(2, int(sqrt(num)) + 1):
        if num % i == 0:
            return False
    return True


if __name__ == '__main__':
    primList = [i for i in range(101, 201) if isPrime(i)]
    print('101-200的素数有', len(primList), '个，分别为:', primList)