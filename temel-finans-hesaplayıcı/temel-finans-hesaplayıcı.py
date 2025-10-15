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
            return
        except ValueError:
            print("Lütfen tam sayı girişi yapınız")


def basit_faiz_hesaplayici():
    ana_para = sayi_kontrolü("Lütfen para miktarını (TL) giriniz: ", int)
    faiz_orani = sayi_kontrolü("Lütfen yıllık faiz oranını (%) giriniz: ", float)
    süre = sayi_kontrolü("Lütfen süreyi (ay) giriniz: ", int)
    faiz_farki = ana_para * (faiz_orani/100) * süre
    nihai_tutar = faiz_farki + ana_para
    print("\n--- SONUÇ ---")
    print(f"Faiz farkı: {faiz_farki}")
    print(f"Nihai tutar: {nihai_tutar}")

if kullanici_secimi == 1:
    basit_faiz_hesaplayici()
if kullanici_secimi == 2:
    None
if kullanici_secimi == 3:
    None
else:
    quit