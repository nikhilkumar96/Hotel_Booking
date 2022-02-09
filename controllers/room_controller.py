class RoomController(object):
    def __init__(self, roomService):
        self.roomService = roomService

    def addRoom(self, room_no, empty=True):
        return self.roomService.addRoom(room_no, empty)
