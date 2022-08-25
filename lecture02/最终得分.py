def finalScore():
    score = [9, 9, 8.5, 10, 7, 8, 8, 9, 8, 10]
    score.sort()
    score.pop(9)
    score.pop(0)
    score.append(9)
    return sum(score) / len(score)


if __name__ == '__main__':
    print("最终得分:", finalScore())
