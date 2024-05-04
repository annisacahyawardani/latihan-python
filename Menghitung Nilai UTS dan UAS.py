#variabel yang berulang menggunakan list atay matriks
list_nim = []
list_uts = []
list_uas = []
list_total = []

ulang = 2
for i in range(ulang):
    print("Data Ke- " + str(i+1))
    list_nim.append(input("Masukan NIM Anda :"))
    list_uts.append(int(input("Masukan Nilai UTS Anda :")))
    list_uas.append(int(input("Masukan Nilai UAS Anda :")))

#Proses
for i in range(ulang):
    list_total.append((list_uts[i] + list_uas[i]) /2)
    
#Cetak
print("=" * 50)
print("NIM      Nilai UTS   Nilai UAS   Nilai Total")
print("=" * 50)
for i in range (ulang):
    print("%s   %i          %i          %i" % (list_nim[i], list_uts[i], list_uas[i], list_total[i]))
print("=" *50)
