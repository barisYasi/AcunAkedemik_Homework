#•	Kullanıcının girdiği bir sayının tek mi çift mi olduğunu bulan bir Python programı yazın.
sayi = int(input("Lütfen Kontrol etmek istediğiniz sayıyı giriniz : "))
if sayi % 2 == 0:
    print(f"{sayi} : sayısı çift bir sayıdır... ")
elif sayi % 2 != 0:
    print(f"{sayi} : sayısı tek bir sayıdır...")
else:
    print("Girdiğiniz sayı negatiftir...")sss


#•	Kullanıcının notunu alarak aşağıdaki not sistemine göre harf notunu hesaplayın:
# 90-100 -> A
# 80-89  -> B
# 70-79  -> C
# 60-69  -> D
# 0-59   -> F

notu = int(input("Lütfen notunuzu giriniz : "))

if notu >=  90 and notu <= 100:
    print(f"{notu} ALDIĞNIZ NOTTUR VE HARF PUANINIZ > > A < <") 

elif notu >=  80 and notu <= 89:
    print(f"{notu} ALDIĞNIZ NOTTUR VE HARF PUANINIZ > > B < <") 

elif notu >=  70 and notu <= 79:
    print(f"{notu} ALDIĞNIZ NOTTUR VE HARF PUANINIZ > > C < <")

elif notu >=  60 and notu <= 69:
    print(f"{notu} ALDIĞNIZ NOTTUR VE HARF PUANINIZ > > D < <")  

elif notu >=  0 and notu <= 59:
    print(f"{notu} ALDIĞNIZ NOTTUR VE HARF PUANINIZ > > F < <") 

else:
    print("Negatif bir değer girdiniz ...")


# •	Kullanıcının yaşına göre hangi yaş grubunda olduğunu bulan bir program yazın:
# 0-12 yaş: Çocuk
# 13-19 yaş: Genç
# 20-59 yaş: Yetişkin
# 60 ve üzeri: Yaşlı

age = int(input("Lütfen yaşınızı  giriniz : "))

if age >= 0 and age <= 12:
    print(f"{age} yaşındasınız ve bulunduğunuz kategori :  > > ÇOCUK < <") 

elif age >= 13 and age <= 19:
    print(f"{age} yaşındasınız ve bulunduğunuz kategori :  > > GENÇ < <") 

elif age >= 20 and age <= 59:
    print(f"{age} yaşındasınız ve bulunduğunuz kategori :  > > YETİŞKİN < <") 

elif age >= 60:
    print(f"{age} yaşındasınız ve bulunduğunuz kategori :  > > YAŞLI < <") 
else:
    print("Negatif değer girdiniz ...")