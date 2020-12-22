#project 4
import random
def shufflestring(kata, n):
    listkata = []
    while (len(listkata) < n):
        acakkata = random.sample(kata, len(kata))
        acakurut = ''.join(acakkata)
        if(acakurut not in listkata):
            listkata.append(acakurut)


    print(listkata)

shufflestring('kamu', 7)
