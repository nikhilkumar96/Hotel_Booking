class HotelController(object):
    def __init__(self, hotelService):
        self.hotelService = hotelService

    def addHotel(self, id, name, address, floors, type='bottom'):
        return self.hotelService.addHotel(id, name, address, floors, type)

    def checkin(self, id, no_of_room):
        hotel_type = self.hotelService.hotelDetails.get(id).getType()
        if hotel_type =='bottom':
            return self.hotelService.checkin(id, no_of_room, False)
        else:
            return self.hotelService.checkin(id, no_of_room, True)

    def checkout(self, id, room_no):
        return self.hotelService.checkout(id, room_no)