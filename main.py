from models.guest import Guest
from models.hotel import Hotel
from models.room import Room
from utils.utils import Utils
from models.reservation import Reservation
from services.hotel_service import HotelService
from services.guest_service import GuestService
from repositories.hotel_repository import HotelRepository
from services.reservation_service import ReservationService

# () Create the Initials class

class MenuOptions():
    def show_main_menu(self):
        return  (f'\n\n{'-' * 50}' '\nROOM BOOKING APP' f'\n{'-' * 50}'
                '\n\t1 - Gerenciar Hotéis'
                '\n\t2 - Gerenciar Hóspedes'
                '\n\t3 - Gerenciar Reservas'
                '\n\t4 - Sair'
                '\n\nEscolha uma das opções acima: ')

    def show_hotel_menu(self):
        return (f'\n{'-' * 30}' '\nGerenciamento de Hotéis' f'\n{'-' * 30}'
                "\n\t1 - Cadastrar um novo hotel"
                "\n\t2 - Mudar o nome do hotel"
                "\n\t3 - Cadastrar um novo quarto"
                "\n\t4 - Remover um quarto"
                "\n\t5 - Deletar cadastro de um hotel"
                "\n\t6 - Retornar ao menu principal"
                '\n\nEscolha uma das opções acima: ')

    def show_reservation_menu(self):
        return (f'\n{'-' * 30}' '\nGerenciamento de Reservas' f'\n{'-' * 30}'
                "\n\t1 - Reservar quarto"
                "\n\t2 - Exibir reservas"
                "\n\t3 - Cancelar reserva"
                "\n\t4 - Mostrar gráficos de reservas"
                "\n\t5 - Retornar ao menu principal"
                '\n\nEscolha uma das opções acima: ')

    def check_op(self, op):
        try:
            dummy = int(op)
            return True
        except ValueError:
            print('\nOpção inválida! Informe uma das opções presentes no menu.')
            return False

    def repeat_input(self, val_type, input_msg, try_again_msg):
        val = None
        while True:
            val = input(input_msg)
            if val_type == 'int':
                if utils.is_int([val]): return int(val)
            elif val_type == 'float':
                if utils.is_float([val]): return float(val)
            elif val_type == 'date':
                converted_date = utils.format_date(val)
                # if converted_date: return converted_date
                if converted_date: return val
            elif val_type == 'cpf':
                return val
            else: break
            print(try_again_msg)
        return val

# def show_registering_hotel_menu(self):
#     return 

if __name__ == '__main__':
    main_op = -1
    utils = Utils()
    menu_options = MenuOptions()
    hotel_service = HotelService()
    guest_service = GuestService()
    hotel_repository = HotelRepository()
    reservation_service = ReservationService()

    while(main_op != 4):
        main_op = input(menu_options.show_main_menu())
        
        if not menu_options.check_op(main_op): continue
        else: main_op = int(main_op)

        if main_op == 1: # --< Manage Hotels >--
            hotel_op = -1
            while hotel_op != 6:
                hotel_op = input(menu_options.show_hotel_menu())

                if not menu_options.check_op(hotel_op): continue
                else: hotel_op = int(hotel_op)

                hotel_id = -1
                if hotel_op in [2, 3, 4, 5]:
                    hotel_id = hotel_service.choose_hotel()

                # Cadastrando um novo hotel
                if hotel_op == 1:
                    print('\nPor favor, preencha os campos abaixo:')
                    name = input('\n> Nome do hotel: ')
                    address = input('> Endereço do hotel: ')
                    total_floors = menu_options.repeat_input('int', '> Número de andares: ',
                                                             '\t< Valor inválido. Informe um valor numérico! >')

                    rooms_per_floor = menu_options.repeat_input('int', '> Número de quartos por andar: ',
                                                                '\t< Valor inválido. Informe um valor numérico! >')

                    default_room_type = input('> Tipo de quarto padrão: ')
                    default_price = menu_options.repeat_input('float', '> Valor padrão da diária (R$): ',
                                                              '\t< Valor inválido. Informe um valor numérico! (ex: 250.50) >')

                    if not hotel_service.create_and_save_hotel(name, address, total_floors,
                                                               rooms_per_floor, default_room_type, 
                                                               default_price):
                        continue
                # Renomeando um hotel existente
                elif hotel_op == 2:
                    new_name = input('\nInforme o novo nome para o hotel: ')
                    hotel_service.rename_hotel(hotel_id, new_name)  

                # Adicionando um novo quarto
                elif hotel_op == 3: 
                    room_id = input('\nInforme o código do quarto: ')
                    floor = input('Informe o andar do quarto: ')
                    room_type = input('Informe o tipo do quarto: ')
                    daily_rate = input('Informe o valor da diária do quarto: ')
                    hotel_service.add_new_room_to_hotel(hotel_id, room_id, floor, room_type, daily_rate)

                # Removendo um quarto
                elif hotel_op == 4: # Remover um quarto
                    room_id = input('\nInforme o código do quarto: ')
                    hotel_service.remove_room(hotel_id, room_id)

                # Removendo um hotel
                elif hotel_op == 5:
                    hotel_service.delete_hotel_data(hotel_id) 
                elif hotel_op == 6:
                    continue
        elif main_op == 2: # --< Manage Guests >--
            pass
        elif main_op == 3: # --< Manage Reservations >--
            reserv_op = -1

            valid_cpf = False
            while not valid_cpf:
                user_cpf = menu_options.repeat_input('cpf', 'Informe seu CPF: ',
                                                 '\t< CPF inválido! >\nInsira novamente: ')
                if guest_service.guest_exists(user_cpf): 
                    break
                else:
                    print('\t< Hóspede não cadastrado >\nInsira novamente: ')
            guest_cpf = user_cpf

            while reserv_op != 5:
                reserv_op = input(menu_options.show_reservation_menu())

                if not menu_options.check_op(reserv_op): continue
                else: reserv_op = int(reserv_op)
                
                if reserv_op in [1, 2, 3]:
                    hotel_id = hotel_service.choose_hotel()

                # Reservar quarto
                if reserv_op == 1:
                    in_progress = True
                    input_new_dates = False
                    while in_progress or input_new_dates:
                        print('\nPor favor, preencha os campos abaixo:')
                        check_in_date = menu_options.repeat_input('date', '> Data de início da reserva (formato DD/MM/AAAA): ',
                                                                  '\t< Data inválida! >\nInsira novamente: ')
                        
                        
                        check_out_date = menu_options.repeat_input('date', '> A data de término da reserva (formato DD/MM/AAAA): ',
                                                                   '\t< Data inválida! >\nInsira novamente: ')
                    
                        # > Mostrar quartos disponíveis
                        room_id = None
                        while not room_id and not input_new_dates:
                            room_id = reservation_service.choose_room(hotel_id, check_in_date, check_out_date)
                            if room_id:
                                in_progress = False
                                input_new_dates = False
                            else:
                                input_new_dates = (input(f'\nDeseja informar outro intervalo de datas? (S/N): ').upper() == 'S')
                            
                        reservation_service.create_and_save_reservation(hotel_id, room_id, guest_cpf, check_in_date, check_out_date)
                # 2 - Exibir reservas
                if reserv_op == 2:
                    pass
                
                # 3 - Cancelar reserva
                if reserv_op == 3:
                    pass

                # 4 - Mostrar gráficos de reservas
                if reserv_op == 4:
                    pass

                # 5 - Retornar ao menu principal
                if reserv_op == 5:
                    continue
        elif main_op == 4: # --< Exit >--
            continue
        
