print('GB Lesson 7')

import keyboard 
import os

weekday_list = {1:'monday', 2:'tuesday', 3:'wednesday', 4:'thursday', 5:'friday', 6:'saturday', 7:'sunday'}
weekday = {1 : 'mon.txt', 2: 'tue.txt', 3 : 'wed.txt', 4: 'thu.txt', 5: 'fri.txt', 6: 'sat.txt', 7: 'sun.txt'}
do = {1: 'прочитать', 2: 'добавить', 3: 'изменить'}

def blocnot (weekday,change,day):
    if change == 1:
        with open(weekday[day], 'r', encoding = 'utf-8') as f:
            print(f.read())  
    elif change == 2:
        event = input('Какое событие записать в день этот недели ? формат "время" - событие ')
        one = 'time is ' + event
        with open(weekday[day], 'a', encoding = 'utf-8') as f:
            f.write(f'\n{one}')
           
    elif change == 3:
        event = input('Фаил будет очищен. Какое событие записать в день этот недели? ')
        with open(weekday[day], 'w', encoding = 'utf-8') as f:
            f.write(f'\n {event}')
 
while True:
    change = int(input('Выберите, что хотите сделать \n 1 : прочитать  2 : добавить   3 : изменить : ')) 
    day = int(input('Выберети день недели от 1 до 7 : '))
    print('-------------------------------------------------------')
    print(f'Вы выбрали {do[change]} в {weekday_list[day]} в файле {weekday[day]} ')
    print('-------------------------------------------------------')

    blocnot(weekday,change,day)
    print()
    print('Вы желаете продолжить ? \nc - продолжить \ne - выход ')
    print(keyboard.read_key())
    if keyboard.read_key() == "c":
        os.system('cls or clear')
    elif keyboard.read_key() == "e":
        break
    
