#VERİ YAPILARI

#Listeler ve özellikleri
''' 
1.Değiştirilebilirdir.
2.Farklı tipte verileri tutabilir.
3.Sıralıdır.

Liste oluşturmak için iki yol var.
1.si [] , 2.si list() ile

'''

grades = [90 , 80 , 70 , 50]
type(grades)

list = ['a' , 19.3 , 60 , grades]
list2 = ['b' , 'c' , 21]
len(list)

type(list[0])

list[3]

list_all = [list , list2]

#Elemanlara erişmek

array = [10,20,30,40,50]

array[0]

array[:3]
array[2:]

new_array = [ 2 , 6 , ['i' , 'r' , 'e' , 'm']]
new_array

new_array[2 ]
new_array[2][2]

#Elemanları değiştirme

names = ['irem ' , 'nisa ' , 'tugrul', 'anne']

names[3]
names[3] = 'cigdem'

names = names + ['baba']
names
del names[4]
names


#Liste methodları

dir(list)

#append() & remove()

names.append('ayse')
names

names.remove('tugrul')
names


#insert() & pop()

name = ['i' , 'r' , 'e' , 'm']
name

name.insert(2, 'k')
name

name.insert(len(name), 'a')
name

name.pop(len(name)-1)
name

#count() & copy() & extend() & index() & reverse() & sort() & clear()

list_e = ['ai' , 'ai' , 'hai' , 'mai' , 'ai']

list_e.count('ai')

'''copy()
Elimizdeki daha sonra kullanmak isteyeceğimiz 
bir listeyi başka bir listeye kopyalamamızı sağlar. 
'''
coppied_list = list_e.copy()
coppied_list

'''extend()
iki listeyi birleştirmek için kullanılır.
'''
list_e.extend(['hai' , 'kai'])

list_e.index('mai')

name.reverse()
name

'''sort()
sıralama yapmak için kullanılır.
type duyarlıdır.
'''

numbers = [10,60,8,41,3,7]
numbers.sort()
numbers

numbers.clear()
numbers






