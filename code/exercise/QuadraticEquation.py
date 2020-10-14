a = float(input("请输入系数a：\n"))
b = float(input("请输入系数b：\n"))
c = float(input("请输入常数C：\n"))

d = b ** 2 - 4 * a * c

if d == 0:
    result1 = result2 = (-b)/(2 * a)
else:
    result1 = (-b + d**0.5)/(2*a)
    result2 = (-b - d**0.5)/(2*a)

print("二次方程的解分别为："+ str(result1) + " 和 " +str(result2))