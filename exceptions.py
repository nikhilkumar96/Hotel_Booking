from enum import Enum


class Exceptions(Enum):
    ROOM_CHECKOUT = "Room has been successfully checked out"
    ROOM_NOT_EXIST = "Room Doesn't Exist"
    ROOM_ALREADY_EMPTY = "Room Already Empty"
    SUCCESSFULL_CHECKIN = "All Rooms Checked In"
    CHECKEDIN_ROOMS = "Rooms cheked in are "
