class Floor(object):
    def __init__(self):
        self.floor = None
        self.rooms = []

    def setFloor(self, id):
        self.id = id

    def getFloor(self):
        return self.id

    def setRooms(self, rooms):
        self.rooms = rooms

    def getRooms(self):
        return self.rooms