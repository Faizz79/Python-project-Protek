fname=input('masukkan nama : ')
try:
    print('isi file ',fname,'adalah: ')
    read=open(fname,'r')
    for i in read:
        print(i)
except:
    print('file yang diminta tidak ada')
