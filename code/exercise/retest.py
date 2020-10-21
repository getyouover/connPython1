import re
para = R'mr_\w+'
string = "MR_SHOP mr_shop"
match = re.match(para, string, re.I)
print("match方法：", match)
print("匹配值起始位置：", match.start())
print("匹配值结束位置：", match.end())
print("匹配位置的元组：", match.span())
print("匹配位置的字符串：", match.string)
print("匹配数据：", match.group())

match_1 = re.search(para, string, re.I)
print("search方法：", match_1)

match_2 = re.findall(para, string, re.I)
print("findall方法：", match_2)

partten = r'1[34579]\d{9}'
string_1 = "联系电话：13345678911"
result = re.sub(partten,'ahahahahaha',string_1)
print("替换结果：", result)