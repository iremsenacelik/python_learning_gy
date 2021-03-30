#Python da fonksiyonel programlama 


#Yan etkisiz fonksiyonlar(Pure Functions)
#Ornek1 : Bagimsizlik


A = 5

def impure_sum(b) :
    return b + A 

def pure_sum(a , b ) :
    return a + b 

impure_sum(10)
A = 10
impure_sum(10)


pure_sum(3, 7)

#Ornek2 : Olumcul yan Etkiler
#OOP

class LineCounter:
    def __init__(self , filename) :
        self.file = open(filename  , 'r')
        self.lines = []
    def read(self) :
        self.lines = [line for line in self.file]
    def count(self) :
        return len(self.lines)


lc = LineCounter('deneme.txt') 

print(lc.lines)
print(lc.count())

lc.read()

print(lc.lines)
print(lc.count())

#FP

def read(filename) :
    with open(filename , 'r') as f :
        return [line for line in f]

def count(lines) :
    return len(lines)

example_lines = read('deneme.txt')
lines_count = count(example_lines)
lines_count





#Isimsiz Fonksiyonlar (Anonymous Functions)

def old_sum(a , b) :
    return a + b
old_sum(3 , 8)

new_sum = lambda a , b : a + b
new_sum(4, 10)

sirasiz_liste = [('b' , 3) , ('a' , 8 ) , ('d' , 12) , ('c' , 1 )]
sirasiz_liste

sorted(sirasiz_liste , key = lambda x : x[1])


#Vektorel Operasyonlar ( Vectoral Operations)
#OOP ile...
a = [ 1, 2, 3, 4]
b = [ 2, 3, 4, 5]

ab = []

range(0 , len(a))

for i in range(0 , len(a)) :
    #ab[i] = a[i] * b[i]
    ab.append(a[i] * b[i])

ab


#FP ile ...

import numpy as np 

c = np.array([1,2,3,4])
d = np.array([2,3,4,5])

c*d 



#Map,Filter ve Reduce fonksiyonlari

liste = [1,2,3,4,5]

list(map(lambda x : x + 10 , liste))

'''
map: fonksiyonu bize ; verilen bir vektorun
icerisinde , belirli bir fonksiyonu calistirma
imkani verir. Ama isimsiz bir fonksiyon icin.
'''

sayilar = [1,2,3,4,5,6,7,8,9,10]

list(filter(lambda x : x % 2 == 0 , sayilar ))

'''
filter : fonksiyonu bize; verilen bir vektor 
icerisinde istenilen kosulu uygular ve true donen 
degerleri yeni bir listede doner.
'''

from functools import reduce

ls = [1,2,3,4]

reduce(lambda a,b : a + b , ls)

'''
reduce : fonksiyonu indirgeme yapar. 

'''





