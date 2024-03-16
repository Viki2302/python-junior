"""
Что будет выведено после выполнения кода? Почему?
"""
x = 42


def some_func():
    global x
    x = x + 1
    print(x)


some_func()
print(x)

"""
43
43

global в функцие меняет значение в переменной x = 42 на x = 43

"""