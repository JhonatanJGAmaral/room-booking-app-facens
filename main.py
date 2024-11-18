from models.guest import Guest
from models.hotel import Hotel
from models.reservation import Reservation
from models.room import Room
from repositories.hotel_repository import HotelRepository

# Create the Initials class

def show_main_menu():
    return  (f'\n\n{'-' * 50}' '\nROOM BOOKING APP\n' f'{'-' * 50}'
             '\n\t1 - Manage Hotels'
             '\n\t2 - Manage Guests'
             '\n\t3 - Manage Reservations'
             '\n\t4 - Exit\n'
             '\nChoose an option above: ')

def show_hotel_menu():
    return (f'\n{'-' * 20}' '\nHotel Management\n' f'{'-' * 50}'
            "\n\t1 - Register a new hotel"
            "\n\t2 - Change hotel name"
            "\n\t3 - Register a new room"
            "\n\t4 - Delete a room"
            "\n\t5 - Delete hotel record"
            "\n\t6 - Return to main menu"
            '\nChoose an option above: ')

# def show_registering_hotel_menu(self):
#     return 

if __name__ == '__main__':
    hotel_repository = HotelRepository()
    main_op = ''
    while(main_op != '4'):
        main_op = input(show_main_menu())

        if main_op == '1':
            hotel_op = ''
            while hotel_op != '6':
                hotel_op = input(show_hotel_menu())

                # Registering a new hotel
                if hotel_op == '1':
                    id = 1 
                    name = input('\nEnter hotel name: ')
                    address = input('\nEnter hotel address: ')
                    total_floors = input('\nEnter the number of floors: ')
                    rooms_per_floor = input('\nEnter the number of rooms per floor: ')
                    default_room_type = input('\nEnter the standard room type: ')
                    default_price = input('\nEnter the standard room price: ')

                    # Data casting
                    id = int(id)
                    total_floors = int(total_floors)
                    rooms_per_floor = int(rooms_per_floor)
                    default_price = float(default_price)

                    hotel = Hotel(id, name, address, total_floors, 
                                 rooms_per_floor, default_room_type, default_price)
                    if not hotel_repository.save(hotel):
                        continue
                elif hotel_op == '2':
                    pass
                elif hotel_op == '3':
                    pass
                elif hotel_op == '4':
                    pass
                elif hotel_op == '5':
                    pass
                elif hotel_op == '6':
                    continue

            # hotel = Hotel(1, 'Transilvania 2', 'Champ Elyssés', 4, 4)
            # if not hotel_repository.save(hotel):
            #     continue
        elif main_op == '2':
            pass
        elif main_op == '3':
            pass
        elif main_op == '4':
            continue
        
