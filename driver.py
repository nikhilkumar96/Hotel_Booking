from controllers.hotel_controller import HotelController
from controllers.floor_controller import FloorController
from controllers.room_controller import RoomController

from services.hotel_service import HotelService
from services.floor_service import FloorService
from services.room_service import RoomService

roomController = RoomController(RoomService())
floorController = FloorController(FloorService())
hotelController = HotelController(HotelService())

room1 = roomController.addRoom(1)
room2 = roomController.addRoom(2)
room3 = roomController.addRoom(3)
room4 = roomController.addRoom(4)
room5 = roomController.addRoom(5)
room6 = roomController.addRoom(6)
room7 = roomController.addRoom(7)
room8 = roomController.addRoom(8)
room9 = roomController.addRoom(9)
room10 = roomController.addRoom(10)

floor1rooms = [room1, room2, room3, room4, room5]
floor2rooms = [room6, room7, room8, room9, room10]

floor1 = floorController.addFloor(1, floor1rooms)
floor2 = floorController.addFloor(2, floor2rooms)

hotel1 = hotelController.addHotel(1, 'Hilton', 'NEW Delhi', [floor1, floor2], 'bottom')

hotelController.checkin(1, 5)

hotelController.checkout(1, 2)
hotelController.checkout(1, 2)

hotelController.checkin(1, 2)
hotelController.checkout(1, 6)
hotelController.checkout(1,100)

