from services.floor_service_interface import FloorServiceInterface
from models.floor import Floor


class FloorService(FloorServiceInterface):
    floorDetails = {}

    def addFloor(self, floor, rooms):
        fl = Floor()
        fl.setFloor(floor)
        fl.setRooms(rooms)
        self.__class__.floorDetails[floor] = fl
        return fl

    # def addRoomToFloor(self, floor, room_no):
    #     all_rooms = self.__class__.floorDetails[floor].getRooms()
    #     if room_no in all_rooms:
    #         print('Room Already Exist')
    #     else:
    #         self.__class__.floorDetails[floor].setRooms(all_rooms.append(room_no))
