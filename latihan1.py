# Tampilan Heading
print('=' *35)
print('     KOLAM RENANG SUKA-SUKA      ')
print('=' *35)
'''Bagian Sambutan'''
print('SELAMAT DATANG DI KOLAM RENANG TERBESAR KE - 2 DI ASIA TENGGARA!! \n\n' \
'HAL YANG DILARANG DILAKUKAN DI AREA KOLAM \n' \
'1.) Dilarang Berlarian\n' \
'2.) Dilarang Makan Di Dalam Kolam\n' \
'3.) Dilarang Mendorong Teman \n\n' \
'Himbauan !! : \n\n' \
'1.) Awasi Barang Bawaan Anda\n' \
'2.) Awasi Buah Hati Anda Saat Bermain Air')

print('=' *55)
print('No \t Kategori \t H-Biasa \t H-Libur')
print('=' *55)
print('1 \t Dewasa \t Rp. 45.000 \t Rp. 52.000')
print('2 \t Anak-anak \t Rp. 32.000 \t Rp. 42.000')
print('=' *55)

# Bagian Input
def input_user ():
    try:
            b_jenis = int(input('Masukan Bnayak jenis Yang Dibeli = '))
            if b_jenis <= 0:
                    print('Jumlah Jenis Harus Positif !')
                    return []
    except ValueError:
       print('Input Harus Berupa Angka!!')
       return[]
    
    penampung = []
    '''Masuk Kedalam Loop'''
    for i in range (1, b_jenis + 1):
                   print(f'Jenis Ke - {i}')
                   ktgr = input('Masukan Kategori Pengunjung [D/A]= ').upper()
                 
            #      Validasi Kategori
                   if ktgr == 'D':
                        kategori = 'Dewasa'
                        h_libur = 52000
                        h_biasa = 45000
                   elif ktgr == 'A':
                        kategori = 'Anak - anak' 
                        h_libur = 42000
                        h_biasa = 32000
                   else:
                        print('KODE TIDAK TERSEDIA')
                        continue
                   
                   try:
                           jml_beli = int(input('Masukan Jumlah Beli = '))
                           if jml_beli <= 0:
                                   print('JUMLAH BELI HARUS POSITIF !!')
                                   continue
                   except ValueError:
                           print('JUMLAH BELI HARUS BERUPA ANGKA!')
                           continue
                   
                   hri_beli = input('Masukan Hari [libur/biasa] = ').lower()

                  #  Tentukan Harga Berdasarkan Hari
                   if hri_beli == 'libur':
                           harga = h_libur
                   elif hri_beli == 'biasa':
                           harga = h_biasa
                   else:
                           print('HARI TIDAK VALID !!')
                           continue
                   voucher = input('Voucher [y,n] = ').lower()

                  #  Hitung Potongan Jika Ada Voucher
                   potongan = 0.10 if voucher == 'y' else 0

                  # Kalkulasi
                   subtotal = harga * jml_beli
                   after_discount = subtotal * (1 - potongan)

                  # Simpan Data
                   penampung.append({
                          'no' : i,
                          'tipe': kategori,
                          'price' : harga,
                          'quantity' : jml_beli,
                          'voucher' : potongan,
                          'sub' : after_discount
                  })
    return penampung

# # Pencetakan
def pencetakan(data):
    print('=' * 75)
    print('                         KOLAM RENANG SUKA - SUKA            ' )
    print('=' * 75)
    print('No     Kategori    Harga Satuan      Jumlah      Diskon      Total')
    print('=' * 75)

    grand_total = 0
    for item in data:
           diskon = f"{item['voucher'] * 100}%" if item['voucher'] > 0 else '-'
           print(f"{item['no']:<6}{item['tipe']:<12} Rp{item['price']:<13,d}   {item['quantity']:<10} {diskon:<10} Rp {item['sub']:,.0f}")
           grand_total += item['sub']

    print('=' * 75)
    print(f'Total Bayar {"":<47}Rp {grand_total:,.0f}')
    print('=' * 75)


# Main Program
data_pesanan = input_user()
if data_pesanan:
       cetak_input = input('\n Cetak Hasil [y/n] = ').lower()
       if cetak_input == 'y':
              pencetakan(data_pesanan)
       else:
              print('Terima kasih telah memesan ' "<:")

   
        

