example = "капибара"
a = list(example)
a[0:3], a[-3:] = a[-3:], a[0:3]
print(''.join(a))

example2 = 'парапсихолог'
a = example2[0:4]
b = example2[4:8]
c = example2[8:12]
print(b+c+a)

example = 'капибара'
a = list(example)
a[1], a[4] = a[4], a[1]
print(''.join(a))

import random
example = 'капибара'
a = list(example)
m = int(a.index(random.choice(a)))
n = int(a.index(random.choice(a)))
a[n],a[m] = a[m],a[n]
print(''.join(a))

# example = 'капибара'
# a = list(example)
# n = int(input('Введите первый номер буквы, которую хотите заменить: '))
# m = int(input('Введите второй номер буквы,которую хотите заменить '))
# n = n-1
# m= m-1
# a[n],a[m] = a[m],a[n]
# print(''.join(a))