# 打印乘法表格
class Table:
    def showout(self):
        for i in range(1,10):
            for j in range(1,i+1):
                print("{0} * {1} = {2}".format(i, j, i*j), end="\t")
            print('\n')
        print("乘法表格打印完毕，请多关照！~~~~")


if __name__ == "__main__":
    t = Table()
    t.showout()
