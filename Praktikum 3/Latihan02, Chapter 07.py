namafile=input('masukkan nama file: ')
file=open('namafile','a')
try:
teks=input('data yang mau ditambahkan: ')
file.write(teks)
jawab=str(input('mau lagi(y/n): '))
while Jawab == 'y' :
    teks=input('Data yang mau ditambahkan: ')
    jawab=str(input('mau lagi(y/n): '))
if Jawab == 'n' :
    file.close()
except:
    print('Masukkan data yang benar')
