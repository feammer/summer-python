def multiTable():
    for i in range(1, 10):
        line = ""
        for j in range(1, i + 1):
            line = line + str(i) + "*" + str(j) + "=" + str(i * j) + " "
        print(line)


if __name__ == '__main__':
    multiTable()
