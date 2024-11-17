from configurations.configurations import Configurations
import pandas as pd

class Utils():
    def __init__(self):
        self.config = Configurations()

    def read_file(self, type):
       return pd.read_csv(f'infrastructure\{type}.csv')

    def write_file(self, type):
        pd.df.to_scv(f'infrastructure\{type}.csv')
