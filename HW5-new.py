import random

#Морской бой
map = [
    ['  ','A ','B ','C ','D ','E ','F ','G ','I ','H ','K '],
    ['1 ','. ','. ','. ','. ','. ','. ','. ','. ','. ','. '],
    ['2 ','. ','. ','. ','. ','. ','. ','. ','. ','. ','. '],
    ['3 ','. ','. ','. ','. ','. ','. ','. ','. ','. ','. '],
    ['4 ','. ','. ','. ','. ','. ','. ','. ','. ','. ','. '],
    ['5 ','. ','. ','. ','. ','. ','. ','. ','. ','. ','. '],
    ['6 ','. ','. ','. ','. ','. ','. ','. ','. ','. ','. '],
    ['7 ','. ','. ','. ','. ','. ','. ','. ','. ','. ','. '],
    ['8 ','. ','. ','. ','. ','. ','. ','. ','. ','. ','. '],
    ['9 ','. ','. ','. ','. ','. ','. ','. ','. ','. ','. '],
    ['10','. ','. ','. ','. ','. ','. ','. ','. ','. ','. ']
    ]

count = 0 #счетчтик убитых кораблей
numb = {'A' : 1, 'B': 2 ,'C': 3 , 'D': 4 , 'E':5 ,'F': 6 ,'G':7 ,'I':8 ,'H':9 ,'K': 10}
level = int(input('Выберите уровень сложности 1 - Easy (4 выстрела) 2 - Medium (3 выстрела) 3 - High (2 выстрела)'))

for n in range(1,4):  #считаем какой уровень выбран, от этого и расставляем выстрелы
    if level == n :
        for i in range(1,6-n):
            x = input(f'Введите букву A,B,C,D,E,F,G,I,H,K по оси Х :')
            x = x.upper()
            x = numb.get(x)
            if x == None:
                print('Вы стреляете в молоко, попробуйте еще раз')
            else:
                x = int(x)
                y = int(input('Цыфру по оси Y :'))
                if y > 10: print('Вы стреляете в молоко, попробуйте еще раз')
                else:
                    map[y][x] = f'S{i}' #shot - выстрелы
                    warshipx = random.randint(1,10) #комп рандомно выбирает координаты
                    warshipy = random.randint(1,10)
                    map[warshipy][warshipx] = f'W{i}'  #warship - корабли 
                    if y == warshipy and x == warshipx: #условие если координаты выстрела и коробля совпали, то count+1
                        count += 1
                        print('Поздравляю, Вы потопили корабль')
                        map[y][x] = '# ' # потопленный корабль 

print('S- Ваши выстрелы, W - корабли, #- потопленный корабль ')
for i in map:
    for j in i:
        print(j, end = ' ')
    print()       
if count > 0: print(f'Поздравляю. Вы потопили {count} кораблей')
else: print(f'Попробуй еще раз.Вы не потопили ни одного корабля')



# крестики нолики
map = [
    ['. ','. ','. '],
    ['. ','. ','. '],
    ['. ','. ','. ']
]

for i in range(1,10):
    if (map[0][0] == 'O 'and map[1][1]== 'O ' and map[2][2]== 'O ') or (map[0][0] == 'O 'and map[0][1]== 'O ' and map[0][2]== 'O ') or\
        (map[1][0] == 'O 'and map[1][1]== 'O ' and map[1][2]== 'O ') or (map[2][0] == 'O 'and map[2][1]== 'O ' and map[2][2]== 'O ') or\
        (map[0][0] == 'O 'and map[1][0]== 'O ' and map[2][0]== 'O ') or (map[0][1] == 'O 'and map[1][1]== 'O ' and map[2][1]== 'O ') or\
        (map[0][2] == 'O 'and map[1][2]== 'O ' and map[2][2]== 'O '):
        print ('Победил компьютер')
        break
    elif (map[0][0] == 'X 'and map[1][1]== 'X ' and map[2][2]== 'X ') or (map[0][0] == 'X 'and map[0][1]== 'X ' and map[0][2]== 'X ') or\
        (map[1][0] == 'X 'and map[1][1]== 'X ' and map[1][2]== 'X ') or (map[2][0] == 'X 'and map[2][1]== 'X ' and map[2][2]== 'X ') or\
        (map[0][0] == 'X 'and map[1][0]== 'X ' and map[2][0]== 'X ') or (map[0][1] == 'X 'and map[1][1]== 'X ' and map[2][1]== 'X ') or\
        (map[0][2] == 'X 'and map[1][2]== 'X ' and map[2][2]== 'X ') :
        print ('Ура, Вы победили!')
        break
    elif (map[0][0] == 'X 'and map[0][1]== 'X ' and map[0][2]== 'X 'and map[1][0] == 'X 'and map[1][1]== 'X ' and map[1][2]== 'X ' and\
        map[2][0] == 'X 'and map[2][1]== 'X ' and map[2][2]== 'X ') or (map[0][0] == 'O 'and map[0][1]== 'O ' and map[0][2]== 'O 'and\
        map[1][0] == 'O 'and map[1][1]== 'O ' and map[1][2]== 'O ' and map[2][0] == 'O 'and map[2][1]== 'O ' and map[2][2]== 'O '):
        print('Вы сыграли вничью')
    else:
        print(f'Ваш ход #{i}')
        print('Куда поставите крестик ?')
        userx = int(input('X : '))
        usery = int(input('Y : '))
        for i in range(1,5):
            if map[usery-1][userx-1] == '. ':
                map[usery-1][userx-1] = 'X '
                break
            elif map[usery-1][userx-1] != '. ':
                print('Поменяйте расположение крестика')
                userx = int(input('X : '))
                usery = int(input('Y : '))
    
    print(f'Ход компьютера #{i}')
    compx = random.randint(0,2)
    compy = random.randint(0,2)
    for n in range(1,10):
        if map[compy][compx] == '. ':
            map[compy][compx] = 'O '
            break
        elif map[compy][compx] != '. ':                
            compx = random.randint(0,2)
            compy = random.randint(0,2)
                
    for k in map:
        for l in k:
            print(l, end = ' ')
        print()