class Level:
    def __init__(self, name, num):
        self.__name = name
        self.__map = {}
        self.__levelnumber = num

    def setName(self,name):
        self.__name = name

    def setMap(self,start,end,map):
        self.__map["start"] = start
        self.__map["end"] = end
        self.__map["map"] = map

    def getName(self):
        return self.__name

    def getStart(self):
        return self.__map["start"]

    def getEnd(self):
        return self.__map["end"]

    def getMap(self):
        return self.__map["map"]

    def getLevelNumber(self):
        return self.__levelnumber;

class LevelController():

    def getMapSetUp(self,type):
        lv1 = Level("Level 1",1)
        map = [[1, 1, 0], [1, 0, 0], [0, 0, 1]]
        start = [0, 2]
        end = [2, 0]
        lv1.setMap(start, end, map)

        lv2 = Level("Level 2",2)
        map = [[1, 1, 0, 0, 1, 1], [0, 0, 0, 0, 1, 1], [1, 1, 1, 0, 0, 0]]
        start = [0, 1]
        end = [5, 2]
        lv2.setMap(start, end, map)

        lv3 = Level("Level 3",3)
        map = [[1,1,0,1,0,0],[1,1,0,1,0,1],[1,1,0,0,0,1],[1,1,0,1,1,1],[0,0,0,0,0,0], [1,1,0,1,1,1]]
        start = [5, 4]
        end = [5, 0]
        lv3.setMap(start, end, map)

        lv4 = Level("Level 4",4)
        map = [[0,0,1,1,1,1],[0,0,1,1,1,1],[0,0,1,1,1,1],[0,0,0,0,1,1],[0,0,0,0,0,0], [0,0,1,0,0,0]]
        start = [5, 5]
        end = [0, 0]
        lv4.setMap(start, end, map)

        lv5 = Level("Level 5",5)
        map = [[0,0,0,0,0,0],[1,1,1,1,1,0],[1,1,1,1,0,0],[1,1,0,0,0,1],[1,1,0,1,1,1], [0,0,0,0,0,0]]
        start = [5, 5]
        end = [0, 0]
        lv5.setMap(start, end, map)

        lv6 = Level("Level 6",6)
        map = [[0,1,1,0,0,0],[0,0,1,0,1,0],[1,0,1,0,1,0],[0,0,1,0,1,0],[0,1,0,0,0,1],[0,0,0,1,1,1]]
        start = [0, 0]
        end = [5, 3]
        lv6.setMap(start, end, map)

        cus1 = Level("Custom 1", 71)
        map = [[0,1,1,0,0,0],[0,0,1,0,1,0],[1,0,1,0,1,0],[0,0,1,0,1,0],[0,1,0,0,0,1],[0,0,0,1,1,1]]
        start = [0, 0]
        end = [5, 3]
        cus1.setMap(start, end, map)

        if type == "1":
            map = lv1
            return map
        elif type == "2":
            map = lv2
            return map
        elif type == "3":
            map = lv3
            return map
        elif type == "4":
            map = lv4
            return map
        elif type == "5":
            map = lv5
            return map
        elif type == "6":
            map = lv6
            return map
        elif type == "71":
            map = cus1
            return map
        else:
            return False

