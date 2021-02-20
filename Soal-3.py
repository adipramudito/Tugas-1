#Menentukan kelulusan siswa
Nteori=float(input("Nilai ujian teori: "))
Npraktek=float(input("Nilai ujian praktek: "))
if Nteori>=70 and Npraktek>=70:
    print("Selamat anda lulus!")
elif Nteori>=70 and Npraktek<70:
    print("Anda harus mengulang ujian praktek.")
elif Nteori<70 and Npraktek>=70:
    print("Anda harus mengulang ujian teori.")
else: print("Anda harus mengulang ujian teori dan praktek.")
