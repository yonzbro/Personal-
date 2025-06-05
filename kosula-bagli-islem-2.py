sayi_1 = float(input("Birinci sayıyı giriniz : "))
ifade = input("Yapılacak işlemi giriniz : ")
sayi_2 = float(input("İkinci sayıyı giriniz : "))

if ifade == "+":
    print("Sonuç :",sayi_1+sayi_2)
elif ifade == "-":
    print("Sonuç :",sayi_1-sayi_2)
elif ifade == "*":
    print("Sonuç :",sayi_1*sayi_2)
elif ifade == "/":
    print("Sonuç :",sayi_1/sayi_2)
else :
    print("Hatalı işlem yaptınız. Program sonlandırıldı.")