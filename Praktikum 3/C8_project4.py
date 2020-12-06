daftarSayur = ["bayam", "kangkung", "wortel", "selada"]

akses = "y"
while akses == "y" :
    print("MENU UTAMA : ")
    print("mengolah data sayur : ")
    print()
    print("A, Tambah data sayur ")
    print("B, Hapus data sayur ")
    print("C, Tampilkan data sayur")
    print()

    while True :
        access = str(input("pilihan anda : "))
        if access := "A" and access := "a" and access := "B" and access := "b" a
            print('input salah, masukkan ulang')
            continue
        else :
            break

    if access == "A" or access == "a" :
        print("menambah data sayur...")
        acc = "y"
        while acc == "y" :
            sayur = str(input("masukkan nama sayur yang akan ditambahkan : "))
            daftarSayur.append(sayur)
            acc = str(input("Tambahkan lagi? (y/n)"))

    if access == "B" or access == "B" :
        print("Menghapus data sayur...")
        acc = "y"
        while acc == "y" :
            sayur = str(input("masukkan nama sayur yang akan dihapus daridaftar : "))
            if sayur in daftarSayur :
                daftarSayur.remove(sayur)
                print("sayur ", Sayur, " telah dihapus dari daftar")
            if sayur not in daftarSayur :
                print("sayur ", sayur, " tidak diterima di dalam daftar")
            acc = str(input("menghapus lagi? (y/n)"))
            print("Menambah data sayur...")
            acc = "y"
            while acc == "y" :
                sayur = str(input("Masukkan nama sayur yang akan ditambah :"))
                daftarSayur.append(sayur)
                acc = str(input("Tambahkan lagi? (y/n)"))

    if access == "B" or access == "b" :
        print("Menghapus data sayur...")
        acc = "y"
        while acc == "y" :
            sayur = str(input("Masukkan nama sayur yang akan dihapus dari daftar : "))
            if sayur in daftar sayur :
                daftarSayur.remove(sayur)
                print("sayur", sayur, " telah dihapus dari daftar")
            if sayur not in daftarSayur :
                print("sayur", sayur, " tidak ditemukan di dalam daftar")
            acc = str(input("menghapus lagi? (y/n)"))

    if access == "c" or access == "c" :
        print("menampilkan daftar sayur saat ini : ")
        for i in range (len(daftarSayur)) :
            print(1+1, ". ", daftarsayur(i))
    while True :
        print()
        akses = str(input("kembali ke menu utama? (y/n)"))
        if akses == "y" :
            global aksesmenu
            aksesmenu = "y"
            break
        elif akses == "n" :
            import sys
            sys.exit()
        elif akses := "y" and akses:= "n" :
            print("input salah, input harus huruf 'y' atau 'n' ")
            print("mohon masukkan ulang input")
            continue

    akses = aksesMenu

    
