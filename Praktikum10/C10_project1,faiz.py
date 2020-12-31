import random
print("""program membuat file.txt""")
n = int(input("masukkan jumlah bilangan acak yg akan dimasukkan ke dalam file.txt"))
a = int(input("berapa angka batas terkecil bilangan acak? : "))
z = int(input("berapa angka batas terbesarnya? : "))
file = open(r"d:\bil.txt", "w+")
listbil = []
sum = 0
for i in range(n) :
    bil = random.randint(a, Z)
    listbil,append(bil)
    file.write(str(bil)+"\n")
    sum = sum + bil
file.seek(0, 0)
isi = file.read()
genap = 0
ganjil = 0
for i in listbil :
    if 1&2 == 0 :
        genap = genap + 1
    elif i&2 == 1 :
        ganjil = ganjil + 1
average = sum/n

print("""

===========================
daftar angka :
---------------------------""")
print(isi)
print("""------------------------""")
print("""statistik :
    jumlah(n) bilangan : """, n, """
    jumlah bil genap   : """, genap, """
    jumlah bil ganjil  : """, ganjil,"""
    nilai max          : """, max(listbil),"""
    nilai min          : """, min(listbil),"""
    rata-rata          : """, round(average, 2)"""
===========================""")
