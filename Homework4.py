def asal_mi():
    sayi = int(input("Lütfen kontrol etmek istediğiniz sayiyi giriniz :"))
    if(sayi ==2 or sayi==3 or sayi==5 or sayi == 7):
      print(f"{sayi}: bir asal sayidir.")
    
    elif(sayi%2==0 or sayi%3==0 or sayi%5==0 or sayi%7==0):
     print(f"{sayi} bir asal sayı değildir.")
   
    else:
     print(f"{sayi}:sayısı bir asal sayıdır")


asal_mi()


class hesap_makinesi():
    def __init__(self,sayi1,sayi2,islem):
        self.sayi1=sayi1
        self.sayi2=sayi2
        self.islem=islem

    def hesapla(self):

            if islem == '+':
                sonuc=self.sayi1+self.sayi2
                print(f"İşlemin sonucu :{sonuc}")

            elif islem == '-' : 
                sonuc=self.sayi1-self.sayi2
                print(f"İşlemin sonucu :{sonuc}")

            elif islem == '/':
                sonuc=self.sayi1/self.sayi2
                print(f"İşlemin sonucu :{sonuc}")


            elif islem == '*':
                sonuc=self.sayi1*self.sayi2
                print(f"İşlemin sonucu :{sonuc}")

            else:
                print("Yanlış tercih yaptınız...")

sayi1=int(input("Lütfen islem yapmak istediğiniz 1. sayiyi giriniz:"))
sayi2=int(input("Lütfen islem yapmak istediğiniz 2. sayiyi giriniz:"))
islem=input("Lütfen yapmak istediğiniz islemi seçiniz '+'   '-'  '/'   '*' ")

makine = hesap_makinesi(sayi1,sayi2,islem)
makine.hesapla()
