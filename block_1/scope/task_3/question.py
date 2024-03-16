"""
Что будет выведено после выполнения кода? Почему?
"""
def print_msg(number):

    def printer():
        nonlocal number
        number=3
        print(number)

    printer()
    print(number)


print_msg(9)

"""
Print в функцие printer вернет 3.
Print в функцие printer вернет 3.
nonlocal - для вложенной функции определенная переменная не является локальной, но она и не является глобальной в общем смысле.

"""