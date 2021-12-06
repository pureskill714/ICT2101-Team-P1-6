class Car:


    # instance attributes
    def __init__(self, name, pwd):
        self.carName = name
        self.__pwd = pwd
        self.status = "disconnect"
        self.state = ""
        self.speed = 0
        self.dist = 0

    def getSpeed(self):
        return self.speed

    def getStatus(self):
        return self.status

    def getDist(self):
        return self.dist

    def getState(self):
        return self.state

    def getPwd(self):
        return self.__pwd

    def setSpeed(self,speed):
        self.speed = speed

    def setDist(self,dist):
        self.dist = dist

    def setStatus(self,status):
        self.status = status

    def setState(self,state):
        self.state = state

    def setPwd(self,pwd):
        self.__pwd = pwd