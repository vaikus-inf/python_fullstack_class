def unique_products(first_store: str, second_store: str):
    first_store_set = set(first_store.split(', '))
    second_store_set = set(second_store.split(', '))
    
    print(f'Только в первом магазине: {", ".join(list(first_store_set.difference(second_store_set)))}')
    print(f'Только во втором магазине: {", ".join(list(second_store_set.difference(first_store_set)))}')
    
unique_products('Хлеб, Молоко, Сыр', 'Молоко, Йогурт, Сок')
unique_products('Кофе, Чай, Сахар', 'Какао, Чай, Сгущенка')