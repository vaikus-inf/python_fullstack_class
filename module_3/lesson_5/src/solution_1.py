# Бот-ассистент "Ромашка"

from telebot import TeleBot
from telebot.types import Message
from dotenv import load_dotenv
from datetime import datetime
import os

class Task:
    def __init__(self, title, description, tag):
        self.date = datetime.now().strftime('%d-%m-%Y')
        self.title = title
        self.description = description
        self.tag = tag

    def __str__(self):
        return f'{self.date} - {self.title} - {self.description} {self.tag}'

# Загрузка переменных окружения
load_dotenv('.env')
TG_TOKEN = os.getenv('TG_TOKEN')

# Сохраняем инициализированный объект бота
bot =TeleBot(TG_TOKEN)

# Хранилище данных пользователей
tasks: list[Task] = []

@bot.message_handler(commands=['start', 'help'])
def send_welcome(message: Message) -> None:
    '''Отправляет приветственное сообщение и помощь по использованию бота.'''
    welcome_text = '''
    Привет! Я бот для управления задачами. Вот как со мной работать:
    - Чтобы добавить задачу, отправьте в  одном сообщении /add_task Название. Описание. Тэг.
    - Чтобы посмотреть ваши задачи, отправьте /show_tasks
    - Чтобы удалить задачу отправьте /del_task и введите номер задачи.
    - Чтобы удалить все задачи отправьте /del_all_tasks.
    - Чтобы посмотреть эту памятку снова, отправьте /help
    '''

    user_id: int = message.chat.id
    bot.send_message(user_id, welcome_text)

@bot.message_handler(commands=['add_task'])
def add_task(message: Message) -> None:
    '''Обрабатывает команду /add_task.'''
    user_id: int = message.chat.id
    text: str = message.text[10:].strip()

    if not text:
        bot.send_message(user_id, 'Вы не указали задачу. Памятка - /help')
        return   
    task_parts = text.split('.')
    title = task_parts[0].strip()
    description = task_parts[1].strip()
    tag = '#' + task_parts[2].strip()
    task = Task(title, description, tag)
    tasks.append(task)
    bot.send_message(user_id, 'Задача успешно записана. Для просмотра списка задач введите /show_tasks')

@bot.message_handler(commands=['show_tasks'])
def show_tasks(message: Message) -> None:
    """Выводит все текущие задачи пользователя."""
    user_id: int = message.chat.id

    message_text = 'Список Ваших задач:\n'
    message_text_2 = 'Для удаления задачи введите /del_task и номер задачи'
    for i, task in enumerate(tasks, start=1):
        message_text += f"{i}. {task}\n"
 
    bot.send_message(user_id, message_text + message_text_2)

@bot.message_handler(commands=['del_task'])
def delete_task(message: Message) -> None:
    '''Обрабатывает команду /del_task'''
    user_id: int = message.chat.id
    text: str = message.text[10:].strip()

    if not text.isdigit():
        bot.send_message(user_id, 'Пожалуйста, введите номер задачи для удаления.')
        return

    task_index = int(text)
    if 1 <= task_index <= len(tasks):
        tasks.pop(task_index - 1)
        bot.send_message(user_id, 'Ваша задача удалена. Для просмотра списка ваших задач введите /show_tasks')
    else:
        bot.send_message(user_id, 'Некорректный номер задачи. Пожалуйста, укажите существующий номер.')

@bot.message_handler(commands=['del_all_tasks'])
def delete_all_tasks(message: Message) -> None:
    '''Удаляет все задачи пользователя'''
    user_id: int = message.chat.id
    tasks.clear()
    bot.send_message(user_id, 'Все Ваши задачи были удалены!')

if __name__ == '__main__':
    bot.infinity_polling() 