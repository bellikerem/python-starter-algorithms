import random

can_hakkı = 5

kelime_havuzu = {
    "İsim" : ["Kerem", "Alper", "Engin", "Hatun", "Emirhan", "Sefa", "Utku", "Berat", "Burak", "Bülent", "Mehmet", "Zeynep", "Nehir"
              , "Ayşe", "Fatma", "Züleyha", "Zahide", "Ali", "Ahmet", "Ömer", "Kasım", "Sabri"],
    "Şehir" : ["İstanbul", "Ankara", "İzmir", "Antalya", "Trabzon", "Eskişehir", "Kocaeli", "Sivas", "Malatya", "Konya"],
    "Ülke" : ["Türkiye", "Almanya", "Fransa", "İngiltere", "İspanya", "Hollanda", "Amerika", "Japonya", "Rusya", "İtalya","Meksika", 
              "Brezilya", "Arjantin", "Portekiz"],
    "Hayvan" : ["At", "Eşek", "Aslan", "Kartal", "Kanarya", "Balık", "Ayı", "Panda", "Koala", "Yılan", "Timsah", "Tavuk", "İnek"],
    "Bitki"  : ["Orkide", "Gül", "Gelincik", "Menekşe", "Papatya", "Domates", "Salatalık", "Soğan", "Ot"],
    "Eşya"   : ["Bilgisayar", "Telefon", "Kumanda", "Koltuk", "Sehpa", "Sandalye", "Lamba", "Defter", "Kalem"]
}

print("\n--- ADAM ASMACA ---")
while True:
    try:
        secim_input = input("Lütfen bir kategori seçiniz: \n" \
        "İsim için 1 \n" \
        "Şehir için 2 \n" \
        "Ülke için 3 \n" \
        "Hayvan için 4 \n" \
        "Bitki için 5 \n" \
        "Eşya için 6'yı tuşlayınız: ")
        secim = int(secim_input)
        if secim not in [1,2,3,4,5,6]:
            print("Lütfen 1-6 arasında bir sayı giriniz")
            continue
        break
    except ValueError:
        print("Lütfen tam sayı girişi yapınız")

def rastgele_kelime_secimi(kategori):
    global rastgele_kelime
    global uygun_kelime
    global gizlenmis_kelime
    rastgele_kelime = random.choice(kelime_havuzu[kategori])
    uygun_kelime = rastgele_kelime.lower()
    gizlenmis_kelime = ["_"]*len(uygun_kelime)

def oyun_döngüsü():
    global harf_tahmin
    global can_hakkı
    global harf_bulundu
    print("5 Can hakkınız var. Amacınız can hakkınız bitmeden kelimeyi bulmak. Bol şans :)")
    while True:
        print(gizlenmis_kelime)
        if "_" not in gizlenmis_kelime:
            print(f"TEBRİKLER {uygun_kelime} KELİMESİNİ DOĞRU TAHMİN ETTİNİZ")
            break
        if can_hakkı == 0:
            print(f"MAALESEF KAYBETTİNİZ. DOĞRU KELİME: {uygun_kelime}")
            break
        harf_tahmin = input("Lütfen küçük harf girişi yapınız: ")
        if harf_tahmin not in ["a","b","c","ç","d","e","f","g","ğ","h","ı","i","j","k","l","m","n","o","ö","p","r","s","ş","t","u","ü",
                               "v","y","z"]:
            print("Lütfen küçük harf girişi yapınız")
            continue
        if harf_tahmin in uygun_kelime:
            print("DOĞRU TAHMİN")
            harf_bulundu = False
            for i, harf in enumerate(uygun_kelime):
                if harf == harf_tahmin:
                    gizlenmis_kelime[i] = harf
                    harf_bulundu = True
        else:
            print("YANLIŞ TAHMİN")
            can_hakkı -= 1
                


if secim == 1:
    rastgele_kelime_secimi("İsim")
    oyun_döngüsü()
elif secim == 2:
    rastgele_kelime_secimi("Şehir")
    oyun_döngüsü()
elif secim == 3:
    rastgele_kelime_secimi("Ülke")
    oyun_döngüsü()
elif secim == 4:
    rastgele_kelime_secimi("Hayvan")
    oyun_döngüsü()
elif secim == 5:
    rastgele_kelime_secimi("Bitki")
    oyun_döngüsü()
else:
    rastgele_kelime_secimi("Eşya")
    oyun_döngüsü()