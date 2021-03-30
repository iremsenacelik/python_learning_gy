#For Dongusu

ogrenci = ['ali' , 'veli' , 'isik' , 'berk']

ogrenci[0]
ogrenci[1]
ogrenci[2]
ogrenci[3]

for i in ogrenci :
    print(i)

#For dongusu - ornek


#Mini Uygulama 
#if,for ve fonksiyonlari birlikte kullanmak

maaslar = [1000,2000,3000,4000,5000]

def maas_ust(x) :
    return (x*10/100 + x)

def maas_alt(x) :
    return (x*20/100 + x)

for i in maaslar :
    #print(i)
    if i >= 3000 :
        print(maas_ust(i))
        
    else:
        print(maas_alt(i))
        

#Break ve Continue

'''
donguler içerisinde belirli sarti saglayan
ifadeler yakalandıgında , dongu bitirilmek istenebilir.
Veya gormezden gelinmek isteniyor olabilir.
'''

maaslar2 = [8000,5000,2000,1000,3000,7000,1000]

maaslar2.sort()
maaslar2

for i in maaslar2 :
    if i == 3000:
        print('Kesildi')
        break
    print(i)


for i in maaslar2:
    if i == 3000:
        continue
    print(i)

#while

sayi = 1

while sayi < 10 :
    print(sayi)
    sayi += 1
    





