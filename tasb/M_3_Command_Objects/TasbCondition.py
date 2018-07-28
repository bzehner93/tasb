import re
"""
Conditionclass for tests and decorators. The passed condition may be evaluated against any received data.
""""
class TasbCondition():
    def __init__(self, command):
        self.command = command

    def accept(self, command):
        return self.command == command

"""
Conditionclass for tests and decorators. The initially passed condition may be evaluated against any received data.
The condition will validate succesful, if the target command starts with the same bytesequence as the 
initally passed condition
"""
class TasbAnyEndingCondition(TasbCondition):
    def __init__(self, command):
        super().__init__(command)

    def accept(self, command):
        string_of_received_command = command.getCommandString()
        string_to_match = self.command.getCommandString()
        match = string_of_received_command.startswith(string_to_match)
        return match
