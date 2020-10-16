# 摄氏温度转换为华氏温度
class Change:

    def change_temp(self):

        result = self * 1.8 + 32
        print("输入摄氏度值为：{}，华氏温度为：{}".format(self, result))

    temp_1 = float(input("请输入摄氏度：\n"))
    change_temp(temp_1)
