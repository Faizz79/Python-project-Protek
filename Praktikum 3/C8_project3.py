access = "y"
daftarNama = []
while access == "y" :
    data = str(input("Masukkan nama Mahasiswa : "))
    daftarNama.append(data)
    access = str(input("masukkan lagi? (y/n)"))

daftarNama.sort()
daftar = tuple(daftarNama)
print()
print("Daftar Nama : ")
for i in range (len(daftarNama)) :
    print(daftarNama[i], " (", len(daftarNama[i]), " karakter )")
    
