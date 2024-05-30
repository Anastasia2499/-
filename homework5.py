immutable_var = 1, 'яблоко', 2, 'груша'
print(immutable_var)

# immutable_var = 1, 'яблоко', 2, 'груша'
# immutable_var[0] = 4
# print(immutable_var)   Ответ: кортеж не изменяем, потому что в нем содержится не список элементов, а ссылка на него

mutable_list = ['Ночь','улица','светильник ','аптека']
mutable_list[2] = 'фонарь'
print(mutable_list)
print(', '.join(mutable_list))
