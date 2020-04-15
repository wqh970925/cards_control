import cards_tools

while True:

    cards_tools.show_menu()

    action_str = input("请选择需要执行的操作: ")

    if action_str in ["1", "2", "3"]:

        # 新增名片
        if action_str == "1":
            cards_tools.new_card()

        # 显示全部
        elif action_str == "2":
            cards_tools.display_all()

        # 查询名片
        elif action_str == "3":
            cards_tools.search_card()

    elif action_str == "0":
        print("欢迎下次使用，再见！")
        break

    else:
        print("抱歉，您的输入有误请重新输入:")
