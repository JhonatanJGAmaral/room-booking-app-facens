from utils.utils import Utils

class Hotel():

    def __init__(self, id_hotel, nome_hotel, endereco_hotel, quantidade_andar, quarto_por_andar):
        self.__id_hotel = id_hotel
        self.__nome_hotel = nome_hotel
        self.__endereco_hotel = endereco_hotel
        self.__quantidade_andar = quantidade_andar
        self.__quarto_por_andar = quarto_por_andar
        self.__total_quarto = quantidade_andar * quarto_por_andar
        
        self.__utils = Utils()

    def update_hotel(self):
        pass

    def delete_hotel(self):
        pass

    def read_hotel(self):
        pass