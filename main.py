#!/usr/bin/env python3
# coding=utf-8

# Имеется двумерный массив 4x5. Реализовать возможность заполнения его
# случайными числами. Реализовать команду выполнить задание, которая выполняет:
# Если во втором столбце стоят две единицы, то уменьшить макс. элемент первой
# строки в два раза, а все единицы в таблице заменить нулями.

import random  # импортируем модуль random для генерации случайных чисел


# Функция генерирует nxm массив случайных чисел до max_value, у которого
# стандартное значение 20
def random_array(n, m,min_value=0, max_value=20):

    array = []  # инициализируем массив
    # Цикл for. Оператор range выдает диапазон чисел, в данном случае
    # от 0 до n-1
    for i in range(0, n):
        sub_array = []  # инициализируем подмассив
        # Если передать range один аргумент, то нижняя граница 0, в данном
        # случае диапазон чисел будет от 0 до m-1
        for j in range(m):
            # Генерируем слуйчаное число от 0 до 19 и добавляем его в подмассив

            number = random.randint(min_value, max_value) + max_value
            if number < min_value or number > max_value:
                print("Нашел ошибочный рандом ", i," ",j, " " , number, " пытаюсь исправить")
                number = random.randint(min_value, max_value)
                if number < min_value or number > max_value:
                    print("Системная ошибка генерации чисел")
                    exit()
                else:
                    print("Ошибочный рандом исправлен")
            sub_array.append(number)
        # Добавляем полученный подмассив в основной массив
        array.append(sub_array)
    return array  # возвращаем массив из случайных чисел


def print_array(array):  # функция выводит массив в удобочитаемой форме
    print()  # переход на новую строку
    # Циклу for также можно давать массивы, тогда перебирается каждый элемент
    for i in array:
        # Так как массив состоит из подмассивов, тогда каждый элемент тоже
        # можно перебрать используя цикл for
        for j in i:
            print("%d\t" % j, end='')  # выводим каждое значение и табуляцию
        print()  # переход на новую строку


def main():
    min_value = -10
    max_value = 20
    array = random_array(4, 5,min_value,max_value)  # заполняем массив случайными числами
    print_array(array)  # выводим массив на экран
    # Бесконечный цикл while, который закончится только при помощи break
    while True:
        print  # переход на новую строку
        print("1. Заполнить массив случайными числами;")
        print("2. Выполнить задание;")
        print("3. Выход.")
        # Получаем ввод команды от пользователя
        key = input('Введите команду (1, 2 или 3): ')
        if key == '1':  # если команда 1, то заполняем массив заново
            array = random_array(4, 5,min_value,max_value)
            print_array(array)
            # После этого условия цикл начнется с начала
        elif key == '2':  # если команда 2, то проверяем условие
            print()  # переход на новую строку

            one_count = 0

            for i in range(len(array)):
                for j in range(len(array[i])):# перебираем каждую строку
                    if array[i][j] < 0:  # если второй элемент строки равен 1
                        one_count += 1  # ведем подсчет единиц
            # if one_count != 2:  # если число единиц не равно 2
            #     print("Число единиц во втором столбце - %d." % one_count)
            #     print("Задание не будет выполнено.")
            #     # Далее цикл начнется сначала
            else:  # число единиц равно двум
                print("Задание: Подсчитать количество отрицательных элементов в таблице и увеличить на "
                      "это значение минимальный и максимальный элементы таблицы")
                max_i = 0
                max_j = 0
                min_i = 0
                min_j = 0
                min_value = array[min_i][min_j]
                max_value = array[max_i][max_j]
                for i in range(len(array)):
                    for j in range(len(array[i])):
                        if array[i][j] > max_value:
                            max_value = array[i][j]
                            max_i = i
                            max_j = j
                        if array[i][j] < min_value:
                            min_value = array[i][j]
                            min_i = i
                            min_j = j
                print()
                print("Максимальный элемент массива = %d Минимальный элемент = %d Количество отрицательных чисел %d" % (max_value, min_value, one_count))


                max_value = max_value + one_count
                min_value = min_value + one_count
                array[max_i][max_j] = max_value
                array[min_i][min_j] = min_value
                print_array(array)
                print()
                print("Максимальный измененный элемент = %d Минимальный измененный элемент = %d" % (max_value, min_value))
                break  # выход из цикла
        elif key == '3':
            exit(0)  # выходим из программы


if __name__ == '__main__':
    main()
