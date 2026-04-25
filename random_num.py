import random

print('Добро пожаловать в числовую угадайку')

def is_valid(num, max_num):
    if num.isdigit():
        if int(num) in range(1, max_num + 1):
            return int(num)
    return None

def game_random_num():
    count = 0
    max_num = int(input('Введите максимальный диапазон для угадывания: '))
    rand_num = random.randint(1, max_num)
    while True:
        num = is_valid(input('Попробуй угадать число: '), max_num)
        if num is not None:
            count += 1
            if num > rand_num:
                print('Ваше число больше загаданного, попробуйте еще разок')
            elif num < rand_num:
                print('Ваше число меньше загаданного, попробуйте еще разок')
            else:
                print('Вы угадали, поздравляем!')
                break
        else:
            print(f'А может быть все-таки введем целое число от 1 до {max_num}?')
    print(f'Спасибо, что играли в числовую угадaйку. Вы потратили {count} попыток.')
    return count

while True:
    count = game_random_num()
    if input('Хотите еще раз поиграть? y/n ').lower() != 'y':
        print('Чтож, пока')
        break