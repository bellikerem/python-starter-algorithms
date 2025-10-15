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
            print("\n--- SONUÇ ---")
            print("Lütfen 1 yada 2 yi tuşlayınız")
            continue
        elif kullanici_tercihi == 1:
            i = 0
            sifre = ""
            while i<4:
                sifre += random.choice(rakamlar)
                i += 1
            print("\n--- SONUÇ ---")
            print(f"Banka kartı şifreniz: {sifre}")
            break
        else:
            while True:
                try:
                    sifre_uzunluğu_input = input("Lütfen şifre uzunluğunu belirleyiniz: ")
                    sifre_uzunluğu = int(sifre_uzunluğu_input)
                    if sifre_uzunluğu < 8 or sifre_uzunluğu > 18:
                        print("\n--- SONUÇ ---")
                        print("Lütfen 8 ile 18 arasında bir sayı giriniz")
                        continue
                    break
                except ValueError:
                    print("\n--- SONUÇ ---")
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
                        print("\n--- SONUÇ ---")
                        print("Lütfen 1, 2 yada 3'ü tuşlayınız")
                        continue
                    break
                except ValueError:
                    print("\n--- SONUÇ ---")
                    print("Lütfen tam sayı girişi yapınız")
            sifre_listesi = [random.choice(büyük_harfler) , random.choice(kücük_harfler)]
            kalan_uzunluk = sifre_uzunluğu-2
            if kullanici_tercihi2 == 1:
                kullanilacak_havuz = büyük_harfler + kücük_harfler + rakamlar
                sifre_listesi.append(random.choice(rakamlar))
                kalan_uzunluk -= 1
            elif kullanici_tercihi2 == 2:
                kullanilacak_havuz = büyük_harfler + kücük_harfler + ozel_karakter
                sifre_listesi.append(random.choice(ozel_karakter))
                kalan_uzunluk -= 1
            else:
                kullanilacak_havuz = büyük_harfler + kücük_harfler + rakamlar + ozel_karakter
                sifre_listesi.extend([random.choice(rakamlar), random.choice(ozel_karakter)])
                kalan_uzunluk -= 2

            
            sifre_listesi.extend(random.choices(kullanilacak_havuz, k=kalan_uzunluk))
            random.shuffle(sifre_listesi)
            gercek_sifre = "".join(sifre_listesi)
            print("\n--- SONUÇ ---")
            print(f"Şifreniz: {gercek_sifre}") 
            break
    except ValueError:
        print("\n--- SONUÇ ---")
        print("Lütfen tam sayı girişi yapınız")