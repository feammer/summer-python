import datetime

if __name__ == '__main__':
    try:
        dateList = input("date (YYYY-MM-DD): ").split(sep='-')
        date = datetime.date(int(dateList[0]), int(dateList[1]), int(dateList[2]))
    except (ValueError,TypeError):
        print('invalid date')
        exit(-1)
    print("{}年{}月{}日是星期{}".format(date.year, date.month, date.day, date.isoweekday()))
    firstDay = datetime.date(int(dateList[0]), 1, 1)
    print("距离{}年{}月{}日有{}天".format(date.year, 1, 1, (date - firstDay).days))
