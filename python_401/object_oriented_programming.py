#Nesne yonelimli progrmalama



#Sinif Ozellikleri

class VeriBilimci() :
    print('Bu bir siniftir')
    bolum = ''
    sql = 'Evet'
    deneyim_yili = 0
    bildigi_diller = []


#Sinif ozelliklerine erismek ve degistirmek

VeriBilimci.bolum

VeriBilimci.sql = 'Hayir'
VeriBilimci.sql

#Sinif Orneklendirmesi (instantication)

irem = VeriBilimci()

irem.sql
irem.bildigi_diller.append('Python')

nisa = VeriBilimci()
nisa.sql

nisa.bildigi_diller

#Ornek Ozellikleri

class VeriBilimi() :
    diller = ['R' , 'Python' , 'C++']
    def __init__(self):
        self.diller = []

irem1 = VeriBilimi()
irem1.diller

nisa1 = VeriBilimi()
nisa1.diller

irem1.diller.append('Python')
irem1.diller

nisa1.diller

VeriBilimi.diller

'''
Bu sekilde her bir obje kendine ozgu ozellikler alır.
Ve her obje ve ana sinif etkilenmez.
'''

#Ornek Metodlar

class VeriSinifi() :
    calisanalr = []
    def __init__(self):
        self.b_diller = []
        self.bolumu = ''
    def dil_ekle(self , yeni_dil) :
        self.b_diller.append(yeni_dil)


irem3 = VeriSinifi()
irem3.dil_ekle('Ruby')
irem3.b_diller

#Miras Yapilari (inheritance)

class Employee() :
    def __init__(self) :
        self.FirstName = ''
        self.LastName = '' 
        self.Address = '' 

class DataScience(Employee) :
    def __init__(self) :
        self.Programming = ''

class Marketing() :
    def __init__(self) :
        self.StoryTelling = ''
 

'''
Miras yapisi DataScience sinifinda 
ornek olarak gosterilmistir.
Marketing sinifi ile farki gosterilmistir.
'''

class New_employee() :
    def __init__(self , FirstName , LastName, Address) :
        self.FirstName = FirstName
        self.LastName = LastName 
        self.Address = Address 


iremss = New_employee('irem', 'celik', 'me')

iremss.Address
iremss.FirstName


        









