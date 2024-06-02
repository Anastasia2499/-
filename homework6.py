#Словарь
my_dict = {'Кирилл': 19, 'Маша':20, 'Света':21, 'Саша':22}
print(my_dict)
print(my_dict ['Кирилл'])
print(my_dict.get ('Настя', 'Отсутствует'))
my_dict.update({'Миша': 23, 'Ира': 24})
print(my_dict)
a = my_dict.pop('Маша')
print(a)
print(my_dict)

#Множества
my_set = {'Яблоко', 'Банан', (1,2,3), 1,2,1,2,1, True}
print(my_set)
my_set.update({65, 'Груша'})
print(my_set)
my_set.discard(1)
print(my_set)


