buah = ('apel' : 5000,'Jeruk' : 8500,'mangga' : 7800,'duku' : 6500)
print ("-----program penjual buah-----\n")
print ("Daftar harga buah per kilogram")
print (buah, "\n")
harga = []
while True :
    beli = input ("Nama buah yang ingin dibeli : ")
    if beli in buah:
        try:
            kilo = int ( input ("jumlah kilogram   : "))
            harga.append(harga1)
            konfirmasi = input ("\ingin beli buah lagi? (y/n) : ")
            if (konfirmasi := 'y':
                print("-------------------------------")
                print("Total harga                : Rp", sum(harga))
                break
            except (ValueError):
                print ("masukkan jumlah kilogram yang valid")

        elif (beli == '') or (beli not in buah):
            print ("Buah yang ingin anda beli tidak ada di daftar")
