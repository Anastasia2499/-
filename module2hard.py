import random
first_cell = random.randint(3, 20)
password = ''
for i in range(1, first_cell):
    for j in range(i+1, first_cell):
        if first_cell % (i + j) == 0:
            password += str(i)+str(j)
print(f'{first_cell} - {password}')
