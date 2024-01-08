def track_low_stock_with_for(dictionary_products: dict[str, int], limit: int = 0) -> None:
    list_products: list[str] = []
    for key, value in dictionary_products.items():
        if value < limit:
            list_products.append(key)
    
    if len(list_products) > 0:
        print('Низкий запас:')
        for key in list_products:
            print(f'{key} - {dictionary_products[key]}')
    else:
        print('Товары с количеством меньше заданного порога отсутствуют')        

track_low_stock_with_for({'apples': 50, 'bananas': 10, 'cherries': 3}, 15)