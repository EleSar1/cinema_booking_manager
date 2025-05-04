from utils import create_JSON_file, upload_data
from film_informations import * 
from user_informations import * 

def display_films(filename):

    films = load_JSON_file(filename)
    
    if len(films["film"]) == 0:
        print("Film list is empty.\n")
    else:
        for i in range(len(films["film"])):
            print("")
            for key, item in films["film"][i].items():
                print(f"{key}: {item}")


def customer(filename: str):
    
    print("\nAvailable films:")
    display_films(filename)

    print("\nPlease enter your data:\n")
    name = ""
    while len(name) < 1:
        name = input("Name: ")
        if len(name) < 1: 
            print("Invalid length, please make sure to enter a valid name.")
    
    surname = ""
    while len(surname) < 1:
        surname = input("Name: ")
        if len(surname) < 1: 
            print("Invalid length, please make sure to enter a valid surname.")

    print(f"\nHello {name}.")
    print("Do you want to make, modify or delete your reservation?")
    choice = int(input("(1: to make a reservation, 2: to modify a reservation, 3: to delete a reservation.)"))

    if choice == 1:

        data = load_JSON_file(filename)
        
        film_id = None
        while not check_id_exist(data, film_id, "film"):
            try:
                film_id = int(input("Please enter the film id: "))
            except ValueError:
                print("Expected an integer, got a different value.")

        reserved_film = film_reservation(data, film_id)

        reserved_seats = 0
        while reserved_seats < 1:
            try:
                reserved_seats = int(input("How many seats you want to reserve? "))
            except ValueError:
                print("Expected an integer, got a different value.")
        
        reservation_id = make_user_id(data)
        print(f"Your id is {reservation_id}. Please note that.")

        new_data = user_data(reservation_id, name, surname, reserved_film, reserved_seats)
        
        for film in data["film"]:
            if film["id"] == film_id:
                old_available_seats = film["availableSeats"]
        new_available_seats = old_available_seats - reserved_seats

        modify_film_info(filename, film_id, "availableSeats", new_available_seats)
        upload_data(filename, new_data, "userData")

    elif choice == 2:

        all_data = load_JSON_file(filename)
        try: 
            id = int(input("Please enter your reservation id: "))
        except ValueError:
            print("Expected an integer, got a different value.")

        if not id_exist(all_data, id, "userData"): 
            print("Id not found.")
        else:
            for data in all_data["userData"]:
                if data["id"] == id:
                    



def admin(filename: str):

    create_JSON_file(filename)
    display_films(filename)

    add_film = input("Do you want to add a new film (Y/N)? ").upper()
    if add_film == "Y":
        id = 0
        while id < 1:
            try: 
                id = int(input("Enter a new film id (id should be an integer): "))
            except ValueError:
                print("Expected an integer, got a non-int.")

        title = input("Please enter the title: ")
        genre = input("Please enter the genre (use / if more than one): ")
        info = input("Please enter a brief description: ")
        time = input("Please enter the time of the projection (e.g. 18:00): ")
        theater = input("Please enter the name/number of the theater: ")
        price = input("Please enter the price: ")

        available_seats = 0
        while available_seats < 1:
            try:
                available_seats = int(input("Please enter how many seats are in the theater: "))
            except ValueError:
                print("Expected an integer, got a non-int.")

        new_film = to_dict(id, title, genre, info, time, theater, price, available_seats)

        if upload_data(filename, new_film, "film") == True:
            print(f"Film added successfully to {filename}.")
            print("\nUpdated film list:")
            display_films(filename)
        else: 
            print(f"The film with id {new_film["id"]} is already in the database.")

    modifications = None
    while modifications not in ["d", "m", "0"]:
        print("\nDo you want to modify or delete some data?")
        modifications = input("d: to delete, m: to make modifications, 0: to exit\n").lower()
        if modifications not in ["d", "m", "0"]:
            print("Expected d, m or 0 as value.")
         
    if modifications == "d":

        print("What film you want to delete?")
        id_to_del = ""
        while not isinstance(id_to_del, int):
            try:
                id_to_del = int(input("Please enter the id of the film you want to delete: "))
            except ValueError:
                print("Expected an integer, got a non-int value.")
        
        if delete_film(filename, id_to_del) == True:
            print("Film correcly deleted!")
            display_films(filename)
        else: 
            print(f"Error. Film with id {id_to_del} not found.")

    elif modifications == "m":

        film = load_JSON_file(filename)
        if len(film["film"]) == 0:
            print("There are no films to modify because the list is empty.")
        else:
            pass



def main():

    filename = "cinemaData.json"

    user_role = "N/A"
    while user_role not in ["a", "c"]:
        user_role = input("Are you an admin or a customer? (press 'a' for admin or 'c' for customer) " ).lower()
        if user_role not in ["a", "c"]:
            print("Invalid input. Please type 'a' for admin or 'c' customer.")

    if user_role == "a":
        admin(filename)
    elif user_role == "c":
        customer(filename)


if __name__ == "__main__":
    main() 