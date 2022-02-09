from services.hotel_service_interface import HotelServiceInterface
from models.hotel import Hotel
from exceptions import Exceptions

class HotelService(HotelServiceInterface):
    hotelDetails = {}

    def addHotel(self, id, name, address, floors, type):
        hotel = Hotel()
        hotel.setId(id)
        hotel.setName(name)
        hotel.setAddress(address)
        hotel.setFloors(floors)
        hotel.setType(type)
        self.__class__.hotelDetails[id] = hotel
        return hotel

    def checkin(self, id, no_of_rooms, reverseType):
        reserved = []
        all_floors = sorted(self.__class__.hotelDetails.get(id).getFloors(), key=lambda x: x.id, reverse=reverseType)
        for floor_item_id in range(len(all_floors)):
            for room_item_id in range(len(all_floors[floor_item_id].getRooms())):
                if all_floors[floor_item_id].getRooms()[room_item_id].getIsEmpty() and len(reserved) < no_of_rooms:
                    reserved.append(all_floors[floor_item_id].getRooms()[room_item_id].getRoomNo())
                    all_floors[floor_item_id].getRooms()[room_item_id].setIsEmpty(False)
        if len(reserved) == no_of_rooms:
            print(Exceptions.SUCCESSFULL_CHECKIN.value)
            print(Exceptions.CHECKEDIN_ROOMS.value, reserved)
        else:
            print('Not Enough Rooms')
            print(Exceptions.CHECKEDIN_ROOMS.value, reserved)
        return reserved

    def checkout(self, id, room_no):
        all_floors = self.__class__.hotelDetails.get(id).getFloors()
        for floor_item_id in range(len(all_floors)):
            for room_item_id in range(len(all_floors[floor_item_id].getRooms())):
                if all_floors[floor_item_id].getRooms()[room_item_id].getRoomNo() == room_no:
                    if all_floors[floor_item_id].getRooms()[room_item_id].getIsEmpty():
                        print(Exceptions.ROOM_ALREADY_EMPTY.value)
                        return False
                    else:
                        all_floors[floor_item_id].getRooms()[room_item_id].setIsEmpty(True)
                        print(f"{room_no}", Exceptions.ROOM_CHECKOUT.value)
                        return True

        print(Exceptions.ROOM_NOT_EXIST.value)
        return False
