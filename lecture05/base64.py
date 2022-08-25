class MyBase64():
    base64_dict = {}
    string_temp = ('ABCDEFGHIJKLMNOPQRSTUVWXYZ'
                   'abcdefghijklmnopqrstuvwxyz'
                   '0123456789+/')
    ascii_string = ''.join([chr(i) for i in range(4, 2 ** 7 - 1)])

    def __init__(self, string):
        # 初始化，创建 base64 编码字典
        self.string = string
        for i in range(2 ** 6):
            self.base64_dict[i] = self.string_temp[i]

    def convert(self):
        # base64 编码过程

        # 编码
        string_encode_byte = self.string.encode('utf-8')
        # 十进制化
        string_digit_list = list(string_encode_byte)

        # 二进制化 + 0 填充
        string_bin_list = []
        for item in string_digit_list:
            string_bin_list.append(str(bin(item))[2:].zfill(8))

        # 字符串合并
        string_sum = ''.join(string_bin_list)

        # 6 的倍数，不足 0 填充
        string_fill = self.fillIt(string_sum, factor=6, item='0')

        # 切片，6位一个单位
        string_bin_list2 = self.splitIt(string_fill, bits=6)

        # 十进制化
        string_digit_list2 = []
        for item in string_bin_list2:
            string_digit_list2.append(int(item, 2))

        # 查表
        string_base64_list = []
        for item in string_digit_list2:
            string_base64_list.append(self.base64_dict[item])

        # 拼接
        string_sum2 = ''.join(string_base64_list)
        # 4 的倍数，不足填充 = 
        string_convert = self.fillIt(string_sum2, factor=4, item='=')

        return string_convert

    def fillIt(self, string, factor, item):
        """
        指定倍数填充指定字符
        string：原字符串
        factor：倍数
        item：填充字符
        """
        length = len(string)
        remainder = length % factor
        if remainder:
            times = factor - remainder
            string = string + times * item
        return string

    def splitIt(self, string, bits):
        """
        指定位数切片
        string：原字符串
        bits：每次切片数量
        """
        length = len(string)
        new_list = []
        for i in range(bits, length + 1, bits):
            new_list.append(string[i - bits:i])
            remain = length % bits
        if remain != 0:
            new_list.append(string[-remain:])
        return new_list


if __name__ == '__main__':
    test_string = '123abcABC测试（）()'
    try:
        myBase64 = MyBase64(test_string)
        string = myBase64.convert()
        print("测试字符串：{}".format(test_string))
        print("base64：{}".format(string))
    except:
        print("发生异常")