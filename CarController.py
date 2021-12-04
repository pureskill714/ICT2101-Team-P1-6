from Car import Car
import serial
import time

class CarController(Car):
    def __init__(self,name,pwd):
        super().__init__(name,pwd)
    """
    establish connection with the car
    input1: car name;
    input2: pwd;
    output: boolean;
    """
    def bluetoothSetUp(self):
        ser = serial.Serial()
        ser.port = "COM15"
        ser.baudrate = 9600
        ser.bytesize = serial.EIGHTBITS  # number of bits per bytes
        ser.parity = serial.PARITY_NONE  # set parity check: no parity
        ser.stopbits = serial.STOPBITS_ONE  # number of stop bits
        # ser.timeout = None          #block read
        ser.timeout = 1  # non-block read
        # ser.timeout = 2              #timeout block read
        ser.xonxoff = False  # disable software flow control
        ser.rtscts = False  # disable hardware (RTS/CTS) flow control
        ser.dsrdtr = False  # disable hardware (DSR/DTR) flow control
        ser.writeTimeout = 2  # timeout for write
        return ser

    def openConnection(self):
        ser = self.bluetoothSetUp()
        try:
            ser.open()
            return True, ser
        except:
            return False, "Open connection fail"


    def testConnection(self,ser):
        if ser[0]:
            if ser[1].isOpen():
                return True,ser[1]
            return False, "connection not open"
        return False, ser[1]

    def closeConnection(self):
        ser = self.bluetoothSetUp()
        ser.close()

    def sendCommand(self,ser,cmd):
        try:
            ser.flushInput()  # flush input buffer, discarding all its contents
            ser.flushOutput()  # flush output buffer, aborting current output
            # write data
            ser.write(str.encode(cmd))
            print(f"write data: {cmd}")

            time.sleep(1)  # give the serial port sometime to receive the data

            response = ser.readline()

            return True, response.decode('UTF-8')

        except Exception as e1:
            # msg[0] = False
            exception = "Exception happens: " + str(e1)
            return False,exception

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