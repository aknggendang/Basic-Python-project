#Alfaizi Ahmad Zahran (Aknggendang)
#20211106
#find a average number
#Python Language
#IND Version


from statistics import mean
from time import sleep


def Average(l):
    avg = mean(l)
    return avg 

nama_siswa = input('Nama siswa/siswi : ')
gender = input("Jenis kelamin :")
kelas = int(input("Kelas : "))
jurusan = input("Jurusan : ")
absen = int(input('No.Absen : '))


my_list = []
n = int(input("Masukan Jumlah Mapel : "))

for i in range (0, n):
    ele = int(input("Nilai : "))

    my_list.append(ele) 
    rata_rata = Average(my_list)
    


print("\nLoading........")
sleep(5)


print("\n=============== Hasil ===============")

print("\nNama :",nama_siswa)
print("Jenis kelamin :",gender)
print("Kelas :",kelas)
print("Jurusan :",jurusan)
print("No. Absen :",absen)
print("Nilai Rata-rata Siswa : ",rata_rata)


if rata_rata > 70:
    print("Siswa Dinyatakan LULUS")
else:
    print("Siswa Dinyatakan Tidak LULUS")    




