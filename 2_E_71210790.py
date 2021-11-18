a = float(input("Masukkan suhu tubuh Anda : "))

if a > 50 :
    print("Anda bukan Manusia :)")
elif (a > 37.5) and (a <= 50) :
    print("Anda demam! Jangan berpergian ke tempat fasilitas Umum.")
elif (a >= 32) and (a <=37.5) :
    print("Suhu Anda normal!")
else :
    print("Anda kedinginan! Silahkan cari sesuatu yang hangat!")
