import string

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
        temiz_satır = satır.strip(string.punctuation)
        kelime_listesi = temiz_satır.lower().split()
print(kelime_listesi)


