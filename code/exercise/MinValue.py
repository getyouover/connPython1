# 两个数值的最小公倍数
class Number:
    def maxvalue(self, sec):
        if self > sec:
            return self
        else:
            return sec

    def result(self, arg1, arg2):
        target = Number.maxvalue(arg1,arg2)
        while True:
            if (target % arg1 == 0) and (target % arg2 == 0):
                result = target
                break
            target = target + 1
        return result


if __name__ == "__main__":
    try:
        first = int(input("请输入第一个数值：\n"))
        second = int(input("请输入第二个数值：\n"))
        n = Number()
        final_result = n.result(first, second)
        print("{} 和 {} 最小公倍数为 {}".format(first,second,final_result))
    except ValueError:
        print("数据输入有误，请输入正确的数值喔~~~~~")