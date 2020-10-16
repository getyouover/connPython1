# 判断数值是否是质数
class PrimeNumber:
    def panduan(self, a):
        for i in range(2, a):
            if a % i == 0:
                return False
            else:
                continue
        return True



if __name__ == "__main__":
    try:
        p = PrimeNumber()
        num = input("请输入数值： \n")
        num = int(num)
        if num == 1: print(" 1 不是质数")
        flag = p.panduan(num)
        if flag:
            print("{} 是质数".format(num))
        else:
            print("{} 不是质数".format(num))
    except ValueError:
        print("输入的数据不是整数，请重新输入哟~~~")