def shelves_for_goods(number_of_shelves: int, shelf_lengths: str) -> list:
    return [[int(item), 0] for item in shelf_lengths.split(', ')]


print(f'Полки: {shelves_for_goods(3, "4, 5, 6")}')
print(f'Полки: {shelves_for_goods(3, "3, 4")}')
