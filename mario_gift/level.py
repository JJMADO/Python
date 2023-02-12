import platform

FILE_DIR = "./levels/1.txt"
BG_DIR = "./levels/bg.gif"


class Level:
    pathLevel: str

    def __init__(self, path=FILE_DIR):
        self.pathLevel = path
        self.lines_of_level = []
        self.__load()
        self.platforms = []

    def __load(self):
        # TODO: реализовать метод загрузки из файла
        with open(self.pathLevel) as file:
            for line in file.readlines():
                self.lines_of_level.append(line[:-1])

    def getPlatform(self):
        # TODO: реализовать метод который будет отдавать объекты платформы
        x = y = 0
        for row in self.lines_of_level:
            for column in row:
                if column == "-":
                    pf = platform.Platform(x, y)
                    self.platforms.append(pf)
                elif column == "!":
                    bd = platform.BlockDie(x, y)
                    self.platforms.append(bd)
                elif column == "*":
                    tp = platform.Teleport(x, y, 50, 50)

                    x += platform.PLATFORM_WIDTH
                y += platform.PLATFORM_HEIGHT
                x = 0


    def get_pr(self, e, a):
        x = y = 0
        for row in self.lines_of_level:
            for column in row:
                if column == "p":
                    p = platform.Princess(x, y)
                    e.add(p)
                    a.add(e)
                    self.platforms.append(p)
                x += platform.PLATFORM_WIDTH
            y += platform.PLATFORM_HEIGHT
            x = 0


if __name__ == "__main__":
    l1 = Level()
    l1.getPlatform()
    print(l1.platforms)
