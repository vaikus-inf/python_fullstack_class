import redis

r = redis.Redis(host='localhost', port=6379, db=0)

def add_task(task):
    r.lpush('tasks', task)
    print(f'Task "{task}" added to the list.')

def view_tasks():
    tasks = r.lrange('tasks', 0, -1)

    if tasks:
        print('Tasks list:')
        for i, task in enumerate(tasks, 1):
            print(f'{i}. {task.decode("utf-8")}')
    else:
        print('Task list is empty.')

def remove_task(task):
    r.lrem('tasks', 1, task)
    print(f'Task "{task}" is deleted.')

def clear_tasks():
    r.delete('tasks')
    print('To-do list is cleared.')

def menu():
    while True:
        print('\nMenu:')
        print('1. Add a task:')
        print('2. View tasks:')
        print('3. Delete a task:')
        print('4. Clear task list:')
        print('5. Exit:')

        choice = input('Choose an option: ')

        if choice == '1':
            task = input('Enter a task name: ')
            add_task(task)
        elif choice == '2':
            view_tasks()
        elif choice == '3':
            task = input('Enter a task name for deletion: ')
            remove_task(task)
        elif choice == '4':
            clear_tasks()
        elif choice == '5':
            print('Quitting the app.')
            break
        else:
            print('Incorrect choice. Please, try again.')


if __name__ == '__main__':
    menu()
