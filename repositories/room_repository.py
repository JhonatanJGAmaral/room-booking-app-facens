from utils.utils import Utils
from models.room import Room

class RoomRepository():
    def __init__(self):
        self.__utils = Utils()

    def save(self, room: Room):
        if self.room_exists(room):
            return False
        room_dict = self.__room_to_dict(room)
        df = self.__utils.dict_to_dataframe(room_dict)
        self.__utils.write_file('rooms', df, 'a')        
        return True       

    def read_room(self):
        return self.__utils.read_file('rooms')

    def room_exists(self, room):
        df = self.read_room()
        if not df.empty:
            return not df[(df['id_hotel'] == room.id_hotel) & (df['id_room'] == room.id_room)].empty
        else:
            return False

    def __room_to_dict(self, room):
        room_data = {'id_hotel': room.id_hotel, 
                     'id_room': room.id_room, 
                     'floor': room.floor, 
                     'room_type': room.room_type, 
                     'daily_rate': room.daily_rate}
        return room_data
