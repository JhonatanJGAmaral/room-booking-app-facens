from services.room_service import RoomService
from repositories.reservation_repository import ReservationRepository
from datetime import datetime
from utils.utils import Utils

class ReservationService():

    def __init__(self):
        self.__reservation_repository = ReservationRepository()
        self.__room_service = RoomService()
        self.__utils = Utils()

    def get_reservations_by_date_range(self, check_in_date, check_out_date):
        reserv_df = self.__reservation_repository.read_reservation()
        # VERIFICAR SE A DATA PRECISARÁ DE VALIDAÇÃO
        return reserv_df[(reserv_df['check_in_date'] >= check_in_date) & (reserv_df['check_out_date'] <= check_out_date)]


    # criar uma correspondência para as colunas da reserva e usar a função "format_dataframe" presente nas Utils
    # criar uma correspondência para as colunas da reserva e usar a função "format_dataframe" presente nas Utils
    # criar uma correspondência para as colunas da reserva e usar a função "format_dataframe" presente nas Utils
    def show_available_rooms(self, hotel_id, check_in_date=None, check_out_date=None):
        check_in_date = self.__utils.format_date(check_in_date)
        check_out_date = self.__utils.format_date(check_out_date)

        reserv_df = self.get_reservations_by_date_range(check_in_date, check_out_date)
        new_df = reserv_df[(reserv_df['hotel_id'] == hotel_id) & (reserv_df['canceled'] != True)]
        rooms_df = self.__room_service.get_rooms_by_hotel_id(hotel_id)
        
        if not new_df.empty: # existem reservas para esse hotel
            unavailable_rooms = self.get_reservations_by_date_range(check_in_date, check_out_date).loc[:,'room_id']
            rooms_df = rooms_df[~rooms_df['room_id'].isin(unavailable_rooms)]

        print(f'\n{rooms_df.loc[:, ['room_id', 'floor', 'room_type', 'daily_rate']]}')
        
    def choose_room(self, hotel_id, check_in_date, check_out_date):
        self.show_available_rooms(hotel_id, check_in_date, check_out_date)
        # choose room
        room_id = None
        return room_id
