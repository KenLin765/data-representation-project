import requests
import json
import csv
from collections import Mapping

def flatten_dict(d, parent_key='', sep='_'):
    """
    Flatten a nested dictionary.
    """
    items = []
    for k, v in d.items():
        new_key = f"{parent_key}{sep}{k}" if parent_key else k
        if isinstance(v, Mapping):
            items.extend(flatten_dict(v, new_key, sep=sep).items())
        elif v is not None:  # Only include non-empty values
            items.append((new_key, v))
    return dict(items)

def fetch_countries_data():
    url = "https://restcountries.com/v3.1/all"
    response = requests.get(url)

    if response.status_code == 200:
        return response.json()
    else:
        print(f"Error fetching data. Status code: {response.status_code}")
        return None

def save_to_json(data, filename="countries.json"):
    with open(filename, "w", encoding="utf-8") as json_file:
        json.dump(data, json_file, ensure_ascii=False, indent=2)


if __name__ == "__main__":
    countries_data = fetch_countries_data()

    if countries_data:
        save_to_json(countries_data)
        print("Data saved to JSON file.")
