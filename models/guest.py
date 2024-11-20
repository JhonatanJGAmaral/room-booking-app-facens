import csv
from utils.utils import Utils


class Guest():
    def __init__(self, id_guest, cpf, name_guest, date_birth, phone):
        self.__id_guest = id_guest
        self.__cpf = cpf
        self.__name_guest = name_guest
        self.__date_birth = date_birth
        self.__phone = phone
        
        self.utils = Utils()
        
        
    def create_guest(self, guest_data):
        try:

                guests = self.read_guest()
                # Se o arquivo não estiver vazio, o próximo ID será o ID da última linha + 1
                if len(guests) > 1:  # Se existir ao menos um convidado, o cabeçalho será pulado
                    last_id = int(guests[-1][0])  # Pega o último ID
                    new_id = last_id + 1  # Incrementa o ID
                else:
                    new_id = 1  # Se o arquivo estiver vazio, começa do ID 1
        except FileNotFoundError:
                    new_id = 1  # Se o arquivo não existir, começa com ID 1

                # Cria um novo convidado com o ID gerado
        new_guest = {
            'id_guest': new_id,
            'cpf': guest_data['cpf'],
            'name_guest': guest_data['name_guest'],
            'date_birth': guest_data['date_birth'],
            'phone': guest_data['phone']
        }

        # Adiciona o novo convidado ao arquivo CSV
        with open('/guest.csv', 'a', newline='', encoding='UTF-8') as arquivo:
            writer = csv.writer(arquivo)
            writer.writerow([new_guest['id_guest'], new_guest['cpf'], new_guest['name_guest'], 
                            new_guest['date_birth'], new_guest['phone']])
        
        print(f'Convidado {new_guest["name_guest"]} criado com sucesso!')
        return new_guest
            
    def read_guest(self):
        with open('/guest.csv', 'r', encoding='UTF-8') as arquivo:
            arquivo_csv = arquivo.readlines()[1:]     
            return list(arquivo_csv)

    def update_guest(self, id_to_update, updates):
        try:
            with open('guest.csv', 'r', encoding='UTF-8') as arquivo:
                reader = csv.reader(arquivo)
                rows = list(reader)

            header = rows[0] 
            found = False
            for i, row in enumerate(rows[1:], start=1):
                if row[0] == str(id_to_update):
                    for key, value in updates.items():
                        if key in ['cpf', 'name_guest', 'date_birth', 'phone']:
                            index = header.index(key)
                            row[index] = value
                    rows[i] = row
                    found = True
                    break

            if found:
                with open('guest.csv', 'w', newline='', encoding='UTF-8') as arquivo:
                    writer = csv.writer(arquivo)
                    writer.writerows(rows)
                print(f"Convidado com ID {id_to_update} atualizado com sucesso.")
            else:
                print(f"Convidado com ID {id_to_update} não encontrado.")
        except FileNotFoundError:
            print("Arquivo guest.csv não encontrado.")


    def delete_guest(self, id_delete):
        # Lê o arquivo CSV
        with open('/guest.csv', 'r', encoding='UTF-8') as arquivo_csv:
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
            with open('/guest.csv', 'w', newline='', encoding='UTF-8') as arquivo_csv:
                writer = csv.writer(arquivo_csv)
                writer.writerows(guests)
            print(f"Convidado ID {id_delete} excluído com sucesso.")
        else:
            print("ID não encontrado. Nenhuma linha foi excluída.")



new_guest = Guest('12345678900', 'John Doe', '1990-01-01', '555-1234')
new_guest.create_guest()