from models.guest import Guest
from models.hotel import Hotel
from models.reservation import Reservation
from models.room import Room
from repositories.hotel_repository import HotelRepository
from services.hotel_service import HotelService
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
        return (f'\n{'-' * 20}' '\nGerenciamento de Hotéis' f'\n{'-' * 20}'
                "\n\t1 - Cadastrar um novo hotel"
                "\n\t2 - Mudar o nome do hotel"
                "\n\t3 - Cadastrar um novo quarto"
                "\n\t4 - Remover um quarto"
                "\n\t5 - Deletar cadastro de um hotel"
                "\n\t6 - Retornar ao menu principal"
                '\n\nEscolha uma das opções acima: ')

    def show_reservation_menu(self):
        return (f'\n{'-' * 20}' '\nGerenciamento de Reservas' f'\n{'-' * 20}'
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

# def show_registering_hotel_menu(self):
#     return 

if __name__ == '__main__':
    menu_options = MenuOptions()
    hotel_repository = HotelRepository()
    hotel_service = HotelService()
    reservation_service = ReservationService()
    main_op = ''
    while(main_op != '4'):
        main_op = input(menu_options.show_main_menu())
        
        if not menu_options.check_op(main_op): 
            continue

        if main_op == '1': # --< Manage Hotels >--
            hotel_op = ''
            while hotel_op != '6':
                hotel_op = input(menu_options.show_hotel_menu())

                hotel_id = -1
                if not menu_options.check_op(hotel_op): 
                    continue
                elif int(hotel_op) in [2, 3, 4, 5]:
                    hotel_id = hotel_service.choose_hotel()

                # Cadastrando um novo hotel
                if hotel_op == '1':
                    name = input('\nInforme o nome do hotel: ')
                    address = input('Informe o endereço do hotel: ')
                    total_floors = input('Enter the number of floors: ')
                    rooms_per_floor = input('Enter the number of rooms per floor: ')
                    default_room_type = input('Enter the standard room type: ')
                    default_price = input('Enter the standard room price: ')

                    # Data casting
                    total_floors = int(total_floors)
                    rooms_per_floor = int(rooms_per_floor)
                    default_price = float(default_price)

                    if not hotel_service.create_and_save_hotel(name, address, total_floors,
                                                               rooms_per_floor, default_room_type, 
                                                               default_price):
                        continue
                # Renomeando um hotel existente
                elif hotel_op == '2':
                    new_name = input('\nInforme o novo nome para o hotel: ')
                    hotel_service.rename_hotel(hotel_id, new_name)  

                # Adicionando um novo quarto
                elif hotel_op == '3': 
                    room_id = input('\nInforme o código do quarto: ')
                    floor = input('Informe o andar do quarto: ')
                    room_type = input('Informe o tipo do quarto: ')
                    daily_rate = input('Informe o valor da diária do quarto: ')
                    hotel_service.add_new_room_to_hotel(hotel_id, room_id, floor, room_type, daily_rate)

                # Removendo um quarto
                elif hotel_op == '4': # Remover um quarto
                    room_id = input('\nInforme o código do quarto: ')
                    hotel_service.remove_room(hotel_id, room_id)

                # Removendo um hotel
                elif hotel_op == '5':
                    hotel_service.delete_hotel_data(hotel_id) 
                elif hotel_op == '6':
                    continue
        elif main_op == '2': # --< Manage Guests >--
            pass
        elif main_op == '3': # --< Manage Reservations >--
            reserv_op = ''
            while reserv_op != '5':
                reserv_op = input(menu_options.show_reservation_menu())

                if not menu_options.check_op(reserv_op): 
                    continue
                else:
                    reserv_op = int(reserv_op)
                
                if reserv_op in [1, 2, 3]:
                    hotel_id = hotel_service.choose_hotel()

                # Reservar quarto
                if reserv_op == 1:
                    reservation_service.show_available_rooms(hotel_id)
                    # > Mostrar quartos disponíveis 
                if reserv_op == 2:
                    pass
                if reserv_op == 3:
                    pass
                if reserv_op == 4:
                    pass
                if reserv_op == 5:
                    continue
        elif main_op == '4': # --< Exit >--
            continue
        
