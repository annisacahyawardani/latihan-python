print(" " * 21,"NOSTALGIA COFFE", " " * 25)
print(" " * 18,"List Menu Minuman Coffe"," "* 20)
print("=" * 50)
print("Kode Minuman   Daftar Menu             Harga")
print("=" * 50)
print("1              Ice Cappucino           18000")
print("2              Espresso                15000")
print("3              Americano               12000")
print("4              Hazelnut                20000")
print("5              Caramel                 16000")

print("=" * 50)

jumlah_pesan = int(input("Jumlah Pesan = "))
kode_minuman= []
banyak_pesan = []
nama_menu = []
harga = []
jumlah = []

i = 0
while i<jumlah_pesan:
    print("Pesanan ke -",i+1)
    kode_minuman.append(input("Kode Minuman [1/2/3/4/5] : "))
    banyak_pesan.append(int(input("Banyak Pesan : ")))

    if kode_minuman [i] == "1":
        nama_menu.append("Ice Cappucino ")
        harga.append("18000")
        jumlah.append(banyak_pesan [i] * int(18000))
    elif kode_minuman [i] == "2":
        nama_menu.append("Espresso      ")
        harga.append("15000")
        jumlah.append(banyak_pesan [i] * int(15000))
    elif kode_minuman [i] == "3":
        nama_menu.append("Americano     ")
        harga.append("12000")
        jumlah.append(banyak_pesan [i] * int(12000))
    elif kode_minuman [i] == "4":
        nama_menu.append("Hazelnut      ")
        harga.append("20000")
        jumlah.append(banyak_pesan [i] * int(20000))
    elif kode_minuman [i] == "5":
        nama_menu.append("Caramel       ")
        harga.append("16000")
        jumlah.append(banyak_pesan [i] * int(16000))
    else :
        kode_minuman [i] == ("Kode MInuman tidak tersedia")
        nama_menu.append("Menu tidak tersedia")
        harga.append("0")
        jumlah.append(banyak_pesan [i] * int(0))
    i = i+1

print(" " * 20,"NOSTALGIA COFFE", " " * 30)
print("=" * 60)
print("No  Menu                Harga      Banyak     Jumlah")
print("                        Satuan     Beli       Harga")
print("=" * 60)

a = 0
jumlah_bayar = 0
while a<jumlah_pesan:
    jumlah_bayar = jumlah_bayar + jumlah[a]
    print("%i   %s      %s      %i           %i" % (a+1,nama_menu[a],harga[a],banyak_pesan[a],jumlah[a]))
    a = a+1
print("=" * 60)
if jumlah_bayar >= 50000:
    diskon = jumlah_bayar * 0.05
else :
    diskon = 0
total_bayar = jumlah_bayar - diskon


print(f"                                 Jumlah Bayar : Rp {jumlah_bayar}")
print(f"                                 Diskon       : Rp {diskon}")
print(f"                                 Total Bayar  : Rp {total_bayar}")
ubay=int(input("                                 Uang Bayar   : Rp "))
uangkembali=ubay-total_bayar
print(f"                                 Uang Kembali : Rp {uangkembali}")
