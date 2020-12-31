""" enkripsi teks atau string dengan sandi caesar """

string = str(input("masukkan teks yg akan di enskripsi (dalam KAPITAL) : "))
change = int(input("masukkan besar pergeseran kode ASCII : "))

enkripsi = ""

for char in string :
    if char == " " :
        karakter = " "
        enkripsi = enkripsi + karakter
    elif string.isupper() :
        charcode = ord(char)
        index = ord(char) - ord("A")
        newIndex = (index + change) & 26
        kode = newIndex + ord("A")
        karakter = chr(kode)

        enkripsi = enkripsi + karakter

print("TEKS ASLI : ", string)
print("TEKS TERENKRIPSI : ",enkripsi)
