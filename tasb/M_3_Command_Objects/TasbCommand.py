import binascii

"""
Main data model of the program. The Command wraps all bytes that should be send over or
received from the bluetooth conneciton. It may be initialized by passing a hexString or bytes.
"""
class TasbCommand:
    def __init__(self, commandBytes):
        self.commandBytes = commandBytes

    @classmethod
    def fromHexString(cls, hexString):
        if type(hexString) != str:
            raise ValueError("TasbCommand expects a string!")
            pass
        commandBytes = bytes.fromhex(hexString)
        return cls(commandBytes)

    """
    Converts the command bytes to a string and returns it
    """
    def getCommandString(self):
        commandBytesAsHex = binascii.hexlify(self.commandBytes)
        hexBytesAsString = commandBytesAsHex.decode("ascii")
        return hexBytesAsString

    """
    Returns the bytesequence of this command
    """
    def getCommandBytes(self):
        return self.commandBytes

    """
    Equals-Operator 
    """
    def __eq__(self, other):
        if isinstance(self, other.__class__):
            return self.getCommandBytes() == other.getCommandBytes()
        return False
