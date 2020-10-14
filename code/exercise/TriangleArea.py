a = float(input("输入第一边长度：\n"))
b = float(input("输入第二边长度：\n"))
c = float(input("输入第三边长度：\n"))

d = (a + b + c)/2

result = (d * (d - a) * (d - b) * (d-c)) ** 0.5

print("三角形面积为：{0}".format(result))
