print("kodlamio")
baslik= "Taşıt Kredisi"
print(baslik)
#string => metinsel ifade
baslik = "İhtiyaç Kredisi"
print(baslik)
#int,integer => tam sayı
vade = 36
vade2 = "36"
ekVade = 12

#float
ayliködeme= 200.50

#boolen,bool =>True veya False
yükseltiMi = False

#matematiksel operatörler
#-
print(5-5)
print(vade - 12)
print(vade - ekVade)
print(36-6)

#*
print(5*5)
print(vade*2)
print(vade*ekVade)
print(10*10)

#/
print(5/5)
print(vade / 2)
print(vade / ekVade)
print(10/2)

yeniVade = vade / 2
fiyat = 100
indirimlifiyat = fiyat - 20

print(yeniVade)
print(indirimlifiyat)

#= % => mod operatörler
print(10 % 2)
print(vade % 5)
print(vade % ekVade)
print(30 % 10)

#mantıksal operatörler
print(1 == 1)
print(1 == 2)

print(1 > 2)
print(3 >1)
print(1 > 1)
print(1 >= 1 )

print(1 < 2)
print(3 < 1)
print(1 < 1)
print(1 <= 1)

print(1 != 1)
print(1 != 2)

#or and
print(1 > 2  or 5 > 2)

#or => veya 
print(1 > 2  or 5 > 2)
print(1 > 2  and  5 > 2)
print(1 > 2  or 5 > 2  and 3 > 2)

print(2 > 1 or 1 > 2 and 3 > 2)

#karar yapıları 
#if else
sayi1 = 10
sayi2 = 15

#sayi1 sayi2'den büyükse ekrana sayi1 daha büyük yazdır 
#condiation

#indent
if sayi1 > sayi2:
 print("Sayi 1  Sayi 2 den büyüktür.")
 print("Hala if bloğunun içerisindeyim")

#farklı bir opsiyon
elif sayi1 == sayi2:
 print("İki sayi eşittir")

 #eğer if ve else if bloklarından hiçbirine girmez ise
else:
 print("Sayi 2  Sayi 1 den büyüktür")

print("Burası if bloğunun dışıdır")








