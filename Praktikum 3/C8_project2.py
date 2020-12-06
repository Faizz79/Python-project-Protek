x = [10, 5, 20, 5]


def dataStat(x) :
    data = tuple(x)
    listhasil = []
    nilaimaks = max(data)
    nilaimin = min(data)
    n = len(data)
    jumlahData = sum(data)
    rata2 = jumlahData/n
    rata2 = round(rata2, 2)
    listhasil.append(rata2)
    listhasil.append(nilaiMaks)
    listhasil.append(nilaiMin)
    return listhasil

print(dataStat(x))
