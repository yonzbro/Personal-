belirlenmis_kullanici_adi = "BattalKoc"
belirlenmis_sifre = "Python"

while True:
    kullanici_adi = input("Kullanıcı adınızı giriniz : ")
    sifre = input("Sifrenizi giriniz : ")



    if belirlenmis_kullanici_adi != kullanici_adi:
        print("Kullanıcı adınız hatalı!")
    elif belirlenmis_sifre != sifre:
        print("Sifreniz hatalı!")
    else :
        print("Giriş yaptınız!")
        exit()
