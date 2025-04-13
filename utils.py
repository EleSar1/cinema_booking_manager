import os
import json

def create_JSON_file(filename: str):

    """
    Creates a new JSON file with default structure if the file does not exist or is empty.

    Parameters:
        filename (str): The name of the JSON file to check or create.

    Returns:
        dict: A dictionary with the default structure containing 'film' and 'userData' keys.
    """

    if not os.path.exists(filename) or os.path.getsize(filename) == 0:
        print("File not found or empty. Will be created a new file.")
        film_info = {"film": [],
                     "userData": []}

        save_JSON_file(film_info, filename)
        return film_info
    

def load_JSON_file(filename: str) -> dict:

    """
    Loads data from a JSON file. If the file is corrupted or contains invalid JSON, 
    it initializes the file with a default structure.

    Parameters:
        filename (str): The name of the JSON file to load.

    Returns:
        dict: A dictionary containing the JSON data. Returns a default structure
              with 'film' and 'userData' keys if the file is corrupted.
    """

    if not isinstance(filename, str):
        raise TypeError("Expected a string, got a non-string.")

    try:
        with open(filename, mode="r") as file:
            film_info = json.load(file)
    
    except json.JSONDecodeError:
        print("File JSON is corrupted. Will be initialized again.")
        film_info = {"film": [],
                     "userData": []}
        
        save_JSON_file(film_info, filename)
             
    return film_info


def save_JSON_file(data: dict, filename: str):

    """
    Saves a dictionary to a JSON file with indentation for readability.

    Parameters:
        data (dict): The data to be saved to the JSON file.
        filename (str): The name of the file where the data will be saved.
    """
    
    with open(filename, mode="w") as file:
        json.dump(data, file, indent=4)
    
