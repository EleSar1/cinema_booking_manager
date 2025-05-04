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


def upload_data(filename: str, new_entry: dict, section: str) -> bool:
    
    """
    Adds a new entry to the specified section of the JSON file if it doesn't already exist.

    Parameters:
        filename (str): The path to the JSON file containing data.
        new_entry (dict): A dictionary representing the entry to be added.
        section (str): The key in the JSON data where the new entry should be added (e.g., 'film', 'userData').

    Returns:
        bool: True if the entry was successfully added, False if it already exists.

    Raises:
        TypeError: If 'filename' or 'section' is not a string or 'new_entry' is not a dict.

    Notes:
        Entry IDs are compared to prevent duplicate entries.
        If an entry with the same ID already exists, the file will not be modified.
    """
        
    if not all(isinstance(variable, str) for variable in (filename, section)):
        raise TypeError("Expected a string, got a non-string instead.")
    if not isinstance(new_entry, dict):
        raise TypeError("Expected a dictionary for new_entry, got a different type.")
    
    data = load_JSON_file(filename)

    if section not in data:
        raise ValueError(f"Section '{section}' not found in the JSON file.")
    
    for entry in data[section]:
        if entry["id"] == new_entry["id"]:
            return False

    data[section].append(new_entry)

    save_JSON_file(data, filename)

    return True
