from repositories.hotel_repository import HotelRepository 
from repositories.room_repository import RoomRepository
from services.room_service import RoomService
from utils.utils import Utils
from models.hotel import Hotel
from models.room import Room
import pandas as pd

# () Change the number of floors, rooms per floor, and total number of rooms for each hotel when adding new rooms
# () Make the "get_hotels_and_addresses" function return the ID as well, but without showing it

class HotelService():
    def __init__(self):
        self.__hotel_menu_columns = {'hotel_id': 'Código',
                                     'name': 'Hotel',
                                     'address': 'Endereço'}
        pd.set_option('display.max_rows', 1000)
        pd.set_option('display.colheader_justify', 'left')
        self.__hotel_repository = HotelRepository()
        self.__room_service = RoomService()
        self.__utils = Utils()
    
    def get_last_column_val(self, column_key):
        df = self.__hotel_repository.read_hotel()            
        return df[column_key].iloc[-1] if not df.empty else 0

    def generate_id(self):
        return self.get_last_column_val('hotel_id') + 1

    def create_and_save_hotel(self, name, address, total_floors,
                              rooms_per_floor, default_room_type, default_price):
        hotel_id = self.generate_id()  
        hotel = Hotel(hotel_id, name, address, total_floors, rooms_per_floor, default_room_type, default_price) 
        return self.__hotel_repository.save(hotel) 

    def get_hotels_and_addresses(self):
        df = self.__hotel_repository.read_hotel()
        if df.empty:
            print('\n\t< Não há hotéis registrados >')
            return pd.DataFrame()
        else:
            return df[['hotel_id', 'name', 'address']]

    def choose_hotel(self):
        hotels_df = self.get_hotels_and_addresses()
        if hotels_df.empty:
            return pd.DataFrame()
        else:
            hotel_codes = list(map(str, hotels_df['hotel_id']))
            df_to_print = self.__utils.format_dataframe(hotels_df, self.__hotel_menu_columns)
            print(f'\n{df_to_print}')

            while True:
                hotel_code = input('\nEscolha um dos hotéis acima através de seu código: ')
                if hotel_code in hotel_codes:
                    break
                else:
                    print('\n\t< Opção inválida! Informe um código existente. >')

            return int(hotel_code)
    
    def update_hotel_total_rooms(self, hotel_id, op='increment'):
        df = self.__hotel_repository.read_hotel()
        df.loc[df['hotel_id']==hotel_id, 'total_rooms'] += 1 if op == 'increment' else -1
        self.__hotel_repository.update_hotel(df)

    def add_new_room_to_hotel(self, hotel_id, room_id, floor, room_type, daily_rate):
        self.__room_service.create_and_save_room(hotel_id, room_id, floor, room_type, daily_rate)
        self.update_hotel_total_rooms(hotel_id, op='increment')
        return True

    def delete_hotel_data(self, hotel_id):
        self.__room_service.delete_hotel_rooms(hotel_id)
        # deletar reservas        
        # deletar reservas        
        # deletar reservas        
        self.__hotel_repository.delete_hotel(hotel_id=hotel_id)

    def rename_hotel(self, hotel_id, new_name):
        df = self.__hotel_repository.read_hotel()
        df.loc[df['hotel_id']==hotel_id, 'name'] = new_name
        self.__hotel_repository.update_hotel(df)

    def remove_room(self, hotel_id, room_id):
        self.__room_service.remove_room(hotel_id, room_id)
        self.update_hotel_total_rooms(hotel_id, op='decrement')