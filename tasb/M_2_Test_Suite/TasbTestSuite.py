from TasbCommand import TasbCommand
from select import select

"""
The test suite object will hold all tests that should be executed for given testszenario. After adding
all desired tests to the suite run() may be called to start execution.
"""
class TasbTestSuite():
    def __init__(self, connection):
        self.connection = connection
        self.connection.setDelegate(self)
        self.stackableTestArray = []

    """
    Add a test object or stream decorator to the teststack. All objects have to comply to The
    stackableStreamObject interface.
    """
    def add(self, stackableStreamObject):
        self.stackableTestArray.append(stackableStreamObject)
        index = self.stackableTestArray.index(stackableStreamObject)
        if index - 1 == -1:
            pass
        else:
            self.stackableTestArray[index - 1].setChildObject(stackableStreamObject)
        return self

    def directChild(self):
        return self.stackableTestArray[0]

    def didParseCommand(self, command):
        self.directChild().didParseCommand(command)

    """
    MAIN-Loop of the program
    """
    def run(self):
        suitIsDone = False
        self.connection.open()
        while not suitIsDone:
            readable, writable, excepting = select([self.connection.getSocket()], [self.connection.getSocket()], [self.connection.getSocket()], 1)
            if self.connection.getSocket() in excepting:
                print(excepting)
            if self.connection.getSocket() in readable:
                self.connection.recvCommand()
            if self.connection.getSocket() in writable:
                self.directChild().connectionAvailableForWriting(self.connection)
