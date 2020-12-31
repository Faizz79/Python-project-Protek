file = open(r"d:\bilangan.txt", "r")
berkas = open("d:\hasilbil.txt", "w+")
print("""  membaca operasi dari data file (bilangan.txt) : """)
for line in file :
    bill, bill2 = line.split("|")
    bill = int(bil1)
    bil2 = int(bil2)
    print(bil1, end=' + ')
    print(bil2 , " = ")
    hasil = bil1 + bil2
    hasil = str(hasil)
    print(hasil)

    berkas.write(hasil + "\n")

file.close()
berkas.close()

file = open(r"d:\hasilbil.txt", "r")
print("""
    isi file hasil penjumlahan (hasilbil.txt) : """)
print(file.read())
