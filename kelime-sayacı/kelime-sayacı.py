import string

sozluk = {

}

print("\n--- Kelime Sayacı ---")
file = open("kelime-sayacı/kelime_sayacı.txt" , "w" , encoding = "utf-8")
while True:
    try:
        secenek_input = input("Lütfen dosyaya girdi yapınız. eğer yaptıysanız 1'i tuşlayınız: ")
        secenek = int(secenek_input)
        if secenek != 1:
            print("lütfen 1 dışında başka bir sayı tuşlamayınız")
            continue
        break
    except ValueError:
        print("Lütfen tam sayı girişi yapınız")
file.close()



with open("kelime-sayacı/kelime_sayacı.txt" , "r" , encoding = "utf-8") as file1:
    kelime_listesi = []
    for satır in file1:
        satır_kelimeleri = satır.lower().split()
        for kelime in satır_kelimeleri:
            temiz_kelime = kelime.strip(string.punctuation)
            if temiz_kelime:
                kelime_listesi.append(temiz_kelime)

    for i in kelime_listesi:
        if i in sozluk:
            sozluk[i] += 1
        else:
            sozluk[i] = 1

kelime_ciftleri = sozluk.items()
sirali_kelime_ciftleri = sorted(kelime_ciftleri , key = lambda item : item[1], reverse=True)


print("\n--- En Sık Geçen 10 Kelime ---")
for kelime, frekans in sirali_kelime_ciftleri[:10]:
    print(f"'{kelime}': {frekans} kez")