from utils import load_JSON_file, save_JSON_file, create_JSON_file


def to_dict(title: str="N/A", genre: str="N/A", info: str="N/A", time: str="N/A", theater: str="N/A", price: str="N/A", available_seats: int=0) -> dict:

    """
    Creates a dictionary representing a movie or show with the provided details.

    Parameters:
        title (str): The title of the movie or show. Default is "N/A".
        genre (str): The genre of the movie or show. Default is "N/A".
        info (str): A short description or additional information. Default is "N/A".
        time (str): The scheduled time of the screening. Default is "N/A".
        theater (str): The name or identifier of the theater. Default is "N/A".
        price (str): The price of a ticket. Default is "N/A".
        available_seats (int): The number of available seats. Default is 0.

    Returns:
        dict: A dictionary containing all the provided details with appropriate keys.
    """

    return {
            "title": title,
            "genre": genre,
            "info": info,
            "time": time,
            "theater": theater,
            "price": price,
            "availableSeats": available_seats
        }
    

def upload_film_info(filename: str, new_film: dict) -> bool:
    
    """
    Adds a new film to the JSON file if it doesn't already exist.

    Parameters:
        filename (str): The path to the JSON file containing film data.
        new_film (dict): A dictionary representing the film to be added.

    Returns:
        bool: True if the film was successfully added, False if it already exists.

    Raises:
        TypeError: If 'filename' is not a string or 'new_film' is not a Film instance.

    Notes:
        Film titles are compared case-insensitively to prevent duplicate entries.
        If the film already exists, the file will not be modified.
    """
        
    if not isinstance(filename, str):
        raise TypeError("Expected a string, got a non-string instead.")
    if not isinstance(new_film, dict):
        raise TypeError("Expected a dictionary, got a different type.")
    
    film_info = load_JSON_file(filename)

    for film in film_info["film"]:
        if film["title"].lower() == new_film["title"].lower():
            print(f"The film {new_film["title"]} is already in the database.")
            return False

    film_info["film"].append(new_film)

    save_JSON_file(film_info, filename)

    return True


def modify_film_info(filename: str, film_title: str, category: str, new_data: str | int) -> bool: 

    """
    Modifies a specific key (category) of a film entry in the JSON file.

    Parameters:
        filename (str): The path to the JSON file containing film data.
        film_title (str): The title of the film to be updated.
        category (str): The key of the film to modify (e.g., 'genre', 'price').
        new_data (str | int): The new value to assign to the specified field.

    Raises:
        TypeError: If 'filename', 'film_title', or 'category' are not strings,
                   or if 'new_data' is neither a string nor an integer.

    Notes:
        - The function updates the key only if the current value differs from the new one.
        - No changes will be saved if the film is not found or the value is already up to date.
    """

    if not isinstance(new_data, (int, str)):
        raise TypeError(f"Expected a string or an integer for {new_data}.")

    if not all(isinstance(variable, str) for variable in (filename, film_title, category)):
        raise TypeError("Expected a string, got a non-string instead.")
    
    film_info = load_JSON_file(filename)

    for film in film_info["film"]:
        if film["title"] == film_title and film[category] != new_data:
            film[category] = new_data
        else:
            print("This film doesn't exist in the database or the data already exist.")
            return False

    save_JSON_file(film_info, filename)      

    return True      


def delete_film(filename: str, film_title: str):

    film_info = load_JSON_file(filename)
        
    for i in range(len(film_info["film"])):
        if film_info["film"][i]["title"] == film_title:
            film_info["film"].pop(i)
            
    save_JSON_file(film_info, filename)