import random

büyük_harfler = ["A","B","C","Ç","D","E","F","G","Ğ","H","I","İ","J","K","L",
                 "M","N","O","Ö","P","R","S","Ş","T","U","Ü","V","Y","Z","X","Q","W"]
kücük_harfler = ["a","b","c","ç","d","e","f","g","ğ","h","ı","i","j","k","l",
                 "m","n","o","ö","p","r","s","ş","t","u","ü","v","y","z","x","q","w"]
rakamlar = ["0","1","2","3","4","5","6","7","8","9"]
ozel_karakter = ["!","@","#","$","%","^","&","*","?"]

while True:
    try:
        kullanici_tercihi_input = input("Banka kartı şifresi oluşturmak için 1'i diğer şifreler için 2'yi tuşlayınız: ")
        kullanici_tercihi = int(kullanici_tercihi_input)
        if kullanici_tercihi != 1 and kullanici_tercihi != 2:
            print("Lütfen 1 yada 2 yi tuşlayınız")
        elif kullanici_tercihi == 1:
            i = 0
            sifre = ""
            while i<4:
                sifre += random.choice(rakamlar)
                i += 1
            print(f"Banka kartı şifreniz: {sifre}")
        else:
            while True:
                sifre_uzunluğu_input = input("Lütfen şifre uzunluğunu belirleyiniz: ")
                sifre_uzunluğu = int(sifre_uzunluğu_input)
                if sifre_uzunluğu < 8 or sifre_uzunluğu > 18:
                    print("Lütfen 8 ile 18 arasında bir sayı giriniz")
    except ValueError:
        print("Lütfen tam sayı girişi yapınız")
