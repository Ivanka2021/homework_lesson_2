
number = int(input("Введите любое натуральное число: "))
my_list = [7, 5, 3, 3, 2]
a = my_list.count(number)
for element in my_list:
    if a > 0:
        b = my_list.index(number)
        my_list.insert(b+a, number)
        break
    else:
        if number > element:
            d = my_list.index(element)
            my_list.insert(d, number)
            break
        elif number < my_list[len(my_list) - 1]:
            my_list.append(number)
print(my_list)
