na, nb, nc = list(input("Masukkan daftar siswa : ") .split(", "))
nac = na.title()
nbc = nb.title()
ncc = nc.title()
print("\nDaftar Siswa : ['"+nac+"', '"+nbc+"', '"+ncc+"']")
b = input("\nMasukkan siswa yang ingin ditambahkan : ")
bc = b.title()
bcu = bc.upper()
if (bc == nac) :
    print("\nSiswa atas nama",bcu,"sudah berada dalam daftar siswa")
elif (bc == nbc) :
    print("\nSiswa atas nama",bcu,"sudah berada dalam daftar siswa")
elif (bc == ncc) :
    print("\nSiswa atas nama",bcu,"sudah berada dalam daftar siswa")
else :
    print("\nHasil penambahan pada daftar siswa : ['"+nac+"', '"+nbc+"', '"+ncc+"', '"+bcu+"']")
