# 阶乘
class Factorial:
    def result(self, a):
        total = 1
        if a == 0 : return total
        for i in range(1,a + 1):
            total = total * i

        return total


if __name__ == "__main__":
    try:
        f = Factorial()
        num = input("请输入数值：\n")
        num = int(num)
        if num < 0: print("很抱歉，负数没有阶乘！")
        result = f.result(num)
        print("{0} 的阶乘为：{1}".format(num, result))
    except ValueError:
        print("输入数值不是整数，请输入正确整数哟~~~~")