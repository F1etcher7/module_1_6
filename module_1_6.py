#Словари
my_dict = {'Vasya' : 2000, 'Sasha' : 1995, 'Dima' : 1999}
print(my_dict)
print(my_dict['Vasya'])
print(my_dict.get('Denis'))
my_dict.update({'Masha' : 2002,
                'Alex' : 2001})
print(my_dict)
a = my_dict.pop('Sasha')
print(a)
print(my_dict)

#Множества
my_set = {1, 5, 7, 'Sasha', (1, 2, 3), 1, 5, 7}
print(my_set)
my_set.add(6)
my_set.add(0)
my_set.discard('Sasha')
print(my_set)