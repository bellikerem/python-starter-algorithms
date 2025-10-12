i = 1
girilen_notlar = []
while True:
    try:
        not_sayisi_input = (input("Gireceğiniz not sayısını giriniz: "))
        not_sayisi = int(not_sayisi_input)
        if not_sayisi < 0:
            print("Hata: Lütfen pozitif tam sayı girişi yapınız")
            continue
        break
    except ValueError:
        print("Hata: Lütfen tam sayı girişi yapınız")
while i<=not_sayisi:
    try:
        notlar_input = (input(f"{i}. ders notunu giriniz: "))
        notlar = int(notlar_input)
        if notlar < 0 or notlar > 100:
            print("Hata: Lütfen 0 - 100 arası tam sayı girişi yapınız")
            continue
        girilen_notlar.append(notlar)
        i += 1
    except ValueError:
        print("Hata: Lütfen tam sayı girişi yapınız")
        


notlar_toplamı = sum(girilen_notlar)
ortalama = notlar_toplamı/not_sayisi


if ortalama>=90:
    harf_notu = "AA"
elif ortalama>=80:
    harf_notu = "BA"
elif ortalama>=70:
    harf_notu = "BB"
elif ortalama>=60:
    harf_notu = "CC"
elif ortalama>=50:
    harf_notu = "DC"
else:
    harf_notu = "FF"

print("\n--- SONUÇLAR ---")
print(f"Girdiğiniz notlar: {girilen_notlar}")
print(f"Ortalamanız: {int(ortalama)}")
print(f"Harf notunuz: {harf_notu}")