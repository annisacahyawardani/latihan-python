print(" " * 21,"DAFTAR HARGA", " " * 25)
print(" " * 18,"TOKO SEMBAKO SUKSES", " " * 20)
print("=" * 50)
print("Kode Produk   Nama Produk             Harga")
print("=" * 50)
print("1             1 Liter Beras           Rp 15000")
print("2             1 Liter Minyak Goreng   Rp 18000")
print("3             1 Kg Gula Pasir         Rp 16000")
print("4             1 Kg Telur Ayam         Rp 23000")
print("5             Susu Kental Manis       Rp 14000")
print("6             Teh                     Rp 6000")
print("7             Kopi                    Rp 8000")
print("8             Indomie                 Rp 3000")
print("9             Kecap                   Rp 10000")
print("=" * 50)

jumlah_produk = int(input(" Jumlah Produk = "))
kode_produk = []
banyak_produk = []
nama_produk = []
harga = []
jumlah = []

i = 0
while i<jumlah_produk:
    print("Produk ke -",i+1)
    kode_produk.append(input("Kode Produk [1/2/3/4/5/6/7/8/9] : "))
    banyak_produk.append(int(input("Banyak Produk : ")))

    if kode_produk [i] == "1":
        nama_produk.append("Beras            ")
        harga.append("15000")
        jumlah.append(banyak_produk [i] * int(15000))
    elif kode_produk [i] == "2":
        nama_produk.append("Minyak Goreng    ")
        harga.append("18000")
        jumlah.append(banyak_produk [i] * int(18000))
    elif kode_produk [i] == "3":
        nama_produk.append("Gula Pasir       ")
        harga.append("16000")
        jumlah.append(banyak_produk [i] * int(16000))
    elif kode_produk [i] == "4":
        nama_produk.append("Telur Ayam       ")
        harga.append("23000")
        jumlah.append(banyak_produk [i] * int(23000))
    elif kode_produk [i] == "5":
        nama_produk.append("Susu Kental Manis")
        harga.append("14000")
        jumlah.append(banyak_produk [i] * int(14000))
    elif kode_produk [i] == "6":
        nama_produk.append("Teh               ")
        harga.append("6000")
        jumlah.append(banyak_produk [i] * int(6000))
    elif kode_produk [i] == "7":
        nama_produk.append("Kopi              ")
        harga.append("8000")
        jumlah.append(banyak_produk [i] * int(8000))
    elif kode_produk [i] == "8":
        nama_produk.append("Indomie           ")
        harga.append("3000")
        jumlah.append(banyak_produk [i] * int(3000))
    elif kode_produk [i] == "9":
        nama_produk.append("Kecap            ")
        harga.append("10000")
        jumlah.append(banyak_produk [i] * int(10000))    
     
    else :
        kode_produk [i] == ("Barang tidak tersedia")
        nama_produk.append("Barang tidak tersedia")
        harga.append("0")
        jumlah.append(banyak_produk [i] * int(0))
    i = i+1

print(" " * 20,"TOKO SEMBAKO SUKSES", " " * 30)
print("=" * 60)
print("No  Nama                   Harga      Banyak     Jumlah")
print("    Produk                 Satuan     Beli       Harga")
print("=" * 60)

a = 0
jumlah_bayar = 0
while a<jumlah_produk:
    jumlah_bayar = jumlah_bayar + jumlah[a]
    print("%i   %s      %s      %i           %i" % (a+1,nama_produk[a],harga[a],banyak_produk[a],jumlah[a]))
    a = a+1
print("=" * 60)
if jumlah_bayar >= 50000:
    diskon = jumlah_bayar * 0.02
else :
    diskon = 0
total_bayar = jumlah_bayar - diskon


print("                                 Jumlah Bayar : Rp", jumlah_bayar)
print("                                 Diskon       : Rp", diskon)
print("                                 Total Bayar  : Rp", total_bayar)
ubay=int(input("                                 Uang Bayar   : Rp "))
uangkembali=ubay-total_bayar
print("                                 Uang Kembali : Rp", uangkembali)
