from datetime import *

def diffdate(x):
    sekarang = datetime.date(datetime.now())
    x = x.split('-')
    x = date(int(x[0]),int(x[1]),int(x[2]))
    result = x - sekarang
    result = result.days
    print (result)

diffdate('2021-01-12')
