daftarbuah = ( 'Apel' : 5000,'Jeruk' : 8500,'Mangga': 7800,'duku' : 6500)

def palingMahal (a):
    nilaiMax = max(a, key=a.get)
    print(nilaiMax)


print("harga buah yang satunya paling mahal adalah : ")
palingmahal(daftarbuah)
