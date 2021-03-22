#Stringlere Yakından Bakalım

print(type(123))
print(type('123'))
''' string ifadeleri kullanırken
 kesme işareti kullanmak daha doğrudur.'''

print('a' + 'b')
print('a''b')
print('a' * 3)


#String Methods

#len() 
'''içerisine girmiş olduğumuz 
ifadenin uzunluğunu geri döndürür'''

my_name  = 'irem_sena_celik'

print(len(my_name))


#upper() & lower()
'''stringlerimizi belirli standartlara 
getirmek için kullanırız'''

my_name.upper()
my_name.lower()

my_name.islower()
my_name.isupper()


#replace()
'''elimizde ki stringdeki karakterleri
değiştirmek için kullanılır.'''

my_name.replace('e' , 'i')


#strip()
'''karakterleri kırpmamızı sağlar.
Default olarak boşlukları kaldırır.'''
my_name_wspace = '*irem_sena_celik*'
print(my_name_wspace.strip("*"))


#Methodlara Genel Bakış

dir(str) 
''' kullanılabilecek methodlara erişmemizi sağlar.'''


#substringler

my_name[0]
my_name[1]
my_name[0:4] #0'dan başla 4'e kadar al.


