import inspect

from datetime import datetime as dt
from random import randint

from access_control import access_control
from constants import ADMIN_USERNAME, UNKNOWN_COMMAND

class Game:
      
    total_games = 0
    username = ''
    
    def __init__(self):
        Game.total_games += 1
        # self.username = Game.username
        self.start_time = dt.now()
        

    @access_control
    def get_statistics(self) -> None:
        self.game_time = dt.now() - self.start_time
        print(f'Общее время игры: {self.game_time}, текущая игра - №{Game.total_games}')


    @access_control
    def get_right_answer(self) -> None:
        print(f'Правильный ответ: {self.number}')


    def check_number(self) -> bool:
        # Если число угадано...
        if self.guess == self.number:
            print(f'Отличная интуиция, {self.username}! Вы угадали число :)')
            # ...возвращаем True
            return True
        
        if self.guess < self.number:
            print('Ваше число меньше того, что загадано.')
        else:
            print('Ваше число больше того, что загадано.')
        return False


    def game(self) -> None:
        # Получаем случайное число в диапазоне от 1 до 100.
        self.number = randint(1, 100)
        print(
            '\nУгадайте число от 1 до 100.\n'
            'Для выхода из текущей игры введите команду "stop"'
        )
        while True:
            # Получаем пользовательский ввод, 
            # отрезаем лишние пробелы и переводим в нижний регистр.
            user_input = input('Введите число или команду: ').strip().lower()

            match user_input:
                case 'stop':
                    break
                case 'stat':
                    self.get_statistics() 
                case 'answer':
                    self.get_right_answer()
                case _:
                    try:
                        self.guess = int(user_input)
                    except ValueError:
                        print(UNKNOWN_COMMAND)
                        continue

                    if self.check_number():
                        break          

    @staticmethod
    def get_username() -> None:
        username = input('Представьтесь, пожалуйста, как Вас зовут?\n').strip()
        if username == ADMIN_USERNAME:
            print(
                '\nДобро пожаловать, создатель! '
                'Во время игры вам доступны команды "stat", "answer"'
            )
        else:
            print(f'\n{username}, добро пожаловать в игру!')
        
        Game.username = username
        
        # return username

# Считается, что не очень хорошо то, что у нас прокидываются переменные 
# username и total_games на протяжении нескольких функций, и необходимо 
# применить OOP для исправления данной ситуации. 
# То есть нужно переделать эту игру на классы, и чтобы 
# Total_Games и username стали атрибутами этого класса или его объекта. 
def guess_number() -> None:
    
    # Счётчик игр в текущей сессии.
    Game.get_username()
    
    while True:
        game = Game()
        game.game()
        
        play_again = input(f'\nХотите сыграть ещё? (yes/no) ')
        if play_again.strip().lower() not in ('y', 'yes'):
            break


if __name__ == '__main__':
    
    # интроспекция проверка врапера @wraps(func) и передача атрибутов с ним и без них. 

    # for f in (Game.get_statistics, Game.get_right_answer, Game.check_number, Game.game):
    #     print(f.__name__)                       # заголовок строки вывода
    #     print('  __name__     =', f.__name__)
    #     print('  __qualname__ =', f.__qualname__)
    #     print('  __module__   =', f.__module__)
    #     print('  __doc__      =', f.__doc__)
    #     print('  signature    =', inspect.signature(f))
    #     print('  __wrapped__  =', getattr(f, '__wrapped__', 'нет'))
    #     print()
    
    
    print(
        'Вас приветствует игра "Угадай число"!\n'
        'Для выхода нажмите Ctrl+C'
    )
    guess_number()
