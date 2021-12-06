from Car import Car
import serial
import time

class CarController(Car):
    def __init__(self,name,pwd):
        super().__init__(name,pwd)
    """
    set up bluetooth connection
    """
    def bluetoothSetUp(self,port):
        ser = serial.Serial()
        ser.port = port
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
    """
    open connection to communicate
    return boolean + object or error message
    """
    def openConnection(self,port):
        ser = self.bluetoothSetUp(port)
        try:
            ser.open()
            return True, ser
        except:
            return False, "Open connection fail"

    """
    open connection to communicate
    return boolean + object or error message
    """
    def testConnection(self,ser):
        if ser[0]:
            if ser[1].isOpen():
                return True,ser[1]
            return False, "connection not open"
        return False, ser[1]

    """
    close connection
    """
    def closeConnection(self,port):
        ser = self.bluetoothSetUp(port)
        ser.close()
        # print("conn closed")

    """
    sending command to car
    input1: communcation object
    input2: command
    return boolean + message
    """
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
    """
    use to get the data of car status
    """
    def getCarStat(self):
        stat = {}
        stat["status"] = Car.getStatus(self)
        stat["state"] = Car.getState(self)
        stat["dist"] = Car.getDist(self)
        stat["speed"] = Car.getSpeed(self)
        return stat
    """
    use to verify password
    input: password
    return boolean
    """
    def verifyPwd(self,pwd):
        if pwd == Car.getPwd(self):
            return True
        return False
    """
    use to change password
    input1: new password
    input2: old password
    return boolean
    """
    def changePwd(self,old,new):
        if self.verifyPwd(old):
            Car.setPwd(self,new)
            return True
        return False

