import random

# получаем случайное число в диапазоне от 1 до 15
number = random.randint(1, 15)
print ('Привет, я загадал число между 1 и 15. Сможешь угадать?')

while True:
    # получаем число от пользователя
    get_Input = int(input('Введи число: '))

    if get_Input < number: # x < y
        print ('Твое число меньше того, что я загадал.')

    if get_Input > number: # x > y
        print ('Твое число больше загаданного мной.')

    if get_Input == number: # x == y
        break

if get_Input == number:
    print ('Молодец! Ты угадал число!')