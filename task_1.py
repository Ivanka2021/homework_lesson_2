
a = 145
b = 'Индира Ганди'
c = 'to be or no to be'
d = True
e = False
f = ['f', 'and', 5]
g = ('k', '3', 17)
h = {'language': 'English', 'level': 'Advanced'}
i = 8.9
j = frozenset('аккомпанемент')

my_list_sum = [a, b, c, d, e, f, g, h, i, j]
print(my_list_sum)

for el in my_list_sum:
    print(f'{el} is {type(el)}')
