from services.room_service_interface import RoomServiceInterface
from models.room import Room


class RoomService(RoomServiceInterface):
    roomDetails = {}

    def addRoom(self, room_no, empty):
        room = Room()
        room.setRoomNo(room_no)
        room.setIsEmpty(empty)
        self.__class__.roomDetails[room_no] = room
        return room
