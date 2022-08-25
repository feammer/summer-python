def factorial(n):
    result = 1
    for i in range(1, n + 1):
        result *= i
        yield result


if __name__ == '__main__':
    for index, value in enumerate(factorial(20)):
        print("{}! = {}".format(index + 1, value))
