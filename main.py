from file_handling import *
from cinema_data_handler import *
from data_builders import *

def display_JSON(all_data: dict):

    """
    Prints the content of a dictionary containing film data in a readable format.

    Parameters:
    all_data (dict): A dictionary where each key is a film ID and the value is another
                     dictionary containing details about the film (e.g. title, genre, time).

    Returns:
    None
    """

    for id in all_data:
        print(f"\nFilm ID: {id}")
        for section in all_data[id]:
            print(f"{section}: {all_data[id][section]}")
        print("\n")


def customer():

    """
    Handles the customer interaction flow.

    Allows the user to:
    1. Make a reservation.
    2. Edit an existing reservation.
    3. Delete a reservation.

    Loads and modifies data from 'userData.json' and 'cinemaData.json'.
    """

    print("Welcome, user. Please, press:")
    print("1 - if you want to make a reservation.")
    print("2 - if you want to edit a reservation.")
    print("3 - if you want to delete a reservation.")

    choice = 0
    while choice not in {1,2,3}:
        try:    
            choice = int(input("-> "))
            if choice not in {1,2,3}:
                print("Error. Please make sure to enter an existing choice.")
        except ValueError:
            print("Error. Expected an integer.")
    
    user_filename = "userData.json"
    film_filename = "cinemaData.json"
    if choice == 1:
        # Reservation process
        film_info = load_JSON_file(film_filename)
        print("\nAvailable films:\n")
        display_JSON(film_info)

        print("Please enter your:")
        name = input("name -> ")
        surname = input("surname -> ")

        print("Enter the projection ID that you want to reserve: ")
        film_id = ""
        while film_id not in film_info:
            film_id = input("-> ")
            if film_id not in film_info:
                print("ID not found. Please enter a valid ID.")
        
        print("How many seats do you want to reserve?")
        seats = 0
        while seats < 1 or seats > film_info[film_id]["availableSeats"]:
            try:
                seats = int(input("-> "))
                if seats < 1:
                    print("Error. You should select more than 0 seats.")
                elif seats > film_info[film_id]["availableSeats"]:
                    print("Error. This quantity of seats is not available.")
            except ValueError:
                print("Expected an integer.")
        
        reservation = film_reservation(film_info, film_id)
        user = create_user_data(name, surname, reservation, seats)
        user_file = load_JSON_file(user_filename)
        user_id = make_id(user_file)
        data_to_upload = upload_entry_data(user_file, user, user_id)

        if data_to_upload:
            save_JSON_file(data_to_upload, user_filename)
            print("Data saved successfully!")
        
        new_available_seats = update_available_seats(film_id, seats, film_info, "reserve")
        if new_available_seats:
            save_JSON_file(film_info, film_filename)

    if choice == 2:
        # Edit existing reservation
        user_data = load_JSON_file(user_filename)
        print("Please enter your reservation id:")
        reservation_id = 0
        while reservation_id not in user_data:
            reservation_id = input("-> ")
            if reservation_id not in user_data:
                print("ID not found, make sure to enter a valid ID.")

        print(f"Welcome, {user_data[reservation_id]["name"]} {user_data[reservation_id]["surname"]}.")
        print("\nYou reserved the film:")
        for film_data in user_data[reservation_id]["reservedFilm"]:
            print(film_data)
        print(f"{user_data[reservation_id]["reservedSeats"]} reserved seats")

        print("\nWhat data do you want to modify (1 for 'name', 2 for 'surname', 3 for 'seats')?")
        print("If you want to change the film reservation, please delete your reservation.")

        section = 0
        while section not in {1,2,3}:
            try:
                section = int(input("-> "))
                if section not in {1,2,3}:
                    print("Invalid input. Please enter a number between 1 and 3.")
            except TypeError:
                print("Expected an integer, got a different type.")

        if section == 1:

            new_data = input("Please type here the new name: ")
            section_name = "name"

        elif section == 2:

            new_data = input("Please type here the new surname: ")
            section_name = "surname"

        elif section == 3: 

            film_info = load_JSON_file(film_filename)
            film_id = user_data[reservation_id]["reservedFilm"][0]
            new_data = 0
            print("Please enter the new amount of seats that you want to reserve:")
            while new_data < 1 or new_data > film_info[film_id]["availableSeats"]:
                try:
                    new_data = int(input("-> "))
                    if new_data < 1:
                        print("Error. You should select more than 0 seats.")
                    elif new_data > film_info[film_id]["availableSeats"]:
                        print("Error. This quantity of seats is not available.")
                except ValueError:
                    print("Expected an integer.")
            
            new_available_seats = update_available_seats(film_id, new_data, film_info, "cancel")
            if new_available_seats:
                save_JSON_file(new_available_seats, film_filename)

            section_name = "reservedSeats"
        
        new_user_data = modify_data(user_data, reservation_id, section_name, new_data)
        if new_user_data:
            save_JSON_file(new_user_data, user_filename)
            print("Data saved successfully!")

    elif choice == 3:
        # Delete a reservation
        user_data = load_JSON_file(user_filename)
        film_data = load_JSON_file(film_filename)
        print("What reservation you want to delete? Please enter the reservation ID:")

        reservation_id = 0
        while reservation_id not in user_data:
            reservation_id = input("-> ")
            if reservation_id not in user_data:
                print("ID not found, please enter a valid ID.")
        
        print("Selected:")
        for film_data in user_data[reservation_id]["reservedFilm"]:
            print(film_data)
        print(f"{user_data[reservation_id]["reservedSeats"]} reserved seats\n")
        
        print("Are you sure (y/n)?")
        confirmation = None

        while confirmation not in {"y", "n"}:
            confirmation = input("-> ").lower()
            if confirmation not in {"y", "n"}:
                print("Please enter a valid input (y/n).")

        if confirmation == "y":      
            deleted = delete_data(user_data, reservation_id)
            if deleted:
                save_JSON_file(deleted, user_filename)
                print("Your reservation was deleted successfully!")
                

