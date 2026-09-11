for x in range(3):
    print("由于本程序错误处理不完善，请使用时请跟着指示做！！！")
e = int((input("计算次数是？ 警告：只能输入数字！")))
for _ in range (e):
    a = float(input("第一个数字"))
    b = float(input("第二个数字"))
    print(f"第一个数是{a},第二个数是{b}")
    print("如果数值正确，请按下回车键，否则请退出程序！")
    input("")        #空输入实现按任意键继续的功能
    c = input("1.加法 2.减法 3.乘法 4.除法 警告：只能填序号！")
    if c == "1": 
        d = a + b
        print(f"结果：{d}")
    if c == "2":
        d = a - b
        print(f"结果：{d}")
    if c == "3":
        d = a * b
        print(f"结果：{d}")
    if c == "4":
        if b == 0:
            print("发生除零错误，自动退出程序！")
            exit()
        d = a / b
        print(f"结果：{d}")
