class PacketTypeException(Exception):
    def __init__(self, msg: str = "Invalid Packet Type detectet"):
        self.msg = msg
        super().__init__(self.msg)