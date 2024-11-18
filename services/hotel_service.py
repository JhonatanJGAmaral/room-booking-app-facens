from repositories.hotel_repository import HotelRepository 
from repositories.room_repository import RoomRepository 
from models.hotel import Hotel
from models.room import Room
import pandas as pd

# () Change the number of floors, rooms per floor, and total number of rooms for each hotel when adding new rooms

class HotelService():
    def __init__(self):
        self.__hotel_repository = HotelRepository()
        # self.__room_repository = RoomRepository()

    def create_and_save_hotel(self, id, name, address, total_floors,
                              rooms_per_floor, default_room_type, default_price): 
        hotel = Hotel(id, name, address, total_floors, rooms_per_floor, default_room_type, default_price) 
        return self.__hotel_repository.save(hotel) 

    def get_hotels_and_addresses(self):
        df = self.__hotel_repository.read_hotel()
        if df.empty:
            print('\n\t< There are no registered hotels >')
            return pd.DataFrame()
        else:
            new_df = df[['name', 'address']].sort_values(by=['name']).reset_index(drop=False)
            new_df.rename(columns={'index': 'Sequential'}, inplace=True)
            return new_df

    def choose_hotel(self):
        hotels_df = self.get_hotels_and_addresses()
        if hotels_df.empty:
            return pd.DataFrame()
        else:
            print(f'\n{hotels_df}')
            hotel_seq = input('\nChoose one of the hotels above by its sequence number: ')
            return hotels_df[hotels_df['Sequential']==hotel_seq]

    def add_new_room_to_hotel(self):
        pass


    