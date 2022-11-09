"""Игра угадай число
Компьютер сам загадывает и сам угадывает число
"""

import numpy as np


def random_predict(number: int = 1) -> int:
    """Рандомно угадываем число

    Args:
        number (int, optional): Загаданное число. Defaults to 1.

    Returns:
        int: Число попыток
    """
    count = 0

    while True:
        count += 1
        predict_number = np.random.randint(1, 101)  # предполагаемое число
        if number == predict_number:
            break  # выход из цикла если угадали
    return count

def binary_predict(number:int = 1) -> int:
    """Алгоритм бинарного поиска. Делим пополам диапазон, в котором
       находится загаданное число, и спрашиваем, в какой половине оно находится,
       тем самым сужая диапазон.

    Args:
        number (int, optional): Загаданное число. Defaults to 1.

    Returns:
        int: Число попыток
    """
    
    count = 0          # Счётчик попыток
    min_number = 0     # Минимальное число диапазона, где может находится загаданное число
    max_number = 100   # Максимальное число диапазона, где может находится загаданное число
    predict = 0        # Число, которое мы "называем", спрашивая, больше оно или меньше загаданного

    while number != predict: # выход из цикла, если угадали число
        predict = round((min_number + max_number) / 2)  # "называем" число посередине диапазона
        count += 1
        # Если "названное" число меньше загаданного, увеличиваем минимальное возможное число диапазона
        if number > predict:
            min_number = predict
        # Если "названное" число больше загаданного, уменьшаем максимальное возможное число диапазона
        elif number < predict:
            max_number = predict

        # Когда диапазон сужается до одного числа, заявляем, что мы угадали число
        # и "называем" его, засчитывая это за последнюю попытку
        if max_number == min_number:
            predict = max_number
            count += 1
            
    return count  



def score_game(predict_func) -> int:
    """За какое количество попыток в среднем за 1000 подходов угадывает наш алгоритм

    Args:
        random_predict ([type]): функция угадывания

    Returns:
        int: среднее количество попыток
    """
    count_ls = []
    #np.random.seed(1)  # фиксируем сид для воспроизводимости
    random_array = np.random.randint(1, 101, size=(1000))  # загадали список чисел

    for number in random_array:
        count_ls.append(predict_func(number))

    score = int(np.mean(count_ls))
    print(f"Ваш алгоритм угадывает число в среднем за:{score} попыток")
    return score


if __name__ == "__main__":
    #RUN
    score_game(random_predict)
    score_game(binary_predict)
    
    
    
"""Проверка работы алгоритма.
   Выводим на экран число попыток, необходимых алгоритму бинарного поиска,
   чтобы угадать все числа от 1 до 100"""
   
#for i in range(1, 101):
#    print(f"Kоличество попыток для угадывания числа {i}, алгоритм v5: ", binary_predict(i))
