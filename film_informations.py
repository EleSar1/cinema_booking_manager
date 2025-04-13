from utils import load_JSON_file, save_JSON_file, create_JSON_file


class Film:

    """
    A class to represent a film in the cinema system.

    Attributes:
        title (str): The title of the film.
        genre (str): The genre of the film.
        info (str): Additional information or description of the film.
        time (str): The showtime of the film.
        theater (str): The name or number of the theater where the film is shown.
        price (float): The ticket price for the film.
        available_seats (int): The number of available seats for the film.

    Methods:
        to_dict():
            Returns a dictionary representation of the film instance,
            suitable for JSON serialization.
    """

    def __init__(self, title: str="N/A", genre: str="N/A", info: str="N/A", time: str="N/A", theater: str="N/A", price: float=0, available_seats: int=0):
        
        """
        Initializes a Film object with optional details.

        Parameters:
            title (str): The title of the film. Defaults to "N/A".
            genre (str): The genre of the film. Defaults to "N/A".
            info (str): Additional film info or description. Defaults to "N/A".
            time (str): The showtime of the film. Defaults to "N/A".
            theater (str): The theater where the film is shown. Defaults to "N/A".
            price (float): The ticket price. Defaults to 0.
            available_seats (int): Number of available seats. Defaults to 0.
        """
            
        self.title = title
        self.genre = genre
        self.info = info
        self.time = time
        self.theater = theater
        self.price = price
        self.available_seats = available_seats


    def to_dict(self):

        """
        Converts the Film instance into a dictionary format.

        Returns:
            dict: A dictionary with keys matching the film's attributes,
                  formatted for JSON serialization.
        """

        return {
            "title": self.title,
            "genre": self.genre,
            "info": self.info,
            "time": self.time,
            "theater": self.theater,
            "price": self.price,
            "availableSeats": self.available_seats
        }
    

def upload_film_info(filename: str, new_film: Film) -> bool:
    
    """
    Adds a new film to the JSON file if it doesn't already exist.

    Parameters:
        filename (str): The path to the JSON file containing film data.
        new_film (Film): An instance of the Film class representing the film to be added.

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
    if not isinstance(new_film, Film):
        raise TypeError("Expected a Film instance, got a different type.")
    
    film_info = load_JSON_file(filename)

    for film in film_info["film"]:
        if film["title"].lower() == new_film.title.lower():
            print(f"The film {new_film.title} is already in the database.")
            return False

    film_info["film"].append(new_film.to_dict())

    save_JSON_file(film_info, filename)

    return True


def modify_film_info(filename: str, film_title: str, category: str, new_data: str | int): 

    if not isinstance(new_data, (int, str)):
        raise TypeError(f"Expected a string or an integer for {new_data}.")

    if not all(isinstance(variable, str) for variable in (filename, film_title, category)):
        raise TypeError("Expected a string, got a non-string instead.")
    
    film_info = load_JSON_file(filename)

    for film in film_info["film"]:
        if film["title"] == film_title and film[category] != new_data:
            film[category] = new_data

    save_JSON_file(film_info, filename)            