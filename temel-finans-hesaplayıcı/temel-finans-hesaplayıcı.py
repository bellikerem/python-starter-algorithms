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
    except ValueError:
        print("Lütfen tam sayı girişi yapınız")