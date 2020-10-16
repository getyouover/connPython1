# 两个数值的最大公约数
class Number:
    def minvalue(fir, sec):
        if fir >= sec:
            return sec
        else:
            return fir

    def result(self, temp_1, temp_2):
        smaller = Number.minvalue(temp_1, temp_2)
        result = 0
        for i in range(1,smaller+1):
            if (temp_1 % i == 0) and (temp_2 % i == 0):
                result = i

        print("{} 和 {} 最大公约数为：{}".format(temp_1, temp_2, result))


if __name__ == "__main__":
    try:
        a = int(input("请输入第一个数值:\n"))
        b = int(input("请输入第二个数值:\n"))
        n = Number()
        n.result(a,b)
    except ValueError:
        print("请输入正确的数值哟~~~~")