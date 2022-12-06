print('GB Lesson 5')
import random

'''


#print(spisok)
#spisok[0] = 'Dima'
#print(spisok[-1]) последний элемент списка
#print(spisok[i], end = ' ') end = ' '- в одну строчку
#spisok.append('Andre') .append добавляет новый элемент в конец списка
#spisok.insert(2,'Boris') .insert(2,'Boris') добавили Boris на индекс 2,остальнгые сдвигаются вправо
#spisok.remove('Bob') .remove('Bob') удалили Bob #1
#spisok.pop() .pop() Удаляет последний элемент
#spisok.pop(1) .pop(1) Удаляет под индексом 1
#a = spisok.pop(1) переменная а сохраняется удаленный эл с индексом 1
#spisok.isdigit() isdigit() проевряет число ли это
#print(len(spisok))

nums = []
n = 10 
for i in range(n):
    nums.append(i**3) #возводим в куб 
print(nums)

n = 10
nums = [.**3 for . in range(n)] #возводим в куб
print(nums)

nums = []
n = 10 
for i in range(n):
    if i % 2 == 0:
        nums.append(i**3) #возводим в куб нечетный индексы
print(nums)

n = 10
#     операция цикл            условие
nums = [.**3 for . in range(n) if . % 2 == 0] #возводим в куб нечетный индексы
print(nums)

lst = [1, 2, 3, 4, 5]
#      ключ:   значение  ключ: значение ключ:значение
dict = {'имя': 'Bob', 'Возраст': 30, 123: True}
for . in dict:
    print(.) #выводит ключи!
    print(., dict[.]) #выводит ключ значение
print(dict)
# обращение к ключу 'имя' словаря dict
print(dict['Возраст'])

dict = {'имя': 'Bob', 'Возраст': 30, 123: True}
for . in dict:
    print(., dict[.]) #выводит ключ значение
print(dict.get('им я')) #выводит none если такого ключа нет
print(dict.get('имя1', 'NO')) #выводит NO если такого ключа нет
print(dict.keys()) #выводит все ключи
print(dict.values()) #выводит все значения
print(dict.items()) #выводит (ключ значение)

dict['имя'] = 'Марк' #изменили значение по ключу имя
dict['имя123'] = 'Марк123' #добавили нгвоый ключ и значение в конец
dict['имя'] = dict['имя'] + 'Боб'
print(dict)

import random
# Камень - ножницы - бумага
print('ДОБРО ПОЖАЛОВАТЬ В ИГРУ КАМЕНЬ НОЖНИЦЫ БУМАГА')
list = {1:'камень', 2 :'ножницы', 3 :'бумага'}
while True:
    numb = int(input(' Выберети 1 = камень 2 = ножницы 3 = бумага или 0 для выхода \n'))
    print(f'Вы выбрали {list[numb]}')
    comp = random.randint(1,3)
    print(f'Компьютер выбрал {list[comp]}')    
    if numb == 0 : break
    
    if numb == comp: print('Ничья. Попробуйте еще раз ')
    elif numb == 1 and comp == 2: print('Вы победили ')
    elif numb == 2 and comp == 3: print('Вы победили ')
    elif numb == 3 and comp == 1: print('Поздравляю, Вы победили ')
    else: print('Вы проиграли. Попробуйте еще раз ')
'''

# Морской бой.
#создаем поле из вложенных списков 10х10
matrix = [
    ['. ','. ','. ','. ','. ','. ','. ','. ','. ','. '],
    ['. ','. ','. ','. ','. ','. ','. ','. ','. ','. '],
    ['. ','. ','. ','. ','. ','. ','. ','. ','. ','. '],
    ['. ','. ','. ','. ','. ','. ','. ','. ','. ','. '],
    ['. ','. ','. ','. ','. ','. ','. ','. ','. ','. '],
    ['. ','. ','. ','. ','. ','. ','. ','. ','. ','. '],
    ['. ','. ','. ','. ','. ','. ','. ','. ','. ','. '],
    ['. ','. ','. ','. ','. ','. ','. ','. ','. ','. '],
    ['. ','. ','. ','. ','. ','. ','. ','. ','. ','. '],
    ['. ','. ','. ','. ','. ','. ','. ','. ','. ','. '],
    ]
