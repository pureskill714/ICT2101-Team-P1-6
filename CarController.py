from Car import Car
class CarController(Car):
    def __init__(self,name,pwd):
        super().__init__(name,pwd)
    """
    establish connection with the car
    input1: car name;
    input2: pwd;
    output: boolean;
    """
    def connection(self):
        if self.carName == "1001": #dummy testing
            return True
        else:
            return False
    '''
    use to set parameter of the car, data retrieve from adpator class
    input1: speed;
    inout2: distance;
    input3: connection status
    input4: state (moving, idle, pause)
    
    '''
    def setCarStat(self,speed,dist,status,state):
        Car.setSpeed(self,speed)
        Car.setDist(self,dist)
        Car.setStatus(self,status)
        Car.setState(self,state)

    def getCarStat(self):
        stat = {}
        stat["status"] = Car.getStatus(self)
        stat["state"] = Car.getState(self)
        stat["dist"] = Car.getDist(self)
        stat["speed"] = Car.getSpeed(self)
        # stat = [Car.getStatus(self),Car.getState(self),Car.getDist(self),Car.getSpeed(self)]
        return stat
# car = CarController("sasas","asasas")
# car.setCarStat("3m/h", "10.7m", "Connected","Idle")
# stat = car.getCarStat()
# print(stat)