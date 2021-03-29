#VERÄ° YAPILARI - SETLER

'''
SÄ±rasÄ±zdÄ±r.
DeÄerleri eÅsizdir.
DeÄiÅtirilebilir.
FarklÄ± tipleri barÄ±ndÄ±rabilir.
'''

#Set oluÅturma

s = set()
s

l = [1, 2 , "irem"]
s = set(l)
s

ali = "lutfen_ata_bakma_uzaya_git"
type(ali)

s = set(ali)
s

#Eleman Ekleme ve ÃÄ±karma

list = ["python" , "learning"]

set3 = set(list)
set3
dir(set3)


set3.add("gelecegi")
set3

set3.add("yazanlar")
set3
'''
Sirasizdir. Rastgele eklenirler.
'''

set3.add("python")
set3


set3.remove("python")
set3
set3.discard("python")
set3

'''
Discard fonksiyonu silecek bir veri bulamasa
da hata vermez ve kod akÄ±ÅÄ±nÄ± bozmaz.
'''

#Setler arasinda kume islemleri
'''
difference() ile iki kumenin farki , "-" ifadesi
intersection() iki kume kesisimi ,  "&" ifadesi
union() iki kumenin birlesimi
symetric_difference() ikisinde de olmayanlar
''' 

set1 = set([1 ,2 ,5])
set2 = set([1 , 2, 3])

set1.difference(set2) 

set2.difference(set1)

set1.symmetric_difference(set2)

set1 - set2
set2 - set1


set1.intersection(set2)

set2 & set1

set1.union(set2)


#Setlerde sorgu islemleri

set4 = set([7,8,9])
set5 = set([5,6,7,8,9,10])

#İki kumenin kesisiminin boş 
#olup olmadigi:
    
set4.isdisjoint(set5)

#Bir kumenin butun elemanlari 
#baska bir kume icerisinde yer aliyor mu?

set4.issubset(set5)

#Bir kumenin baska bir kumeyi
#kapsayip kapsamadigi

set5.issuperset(set4)