#вывели поле на экран
for i in matrix:
    for j in i:
        print(j, end = ' ')
    print()

x1 = int(input('Введите координаты корабля №1 по оси Х :'))
y1 = int(input('Введите координаты корабля №1 по оси Y :'))
x2 = int(input('Введите координаты корабля №2 по оси Х :'))
y2 = int(input('Введите координаты корабля №2 по оси Y :'))
x3 = int(input('Введите координаты корабля №3 по оси Х :'))
y3 = int(input('Введите координаты корабля №3 по оси Y :'))
matrix[x1-1][y1-1] = 'O '    
matrix[x2-1][y2-1] = 'O '
matrix[x3-1][y3-1] = 'O '  
print('Корабли расставлены на поле боя')
for i in matrix:
    for j in i:
        print(j, end = ' ')
    print()

compx1 = random.randint(1,10)
compy1 = random.randint(1,10)
compx2 = random.randint(1,10)
compy2 = random.randint(1,10)
compx3 = random.randint(1,10)
compy3 = random.randint(1,10)
compx4 = random.randint(1,10)
compy4 = random.randint(1,10)
compx5 = random.randint(1,10)
compy5 = random.randint(1,10)
 
if matrix[compx1-1][compy1-1] == matrix[x1-1][y1-1] or matrix[compx1-1][compy1-1] == matrix[x2-1][y2-1] or matrix[compx1-1][compy1-1] == matrix[x3-1][y3-1]:
    print(f'Компьютер попал. Корабль утонул .')
    matrix[x1-1][y1-1] = 'X '
else: 
    print(f'Компьютер промазал ') 
    matrix[compx1-1][compy1-1] = 'Й '
for i in matrix:
    for j in i:
        print(j, end = ' ')
    print()

if matrix[compx2-1][compy2-1] == matrix[x1-1][y1-1] or matrix[compx2-1][compy2-1] == matrix[x2-1][y2-1] or matrix[compx2-1][compy2-1] == matrix[x3-1][y3-1]:
    print(f'Компьютер попал. Корабль утонул .')
    matrix[x2-1][y2-1] = 'X '
else: 
    print(f'Компьютер промазал ')
    matrix[compx2-1][compy2-1] = 'Й '
for i in matrix:
    for j in i:
        print(j, end = ' ')
    print()

if matrix[compx3-1][compy3-1] == matrix[x1-1][y1-1] or matrix[compx3-1][compy3-1] == matrix[x2-1][y2-1] or matrix[compx3-1][compy3-1] == matrix[x3-1][y3-1]:
    print(f'Компьютер попал. Корабль утонул .')
    matrix[compx3-1][compy3-1] = 'X '
else: 
    print(f'Компьютер промазал ')
    matrix[compx3-1][compy3-1] = 'Й '
for i in matrix:
    for j in i:
        print(j, end = ' ')
    print()

if matrix[compx4-1][compy4-1] == matrix[x1-1][y1-1] or matrix[compx4-1][compy4-1] == matrix[x2-1][y2-1] or matrix[compx4-1][compy4-1] == matrix[x3-1][y3-1]:
    print(f'Компьютер попал. Корабль утонул .')
    matrix[compx4-1][compy4-1] = 'X '
else: 
    print(f'Компьютер промазал ')
    matrix[compx4-1][compy4-1] = 'Й '
for i in matrix:
    for j in i:
        print(j, end = ' ')
    print()

if matrix[compx5-1][compy5-1] == matrix[x1-1][y1-1] or matrix[compx5-1][compy5-1] == matrix[x2-1][y2-1] or matrix[compx5-1][compy5-1] == matrix[x3-1][y3-1]:
    print(f'Компьютер попал. Корабль утонул .')
    matrix[compx5-1][compy5-1] = 'X '
else: 
    print(f'Компьютер промазал ')
    matrix[compx5-1][compy5-1] = 'Й '
for i in matrix:
    for j in i:
        print(j, end = ' ')
    print()