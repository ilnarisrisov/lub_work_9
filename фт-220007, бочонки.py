import random
import logging

logging.basicConfig(filename='barrels.log', level=logging.INFO)

while True:
    try:
        N = int(input('Введите количество бочонков: '))
        if N < 1:
            print('Должно быть введено натуральное число(больше 0)')
            logging.error('Должно быть введено натуральное число(больше 0)')
        break
    except ValueError:
        print('Должно быть введено число')
        logging.error('Должно быть введено число')
        pass

i = 0
random_sequence = list(range(1, N+1))
random.shuffle(random_sequence)
while i < N:

    enter = input('\nНажмите Enter, чтобы вытащить бочку: {}'.format(random_sequence[i]))
    logging.info('Вытащен бочонок с номером {}'.format(random_sequence[i]))
    i += 1

