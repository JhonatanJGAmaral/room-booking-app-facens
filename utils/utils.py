from configurations.configurations import Configurations
import pandas as pd
import os

class Utils():
    def __init__(self):
        self.config = Configurations()

    def empty_file(self, file_path):
        return os.path.exists(file_path) and os.path.getsize(file_path) <= 0

    def dict_to_dataframe(self, dictionary):
        return pd.DataFrame(dictionary, index=[0])

    def read_file(self, type):
        file_path = f'{self.config.storage_path}/{type}.csv'
        return pd.read_csv(file_path) if not self.empty_file(file_path) else pd.DataFrame()    

    def write_file(self, type, df, mode='w'):
        file_path = f'{self.config.storage_path}/{type}.csv'
        if self.empty_file(file_path):
            df.to_csv(file_path, mode='w', index=False, header=True)
        else:
            df.to_csv(file_path, mode=mode, index=False, header=False, )
