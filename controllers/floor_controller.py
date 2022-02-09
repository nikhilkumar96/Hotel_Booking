class FloorController(object):
    def __init__(self, floorService):
        self.floorService = floorService

    def addFloor(self, floor, rooms):
        return self.floorService.addFloor(floor, rooms)

    # def addRoomToFloor(self, floor, room_no):
    #     return self.floorService.addRoomToFloor(floor, room_no)
