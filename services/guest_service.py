from repositories.guest_repository import GuestRepository
from utils.utils import Utils
from models.guest_model import Guest
import pandas as pd

class GuestService():
    def __init__(self):
        self.__guest_menu_columns = {
            'id': 'Código',
            'name': 'Cliente',
            'cpf': 'CPF'
        }
        pd.set_option('display.max_rows', 1000)
        pd.set_option('display.colheader_justify', 'left')
        self.__guest_repository = GuestRepository()
        self.__utils = Utils()
        
    def get_last_column_val(self, column_key):
        df = self.__guest_repository.read_guest()
        return df[column_key].iloc[-1] if not df.empy else 0
    
    def generate_id(self):
        return self.get_last_column_val('id') + 1
    
    def create_and_save_guest(self, cpf, name, date_birth, phone):
        guest_id = self.generate_id()
        guest = Guest(guest_id, cpf, name, date_birth, phone)
        return self.__guest_repository.save(guest)
        
    def get_guest_and_cpf(self):
        df = self.__guest_repository.read_guest()
        if df.empty:
            print('\n\t< Não há clientes registrados >')
            return pd.DataFrame()
        else:
            return df[['id', 'cpf', 'name']]
        
    def choose_guest(self):
        guest_df = self.get_guest_and_cpf()
        if guest_df.empty:
            return pd.DataFrame()
        else:
            guest_codes = list(map(str, guest_df['id']))
            df_to_print = self.__utils.format_dataframe(guest_df, self.__guest_menu_columns)
            print(f'\n{df_to_print}')
            
            while True:
                guest_code = input('\nEscolha um dos clientes acima através de seu código: ')
                if guest_code in guest_codes:
                    break
                else:
                    print('\n\t< Opção inválida! Informe um código existente. >')

            return int(guest_code)

    def delete_guest_data(self, guest_id):
        self.__guest_repository.delete_guest(guest_id=guest_id)

    def rename_guest(self, guest_id, new_name):
        df = self.__guest_repository.read_guest()
        df.loc[df['id']==guest_id, 'name'] = new_name
        self.__guest_repository.update_guest(df)