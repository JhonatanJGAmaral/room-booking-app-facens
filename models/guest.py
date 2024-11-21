import csv
from utils.utils import Utils
import os

class Guest():
    file_path = r'C:\Users\luca.alcalde_simoesp\Desktop\Backup 15.03.24\Projetos\ProjetoHotelPos\room-booking-app-facens\infrastructure\database\guests.csv'
    
    def __init__(self, id_guest=None, cpf=None, name_guest=None, date_birth=None, phone=None):
        self.__id_guest = id_guest
        self.__cpf = cpf
        self.__name_guest = name_guest
        self.__date_birth = date_birth
        self.__phone = phone
        
        self.utils = Utils()
        
    def preenche_cabecalho(self):
        # Verifica se o arquivo já existe
        if not os.path.exists(self.file_path):
            # Se o arquivo não existir, cria um arquivo novo e adiciona o cabeçalho
            with open(self.file_path, 'w', newline='', encoding='UTF-8') as arquivo:
                writer = csv.writer(arquivo)
                header = ['id_guest', 'cpf', 'name_guest', 'date_birth', 'phone']
                writer.writerow(header)
                print(f"Cabeçalho adicionado ao arquivo {self.file_path}")
        else:
            # Se o arquivo existe, verificar se já tem cabeçalho
            with open(self.file_path, 'r', encoding='UTF-8') as arquivo:
                reader = csv.reader(arquivo)
                first_line = next(reader, None)  # Lê a primeira linha

                # Se não houver cabeçalho, insere um
                if not first_line or len(first_line) != 5:
                    with open(self.file_path, 'w', newline='', encoding='UTF-8') as arquivo:
                        writer = csv.writer(arquivo)
                        header = ['id_guest', 'cpf', 'name_guest', 'date_birth', 'phone']
                        writer.writerow(header)
                        print(f"Cabeçalho adicionado ao arquivo {self.file_path}")
                else:
                    print("O arquivo já possui cabeçalho.")   
        
            
    def read_guest(self):
        with open(self.file_path, 'r', encoding='UTF-8') as arquivo:
            arquivo_csv = arquivo.readlines()[1:]     
            return list(arquivo_csv)
        

    def create_guest_to_csv(self, guest_data):
        guests = self.read_guest()

        if guests: 
            # Pega o último ID, que está na primeira coluna do último convidado
            last_id = int(guests[-1][0])
            new_id = last_id + 1 
        else:
            # Se não houver convidados, começa com ID 1
            new_id = 1 
        new_guest = {
            'id_guest': new_id,
            **guest_data
        }
        # Adiciona o novo convidado ao arquivo CSV
        with open(self.file_path, 'a', newline='', encoding='UTF-8') as arquivo:
            writer = csv.writer(arquivo)
            writer.writerow([new_guest['id_guest'], new_guest['cpf'], new_guest['name_guest'], 
                             new_guest['date_birth'], new_guest['phone']])

        return new_guest

    def update_guest_models(self, id_to_update, updates):
        try:
            with open(self.file_path, 'r', encoding='UTF-8') as arquivo:
                reader = csv.reader(arquivo)
                rows = list(reader)

            header = rows[0]  # Primeiro elemento da lista (cabeçalho)
            found = False
            for i, row in enumerate(rows[1:], start=1):
                if row[0] == str(id_to_update):
                    for key, value in updates.items():
                        if key in header:  # Verifique se a chave existe no cabeçalho
                            index = header.index(key)
                            row[index] = value
                    rows[i] = row
                    found = True
                    break

            if found:
                with open(self.file_path, 'w', newline='', encoding='UTF-8') as arquivo:
                    writer = csv.writer(arquivo)
                    writer.writerows(rows)
                print(f"Convidado com ID {id_to_update} atualizado com sucesso.")
            else:
                print(f"Convidado com ID {id_to_update} não encontrado.")
        except FileNotFoundError:
            print(f"Arquivo {self.file_path} não encontrado.")

    def delete_guest(self, id_delete):
        # Lê o arquivo CSV
        with open(self.file_path, 'r', encoding='UTF-8') as arquivo_csv:
            reader = csv.reader(arquivo_csv)
            guests = list(reader)

        # Encontra o convidado a ser deletado
        guest_to_delete = None
        for idx, guest in enumerate(guests):
            if guest[0] == id_delete:
                guest_to_delete = idx
                break

        if guest_to_delete is not None:
            # Armazena o ID excluído
            print(f"ID {id_delete} será excluído.")

            # Remove o convidado
            guests.pop(guest_to_delete)

            # Regrava o CSV sem o convidado excluído
            with open(self.file_path, 'w', newline='', encoding='UTF-8') as arquivo_csv:
                writer = csv.writer(arquivo_csv)
                writer.writerows(guests)
            print(f"Convidado ID {id_delete} excluído com sucesso.")
        else:
            print("ID não encontrado. Nenhuma linha foi excluída.")

