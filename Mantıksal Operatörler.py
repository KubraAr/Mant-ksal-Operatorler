#Görev1
yas = 19

print(yas > 18 and yas < 65)
print(yas < 18 or yas > 65)
print(not(yas==25))

#Görev2
sayi = int(input("Bir sayı gir:"))

cift_mi = (sayi % 2 == 0)
pozitif_mi = (sayi > 0)

print("Çift mi?:", cift_mi)
print("Pozitif mi?:", pozitif_mi)

#Görev3
yas = int(input("Yaşınızı girin: "))
ehliyet = input("Ehliyetiniz var mı? (True or False): ")

if yas > 18 and ehliyet == "True":
    print("Araba kullanabilirsiniz.")
else:
    print("Araba kullanamazsınız.")
