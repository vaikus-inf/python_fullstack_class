def authorization(func):
    def wrapper(login, password):
        user_dictionary = {'Роман': 'correctpassword'}
        return func(login in user_dictionary and password == user_dictionary[login])
    return wrapper

@authorization
def access_client_data(access) -> None:
    if access:
        print('Доступ получен. Данные: ...')
    else:
        print('В доступе отказано!')

access_client_data('Роман', 'correctpassword')
access_client_data('Олег', 'wrongpassword')