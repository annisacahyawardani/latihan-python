def format_rupiah(uang):
    uang_str = str(uang).replace('-', '')
    if '.' in uang_str:
        rupiah, desimal = uang_str.split('.')
    else:
        rupiah, desimal = uang_str, '00'
    
    ribuan = ''.join([rupiah[::-1][i:i+3] + '.' if i < len(rupiah) else '' for i in range(0, len(rupiah), 3)])[::-1].strip('.')
    
    hasil = ribuan + ',' + desimal[:2]

    return 'Rp ' + hasil if uang >= 0 else '-Rp ' + hasil

# Contoh list dengan banyak nominal
nominals = [1500000, 2500.75, 10000000, -500000]

# Loop untuk memformat setiap nominal
for nominal in nominals:
    print(format_rupiah(nominal))
