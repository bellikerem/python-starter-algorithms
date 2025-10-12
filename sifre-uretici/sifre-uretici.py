import random

büyük_harfler = ["A","B","C","Ç","D","E","F","G","Ğ","H","I","İ","J","K","L",
                 "M","N","O","Ö","P","R","S","Ş","T","U","Ü","V","Y","Z","X","Q","W"]
kücük_harfler = ["a","b","c","ç","d","e","f","g","ğ","h","ı","i","j","k","l",
                 "m","n","o","ö","p","r","s","ş","t","u","ü","v","y","z","x","q","w"]
rakamlar = ["0","1","2","3","4","5","6","7","8","9"]
ozel_karakter = ["!","@","#","$","%","^","&","*","?"]

while True:
    try:
        print("\n---Seçenekler---")
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
            break
        else:
            while True:
                try:
                    sifre_uzunluğu_input = input("Lütfen şifre uzunluğunu belirleyiniz: ")
                    sifre_uzunluğu = int(sifre_uzunluğu_input)
                    if sifre_uzunluğu < 8 or sifre_uzunluğu > 18:
                        print("Lütfen 8 ile 18 arasında bir sayı giriniz")
                        continue
                    break
                except ValueError:
                    print("Lütfen tam sayı girişi yapınız")
            while True:
                try:
                    print("\n---Seçenekler---")
                    kullanici_tercihi_input2 = input("Şifrede büyük ve küçük harf zorunludur \n" \
                    "yanında rakamların olması için 1'i\n" \
                    "yanında özel karakterler olması için 2'yi\n" \
                    "her 2 si için 3'ü tuşlayınız: ")
                    kullanici_tercihi2 = int(kullanici_tercihi_input2)
                    if kullanici_tercihi2 != 1 and kullanici_tercihi2 != 2 and kullanici_tercihi2 != 3:
                        print("Lütfen 1, 2 yada 3'ü tuşlayınız")
                        continue
                    break
                except ValueError:
                    print("Lütfen tam sayı girişi yapınız")
            if kullanici_tercihi2 == 1:
                while True:
                    büyük_harf_icin = random.randint(1,sifre_uzunluğu)
                    kücük_harf_icin = random.randint(1,sifre_uzunluğu-büyük_harf_icin)
                    if büyük_harf_icin + kücük_harf_icin == sifre_uzunluğu:
                        continue
                    else:
                        break
                rakamlar_icin = sifre_uzunluğu-(büyük_harf_icin + kücük_harf_icin)
                i = 0
                sifre = ""
                while i<büyük_harf_icin:
                    sifre += random.choice(büyük_harfler)
                    i += 1
                i = 0
                while i<kücük_harf_icin:
                    sifre += random.choice(kücük_harfler)
                    i += 1
                i = 0
                while i<rakamlar_icin:
                    sifre += random.choice(rakamlar)
                    i += 1
                liste_sifre = list(sifre)
                random.shuffle(liste_sifre)
                gercek_sifre = "".join(liste_sifre)
                print(f"Şifreniz: {gercek_sifre}")
                break
            elif kullanici_tercihi2 == 2:
                while True:
                    büyük_harf_icin = random.randint(1,sifre_uzunluğu)
                    kücük_harf_icin = random.randint(1,sifre_uzunluğu-büyük_harf_icin)
                    if büyük_harf_icin + kücük_harf_icin == sifre_uzunluğu:
                        continue
                    else:
                        break
                ozel_karakter_icin = sifre_uzunluğu-(büyük_harf_icin + kücük_harf_icin)
                i = 0
                sifre = ""
                while i<büyük_harf_icin:
                    sifre += random.choice(büyük_harfler)
                    i += 1
                i = 0
                while i<kücük_harf_icin:
                    sifre += random.choice(kücük_harfler)
                    i += 1
                i = 0
                while i<ozel_karakter_icin:
                    sifre += random.choice(ozel_karakter)
                    i += 1
                liste_sifre = list(sifre)
                random.shuffle(liste_sifre)
                gercek_sifre = "".join(liste_sifre)
                print(f"Şifreniz: {gercek_sifre}")
                break
            else:
                while True:
                    büyük_harf_icin = random.randint(1,sifre_uzunluğu)
                    kücük_harf_icin = random.randint(1,sifre_uzunluğu-büyük_harf_icin)
                    rakamlar_icin = random.randint(1, sifre_uzunluğu-(büyük_harf_icin + kücük_harf_icin))
                    if büyük_harf_icin + kücük_harf_icin + rakamlar_icin == sifre_uzunluğu:
                        continue
                    else:
                        break
                ozel_karakter_icin = sifre_uzunluğu-(büyük_harf_icin + kücük_harf_icin + rakamlar_icin)
                i = 0
                sifre = ""
                while i<büyük_harf_icin:
                    sifre += random.choice(büyük_harfler)
                    i += 1
                i = 0
                while i<kücük_harf_icin:
                    sifre += random.choice(kücük_harfler)
                    i += 1
                i = 0
                while i<rakamlar_icin:
                    sifre += random.choice(rakamlar)
                    i += 1
                i = 0
                while i<ozel_karakter_icin:
                    sifre += random.choice(ozel_karakter)
                    i += 1
                liste_sifre = list(sifre)
                random.shuffle(liste_sifre)
                gercek_sifre = "".join(liste_sifre)
                print(f"Şifreniz: {gercek_sifre}")
                break
        break
    except ValueError:
        print("Lütfen tam sayı girişi yapınız")
