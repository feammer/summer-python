def guessNum():
    from random import randint
    realNum = randint(0, 30)
    cnt = 0
    while cnt < 5:
        guessNUm = int(input("猜测数字为: "))
        if guessNUm == realNum:
            print("猜对了")
            break
        elif guessNUm > realNum:
            print("太大了")
            cnt += 1
        else:
            print("太小了")
            cnt += 1
        print("剩余机会", 5 - cnt)


if __name__ == '__main__':
    guessNum()
