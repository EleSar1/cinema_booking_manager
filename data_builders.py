def create_user_data(name: str, surname: str, reserved_film: list, reserved_seats: int) -> dict:

    """
    Creates a dictionary containing user reservation details.

    Parameters:
        name (str): The first name of the user.
        surname (str): The surname of the user.
        reserved_film (list): A list containing information about the reserved film,
                              such as [title, genre, time].
        reserved_seats (int): The number of seats the user has reserved.

    Returns:
        dict: A dictionary with the user's name, surname, film details, and number of reserved seats.
    """

    return {
        "name": name,
        "surname": surname,
        "reservedFilm": reserved_film,
        "reservedSeats": reserved_seats
        }


def create_show_data(title: str="N/A", genre: str="N/A", time: str="N/A", theater: str="N/A", price: str="N/A", available_seats: int=0) -> dict:

    """
    Creates a dictionary representing a movie or show with the provided details.

    Parameters:
        title (str): The title of the movie or show. Default is "N/A".
        genre (str): The genre of the movie or show. Default is "N/A".
        time (str): The scheduled time of the screening. Default is "N/A".
        theater (str): The name or identifier of the theater. Default is "N/A".
        price (str): The price of a ticket. Default is "N/A".
        availableSeats (int): The number of available seats. Default is 0.

    Returns:
        dict: A dictionary containing all the provided details with appropriate keys.
    """

    return {
                "title": title,
                "genre": genre,
                "time": time,
                "theater": theater,
                "price": price,
                "availableSeats": available_seats
            }


def make_id(all_data: dict) -> str:

    """
    Generates a new unique ID based on the keys of the provided dictionary.

    Parameters:
        all_data (dict): A dictionary where keys are existing IDs (as strings or integers).

    Returns:
        str: A new ID that does not exist in the dictionary, as a string.
    """

    existing_ids = set()

    for id in all_data:
        existing_ids.add(int(id))
    
    if existing_ids:
        last_id = max(existing_ids)
        new_id = last_id + 1
        return str(new_id)
    else:
        last_id = 1
        return last_id