a = int(input("Masukkan jumlah perulangan : "))
daftarBil1 = []
for i in range (a) :
    bil = int(input("Masukkan Bilangan : "))
    daftarBil.append(bil)
daftarBil.sort(reverse=True)
print("Daftar bilangan terurut dari besar ke kecil : ")
print(daftarBil)
