i = 1
girilen_notlar = []
not_sayisi = int(input("Gireceğiniz not sayısını giriniz: "))
while i<=not_sayisi:
    notlar = int(input(f"{i}. ders notunu giriniz: "))
    girilen_notlar.append(notlar)
    i += 1
notlar_toplamı = sum(girilen_notlar)
ortalama = notlar_toplamı/not_sayisi
if ortalama>=90:
    harf_notu = "AA"
elif ortalama<90 and ortalama>=80:
    harf_notu = "BA"
elif ortalama<80 and ortalama>=70:
    harf_notu = "BB"
elif ortalama<70 and ortalama>=60:
    harf_notu = "CC"
elif ortalama<60 and ortalama>=50:
    harf_notu = "DC"
else:
    harf_notu = "FF"

print(f"Girdiğiniz notlar: {girilen_notlar}")
print(f"Ortalamanız: {int(ortalama)}")
print(f"Harf notunuz: {harf_notu}")