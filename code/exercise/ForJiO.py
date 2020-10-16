# 判断输入数值为奇数还是偶数
class JiOu(object):
    def panduan(self, a):
        if a % 2 == 0:
            return True
        else:
            return False

    def result(self, flag,temp):
        if flag:
            print("{} 是偶数".format(temp))
        else:
            print("{} 是奇数".format(temp))


if __name__ == "__main__":
    J = JiOu()
    temp = input("请输入数据：\n")
    try:
        temp = int(temp)
        flag = J.panduan(temp)
        J.result(flag,temp)
    except ValueError:
        print("很遗憾！输入的数据不是整数哟！~~~~")