from TasbStackableTest import TasbStackableTest
from TasbStackableStreamObject import StreamObjektState
import time

"""
This test may be initialized with an action, condition and a title. The action will be
qued for execution when added to the teststack. The test will evaluate to SUCCESS upon
validation of the passed condition and print the result to the command line. While evaluating the
communcation traffic, this test object will not pass any read or write slots on.
"""
class TasbActionAndConditionTest(TasbStackableTest):
    def __init__(self, action, condition, title):
        super().__init__()
        self.action = action
        self.condition = condition
        self.queAction(self.action)
        self.title = title
        self.startTime = None

    def didParseCommand(self, command):
        if self.state == StreamObjektState.DONE:
            super().didParseCommand(command)
        elif self.condition != None and self.condition.accept(command):
            self.state = StreamObjektState.DONE
            print(self.title, 'did validate... SUCCESS')
        else:
            super().didParseCommand(command)

    def connectionAvailableForWriting(self, stream):
        if self.state != StreamObjektState.DONE and self.startTime != None and time.time() - self.startTime > 3:
            print(self.title, 'did time out... FAILURE')
            self.state = StreamObjektState.DONE

        # will execute qued actions
        super().connectionAvailableForWriting(stream)
        if self.state != StreamObjektState.DONE and self.state != StreamObjektState.BLOCKING:
            #after executing our actions we lock the writing until we are done
            self.state = StreamObjektState.BLOCKING
            self.startTime = time.time()
