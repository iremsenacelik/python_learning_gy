#VERİ YAPILARI - DICTIONARY

#Dictionary (sözlük) oluşturma.
'''
Listelerde olduğu gibi bir indexleme yapılamaz.
Dictionary'lerde sıralama yapılamaz.
Key-value değerlerinden oluşur.
'''

d1 = { "name" : "irem" ,
       "language" : "python",
       "about" : "learning"}

len(d1)

d2 = { "name" : ["irem" , "nisa" ] ,
       "age" : [23 , 20]}

#Eleman işlemleri

d1["name"]
d2["name"]

d3 = { "name" : {"irem" : "abla" ,
                 "nisa" : "kardes"} ,
       "age" : {23 : "buyuk",
                20 : "kucuk"}}


d3
d3["name"]
d3["age"][23]


#Eleman Ekleme & Değiştirme

d3["weight"] = {"irem" : 77.5 ,
                "nisa" : 120.5}

d3

'''
sözlüklerde verilen ancak sabit veri yapıları ile oluşturulabilir.
listelerle oluşturulamaz.
key'lerin sabitliğinden endişe etmememiz gerekir sabit olmak zorundadırlar.

'''


















