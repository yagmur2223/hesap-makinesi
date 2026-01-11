print("Hoş geldiniz")
while True:
    try:
        sayi1 = float(input("İlk sayıyı giriniz: "))
        sayi2 = float(input("2. sayıyı giriniz: "))
    except ValueError:
        print("Geçersiz sayı girdiniz. Tekrar deneyin.")
        continue

    islem = input("Hangi işlem olsun? (çarpma, bölme, toplama, çıkarma, çıkış): ").strip().lower()
    if islem in ("çıkış", "cikis", "exit"):
        print("Çıkılıyor.")
        break

    if islem == "çarpma":
        print("sonuç =", sayi1 * sayi2)
    elif islem == "bölme" or islem == "bolme":
        if sayi2 == 0:
            print("Hata: Sıfıra bölme.")
        else:
            print("sonuç =", sayi1 / sayi2)
    elif islem == "toplama":
        print("sonuç =", sayi1 + sayi2)
    elif islem in ("çıkarma", "cikarma"):
        print("sonuç =", sayi1 - sayi2)
    else:
        print("Geçersiz işlem girdiniz.")
