def authorization(func):
    def wrapper(login, password):
        user_dictionary = {'Роман': 'correctpassword'}
        if login in user_dictionary and password == user_dictionary[login]:
            func('Доступ получен. Данные: ...')
        else:
            func('В доступе отказано!')
    return wrapper

@authorization
def access_client_data(text) -> None:
    print(text)

access_client_data('Роман', 'correctpassword')
access_client_data('Олег', 'wrongpassword')