class Exchange:
    def change_1(self, x, y):
        print("使用中间变量方式：\n")
        temp = x
        x = y
        y = temp
        print("交换后的x的值为：{}".format(x))
        print("交换后的y的值为：{}".format(y))

    def change_2(self, x, y):
        print("无中间变量方式：\n")
        x, y = y, x
        print("交换后的x的值为：{}".format(x))
        print("交换后的x的值为：{}".format(x))

    def speak(self):

        print("hahaha, self 不需要传进来！")


if __name__ == "__main__":
    e = Exchange()
    x = float(input("请输入x值：\n"))
    y = float(input("请输入y值：\n"))
    e.change_1(x, y)
    e.change_2(x, y)
    e.speak()
