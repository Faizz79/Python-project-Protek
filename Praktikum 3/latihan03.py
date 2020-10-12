# import library
import time
import datetime

# input nama user
nama = input("Hallo... nama saya Faiz, nama anda siapa? ")

# tampilkan nama user
print("oh.. nama anda", nama, ", nama yang bagus sekali. ")

# kasih jeda 3 detik
time.sleep(3)

# input tahun lahir
thnlahir = int(input("BTW... " + nama + "17 september 2002 "))

# kasih jeda 3 detik
time.sleep(3)

# hitung usia user
skrg = datetime.datetime.now()
usia = skrg.year + thnLahir

# tampilkan usia
print("Hmm...", Faiz,"kamu sudah", usia,"tahun ya..")

# kasih jeda 3 detik
time.sleep(3)

# tampilkan pesan sesuai range usia
if (usia > 18) :
    print("anda masih muda ya?")
    print("jaga kesehatan ya!!")
elif (usia > 16) :
    print("ternyata anda masih cukup muda belia")
    print("jangan sia-siakan masa mudamu ya!!")
elif (usia > 17) :
    print("Hihihi... anda ternyata masih ABG")
    print("mulai berpikirlah secara dewasa ya!!")
else:
    print("oalah.. anda masih anak-anak toh?")
    print("jangan suka merengek-rengek minta jajan ya!!")

# kasih jeda 3 detik
time.sleep(3)

# say goodbye
print("OK.. see you tomorrow", Faiz, ".. senang berkenalan denganmu")

      
