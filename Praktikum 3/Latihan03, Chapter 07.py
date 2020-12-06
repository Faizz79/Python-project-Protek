print('-------------------------------------------')
print('PROGRAM HITUNG RATA-RATA')
PRINT('-------------------------------------------')

data=(]
sum=0
i=0
try:
    angka=int(input('masukkan bilangan bulat: '))
except valueError:
    print('Bukan bilangan bulat')
jawab=str(input('lagi(y/n): '))
while jawab == 'y' :
    try:
        angka=int(input('masukkan bilangan bulat: '))
    except valueError:
        print('bukan bilangan bulat')
        angka=int(input('masukkan bilangan bulat: '))
    jawab=str(input('Lagi(y/n): '))
if jawab == 'n' :
    i += 1
    for angka in data:
        sum += angka
    rerata=sum/i
    print('Rata - ratanya adalah: ',rerata)

