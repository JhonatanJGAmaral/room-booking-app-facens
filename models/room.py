class Room():
    def __init__(self, id_hotel, id_room, floor, room_type, daily_rate):
        self.__id_hotel = id_hotel
        self.__id_room = id_room
        self.__floor = floor
        self.__room_type = room_type
        self.__daily_rate = daily_rate
        
    @property
    def id_hotel(self):
        return self.__id_hotel

    @property
    def id_room(self):
        return self.__id_room

    @property
    def floor(self):
        return self.__floor

    @property
    def room_type(self):
        return self.__room_type

    @property
    def daily_rate(self):
        return self.__daily_rate