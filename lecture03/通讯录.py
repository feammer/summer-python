contact = {'name': {'tele': 'addr'}}


def insert():
    name = input("姓名: ")
    tele = input("电话: ")
    addr = input("地址: ")
    if contact.get(name) is not None:
        contact[name].update({tele: addr})
    else:
        contact[name] = {tele: addr}
    print("已添加联系人信息，姓名：{}，电话：{}，地址：{}".format(name, tele, addr))


def index():
    name = input("输入联系人姓名：")
    if contact.get(name) is None:
        print("{} 的信息不存在".format(name))
    else:
        info = list(contact[name].items())
        if len(info) > 1:
            print("存在多个联系人 {}".format(name))
            for i in info:
                print("电话：{}，地址：{}".format(i[0], i[1]))
        else:
            print("查找到 {} 的电话：{}，地址：{}".format(name, info[0][0], info[0][1]))


def delete():
    name = input("输入联系人姓名：")
    if contact.get(name) is None:
        print("联系人不存在")
    else:
        info = list(contact[name].items())
        if len(info) > 1:
            print("存在多个联系人 {}".format(name))
            for i in info:
                print("电话：{}，地址：{}".format(i[0], i[1]))
            tele = input("输入联系人电话: ")
            del contact[name][tele]
            print("已删除电话是 {} 的联系人 {}".format(tele, name))
        else:
            print("已删除联系人 {}".format(name))


def contactManage(mode):
    if mode == 0:
        return False
    elif mode == 1:
        insert()
        return True
    elif mode == 2:
        index()
        return True
    elif mode == 3:
        delete()
        return True
    else:
        print("无效的选项")
        return True


if __name__ == '__main__':
    from os import system

    hint ='''
   通讯录程序
退出程序    0
添加联系人   1
查找联系人   2
删除联系人   3
输入所需操作: '''
    while contactManage(int(input(hint))):
        # may cause encode problem in pycharm
        # system('pause')
        # system('cls')
        continue
