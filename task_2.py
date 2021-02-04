a = input('Введите любое текстовое и/или числовое значение: ')
b = input('Введите любое текстовое и/или числовое значение: ')
c = input('Введите любое текстовое и/или числовое значение: ')
d = input('Введите любое текстовое и/или числовое значение: ')
e = input('Введите любое текстовое и/или числовое значение: ')
my_list = [a, b, c, d, e]
print(my_list)

if len(my_list) / 2 == 0:
    el = 0
    while el < len(my_list):
        tmp = my_list[el]
        my_list[el] = my_list[el + 1]
        my_list[el + 1] = tmp
        el += 2
else:
    el = 0
    while el < len(my_list) - 1:
        tmp = my_list[el]
        my_list[el] = my_list[el + 1]
        my_list[el + 1] = tmp
        el += 2
print(my_list)