def administrator():
    
    """
    Handles the administrator interaction flow.

    Allows the administrator to:
    1. Add a new film to the database.
    2. Edit an existing film.
    3. Delete a film.

    Works with the 'cinemaData.json' file.
    """

    print("Welcome to the administrator section. Please, press:")
    print("1 - if you want to insert a film to the database.")
    print("2 - if you want to modify a film.")
    print("3 - if you want to delete a film.")

    choice = 0
    while choice not in {1,2,3}:
        try:    
            choice = int(input("-> "))
            if choice not in {1,2,3}:
                print("Error. Please make sure to enter an existing choice.")
        except ValueError:
            print("Error. Expected an integer.")
    
    filename = "cinemaData.json"

    if choice == 1:
        # Insert new film
        id = 0
        film_info = load_JSON_file(filename)
        display_JSON(film_info)

        while id < 1 or str(id) in film_info:
            try:
                id = int(input("Please enter an id for the new projection: "))
                if str(id) in film_info:
                    print("This id already exist. Please enter a new id.")
            except ValueError:
                print("The ID should be a number.")

        title = input("Please enter the title: ")
        genre = input("Please enter the genre (use / if more than one): ")
        time = input("Please enter the time of the projection (e.g. 18:00): ")
        theater = input("Please enter the name/number of the theater: ")
        price = input("Please enter the price: ")
        available_seats = 0
        while available_seats < 1:
            try:
                available_seats = int(input("Please enter the available seats in the theater: "))
            except ValueError:
                print("The number of seats must be an integer.")
                
        new_film = create_show_data(title, genre, time, theater, price, available_seats)
        film_info = upload_entry_data(film_info, new_film, id)
        if film_info:
            save_JSON_file(film_info, filename)
            print("Data saved successfully!")


    elif choice == 2:
        # Modify existing film
        film_info = load_JSON_file(filename)
        display_JSON(film_info)

        id = ""
        while id not in film_info:
            id = input("Please enter the ID of the film that you want to edit: ")
            if id not in film_info:
                print("Error. This ID does not exist.")

        print("What section you want to edit (e.g. time, price)?")
        section = ""
        while section not in film_info[id]:
            section = input("-> ")
            if section not in film_info[id]:
                print("Section not found. Please enter a valid section.")

        print("Please enter the new data:")
        new_data = input("-> ")
        if new_data.isdigit():
            new_data = int(new_data)    
        
        update_data = modify_data(film_info, id, section, new_data)
        if update_data:
            save_JSON_file(update_data, filename)
            print("Data saved successfully!")

    elif choice == 3:
        # Delete a film
        film_info = load_JSON_file(filename)
        display_JSON(film_info)

        print("What film you want to delete? Please choose an ID.")
        id = ""
        while id not in film_info:
            id = input("Please enter the ID of the film that you want to delete: ")
            if id not in film_info:
                print("Error. This ID does not exist.")

        deleted_film = delete_data(film_info, id)
        if deleted_film: 
            save_JSON_file(deleted_film, filename)
            print("Data saved successfully!")

def main():
    print("Are you a customer o an administrator?")

    privilege = None
    while privilege not in {"c", "a"}:
        privilege = input("Please press 'a' for admin, 'c' for customer: ").lower()
        if privilege not in {"c", "a"}:
            print("Input error. Please make sure to press 'a' or 'c'.")

    if privilege == "a":
        administrator()
    else:
        customer()


if __name__ == "__main__":
    main()