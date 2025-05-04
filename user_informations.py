from utils import load_JSON_file, save_JSON_file
from film_informations import modify_film_info

def user_data(id: int, name: str, surname: str, reserved_film: str, reserved_seats: str) -> dict:

    return {
        "name": name,
        "surname": surname,
        "reservedFilm": reserved_film,
        "reservedSeats": reserved_seats
        }


def make_user_id(info: dict) -> int:

    user_id = len(info["userData"])
    
    return user_id + 1


def film_reservation(info: dict, film_id: int) -> list:

    if not isinstance(info, dict):
        raise TypeError("Expected a string for filename, got a non-string instead.")
    if not isinstance(film_id, int):
        raise TypeError("Expected an integer for film_id, got a different type.")

    for film in info["film"]:
        if film["id"] == film_id:
            return [film["title"], film["time"], film["price"], film["theater"]]


    
def check_id_exist(all_data, id, section):

    return any(data["id"] == id for data in all_data[section])
 