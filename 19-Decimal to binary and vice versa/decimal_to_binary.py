# 十进制到二进制  或 二进制到十进制

try:
    menu = int(input("选择一个选项:\n 1.十进制到二进制 \n 2.二进制到十进制 \n 输入:"))
    if menu < 1 or menu > 2:
        raise ValueError
    if menu == 1:
        dec = int(input("输入你的数字:"))
        print("二进制: {}".format(bin(dec)[2:]))
    if menu == 2:
        binary = input("输入你的数字: ")
        print("十进制: {}".format(int(binary, 2)))
except ValueError:
    print("请输入有效选项!")
