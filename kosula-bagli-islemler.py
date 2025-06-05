print("""
    1) Ankara
    2) İstanbul
    3) İzmir
    4) Konya
""")

a = input("Herhangi bir şehri seçiniz : ")

if a == "1":
    print("Ankara'yı seviyor musunuz?")
elif a == "2":
    print("İstanbul'un neyi meşhur?")
elif a == "3":
    b = input("İzmir'i neden seçtiniz? : ")
elif a == "4":
    print("Konya neden bu kadar düz!")
else :
    print("Sadece seçenekleri yazınız.")