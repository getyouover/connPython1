# 判断输入年份数据是否是闰年
class RunYear:
    def run_year(self, year):
        if year % 4 == 0:
            if year % 100 == 0:
                if year % 400 == 0:
                    return True
                else:
                    return False
            else:
                return True
        else:
            return False


if __name__ == "__main__":
    try:
        r = RunYear()
        num = input("请输入年份：\n")
        num = int(num)
        flag = r.run_year(num)
        if flag:
            print("{} 年是闰年！".format(num))
        else:
            print("{} 年不是闰年！".format(num))
    except ValueError:
        print("输入年份不为整数，请输入正确的年份哟~~")