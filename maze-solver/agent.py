from collections import namedtuple

class Agent:
    __score = 0
    __x = 0
    __y = 0

    def __init__(self, x, y):
        self.__x = x
        self.__y = y

    def getScore(self):
        return self.__score

    def updateScore(self, score):
        self.__score += score

    def getPosition(self):
        return namedtuple("position", ["x", "y"])(self.__x, self.__y)

    def setPosition(self, x, y):
        self.__x = x
        self.__y = y
