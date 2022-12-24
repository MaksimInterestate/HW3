# Написать программу, где создадим класс Soup (для определения типа супа)
# принимающий 1 аргумент - который отвечает за основной продукт к выбираемому супу. 
# В этом классе создать метод show_my_soup(), выводящий на печать «Суп - {Основной продукт}» 
# в случае наличия добавки Это как доп к этой задаче - иначе отобразится следующая фраза: «Обычный кипяток»
'''
class Soup:
    def __init__(self, name):
        self.name = name
    
    def show_my_soup(self):
        arr = {'борщ': 'свекла и томатное пюре', 'щи':'капуста', 'харчо':' говядина', 'солянка':'мясо'}
        count = 0
        for i in arr: 
            if i == self.name:
                print(f'Суп - {self.name}: \nОсновной продукт : {arr[i]}')
                count += 1
        if count == 0: print('Такой суп не найден')        
    


n = input('Введите название супа - ')
m = Soup(n)
print('Вы выбрали суп ',n)
print(m.show_my_soup())
'''


# Нужно напистать программу
# В ней используем классы - имя студента name, номер группы group и список полученных оценок progress. 
# В самой программе вводим список всех студентов. 
# В программе нужно вывести список студентов, отсортированный по имени, А так же студентов, у которых низкие оценки

name = {1 : 'Ivanov',2:'Sidorov', 3:'Petrov', 4:'Verhorubov',5:'Okynev',6:'Smalin',7:'Stolov'}
group = {'ivanov': '5 A', 'sidorov': '5 B', 'petrov': '6 C', 'verhorubov': '6 A', 'okynev': '8 C', 'smalin': '8 A',
             'smirnov': '8 B'}
progress = {
        'ivanov': [3, 4, 3, 4, 2, 4],
        'sidorov': [5, 5, 4, 5, 4, 4],
        'petrov': [4, 4, 5, 3, 3, 4],
        'verhorubov': [4, 4, 5, 3, 5, 5],
        'okynev': [5, 3, 4, 5, 3, 3],
        'smalin': [2, 3, 2, 4, 3, 2],
        'smirnov': [4, 3, 4, 4, 5, 3]
        }
class Studient:

    def __init__(self, name):
        self.name = name.lower()
        self.group = group
        self.progress = progress
        s = 0
        self.s = s
        #self.progress_stud = progress_stud

    def find_name(self):
        count = 0
        for i in self.group:
            if i == self.name:
                print(f'Ваш ученик в {self.group[i]} классе')
                count += 1
        if count < 1: print('Ученик с такой фамилией не найден. Попробуйте снова')

    def find_progress_student(self):
        for i in self.progress:
            self.s = 0
            if i == self.name:
                print('Оценки ученика : ')
                for j in self.progress[i]:
                    print(j, end = ', ')
                    self.s = self.s + j
                print(f'\nСредняя балл у {self.name} = {round((self.s / len(self.progress[i])), 2)} балла')
                self.res = round((self.s / len(self.progress[i])), 2)

    def status_student(self):
        if self.res < 3.5 : print(f'{self.name} отстающий ')
        elif self.res > 3.5 and self.res < 4.2:
            print(f'{self.name} в списке хорошистов')
        elif self.res >= 4.3:
            print(f'{self.name} в списке отличников ')

    def find_student(self):
        for i in self.progress:
            s = 0
            for j in self.progress[i]:
                s = s + j
            s = round((s / len(self.progress[i])), 2)
            if self.res < 3.5 and s < 3.5: print(f'В списке отстающих :  {i} средний балл {s}')
            elif self.res > 3.5 and self.res < 4.3 and s < 4.3 and s > 3.5: print(f'В списке хорошистов:  {i} средний балл {s}')
            elif self.res >= 4.3 and s >= 4.3: print(f'В списке отличников :  {i} средний балл {s}')





name = input('Введите фамилию ученика - ')
g = Studient(name)
print(g.find_name())  # ищем в списке фамилию
g.find_progress_student()
g.status_student()
g.find_student()

# findx = int(input('Введите балл успеваемости : \n 1 : отличник 2 : хорошист 3 : удовл 2 : отстающие'))
# print(g.find_progress_list(findx))


# group = {'Ivanov': '5 A', 'Sidorov': '5 B', 'Petrov': '6 C', 'Verhorubov': '6 A', 'Okynev': '8 C', 'Smalin': '8 A', 'Stolov': '8 B'}
#
# n = input('name ')
# c = 0
# for i in group:
#     if i == n:
#         print(f'Ваш ученик в {group[i]} классе')
#         c += 1
#
# if c < 1: print('Ученик не найден')

