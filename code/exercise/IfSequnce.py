class Test:
    def method_1(self, a):
        print("正在运行方法1.........")
        if a > 0:
            print("输入数值大于零")
        elif a == 0:
            print("输入数值等于零")
        else:
            print("输入数值小于零")

    def method_2(self, a):
        print("正在运行方法2.........")
        if a >= 0:
            if a > 0 :
                print("输入数值大于零")
            else :
                print("输入数值等于零")
        else:
            print("输入数值小于零")


if __name__ == "__main__":
    try:
        temp = float(input("请输入数值：\n"))
        t = Test()
        t.method_1(temp)
        t.method_2(temp)
    except ValueError:
        print("输入非数值类型，请输入数值！感谢啦~~~~")