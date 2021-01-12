import datetime

def search(code):
    list = []
    file = open('module.txt','r')
    dft = [str(i) for i in file.readlines()]
    for data in dft:
        data = data.replace("\n","")
        data = data.split("|")
        list.append(data)

    for n in daftar:
        if code in n:
            print("_" * 20)
            print("book loan data")
            print("_" * 20)
            print("data was found :\n",n)
            print("your member code : ",n[0])
            print("your book title : ",n[2])
            print("your start date of borrowing : ",n[3])
            print("your max date of borrowing : ",n[4])
            yyyy,mm,dd = [int(i) for i in n[4].split("_")]
            day = (datetime.datetime(yyyy,mm,dd,0,0,0,0) - datetime.datetime.now()).days
            if day >= 0:
                print("loan time remaining : ", day," day")
            else :
                late = abs(int((datetime.datetime(yyyy,mm,dd,0,0,0,0) - datetime.datetime.now())).days)
                print("you've been late : ",late," Hari")
                print("bill : Rp", 6000 * late)
                exit()
                print("data was not found")

code = input("please entry your member code :")

search(code)



                
