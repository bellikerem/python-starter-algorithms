büyük_harfler = ["A","B","C","Ç","D","E","F","G","Ğ","H","I","İ","J","K","L",
                 "M","N","O","Ö","P","R","S","Ş","T","U","Ü","V","Y","Z","X","Q","W"]
kücük_harfler = ["a","b","c","ç","d","e","f","g","ğ","h","ı","i","j","k","l",
                 "m","n","o","ö","p","r","s","ş","t","u","ü","v","y","z","x","q","w"]
rakamlar = [0,1,2,3,4,5,6,7,8,9]
ozel_karakter = ["!","@","#","$","%","^","&","*","?"]


while True:
    try:
        sifre_uzunluğu_input = input("Lütfen oluşturulacak şifrenin uzunluğunu giriniz: ")
        sifre_uzunluğu = int(sifre_uzunluğu_input)
        if sifre_uzunluğu <8 or sifre_uzunluğu>18 :
            print("Lütfen 8 ile 18 arasında bir sayı girişi yapınız")
            continue
        break
    except ValueError:
        print("Lütfen tam sayı girişi yapınız")