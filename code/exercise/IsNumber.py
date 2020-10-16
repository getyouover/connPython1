class Number:
    def is_number(self, a):
        try:
            float(a)
            return True
        except ValueError:
            pass

        try:
            import unicodedata
            unicodedata.numeric(a)
            return True
        except (TypeError, ValueError):
            pass

        return False


if __name__ == "__main__":
    temp = Number()
    num = input("请输入内容：\n")
    flag = temp.is_number(num)
    if flag:
        print("输入内容为纯数字！")
    else:
        print("很遗憾~~~ 输入的不是纯数字内容哟！")