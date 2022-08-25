class Stu:
    def __init__(self,
                 name="",
                 age=0,
                 gender="",
                 chineseScore=0,
                 mathScore=0,
                 englishScore=0):
        self.name = name
        self.age = age
        self.gender = gender
        self.chineseScore = chineseScore
        self.mathScore = mathScore
        self.englishScore = englishScore

    def totalScore(self):
        return self.chineseScore + self.mathScore + self.englishScore

    def avgScore(self):
        return self.totalScore() / 3

    def showInfo(self):
        from string import Template
        t = Template("姓名：$name\n年龄：$age\n性别：$gender\n语文成绩：$cs\n数学成绩：$ms\n英语成绩：$es\n总成绩：$ts\n平均成绩：$avs\n")
        s = t.substitute(name=self.name, age=self.age, gender=self.gender,
                         cs=self.chineseScore, ms=self.mathScore, es=self.englishScore,
                         ts=self.totalScore(), avs=self.avgScore())
        print(s)


if __name__ == '__main__':
    student = Stu("alice", 18, 'female', 90, 91, 92)
    print(student.totalScore())
    print(student.avgScore())
    student.showInfo()
