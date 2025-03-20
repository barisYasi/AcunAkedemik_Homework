#•	1’den 100’e kadar olan sayıları ekrana yazdırın.
for i in range(0,101,1):
    print(i)

#•	1’den 100’e kadar sadece çift sayıları ekrana yazdıran bir program yazın.
print("ÇİFT SAYILAR")
print("-"*45)
for i in range(0,101,1):
    if i % 2 == 0:
        print(i)
    else:
        continue
print("-"*45)

#•	Kullanıcıdan bir sayı alıp, bu sayının faktöriyelini hesaplayan bir program yazın.
#Örnek: 5! = 5 * 4 * 3 * 2 * 1 = 120

fak_al = int(input("Lütfen faktöriyelini almak istediğiniz sayıyı giriniz: ")) 

sonuc = 1  
i = 1


while i <= fak_al:
    sonuc *= i  
    i += 1 

print(f"Girdiğiniz {fak_al} sayısının faktöriyeli: {sonuc}")

# •	1’den 100’e kadar olan tüm asal sayıları bulan bir program yazın.
for i in range(0,101,1):
    if i % 2 == 0 and i % 3 ==0 and i%5==0 and i%7==0 :
        print(f"{i} ' sayısı bir ASAL SAYI DEĞİLDİR.")
    elif i % 2 != 0 and i % 3 !=0 and i%5!=0 and i%7!=0 :
        print(f"{i} ' sayısı bir ASAL SAYIDIR.")
    