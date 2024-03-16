"""
Что будет выведено после выполнения кода? Почему?
"""


def transmit_to_space(message):
   
    def data_transmitter():        
        print(message)

    data_transmitter()


print(transmit_to_space("Test message"))

"""

Print в функцие data_transmitter вернет "Test message".
Print в функцие transmit_to_space вернет ничего, так как нет print 

"""