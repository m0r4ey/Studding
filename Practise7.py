#Словари и множества
my_dict = {'Ilya' : 2000, 'Naslya' : 2001, 'Tatya' : 1998, 'Alex' : 2000}
print (my_dict)
print ('Ilya:', my_dict['Ilya'])
print ('Vova:', my_dict.get('Vova'))
my_dict.update ({'Valera' : 1999,
                'Lukya' : 2002})
deleted = my_dict.pop('Alex')
print('Alex:', deleted)
print(my_dict, '\n')

my_set = {1, 3, "A", 4, 3, 4, 9, 9, "A", 1, 2, 2, 3, "A", "B"}
print (my_set)
my_set.add(10)
my_set.add("light")
my_set.discard(1)
print (my_set)