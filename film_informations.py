from utils import load_JSON_file, save_JSON_file, create_JSON_file


class Film:

    def __init__(self, title: str="N/A", genre: str="N/A", info: str="N/A", time: str="N/A", theater: str="N/A", price: float=0, available_seats: int=0):
        
        self.title = title
        self.genre = genre
        self.info = info
        self.time = time
        self.theater = theater
        self.price = price
        self.available_seats = available_seats


    def to_dict(self):

        return {
            "title": self.title,
            "genre": self.genre,
            "info": self.info,
            "time": self.time,
            "theater": self.theater,
            "price": self.price,
            "availableSeats": self.available_seats
        }
    

def upload_film_info(filename: str, new_film: Film):
    
    film_info = load_JSON_file(filename)

    for film in film_info["film"]:
        if film["title"] == new_film.title:
            print("This film already exist.")
            return

    film_info["film"].append(new_film.to_dict())

    save_JSON_file(film_info, filename)


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