# -*- coding: utf-8 -*-
"""
Created on Tue Sep 10 16:01:39 2024

@author: YUNUS
"""

sayi1=12
sayi2=23
print("çarpma",sayi1*sayi2)

#değişken türü
print(type(sayi1))
print(type(sayi2))

#ramdeki yeri
print(id(sayi1))
print(id(sayi2))


#float


sayi1=11.4
sayi2=15.3

print("çarpma:",sayi1*sayi2)
print(type(sayi1))
print(type(sayi2))
#%%
#karakter diizisi değişkeni str(string)
isim="yunus baba"
soyisim='SUNTAY'
print(isim,type(isim))
print(soyisim,type(soyisim))
#length
print(len(isim))
print(len(soyisim))

print(isim,soyisim)
#contenecate
ismintamami=isim+" "+soyisim

print(ismintamami)
print(ismintamami[1],ismintamami[2],ismintamami[5])



#str elemanlarına ulaşmak
#değişkenlerin ramde depolanması

#heapte depolanır ramde
import sys

sayi1=111
str1="karaköy"


print(sys.getsizeof(sayi1))
print(sys.getsizeof(str1))

meyve="armut"
print(meyve[1])
print(meyve[2])
print(meyve[3])
print(meyve[4])

#tip dönüşümü(type conversion)
x=6
y=10
z="54"
print(z*2)
print(int(z)*2)

print(17/2)
print(int(17/2))
print(17//2)
#%%kullanıcıdan girdi alma(input)
girdi1=input("sayı gir:")


#kullanıcıdan girdi alma işlemleri
isim=input("isim gir:")
doğumyili=int(input("doğum yılı gir:"))
print("MERHABALARAQ {} {}".format(isim,2024-doğumyili))

