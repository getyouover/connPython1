
class TVShow:
    def __init__(self, show):
        self.__show = show

    @property
    def show(self):
        return self.__show


class Fruit:
    color = None

    def __init__(self, color="绿色"):
        Fruit.color = color

    def hverst(self):
        print("水果是：" + Fruit.color + "的！")


class Apple(Fruit):
    def __init__(self):
        super().__init__()
        print("I am an Apple")


if __name__ == "__main__":
    TV = TVShow("齐天大圣")
    print("播放中："+TV.show)
    #print("播放中：" + TV.__show)
    print("播放中：" + TV._TVShow__show)
    print("播放中：" + str(TVShow.show))
    apple = Apple()
    apple.hverst()
