# Задача 10: На столе лежат n монеток. Некоторые из них лежат вверх решкой, а некоторые – гербом. Определите минимальное число монеток, которые нужно перевернуть, 
# чтобы все монетки были повернуты вверх одной и той же стороной. 
# Выведите минимальное количество монет, которые нужно перевернуть


orel = input('Введите кол-во монеток, которые упали решкой: ')
reshka = input('Введите кол-во монеток, которые упали орлом: ')

def findminreverse(orel, reshka):
    reverse = 0
    if orel > reshka:
        reverse = reshka
    else: reverse = orel
    return reverse


print(f'Минимальное кол-во монет, которое нужно перевернуть ---> {findminreverse(orel, reshka)}')