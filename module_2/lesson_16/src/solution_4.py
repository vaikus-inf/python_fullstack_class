def shelves_for_goods(number_of_shelves: int, sales_list: str) -> list:
    return [[int(item) for item in sales.split(',')] for sales in sales_list.split(';')]


print(f'Продажи: {shelves_for_goods(2, "5,3;7,2")}')
print(f'Продажи: {shelves_for_goods(3, "2,6,4;3,5,7;1,2,3")}')
