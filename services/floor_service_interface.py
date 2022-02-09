import abc


class FloorServiceInterface(metaclass=abc.ABCMeta):
    @abc.abstractmethod
    def addFloor(self, floor, rooms):
        pass

    # @abc.abstractmethod
    # def addRoomToFloor(self, floor, room_no):
    #     pass
