print("\n--- TEMEL FİNANS HESAPLAYICI---")
while True:
    try:
        kullanici_secimi_input = input("Basit Faiz Hesaplayıcı için 1: \n" \
        "Taksit/Kredi Ödeme Hesaplayıcı için 2: \n" \
        "KDV Hesaplayıcıs için 3: \n" \
        "Çıkış için 4'ü tuşlayınız: ")
        kullanici_secimi = int(kullanici_secimi_input)
        if kullanici_secimi not in [1,2,3,4]:
            print("Lütfen seçeneklerdeki sayılardan birini giriniz.")
            continue
        break
    except ValueError:
        print("Lütfen tam sayı girişi yapınız")


def sayi_kontrolü(prompt,tip):
    while True:
        try:
            deger = tip(input(prompt))
            if deger<=0:
                print("Lütfen 0'dan büyük bir sayı giriniz")
                continue
            return deger
        except ValueError:
            print("Lütfen tam sayı girişi yapınız")

def basit_faiz_hesaplayici():
    print("\n--- BASİT FAİZ HESAPLAYICI ---")
    ana_para = sayi_kontrolü("Lütfen para miktarını (TL) giriniz: ", int)
    faiz_orani = sayi_kontrolü("Lütfen yıllık faiz oranını (%) giriniz: ", float)
    süre = sayi_kontrolü("Lütfen süreyi (ay) giriniz: ", int)
    faiz_farki = ana_para * (faiz_orani/100) * süre
    nihai_tutar = faiz_farki + ana_para
    print("\n--- SONUÇ ---")
    print(f"Faiz farkı: {faiz_farki} TL")
    print(f"Nihai tutar: {nihai_tutar} TL")

def taksit_hesapla():
    print("\n--- TAKSİT HESAPLAYICI ---")
    kredi_miktari = sayi_kontrolü("Lütfen kredi miktarını giriniz: ", int)
    faiz_orani = sayi_kontrolü("Lütfen yıllık faiz oranını (%) giriniz: ", float)
    süre = sayi_kontrolü("Lütfen süreyi (ay) giriniz: ", int)
    faiz_orani = faiz_orani/(100*12)
    bölüm_üst = faiz_orani*((1 + faiz_orani)**süre)
    bölüm_alt = ((1 + faiz_orani)**süre) - 1
    bölüm = bölüm_üst/bölüm_alt
    aylik_taksit = kredi_miktari * bölüm
    print("\n--- SONUÇ ---")
    print(f"Aylık kredi taksit ücretiniz {aylik_taksit} TL")

def kdv_hesapla():
    print("\n--- KDV HESAPLAYICI ---")
    toplam_tutar = sayi_kontrolü("Lütfen toplam tutarı giriniz: ", int)
    kdv = sayi_kontrolü("Lütfen KDV oranını (%) giriniz: ", int)
    while True:
        try:
            karar_input = input("KDV Eklemek için 1\n"
            "KDV Çıkarmak için 2'yi tuşlayınız: ")
            karar = int(karar_input)
            if karar not in [1,2]:
                print("Lütfen 1 yada 2 yi tuşlayınız")
                continue
            break
        except ValueError:
            print("Lütfen tam sayı girişi yapınız")
    if karar == 1:
        kdv_miktari = toplam_tutar * (kdv/100)
        eklenmis_tutar = toplam_tutar + kdv_miktari
        print("\n--- SONUÇ ---")
        print(f"KDV Eklenmiş fiyat: {eklenmis_tutar} TL")
    else:
        kdv_miktari = toplam_tutar * (kdv/100)
        cikarilmis_tutar = toplam_tutar - kdv_miktari
        print("\n--- SONUÇ ---")
        print(f"KDV Çıkarılmış fiyat: {cikarilmis_tutar} TL")


if kullanici_secimi == 1:
    basit_faiz_hesaplayici()
if kullanici_secimi == 2:
    taksit_hesapla()
if kullanici_secimi == 3:
    kdv_hesapla()
else:
    SystemExit