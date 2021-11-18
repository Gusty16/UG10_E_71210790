print("===== Kalkilator Akar dan Pangkat =====")
print("Pilihan menu :")
print("1. Pangkat 2 (Kuadrat)")
print("2. Pangkat 3 (Kubik)")
print("3. Akar Kuadrat")
a = int(input("Masukkan menu yang anda pilih :"))

if a == 1 :
    b = int(input("\nMasukkan bilangan yang ingin di pangkatkan : "))
    print("Hasil dari pemangkatan bilangan",b,"dengan 2 (Kuadrat) adalah",b*b)
elif a == 2 :
    c = int(input("\nMasukkan bilangan yang ingin di pangkatkan : "))
    print("Hasil dari pemangkatan bilangan",c,"dengan 3 (Kubik) adalah",c*c*c)
elif a == 3 :
    d = int(input("\nMasukkan bilangan yang ingin di akarkan : "))
    print("Hasil dari kuadrat dari bilangan",d,"adalah",d**0.5)
else :
    print("\nPilihan menu yang dimasukkan tidak sesuai!")
