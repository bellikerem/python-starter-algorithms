i = 1
girilen_notlar = []
not_sayisi = int(input("Gireceğiniz not sayısını giriniz: "))
while i<=not_sayisi:
    notlar = int(input(f"{i}. ders notunu giriniz: "))
    girilen_notlar.append(notlar)
    i += 1
notlar_toplamı = sum(girilen_notlar)
ortalama = notlar_toplamı/not_sayisi
print(ortalama)