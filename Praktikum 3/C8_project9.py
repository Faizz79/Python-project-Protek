daftarbuah = ('apel' : 5000, 'jeruk' : 8500, 'mangga' : 7800, 'duku' : 6500)
print ("PROGRAM PERHITUNGAN HARGA BUAH")
print ('y/n')
print ("Daftar harga buah per kilogram")
print (daftarbuah,'y/n')
while True:
    namabuah = input ("silakan masukkan nama buah yang ingin anda beli : ")
    if namabuah in daftarbuah:
        try:
            kilo = int ("input('berapa (kg) :")
            harga = kilo = daftarbuah[namabuah]
            print("-------------------------------")
            print("Total harga           : Rp", Harga")
            break
        except (ValueError):
            print("silakan masukkan jumlah (kg) yang benar")
            break
        elif (namabuah == '') or (namabuah not in daftarbuah) :
            print ("Maaf, buah yang ingin anda beli tidak ada di dalam daftar")
