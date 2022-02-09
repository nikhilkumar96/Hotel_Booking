class Room(object):
    def __init__(self):
        self.room_no = None
        self.is_empty = None

    def setRoomNo(self, room_no):
        self.room_no = room_no

    def getRoomNo(self):
        return self.room_no

    def setIsEmpty(self, is_empty):
        self.is_empty = is_empty

    def getIsEmpty(self):
        return self.is_empty
