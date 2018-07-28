from bluetooth import *
from TasbCommand import TasbCommand
"""
Connection object of the tasb library. This object is able to open a RFCOMM connection
given address port combination. Further the neccessary interfaces to read from and write to the connection a included.
"""
class TasbConnection:
    """
        # connectionAddress of the target RFCOMM service
        # servicePort of the target RFCOMM service
        # timeout for the socket
    """
    def __init__(self, connectionAddress, servicePort, timeOutSeconds):
        self.delegate = None
        self.socket = None
        self.servicePort = servicePort
        self.connectionAddress = connectionAddress
        self.timeOutSeconds = timeOutSeconds
        self.isLogging = False

    """
    set the connection delegate. will pass all socket events to the set delegate
    """
    def setDelegate(self, delegate):
        self.delegate = delegate

    def getSocket(self):
        return self.socket

    """
    when enabled, will log all traffic of the RCFOMM connection, default is False
    """
    def setCommandLoggingEnabled(self, enabled):
        self.isLogging = enabled

    def open(self):
        self.socket = BluetoothSocket(RFCOMM)
        self.socket.connect((self.connectionAddress, self.servicePort))
        self.socket.settimeout(self.timeOutSeconds)
        self.socket.setblocking(0)
    """
    public interface to communicate with the included socket
    """
    def sendCommand(self, command):
        self.writeToSocket(command.getCommandBytes())

    def recvCommand(self):
        data = self.readFromSocket()
        self.delegate.didParseCommand(TasbCommand(data))

    # Socket #
    def writeToSocket(self, bytesToSend):
        self.socket.send(bytesToSend)
        if self.isLogging:
            print(">>>", binascii.hexlify(bytesToSend))

    def readFromSocket(self, size = 1024):
        dataReceived = self.socket.recv(size)
        if self.isLogging:
            print("<<<", binascii.hexlify(dataReceived))
        return dataReceived
