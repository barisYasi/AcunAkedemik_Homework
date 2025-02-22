faiz = 1.59
vade = "36"
krediAdi = "İhtiyaç Kredisi"

print(type(faiz))
print(type(vade))
print(type(krediAdi))

print(int(vade)+12)
faiz = str(faiz)
print(type(faiz))

vade = int(input("Lütfen istediğiniz vade sayısını giriniz:"))
print(type(vade))
vade = vade + 12

#string interpolation
#Seçtiğiniz vade sonucu ortaya çıkan vade:
print("Seçtiğiniz vade osnucu ortaya çıkan vade : "+ str(vade))
print("Seçtiğiniz vade sonucu ortaya çıkan vade: {vadeSayisi}".format(vadeSayisi=vade))

isim = "Halit"
metin = "Merhaba {name}".format(name=123)
print(metin)

#f-string
metin = f"Hoşgeldiniz{1+1}"
print(metin)

krediler = ["İhtiyaç Kredisi","Taşıt Kredisi","Konut Kredisi"]
print(type(krediler))

print(krediler[0])

print(len(krediler)) #lengeth
#print(krediler[3]) => hata verir

dizi = ["İhtiyaç Kredisi",10,5.2,True]
print(dizi)


krediler.append("Özel Kredi")
print(krediler)

krediler.append("X Kredisi")
print(krediler)

krediler.pop(0)
print(krediler)

krediler.remove("Taşıt Kredisi")
print(krediler)

krediler.extend("Y Kredisi")
print(krediler)

for i in range(10):
   print("xx")
   print(i)
print("*"*50)

for i in range(5,11):
   print(i)
   print("*"*50)

for i in range(0,51,10):
    print(i)


krediler = ["İhtiyaç Kredisi","Taşıt Kredisi","Konut Kredisi"]
for kredi in krediler:
    print(kredi)
print("*"*50)

for i in range(len(krediler)):
  print(krediler[1])


#While Döngüsü
i = 0
while i < 10:
 print("x")
 i += 1

print("y")

print("*"*50)

while True:
    print("X")
    break

print("****** Son Döngü ******")

i = 0
while i < len(krediler):
   
   print(i)
   print(krediler[i])
   i += 1

   if krediler[i] == "Konut Kredisi":
      break
   

#Fonskiyonlar 

fiyat = 100
indirim = 20

#definition define
def calculate(fiyat,indirim):
   print(fiyat-indirim)

def calculateWithParams(fiyat,indirim):
   print(fiyat - indirim)


def sayHello(name):
   print(f"Merhaba {name}")


calculate(100,20)
calculateWithParams(100,20)
calculate(50,10)
sayHello("Barış")
sayHello("Yasin")
sayHello("Şahin")

def calculateAndReturn(fiyat,indirim):
   return fiyat-indirim

yeniFiyat = calculateAndReturn(200,50)
print(yeniFiyat)





