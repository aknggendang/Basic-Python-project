from math import sqrt



print("============= Pythagoras =============")

print("ini adalah Kalkulator Pitagoras,asmusikan hypotenusa sebagai C")
rumus = input("Pilih Salah satu Sisi (a,b,c) :")


if rumus == 'a':
    b = int(input("Masukan sisi b: "))
    c = int(input("Masukan sisi C: "))

    a = sqrt(c**2 - b**2)

    print("Hasilnya Adalah: ",a)


elif rumus == 'b':
    a = int(input("Masukan sisi a: "))
    c = int(input("Masukan sisi c: "))

    b = sqrt(c**2 - a**2)    
    print("Hasilnya Adalah: ",b)

elif rumus == 'c':
    a = int(input("Masukan sisi a: "))
    b = int(input("Masukan sisi b: "))

    c = sqrt(a**2 + b**2)
    print("Hasilnya Adalah: ",c)


         

