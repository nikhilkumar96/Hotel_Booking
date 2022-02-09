class Hotel(object):
    def __init__(self):
        self.id = None
        self.name = None
        self.address = None
        self.floors = []
        self.type = None

    def setId(self, id):
        self.id = id

    def getId(self):
        return self.id

    def setName(self, name):
        self.name = name

    def getName(self):
        return self.name

    def setAddress(self, address):
        self.address = address

    def getAddress(self):
        return self.address

    def setFloors(self, floors):
        self.floors = floors

    def getFloors(self):
        return self.floors

    def setType(self, type):
        self.type = type

    def getType(self):
        return self.type
