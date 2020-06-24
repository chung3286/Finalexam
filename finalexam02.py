import math

class Point():
    __x = 0
    __y = 0
    def __init__(self, x, y): 
        self.__x = x
        self.__y = y
    def distance(self, z, w):
        dist = math.sqrt((self.__x-z)**2 + (self.__y - w)**2)
        return dist
    def __add__(self, other):
        return (self.__x + other.z, self.__y + other.w)

if __name__ == "__main__":
    Point.__init__(1,1)
    print(Point.distance(2,2))
    print(Point.__add__())