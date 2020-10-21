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
    data = '510722199511011455'
    model = r'([1-2][0|9]{2}[0-9][0-9]{4})'
    result_2 = re.search(model, data)
    print(type(result_2))
    print(result_2)

for_birthday()