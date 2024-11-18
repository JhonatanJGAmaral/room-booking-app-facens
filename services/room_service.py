from repositories.room_repository import RoomRepository
from models.room import Room
import pandas as pd

class RoomService():
    
    def __init__(self):
        self.__room_repository = RoomRepository()

    def create_and_save_room(self, hotel_id, room_id, floor, room_type, daily_rate):
        room = Room(hotel_id, room_id, floor, room_type, daily_rate)
        return self.__room_repository.save(room)
    