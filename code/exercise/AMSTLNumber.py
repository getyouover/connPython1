#阿姆斯特朗数 即：一个几位数的数值 等于 各个数位数字几次方的总和
class Number:
    def result_1(self, a):
        lenth = len(str(a))
        old = a
        total = 0
        while a >0:
            temp = a % 10
            total = total + temp**lenth
            a = a // 10
        if total == old:
            return True
        else:
            return False

    def result_2(self, a, b):
        print("{} ~ {} 范围内一下数字是阿姆斯特朗数：\n".format(a,b))
        for i in range(a, b+1):
            old = i
            n = len(str(i))
            total = 0
            while i > 0:
                temp = i % 10
                total = total + temp**n
                i = i // 10
            if total == old:
                print("{} 是阿姆斯特朗数".format(old))
            else:
                continue


if __name__ == "__main__":
    try:
        n = Number()
        num = input("请输入数值：\n")
        num = int(num)
        flag = n.result_1(num)
        if flag:
            print("{} 是阿姆斯特朗数".format(num))
        else:
            print("{} 不是阿姆斯特朗数".format(num))
        n.result_2(1,10000)
    except ValueError:
        print("请输入正确的整数哟~~~~")