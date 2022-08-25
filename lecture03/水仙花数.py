def num2list(var):
    varList = []
    while var != 0:
        varList.append(var % 10)
        var = var // 10
    return varList


def narcissisticNum():
    result = []
    for i in range(100, 1000):
        numList = num2list(i)
        if i == numList[0] ** 3 + numList[1] ** 3 + numList[2] ** 3:
            result.append(i)
    print("100-1000的水仙花数", result)


if __name__ == '__main__':
    narcissisticNum()