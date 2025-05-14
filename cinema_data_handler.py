
def upload_entry_data(data: dict, new_data: dict, id: str) -> dict | bool:
    
    """
    Adds a new entry (e.g., user, film) to the provided dictionary if the ID doesn't already exist.

    Parameters:
        data (dict): The main dictionary containing existing entries (e.g., users or films).
        new_data (dict): A dictionary representing the new entry to be added.
        id (str): The ID to assign to the new entry.

    Returns:
        dict: The updated dictionary if the new entry was successfully added.
        bool: False if an entry with the same ID already exists.

    Raises:
        TypeError: If 'data' is not a dictionary or 'new_data' is not a dictionary.

    Notes:
        The ID must be unique. If the ID already exists in 'data', the entry will not be added.
    """

    if not isinstance(data, dict):
        raise TypeError("Expected a dictionary for 'data'.")
    if not isinstance(new_data, dict):
        raise TypeError("Expected a dictionary for 'new_data'.")

    if id in data:
        return False

    data[id] = new_data
    return data


def modify_data(data: dict, id: str, section: str, new_data: str | int) -> dict | bool: 

    """
    Modifies a specific field of an entry in the provided dictionary.

    Parameters:
        data (dict): The main dictionary containing entries (e.g., films or users).
        id (str): The ID of the entry to update.
        section (str): The key (field) of the entry to modify (e.g., 'genre', 'age').
        new_data (str | int): The new value to assign to the specified field.

    Returns:
        dict: The updated dictionary if the modification was successful.
        bool: False if the ID or section does not exist, or if the value is already up to date.

    Raises:
        TypeError: If 'data' is not a dictionary, if 'id' or 'section' are not strings,
                   or if 'new_data' is neither a string nor an integer.

    Notes:
        - The function only updates the value if it differs from the current one.
        - If the ID or section is not found, or the value is unchanged, no update is made.
    """

    if not isinstance(data, dict):
        raise TypeError(f"Expected a dict for {data}.")
    
    if not isinstance(new_data, (int, str)):
        raise TypeError(f"Expected a string or an integer for {new_data}.")

    if not all(isinstance(variable, str) for variable in (id, section)):
        raise TypeError("Expected a string, got a non-string instead.")

    if id in data and data[id][section] != new_data:
        data[id][section] = new_data
        return data

    return False      


def delete_data(data: dict, id: str) -> dict | bool:

    """
    Deletes an entry from the provided dictionary based on its ID.

    Parameters:
        data (dict): The dictionary containing the data entries.
        id (str): The ID of the entry to delete.

    Returns:
        dict: The updated dictionary if the entry was successfully deleted.
        bool: False if the ID was not found in the dictionary.

    Raises:
        TypeError: If 'data' is not a dictionary or 'id' is not a string.

    Notes:
        - The function permanently removes the entry associated with the given ID.
        - No changes are made if the ID does not exist.
    """

    if not isinstance(id, str):
        raise TypeError("Expected a string for 'id'.")
    if not isinstance(data, dict):
        raise TypeError("Expected a dictionary for 'data'.")
    
    if id in data:
        data.pop(id)
        return data
    
    return False


def film_reservation(info: dict, film_id: str) -> list:

    """
    Retrieves reservation details for a specific film from the given data.

    Parameters:
        info (dict): A dictionary containing film data, where each key is a film ID (as a string)
                     and each value is a dictionary with film details such as title, time, price, and theater.
        film_id (str): The ID of the film to retrieve details for.

    Returns:
        list: A list containing the film's title, time, price, and theater, in that order.

    Raises:
        TypeError: If 'info' is not a dictionary or 'film_id' is not a string.
    """
    
    if not isinstance(info, dict):
        raise TypeError("Expected a dict for info, got a non-string instead.")
    if not isinstance(film_id, str):
        raise TypeError("Expected a string for film_id, got a different type.")

    if film_id in info:
        return [film_id,
                info[film_id]["title"], 
                info[film_id]["time"], 
                info[film_id]["price"], 
                info[film_id]["theater"]]


def update_available_seats(id: str, seats: int, film_data: dict, action: str) -> int | bool:

    """
    Modifies the number of available seats for a film based on reservation or cancellation.

    Parameters:
        id (str): The ID of the film.
        seats (int): The number of seats to reserve or cancel.
        film_data (dict): The dictionary containing film data.
        action (str): The action to perform: 'reserve' or 'cancel'.

    Returns:
        dict: The updated film_data dictionary if successful.
        bool: False if the operation cannot be completed (e.g., insufficient seats or invalid ID/action).

    Raises:
        TypeError: If the input types are incorrect.
        ValueError: If 'action' is not 'reserve' or 'cancel'.
    """

    if not isinstance(id, str):
        raise TypeError("Expected a string for id, got a different type.")
    if not isinstance(seats, int):
        raise TypeError("Expected an integer for reserved_seats, got a different type.")
    if not isinstance(film_data, dict):
        raise TypeError("Expected a dict for reserved_seats, got a different type.")
    if action not in {"reserve", "cancel"}:
        raise ValueError("Action must be 'reserve' or 'cancel'.")

    if id not in film_data:
        return False

    current = film_data[id]["availableSeats"]

    if action == "reserve":
        if current >= seats:
            film_data[id]["availableSeats"] -= seats
            return film_data
        
    elif action == "cancel":
        film_data[id]["availableSeats"] += seats
        return film_data

    return False