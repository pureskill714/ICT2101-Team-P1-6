from CarController import CarController
import pytest

class TestClass:

    def test_instance(self):
        name = "1001"
        pwd = "123456"
        car = CarController(name,pwd)
        assert isinstance(car, CarController) == True

    def test_password(self):
        name = "1001"
        pwd = "123456"
        car = CarController(name,pwd)
        assert car.verifyPwd(pwd) == True

    def test_changepassword(self):
        name = "1001"
        pwd = "123456"
        car = CarController(name,pwd)
        invalidPwd = "21212"
        newPwd = "qwerty"
        assert car.changePwd(invalidPwd,newPwd) == False
        assert car.changePwd(pwd,newPwd) == True

    def test_statset(self):
        name = "1001"
        pwd = "123456"
        car = CarController(name,pwd)
        speed = "10m/h"
        dist = "12m"
        status = "Connected"
        state = "Idle"
        car.setCarStat(speed,dist,status,state)
        stat = car.getCarStat()
        assert stat['speed'] == speed
        assert stat['dist'] == dist
        assert stat['status'] == status
        assert stat['state'] == state

    def test_bluetoothSetup(self):
        name = "1001"
        pwd = "123456"
        car = CarController(name,pwd)
        port = "COM15" #change here
        con = car.bluetoothSetUp(port)
        assert con.port == port

    def test_openconnection(self):
        name = "1001"
        pwd = "123456"
        car = CarController(name,pwd)
        #port vaires from diff device, change accordingly
        invalidport = "COM15"
        validport = "COM9" #change here
        con = car.openConnection(invalidport)
        con1 = car.openConnection(validport)
        assert con[0] == False
        assert con[0] == True #when connection success

    def test_testconnection(self):
        name = "1001"
        pwd = "123456"
        car = CarController(name,pwd)
        validport = "COM15" #change here
        con = car.openConnection(validport)
        result = car.testConnection(con)
        # assert result[0] == False
        # assert result[1] == "Open connection fail"
        #ensure here
        assert result[0] == False
        assert result[1] == "connection not open"
        assert result[0] == True
        assert result[1].port == validport

    def test_sendCommand(self):
        name = "1001"
        pwd = "123456"
        car = CarController(name,pwd)
        validport = "COM15" #change here
        con = car.openConnection(validport)
        validcmd = "0" #change here
        invalidcmd = "@#$" #change here
        result = car.sendCommand(con,validcmd)
        assert result == True
        result = car.sendCommand(con,invalidcmd)
        assert result == False
