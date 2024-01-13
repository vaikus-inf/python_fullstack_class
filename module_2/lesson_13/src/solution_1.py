def decorator_change_price(func):
    def wrapper(*args):
        if args[1] > args[2]:
            print(f'Цена на {args[0]} изменилась! {args[1]} > {args[2]}')
        elif args[1] < args[2]:
            print(f'Цена на {args[0]} изменилась! {args[1]} < {args[2]}')
        else:
            print(f'Цена на {args[0]} не изменилась!')
    return wrapper   
    

@decorator_change_price
def change_price(data) -> None:
    pass

change_price('Кресло', 5000, 4500)
change_price('Стол', 8000, 7600)