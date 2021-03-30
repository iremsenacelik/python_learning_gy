#Modul Olusturmak

'''
Moduller amaclarimiza ve isteklerimize uygun
olacak bicimde ,  istedigimiz sekilde yazılabilir.
'''

#Hatalar / Istisnalar (exceptions)

#ZeroDivisionError
a = 10
b = 0
a/b

try:
    print(a/b)
except ZeroDivisionError :
    print('Payda da sifir olmaz.')


#type hatasi

c = 10
d = '2'
c/d

try :
    print(c/d)
except TypeError :
    print('Sayi ve string ifadeler bolunemez')


