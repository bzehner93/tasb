from TasbStackableStreamObject import TasbStackableStreamObject
from TasbCommand import TasbCommand
from TasbAction import TasbAction
from TasbStackableStreamObject import StreamObjektState
import time
import sys
"""
The decorators included in this class are intended to filter the incoming
traffic on the enstablished RFCOMM connection.
This decorator will filter the connection for the passed pingCommand and answer it with the defined ackCommand,
whithout passing ping commands further on.
"""
class TasbPingAcknowledgeDecorator(TasbStackableStreamObject):
    def __init__(self, pingCommand, ackCommand):
        super().__init__()
        self.pingCommand = pingCommand
        self.ackCommand = ackCommand
        self.timeSincePing = time.time()

    def didParseCommand(self, command):
        if (self.pingCommand == command) and (self.ackCommand != None):
            self.queAction(TasbAction(self.ackCommand))
            self.timeSincePing = time.time()
            return True
        else:
            return super().didParseCommand(command)
"""
The decorators included in this class are intended to filter the incoming
traffic on the enstablished RFCOMM connection.
Upon being assigned the first write slot on the RFCOMM socket this decorator
will activate and lock the the socket for the defined timeToWasteself.
Afterwards it becomes a passive member of the teststack.
"""
class TasbTestDelay(TasbStackableStreamObject):
    def __init__(self, timeToWaste):
        super().__init__()
        self.state = StreamObjektState.BLOCKING
        self.activationTime = None
        self.ttw = timeToWaste

    def connectionAvailableForWriting(self, stream):
        if self.state == StreamObjektState.PASSING:
            super().connectionAvailableForWriting(stream)
            return

        # business logic
        if self.activationTime != None:
            if time.time() - self.activationTime > self.ttw:
                # print("Streamlock expired... PASSING")
                self.state = StreamObjektState.PASSING
                pass
        elif self.state == StreamObjektState.BLOCKING:
            self.activationTime = time.time()
            # print("Streamlock activated... BLOCKING")
            pass

class TasbSuiteFinalizer(TasbStackableStreamObject):
    def connectionAvailableForWriting(self, stream):
        print('Done... exiting')
        sys.exit()
