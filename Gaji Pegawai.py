#input
print("========================================")
print("       Progam Hitung Gaji Karyawan      ")
print("            PT. DINGIN DAMAI            ")
print("========================================")

nama = input("Nama Karyawan : ")
golongan = input("Golongan Jabatan [1/2/3] : ")
pendidikan = input("Pendidikan [SMA/D1/D3/S1] : ")
jumlah_jamker = int(input("Jumlah Jam Kerja : "))

#Tunjangan Jabatan
gaji_pokok=300000
if golongan=="1" :
    tunjanganjabatan= 0.05 * 300000
elif golongan=="2" :
    tunjanganjabatan= 0.1 * 300000
else :
    tunjanganjabatan= 0.15 * 300000

#Tunjangan Pendidikan
if pendidikan=="SMA" :
    tunjanganpendidikan= 0.025 * 300000
elif pendidikan=="D1" :
    tunjanganpendidikan= 0.05 * 300000
elif pendidikan=="D3" :
    tunjanganpendidikan= 0.2 * 300000
else :
    tunjanganpendidikan= 0.3 * 300000

#Honor Lembur
if jumlah_jamker >= 8 :
    honor_lembur = (jumlah_jamker - 8) * 3500
else :
    honor_lembur = 0

#Jumlah Tunjangan
tunjangan = tunjanganjabatan + tunjanganpendidikan

#Cetak Hasil
print("---------------------------------------------")
print("             Slip Gaji Karyawan              ")
print("---------------------------------------------")
print("Karyawan yang bernama    : ", str(nama))
print("Honor yang diterima")
print("    Tunjangan Jabatan    : Rp", str(tunjanganjabatan))
print("    Tunjangan Pendidikan : Rp", str(tunjanganpendidikan))
print("    Honor Lembur         : Rp", str(honor_lembur))
print("                         -------------------------- + ")
total_gaji = (gaji_pokok) + (tunjangan) + (honor_lembur)
print("Total Gaji               : Rp", str(total_gaji))
print("----------------------------------------------")
