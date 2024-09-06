#Неизменяемые и изменяемые объекты. Кортежи
immutable_bar = 777, False, "Sunshine", 3.14, [1, 2]
print (immutable_bar, '\n')

#immutable_bar[0] = 365
#Изменения недопустимы к элементам кортежа
immutable_bar[4][0] = 3
print (immutable_bar, '\n')
#Изменить можно только список, хоть он и находится внутри кортежа

mutable_list = [777, False, 3.14, "Sunshine"]
print (mutable_list)
mutable_list[0] = 365
mutable_list[2] = mutable_list[2] /2
mutable_list.remove(False)
mutable_list.extend("bright")
print (mutable_list)