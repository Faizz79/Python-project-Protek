from datetime import *

print('welcome to our office')
def loandata(code, name, title):
    date = datetime.date(datetime.now())
    date2 = date + timedelta(days=4)
    listinput = [kode, nama, judul, str(date), str(date2)]
    file = open("module.txt", 'a')
    file.write('|'.join(listinput))
    file.write('\n')
    file.close()

while True:
    code = input('enter member code :')
    name = input('enter member name :')
    title = input('enter book title :')
    loandata(code,name,title)
    again = input('repeat again (y/n):')
    if again == 'y':
        continue
    elif again == 'n':
        break
    else:
        print('eror')
        break
