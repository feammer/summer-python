import sqlite3

MENU_PROMPT = """
-- 电话簿 --
1) 添加联系人
2) 查找联系人
3) 删除联系人
4) 修改联系人
5) 查看全部联系人
0) 退出
输入选项: """

connector = sqlite3.connect('data.db')
cursor = connector.cursor()
cursor.execute(
    "CREATE TABLE IF NOT EXISTS CONTACTBOOK (Id INTEGER PRIMARY KEY, NAME TEXT, ADDRESS TEXT, PHONENUMBER INTEGER )")
connector.commit()


def menu():
    while (user_input := input(MENU_PROMPT)) != "0":
        if user_input == "1":
            global Name, Address, PhoneNumber
            Name = input("输入姓名: ")
            PhoneNumber = input("输入电话: ")
            Address = input("输入地址: ")

            connector = sqlite3.connect('data.db')
            cursor = connector.cursor()
            cursor.execute("INSERT INTO CONTACTBOOK (Name, Address, Phonenumber) VALUES (?, ?, ?)",
                           (Name, Address, PhoneNumber))
            connector.commit()


        elif user_input == "2":
            connector = sqlite3.connect('data.db')
            Name = input("输入姓名: ")
            cursor = connector.execute("SELECT * FROM CONTACTBOOK WHERE Name = ? ", [Name])
            fetch = cursor.fetchall()
            if fetch == []:
                print("查无此人!!!")
            else:
                print(f"共{len(fetch)}条结果")
                for data in fetch:
                    print(data)


        elif user_input == "3":
            connector = sqlite3.connect('data.db')
            cursor = connector.cursor()
            Name = input("输入需要删除的联系人姓名: ")
            cursor = connector.execute("SELECT * FROM CONTACTBOOK WHERE Name = ? ", [Name])
            fetch = cursor.fetchall()
            if fetch == []:
                print("查无此人!!!")
            elif len(fetch) == 1:
                cursor.execute("DELETE FROM CONTACTBOOK WHERE Name = ? ", [Name])
                connector.commit()
                print(f"{Name} 已经删除")
            else:
                print(f"共{len(fetch)}条结果，选择联系人ID")
                for data in fetch:
                    print(data)
                Id = input("输入需要删除的联系人ID: ")
                cursor.execute("DELETE FROM CONTACTBOOK WHERE Id = ? ", [Id])
                connector.commit()
                print(f"{Name} 已经删除")



        elif user_input == "4":
            connector = sqlite3.connect('data.db')
            cursor = connector.execute("SELECT * FROM CONTACTBOOK")
            fetch = cursor.fetchall()
            for data in fetch:
                print(data)

            cursor = connector.cursor()
            Id = input("输入现有联系人Id: ")
            Name = input("输入新姓名: ")
            PhoneNumber = input("输入新电话: ")
            Address = input("输入新地址: ")
            cursor.execute(
                "Update CONTACTBOOK SET Name = ? , Address = ?, PhoneNumber = ? WHERE ID= ?  ",
                [Name, Address, PhoneNumber, Id])

            connector.commit()
            print(f"联系人信息已修改")

        elif user_input == "5":
            connector = sqlite3.connect('data.db')
            cursor = connector.execute("SELECT * FROM CONTACTBOOK")
            fetch = cursor.fetchall()

            for data in fetch:
                print(data)

        else:
            print("无效的选项")
        print("-----------")


if __name__ == '__main__':
    menu()
    connector.close()
