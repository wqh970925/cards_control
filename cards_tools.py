# 建立一个列表用以保存用户的字典名片
card_list = []


def show_menu():
    print("*" * 50)
    print("1.新建名片")
    print("2.显示全部")
    print("3.查询名片")
    print("0.退出系统")
    print("*" * 50)


def new_card():
    print("您正在使用功能--新建名片")

    # 1.提示用户输入要添加的用户信息
    name = input("请输入要添加的用户姓名：")
    age = input("请输入要添加的用户年龄：")
    phone = input("请输入要添加的用户电话：")
    addr = input("请输入要添加的用户住址：")

    # 2.使用用户添加的信息建立名片字典
    card_dict = {"name": name,
                 "age": age,
                 "phone": phone,
                 "addr": addr}

    # 3.将建立的名片字典添加到列表中并显示
    card_list.append(card_dict)

    print(card_list)

    # 4.提示用户添加成功
    print("添加 %s 的名片成功！" % name)


def display_all():
    print("您正在使用功能--显示全部")

    # 判断是否为空的列表,若为空，提示用户并返回
    if len(card_list) == 0:
        print("现在无任何用户名片，请先添加数据！")

        # return关键字返回一个函数的执行结果，下方的代码不会被执行
        return

    # 输出表头
    for headers in ["姓名", "年龄", "电话", "地址"]:
        print(headers, end=" \t\t")

    print("")

    # 遍历输出用户名片信息
    for card_dict in card_list:
        print("%s \t\t%s \t\t%s \t\t%s \t\t" % (card_dict["name"],
                                                card_dict["age"],
                                                card_dict["phone"],
                                                card_dict["addr"]))


def search_card():
    print("您正在使用功能--查询名片")
    pass
