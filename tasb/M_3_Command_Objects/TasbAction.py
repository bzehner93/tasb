"""
Actionclass for tests and decorators. The action may be executed on given stream.
"""
class TasbAction():
    def __init__(self, command):
        self.command = command

    def executeWith(self, connection):
        connection.sendCommand(self.command)

    def __eq__(self, other):
        if isinstance(self, other.__class__):
            return self.command == other.command
        return False
