#  dictionaries --->
print('Dictionaries:')
print('=============')
my_dict = {'Oleg': 1960,
           'Alex': 1989,
           'Daniil': 2003,
           'Anton': 1999,
           'Victor': 1962}

print('Пример словаря:', my_dict)

print('\r')  # добавим пустую строку
print('Существующий ключ:', my_dict['Victor'])
print('Несуществующий ключ:', my_dict.get('Artem', 'В словаре нет данных по этому имени!'))

#  пополняем словарь:
my_dict['Dima'] = 2005  # вариант добавления одной пары
my_dict.update({'Stas': 1995,  # вариант добавления нескольких пар
                'Ivan': 2000
                })
print('\r')  # добавим пустую строку
print('Пополненный словарь: ', my_dict)  # вывод пополненного словаря
# удаляем произвольный ключ:
del my_dict['Anton']
print('После удаления ключа:', my_dict)  # проверяем факт удаления пары
#  <--- dictionaries

# sets --->
print('\r')  # добавим пустую строку
print('Sets:')
print('=====')
my_set = {True, 'Apple', 12.5, True, 'Apple', 'Pineapple'}
print('Множество:', my_set)
my_set.add(False)  # добавляем один элемент
my_set.add('Cherry')  # добавляем ещё один элемент
my_set.remove(12.5)  # удаляем один элемент
print('Изменённое множество:', my_set)
# <--- sets
