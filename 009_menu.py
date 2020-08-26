print("MENÜ")
print("1- Sayının karesi")
print("2- Adınız on kere")
print("3- Adınız tersten")
print("4- Çıkış")

secim = 0
while secim != "4":
    secim = input("seçiminiz:")
    if secim == "1":
        print("KARE")
        sayi = int(input("Sayı giriniz:"))
        print(sayi ** 2)
    elif secim == "2":
        print("ADINIZ 10 KERE")
        ad = input("adınız:")
        for i in range(1, 11):
            print(i, ad)
    elif secim == "3":
        print("ADINIZ TERSTEN")
        ad = input("adınız:")
        print(ad[::-1])
    else:
        print("Hatalı seçim!")

print("bay bay")
