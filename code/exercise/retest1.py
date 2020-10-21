import re


def str_reverse():
    para = r'[\s|,]'
    string = "I am a good boy,"
    result = re.split(para, string)
    print(result)
    print(result[::-1])
    result_1=''
    print(type(result))
    for item in result[::-1]:
        result_1 = result_1+item+" "
    print(result_1)


def for_birthday():
    data = '510722210011011455'
    model = r'([0-9]{6})([12][0-9]{3}[01][0-9][0-3][0-9])'
    result_2 = re.search(model, data)
    print(result_2.group()[6:])

for_birthday()