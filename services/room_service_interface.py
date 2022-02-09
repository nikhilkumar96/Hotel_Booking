import abc


class RoomServiceInterface(metaclass=abc.ABCMeta):
    @abc.abstractmethod
    def addRoom(self, room_no, empty):
        pass
