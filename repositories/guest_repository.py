import csv
from utils.utils import Utils
from models.guest_model import Guest

class GuestRepository():
    def __init__(self):
        self.__utils = Utils()
        
    def create_guest(self, guest: Guest):
        if self.guest_exists(guest):
            print(f'\nO CPF \'{guest.cpf}\' já foi cadastrado.')

    def read_guest(self):
        return self.__utils.read_file('guests')
    
    def update_guest(self, guest_df):
        return self.__utils.write_file('guests', guest_df, 'w')        
    
    def delete_guest(self, id=None, cpf=''):
        df = self.read_guests()
        new_df = df[df['id'] != id] if id else df[~(df['cpf'])]
        self.update_hotel(new_df)
        
    def guest_exists(self, guest):
        df = self.read_guests()
        if not df.empty:
            return not df[(df['cpf'])].empty
        else:
            return False
        
    def __guest_to_dict(self, guest):
        guest_data = {
            'id': guest.id,
            'cpf': guest.cpf,
            'name': guest.name,
            'date_birth': guest.date_birth,
            'phone': guest.phone
        }
        
        return guest_data
