def palindrome(var):
    if type(var) == int:
        varList = []
        while var != 0:
            varList.append(var % 10)
            var = var // 10
        varLen = len(varList)
        for i in range(int(varLen - 1 / 2)):
            if varList[i] != varList[- 1 - i]:
                return False
        return True
    elif type(var) == str:
        varLen = len(var)
        for i in range(int(varLen - 1 / 2)):
            if var[i] != var[varLen - 1 - i]:
                return False
        return True
    else:
        print('invalid type')
        return None


if __name__ == '__main__':
    print('字符串回文结构:', 'qwerq', palindrome('qwerq'), 'didid', palindrome('didid'))
    print('数字回文结构:  ', 12345, palindrome(12345), 67876, palindrome(67876))
