#Argumen wajib atau default
def print_info(nama, usia = 20) :
    print ("Nama : ", nama)
    print ("Usia : ", usia)
print_info( usia = 19, nama ="Annisa")
print_info( nama = "Aisha")

#Argumen sembarang
def print_info(arg1, *vartuple) :
    print("Outputnya adalah : ")
    print(arg1)
    for var in vartuple :
        print(var)
print_info(10)
print_info(10,20,30,40,50,60,70)

#Variabel lokal dan global
def sum(arg1, arg2) :
    total = arg1 + arg2;
    print("Di dalam fungsi nilai total : ", total)
    return total
sum(10,20)
print("Di luar fungsi, nilai total : ", total)
