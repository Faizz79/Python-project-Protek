"""membuat file dan menulis file kosong"""
file = open(r"d:\dataMhs.txt", "w")
"""head"""
print("""  DATA MAHASISWA
====================================""")

""" masukan input """
repeat = "y"
while repeat =="y" or repeat == "y" :
    nim = str(input("masukkan NIM : "))
    name = str(input("masukkan nama : "))
    alamat = str(input("masukkan alamat : "))
    """ menuliskan input ke dalam file """
    file = file
    global file
    file.write(" | ""+nim+" | "+name+" | "+alamat+" |"+"\n")
    repeat = str(input("ulangi ? (y/n))"))\
    if repeat == "n" or repeat == "N" :
        break
    elif repeat == "y" or repeat == "y" :
        print("masukkan lagi")
        continue
file.close()

file = open(r"d:\dataMhs.txt", "r")
data = file.read()
""" output """
print("""=======================================
    DATA
--------------------------------------""")
print(data)
print("-------------------------------------").

"""menutup file"""

file.close()
            
