smartphone: list[dict[str, int]] = [
    {'serial_number': 12431, 'year_release': 2020, 'price': 15000},
    {'serial_number': 10895, 'year_release': 2022, 'price': 32000},
    {'serial_number': 43678, 'year_release': 2019, 'price': 16000},
    {'serial_number': 21510, 'year_release': 2024, 'price': 48000},
    {'serial_number': 71156, 'year_release': 2023, 'price': 39000}
]

def sort_objects(list_dictionaries: list[dict[str, int]], string_key: str) -> list[dict[str, int]]:
    list_dictionaries.sort(key = lambda dictionary: dictionary[string_key])
    return list_dictionaries


sorting_results = sort_objects(smartphone, 'year_release')

for item in sorting_results:
    print(item)
