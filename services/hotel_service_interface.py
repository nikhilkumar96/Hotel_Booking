import abc


class HotelServiceInterface(metaclass=abc.ABCMeta):
    @abc.abstractmethod
    def addHotel(self, id, name, address, floors, type):
        pass
