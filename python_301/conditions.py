#True-False Sorgulamalari

sinir = 50000
gelir = 40000

gelir < sinir

#If Yapisi

if gelir < sinir :
    print('Gelir sinirdan kucuk!')

#Else Yapisi

irem = 23
nisa = 20

if irem > nisa :
    print('irem nisadan buyuk!')
else:
    print('nisa iremden buyuk!')

#Elif Yapisi

if irem > nisa :
    print('irem nisadan buyuk!')
elif nisa == irem :
    print('Yaslari esit!')
else:
    print('nisa iremden buyuk')
    
'''
istedigimiz kadar kosulu elif ile belirtebiliriz.
'''

#Mini Uygulama

magaza_adi = input('Magaza adi nedir? ')
user_gelir = int(input('Gelirinizi Giriniz : '))

if user_gelir > sinir:
    print('Tebrikler : '+ str(magaza_adi) +' promosyon kazandiniz')
elif user_gelir < sinir:
    print('Uyari! Çok dusuk gelir : ' + str(user_gelir) )
else:
    print('Takibe devam')



























