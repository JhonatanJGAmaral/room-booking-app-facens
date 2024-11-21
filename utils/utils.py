from configurations.configurations import Configurations
from datetime import datetime
import pandas as pd
import os

class Utils():
    def __init__(self):
        self.config = Configurations()

    def is_int(self, values):
        try:
            dummy = list(map(int, values))
            return True
        except ValueError:
            return False

    def empty_file(self, file_path):
        return os.path.exists(file_path) and os.path.getsize(file_path) <= 0

    def dict_to_dataframe(self, dictionary):
        return pd.DataFrame(dictionary, index=[0])

    def format_dataframe(self, df, new_col_names):
        df = df.rename(columns=new_col_names)
        return df.reset_index(drop=True).applymap(str).to_string(index=False, justify='left')

    def format_date(self, data_str):
        return datetime.strptime(data_str, "%d/%m/%Y")

    def str_to_date_format(self, df, key):
        return df[key] = pd.to_datetime(df[key])

    # def extract_yy_mm_dd(self, date_str):
    #     if type(date_str) != str:
    #         date_str = str(date_str)
    #     sepa = '-' if '-' in date_str else '/'
    #     year, month, day = separator.split(sepa)
    #     if not self.is_int([year, month, day]):
    #         return '01', '01', '0001'
    #     else:
    #         return '', '', ''

    def read_file(self, type):
        file_path = f'{self.config.storage_path}/{type}.csv'
        return pd.read_csv(file_path) if not self.empty_file(file_path) else pd.DataFrame()    

    def write_file(self, type, df, mode='w'):
        file_path = f'{self.config.storage_path}/{type}.csv'
        if self.empty_file(file_path):
            df.to_csv(file_path, mode='w', index=False, header=True)
        else:
            df.to_csv(file_path, mode=mode, index=False, header=(mode == 'w'))
