from utils.utils import Utils
from models.hotel import Hotel
from repositories.room_repository import RoomRepository

class HotelRepository():
    def __init__(self):
        self.__utils = Utils()
        self.__room_repository = RoomRepository()

    def save(self, hotel: Hotel):
        if self.hotel_exists(hotel):
            print(f'The hotel \'{hotel.name}\' in \'{hotel.address}\' address has been already registered.')
            return False

        hotel_dict = self.__hotel_to_dict(hotel)
        df = self.__utils.dict_to_dataframe(hotel_dict)
        self.__utils.write_file('hotels', df, 'a')

        # create rooms
        for room in hotel.default_rooms:
            dummy = self.__room_repository.save(room)

        print(f'\nHotel {hotel.name} successfully created.')      
        return True

    def update_hotel(self):
        pass

    def delete_hotel(self):
        pass

    def read_hotel(self):
        return self.__utils.read_file('hotels')

    def hotel_exists(self, hotel):
        df = self.read_hotel()
        if not df.empty:
            return not df[(df['name'] == hotel.name) & (df['address'] == hotel.address)].empty
        else:
            return False

    def __hotel_to_dict(self, hotel):
        hotel_data = {'id': hotel.id,
                      'name': hotel.name,
                      'address': hotel.address,
                      'total_floors': hotel.total_floors,
                      'rooms_per_floor': hotel.rooms_per_floor,
                      'total_rooms': hotel.total_rooms}
        
        return hotel_data
