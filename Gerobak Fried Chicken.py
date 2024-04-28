print(" " * 15,"GEROBAK FRIED CHIKEN", " " * 15)
print("=" * 45)
print("Kode Jenis Potong   Harga")
print("=" * 45)
print("D    Dada           Rp 2500")
print("P    Paha           Rp 2000")
print("S    Sayap          Rp 1500")
print("=" * 45)

banyak_jenis = int(input("Banyak Jenis :"))
kode_potong = []
banyak_potong = []
jenis_potong = []
harga = []
jumlah = []

i = 0
while i<banyak_jenis:
    print("Jenis ke - ",i+1)
    kode_potong.append(input("Kode Potong [D/P/S] :"))
    banyak_potong.append(int(input("Banyak Potong :")))

    if kode_potong [i] == "D" or kode_potong [i] == "d":
        jenis_potong.append("Dada")
        harga.append("2500")
        jumlah.append(banyak_potong [i] * int(2500))
    elif kode_potong [i] == "P" or kode_potong [i] == "p":
        jenis_potong.append("Paha")
        harga.append("2000")
        jumlah.append(banyak_potong [i] * int(2000))
    elif kode_potong [i] == "S" or kode_potong [i] == "s":
        jenis_potong.append("Sayap")
        harga.append("1500")
        jumlah.append(banyak_potong [i] * int(1500))
    else :
        kode_potong [i] == ("Kode Salah")
        jenis_potong.append("Kode Salah")
        harga.append("0")
        jumlah.append(banyak_potong [i] * int(0))
    i = i+1

print(" " * 15,"GEROBAK FRIED CHIKEN", " " * 15)
print("=" * 45)
print("No  Jenis      Harga     Banyak    Jumlah")
print("    Potong     Satuan    Beli      Harga")
print("=" * 45)

a = 0
jumlah_bayar = 0
while a<banyak_jenis:
    jumlah_bayar = jumlah_bayar + jumlah[a]
    print("%i   %s      %s        %i         %i" % (a+1,jenis_potong[a],harga[a],banyak_potong[a],jumlah[a]))
    a = a+1
print("=" * 45)
pajak = jumlah_bayar * 0.1
total_bayar = jumlah_bayar + pajak
print("                    Jumlah Bayar Rp", jumlah_bayar)
print("                    Pajak 10%    Rp", pajak)
print("                    Total Bayar  Rp", total_bayar)
