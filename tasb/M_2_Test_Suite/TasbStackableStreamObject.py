from enum import Enum

"""
Enum defining all possible states of stream objects in the
teststack of the testsuite.
"""
class StreamObjektState(Enum):
    # Object is passing all read and write slots
    PASSING = 1
    # Object is fully executed and behaves like PASSING state
    DONE = 2
    # Object is evaluating the communication stream and will not pass read or write slots
    BLOCKING = 3

"""
Basic interface for all objects that should be included into the
teststack of an test suite instance.
"""
class TasbStackableStreamObject():
    def __init__(self):
        self.childObject = None
        self.actionQue = []
        self.state = StreamObjektState.PASSING

    def setChildObject(self, stackableTest):
        self.childObject = stackableTest

    """
    Ques an action for execution. the stream object will consume write slots until all
    actions are executed.
    """
    def queAction(self, action):
        self.actionQue.append(action)

    def executeNextActionWith(self, stream):
        nextAction = self.nextAction()
        if nextAction != None:
            nextAction.executeWith(stream)
            self.actionQue.remove(nextAction)
            return True
        else:
            return False

    def nextAction(self):
        if len(self.actionQue) > 0:
            return self.actionQue[0]
        else:
            return None

    """
    Interface of all stackable stream objects. Needs to be implemented by
    all subclasses in order to be able to be added to the teststack of the test suite.
    """
    def didParseCommand(self, command):
        if self.childObject != None:
            self.childObject.didParseCommand(command)
        else:
            return False

    def connectionAvailableForWriting(self, stream):
        if self.executeNextActionWith(stream) or self.state == StreamObjektState.BLOCKING:
            pass
        elif self.childObject != None:
            return self.childObject.connectionAvailableForWriting(stream)
        else:
            return False
