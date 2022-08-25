def reverseStr(someStr="str"):
    str_array = list(someStr)
    str_array.reverse()
    return ''.join(str_array)


if __name__ == '__main__':
    print('!dlrow,olleH 解密为', reverseStr('!dlrow,olleH'))
