
# %% veriable (degisken)

var1 = 10 # integer = int
var2 = 15

gun="pazartesi" # string

var3 = 10.0 # double(float)

# 5var = 10  # hata verir

Var7 = 19  # standart convention of python'a gore buyuk harfle baslamasi uygun degil

# %% string 

s = "bugun gunlerden pazartesi"
variable_type = type(s)   # str = string
print(s) # s 'e atadığımız veriler okunur

var1 = "ankara"
var2 = "ist"
var3 = var1+var2 # ankaraist çıktısını alırız

var4 = "100"
var5 = "200"
var6 = var4+var5 #100200 çıktısını alırız, çünkü string değerlerdir.

uzunluk = len(var6)  #Çıktı olarak 6 değerini alırız

# %% numbers

integer_deneme = -50 # int

float_deneme = -30.7 # double = float = ondalikli sayi

# %% tür dönüşümleri

float1 = 10.6 
# int(float1) = float bir sayısı int değerine çeviriyor.
# round(float1) = onluk bir sayıyı int değere çevirme

str2 = "1005"
int(str2) # string değeri integer a çevirir.

# %% user defined functions
var1 = 20
var2 = 50
output = (((var1+var2)*50)/100.0)*var1/var2

# fonksiyon parametresi = input
def benim_ilk_func(a,b):
    
    """
    bu benim ilk denemem
    parametre:  
    return: 
    """
    output = (((a+b)*50)/100.0)*a/b
    return output
    
sonuc = benim_ilk_func(var1,var2)
print(sonuc)

# %% default ve flexible functionları

# default = Cemberin cevresini hesapla
def cember_cevresi_hesapla(r,pi=3.14): # input = r, output = cemberin cevresi
    output = 2*pi*r
    return output

# flexible
def hesapla(boy,kilo,*args):
    print(args) # istediğiniz parametreyi girebilirsin
    output = (boy+kilo)*args[0]
    return output

# %% lambda function
def hesapla(x):
    return x*x
sonuc1 = hesapla(3)
# sonuc1 ve sonuc2 de aynı işlevleri gerçekleştiriyoruz.
sonuc2 = lambda x: x*x
print(sonuc2(3))

# %% list

liste = [1,2,3,4,5,6]
type(liste) # integer liste oluşumu

liste_str = ["ptesi","sali","cars"]
type(liste_str) # string liste oluşumu

value = liste[1]
print(value) # listenin 1. indexini yazdır

last_value = liste[-1] # listenin en sonundan başlayarak -1. değerini yazdır

liste_divide = liste[0:3] # listenin 0 dan 3 e kadar olan değerlerini yazdır

liste.append(7) # listenin sonuna 7 ekle
liste.remove(7) # listeden 7 yi çıkar
liste.reverse() # listeyi terseten yazdır

liste2 = [1,5,4,3,6,7,2]
liste2.sort() # listeyi küçükten büyüğe yazdırır

string_int_liste = [1,2,3,"aa","bb"] # Karışık değişkenli liste oluşturma

# %% tuple

t = (1,2,3,3,4,5,6)

t.count(3) # t'nin içinde kaç tane 3 var
t.index(3) # 3'ün index sayısını bul

# %% dictionary

def deneme():
    dictionary = {"ali":32,"veli":45,"ayse":13}
    return dictionary

dic = deneme()

# %% conditionals
# if else statement

var1 = 10
var2 = 20

if(var1 > var2):
    print("var1 buyuktur var2")
elif(var1 == var2):
    print("var and var2 esitler")
else:
    print("var1 kucuktur var2")

# format ile yazdırma
liste = [1,2,3,4,5]
value = 3
if value in liste:
    print("evet {} degeri listenin icinde".format(value))
else:
    print("hayir")


# %% loops (donguler)

# for loop

for each in range(1,11):
    print(each) # 1'den 10'a kadar yazdır
    
for each in "ankara ist":
    print(each) # tüm harfleri tek tek yazdır
    
for each in "ankara ist".split(): 
    print(each) # split kelimeleri boşluklarına göre ayır
    
liste = [1,4,5,6,8,3,3,4,67]
summation = sum(liste) # listenin içindeki değerleri topla 

count = 0
for each in liste:
    count = count + each
    print(count) # for ile listenin içindeki değerleri topla
    
# -------------------------------------------------------------------------------------------------   
# while loop
    
i = 0
while(i <4):
    print(i)
    i = i + 1 # 0,1,2,3 değerilerini yazdırır

sinir = len(liste)   
each = 0
count = 0
while(each < sinir):
    count = count + liste[each]
    each = each + 1 

 
# %% class
 
class Calisan:
    zam_orani = 1.8
    counter = 0
    def __init__(self,isim,soyisim,maas): # constructor
        self.isim = isim
        self.soyisim = soyisim
        self.maas = maas
        self.email = isim+soyisim+"@asd.com"
        
        Calisan.counter = Calisan.counter + 1
    
    def giveNameSurname(self):
        return self.isim +" " +self.soyisim # isim ve soyismi aynı anda veren metod
        
    def zam_yap(self):
        self.maas = self.maas + self.maas*self.zam_orani
        
# class variable
calisan1 = Calisan("ali", "veli",100) 
print("ilk maas: ",calisan1.maas)
calisan1.zam_yap()
print("yeni maas: ",calisan1.maas)

calisan2 = Calisan("ayse", "hatice",200) 
calisan3 = Calisan("ayse", "yelda",600) 
calisan4 = Calisan("eren", "hilal",500) 


#  class example
liste  = [calisan1,calisan2,calisan3,calisan4]
maxi_maas = -1
index = -1
for each in liste:
    if(each.maas>maxi_maas):
        maxi_maas = each.maas
        index = each
        
print(maxi_maas)
print(index.giveNameSurname())

