#Словари и множества
my_dict = {'Ilya' : 2000, 'Naslya' : 2001, 'Tatya' : 1998, 'Alex' : 2000}
print (my_dict)
print (my_dict['Ilya'])
my_dict ['Sasha'] = 1995
print (my_dict['Sasha'])
my_dict.update ({'Valera' : 1999,
                'Lukya' : 2002})
my_dict.pop('Alex')
print(my_dict, '\n')

my_set = {1, 3, "A", 4, 3, 4, 9, 9, "A", 1, 2, 2, 3, "A", "Chi", "Gaga", "B"}
print (my_set)
my_set.add(10)
my_set.add("GH")
my_set.add("light")
print (my_set)