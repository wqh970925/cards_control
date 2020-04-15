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

    print("您正在使用功能[1]--新建名片")

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

    # 3.将建立的名片字典添加到列表中
    card_list.append(card_dict)

    # 4.提示用户添加成功
    print("添加 %s 的名片成功！" % name)


def display_all():

    print("您正在使用功能[2]--显示全部")

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

    print("您正在使用功能[3]--查询名片")

    # 1.提示用户要查找的姓名
    search_name = input("请输入要查找的用户名：")

    # 2.遍历名片列表，查找要搜索的名片字典，若没有找到提示用户
    for card_dict in card_list:

        if search_name == card_dict["name"]:

            print("用户信息已找到")
            print("姓名 \t\t年龄 \t\t电话 \t\t地址 \t\t")
            print("-" * 50)
            print("%s \t\t%s \t\t%s \t\t%s \t\t" % (card_dict["name"],
                                                    card_dict["age"],
                                                    card_dict["phone"],
                                                    card_dict["addr"]))

            # 针对找到的名片信息执行修改删除操作
            handle_card(card_dict)

            break

    else:
        print("未找到%s相关信息,请重新输入" % search_name)
        search_card()


def handle_card(search_dict):
    """处理查找到的名片

    :param search_dict:查找到的名片字典
    """
    action_str = input("请输入要执行的操作："
                       "[1]修改[2]删除[0]返回主菜单")

    if action_str == "1":

        search_dict["name"] = input_info(search_dict["name"], "姓名：")
        search_dict["age"] = input_info(search_dict["age"], "年龄：")
        search_dict["phone"] = input_info(search_dict["phone"], "电话：")
        search_dict["addr"] = input_info(search_dict["addr"], "地址：")

    elif action_str == "2":

        card_list.remove(search_dict)

        print("已删除名片信息！")


def input_info(dict_value, tip_message):
    """输入名片信息

    :param dict_value:字典中原有的值
    :param tip_message:输入提示
    :return:若用户输入了内容，就返回内容，反之，返回字典中原有的值
    """
    # 1.提示用户输入内容
    result_str = input(tip_message)

    # 2.针对用户输入的内容进行判断，若有输入内容，则返回输入结果
    if len(result_str) > 0:
        return result_str

    # 3.若无输入，则返回原名片信息
    else:
        return dict_value
