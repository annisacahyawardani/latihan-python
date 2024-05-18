#Menghitung Nilai

nilai = int(input("Masukan Nilai : "))
if nilai >10 and nilai <=50:
    print("Nilai Kurang")
elif nilai >50 and nilai <=70:
    print("Nilai Cukup")
elif nilai >70 and nilai <=85:
    print("Nilai Baik")
elif nilai > 85:
    print("Nilai Sangat Baik")
else :
    print("Tidak masuk dalam kriteria")
