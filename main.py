from models.guest import Guest
from models.hotel import Hotel
from models.reservation import Reservation
from models.room import Room
from repositories.hotel_repository import HotelRepository
from services.hotel_service import HotelService

# Create the Initials class

def show_main_menu():
    return  (f'\n\n{'-' * 50}' '\nROOM BOOKING APP' f'\n{'-' * 50}'
             '\n\t1 - Manage Hotels'
             '\n\t2 - Manage Guests'
             '\n\t3 - Manage Reservations'
             '\n\t4 - Exit'
             '\n\nChoose an option above: ')

def show_hotel_menu():
    return (f'\n{'-' * 20}' '\nHotel Management' f'\n{'-' * 50}'
            "\n\t1 - Register a new hotel"
            "\n\t2 - Change hotel name"
            "\n\t3 - Register a new room"
            "\n\t4 - Delete a room"
            "\n\t5 - Delete hotel record"
            "\n\t6 - Return to main menu"
            '\n\nChoose an option above: ')

# def show_registering_hotel_menu(self):
#     return 

if __name__ == '__main__':
    hotel_repository = HotelRepository()
    hotel_service = HotelService()
    main_op = ''
    while(main_op != '4'):
        main_op = input(show_main_menu())

        if main_op == '1': # --< Manage Hotels >--
            hotel_op = ''
            while hotel_op != '6':
                hotel_op = input(show_hotel_menu())

                # Registering a new hotel
                if hotel_op == '1':
                    id = 1 
                    name = input('\nEnter hotel name: ')
                    address = input('Enter hotel address: ')
                    total_floors = input('Enter the number of floors: ')
                    rooms_per_floor = input('Enter the number of rooms per floor: ')
                    default_room_type = input('Enter the standard room type: ')
                    default_price = input('Enter the standard room price: ')

                    # Data casting
                    id = int(id)
                    total_floors = int(total_floors)
                    rooms_per_floor = int(rooms_per_floor)
                    default_price = float(default_price)

                    if not hotel_service.create_and_save_hotel(id, name, address, total_floors,
                                                               rooms_per_floor, default_room_type, 
                                                               default_price):
                        continue
                elif hotel_op == '2':
                    pass
                # Adding a new room
                elif hotel_op == '3':
                    # (x) show all registered hotels
                    # (x) choose a hotel by its sequential
                    # () create the room (and update its table)
                    # () update the hotel
                    chosen_hotel = hotel_service.choose_hotel()
                    # ...
                    pass
                elif hotel_op == '4':
                    pass
                elif hotel_op == '5':
                    pass
                elif hotel_op == '6':
                    continue
        elif main_op == '2': # --< Manage Guests >--
            pass
        elif main_op == '3': # --< Manage Reservations >--
            pass
        elif main_op == '4': # --< Exit >--
            continue
        
