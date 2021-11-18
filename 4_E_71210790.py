a = int(input("Masukkan bilangan 1 : "))
b = int(input("Masukkan bilangan 2 : "))
c = int(input("Masukkan bilangan 3 : "))

if (a <= b) and (b <= c) and (c >=a) :
    print("Urutan bilangan dari yang terkecil adalah ",a,b,c)
elif (a >= b) and (b >= c) and (c <=a) :
    print("Urutan bilangan dari yang terkecil adalah ",c,b,a)
elif (c <= a) and (a <= b) and (b >= c) :
    print("Urutan bilangan dari yang terkecil adalah ",c,a,b)
elif (b <= c) and (c <= a) and (a >= b) :
    print("Urutan bilangan dari yang terkecil adalah ",b,c,a)
elif (b <= c) and (c == a) and (a >= b) :
    print("Urutan bilangan dari yang terkecil adalah ",b,c,a)
elif (a <= c) and (c <= b) and (b >= a) :
    print("Urutan bilangan dari yang terkecil adalah ",a,c,b)
elif (b <= a) and (a <= c) and (c >= b) :
    print("Urutan bilangan dari yang terkecil adalah ",b,a,c)
elif (a <= c) and (a == b) and (c >= b) :
    print("Urutan bilangan dari yang terkecil adalah ",b,c,a)
else :
    print("ye")
