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
    global gizlenmis_kelime
    rastgele_kelime = random.choice(kelime_havuzu[kategori])
    gizlenmis_kelime = ["_"]*len(rastgele_kelime)
    print(gizlenmis_kelime)

if secim == 1:
    rastgele_kelime_secimi("İsim")
elif secim == 2:
    rastgele_kelime_secimi("Şehir")
elif secim == 3:
    rastgele_kelime_secimi("Ülke")
elif secim == 4:
    rastgele_kelime_secimi("Hayvan")
elif secim == 5:
    rastgele_kelime_secimi("Bitki")
else:
    rastgele_kelime_secimi("Eşya")