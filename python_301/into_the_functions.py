#Fonksiyonlara giris ve fonksiyon okuryazarligi

#?print


print('a' , 'b' , sep = '_')

#Fonksiyon nasil yazilir?

def kare_al( x ):
    print(x**2)
    
kare_al(15) 

#Bilgi notu ile cikti uretmek

def kare_with_script(x):
    print("Girilen sayinin karesi : " + str(x**2))

kare_with_script(9)

def kare_with_all(x):
    print(str(x) + 
          'in karesi: '
          + str(x**2) 
          + 'dir.' )
    
kare_with_all(8)

#IKI ARGUMANLI FONKSIYON TANIMLAMA

def carpma_yap( x , y ):
    print( x*y )
    
carpma_yap(6,7)


#ON TANIMLI ARGUMANLAR

def kup_carpma( x = 1 , y = 1 , z = 1):
    print( x*y*z )

kup_carpma(4 , 6)
kup_carpma(2,4,5)

kup_carpma( z = 5 , y = 3 , x = 8)

#RETURN KAVRAMI

def direkt_hesap(isi , nem ,sarj):
    print((isi + nem)/ sarj )

cikti = direkt_hesap(25, 40, 83)
cikti

print(cikti)

def return_ort(i , k):
    return (i + k)/(i*k)

ortalama = return_ort(8, 5)
ortalama
ortalama*9



#LOCAL VE GLOBAL DEGISKENLER

'''
Global degiskenler tum alanda etkilidir ,
local degiskenler fonksiyonun etki 
alanina ozgudur.
'''
a = 10
b = 20

def topla(a, b):
    return a+b

topla(a, b)

topla(5,6)


x = []

def eleman_ekle(y):
    x.append(y)
    return print(str(y) + ' îfadesi listeye eklendi.')

eleman_ekle('irem')
eleman_ekle(23)

x    






























