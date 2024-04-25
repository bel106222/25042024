# from random import randint

# lst = []
# ln = 12
# for i in range(ln):
#     lst.append(randint(-50,50))

# print('Сгенерирован список:',lst)

# new_list = sorted(lst)
# print(new_list)

# word = 'one two three'
# position = word.find('two')

#print(word.count('two'))

# lst.sort()
# print(list)

# symbols = 'привет'
# symbols2 = sorted(symbols)
# print(symbols2)

# numbers = (1,2,3,4,5,6,7,8,9,10)
# numbers2 = list (numbers)
# numbers3 = tuple (lst)
# print(numbers3)
# lst = ['banana', 'apple', 'bananabanana', 'banana-apple', 'orange', 'orangebanana']
# tpl = tuple(lst)
# fruit = input('Введите фрукт:\n>')
# count = 0
# for i in tpl:
#     if fruit in i:
#         count += 1
# print(f'Фрукт {fruit} встречается в списке {count} раз.')
lst = ['bmw', 'volvo', 'fiat', 'lada']
tpl = tuple(lst)
print('Текущий кортеж:', tpl)
brend = input('Введите бренд который меняем:\n>')
change = input('Введите на что меняем:\n>')
count = 0
new_list = list(tpl)

for i in range(len(new_list)):
    if brend == new_list[i]:
        new_list[i] = change
tpl = tuple(new_list)
print('Изменённый кортеж:',tpl)