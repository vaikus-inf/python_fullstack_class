def count_specific_items_with_while(list_products: list[str], category: str) -> None:
    i = number_of_products = 0
    while i < len(list_products):
        if list_products[i] == category:
            number_of_products += 1
        i += 1                
    
    print(f"Количество '{category}': {number_of_products}")

count_specific_items_with_while(['fruit', 'toy', 'fruit', 'toy'], 'toy')
count_specific_items_with_while(['clothes', 'clothes', 'clothes'], 'clothes')