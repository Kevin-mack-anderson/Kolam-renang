
              #   Ngasih nilai awal untuk buat garis & semua insialisasi taro sini
garis_head_bottom = '=' * 75 
judul_kolam = 'CIHUY WATERPARK'.center(len(garis_head_bottom))
sambutan =  'SELAMAT DATANG DI KOLAM RENANG TERBESAR KE - 2 DI ASIA TENGGARA!!'
peraturan_kolam = 'HAL YANG DILARANG DILAKUKAN DI AREA KOLAM !! \n 1.) Dilarang Berlarian \n ' \
                  '2.) Dilarang Makan Di Dalam Kolam \n 3.) Dilarang Mendorong Teman'
himbauan_pengunjung = 'HIMBAUAN \n 1.) Awasi Barang Bawaan Anda \n 2.) Awasi Buah Hati Anda Saat Bermain Air'
table_atas = 'No \t Kategori \t H-Biasa \t H-Libur'
table_tengah = '1 \t Dewasa \t Rp. 45.000 \t Rp. 52.000'
table_bawah =  '2 \t Anak-anak \t Rp. 32.000 \t Rp. 42.000'
# Ini Inisialisasi Function 2
ktrngn = 'No     Kategori    Harga Satuan      Jumlah      Diskon      Total'
              #   nilai awal garis & semua insialisasi selesai

# Kita Buat Kumpulan List
list_judul_kolam = [garis_head_bottom, judul_kolam]
sambutan_peraturan_himbauan = [
                 # Ini Bagian Sambutan
                sambutan,
                 # Ini bagian Peraturan
                peraturan_kolam,
                # Ini Bagian Himbauan
                himbauan_pengunjung
                 ]
list_table_harga = [   
     table_atas,
        table_tengah,
          table_bawah
            ]
list_alamat = [
         '08912345',
            'KUTABUMI KUTAJAYA PASARKEMIS KABUPATEN TANGERANG'
]
# List nya Selesai
     #Kita buat Kamus Biar Kodenya Rapih ~      
dictionary_nya = {
       #Jangan Lupa Kasih Kunci sama isi~
         #Ini Bagian Headingnyaa       
            'heading' : list_judul_kolam[0],
            'nama' : list_judul_kolam[1],
         #Ini Bagian Sambutan nyaa       
            'sambutan' : sambutan_peraturan_himbauan[0],
         #Ini Bagian Peraturannyaa       
            'peraturan' : sambutan_peraturan_himbauan[1],
         #Ini Bagian Himbauannyaa       
            'himbauan' : sambutan_peraturan_himbauan[2],
       #Ini Bagian Isi Table Harga
            'b_atas': list_table_harga[0],
            'b_tengah': list_table_harga[1],
            'b_bawah': list_table_harga[2],
        # Ini Punya Function 2
             'keterangan' : ktrngn,
             'notlp' : list_alamat[0],
             'alamat' : list_alamat[1],
}
       #Kamusnya Udahan yaa... 
# Ini Bagian Print nyaa       
   #  Bagian Judul Kolam
print(f"{dictionary_nya ['heading']} \n {dictionary_nya['nama']} \n {dictionary_nya['heading']}")
   # Bagian Sambutan dan Peraturan
print(f"{dictionary_nya['sambutan']} \n {dictionary_nya['peraturan']} \n {dictionary_nya['himbauan']}")
   # Bagian Table Harga
print(f"{dictionary_nya['heading']} \n {dictionary_nya['b_atas']} \n {dictionary_nya['heading']} \n\
{dictionary_nya['b_tengah']:>37} \n {dictionary_nya['b_bawah']} \n {dictionary_nya['heading']}")
# Printnya Selesai Yaaa

# # Bagian Input
def input_user ():
    try:
            b_jenis = int(input('Masukan Banyak Jenis Yang Dibeli = '))
            if b_jenis <= 0:
                    print('JUMLAH JENIS HARUS POSITIF !')
            elif b_jenis > 2:
                    print('MAX 2 JENIS!')
                    return []
    except ValueError:
       print('INPUT HARUS BERUPA ANGKA!!')
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
                   
                   hri_beli =   input('Masukan Hari [libur/biasa] = ').lower()

                  #  Tentukan Harga Berdasarkan Hari
                   if hri_beli == 'libur':
                            harga = h_libur
                   elif hri_beli == 'biasa':
                         harga = h_biasa
                   else:
                           print('HARI TIDAK VALID !!')
                           continue
                   voucher =  input('Voucher [y,n] = ').lower()

                  #  Hitung Potongan Jika Ada Voucher
                   potongan = 0.10 if voucher == 'y' else 0

                  # Kalkulasi
                   subtotal = harga * jml_beli
                   global after_discount
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


  

# Program Cetak Pesanan
def pencetakan (data):
  '''Bagian Printnyaa'''
  print(f"{dictionary_nya['nama'].center(len(dictionary_nya['heading']))}  \n {dictionary_nya['notlp'].center(len(dictionary_nya['heading']))} \n {dictionary_nya['alamat'].center(len(dictionary_nya['heading']))} \
        \n {dictionary_nya['heading']} \n {dictionary_nya['keterangan']} \n {dictionary_nya['heading']}")
  '''Printya Udahan Yaa'''

  '''Ini Kita Buat Dummy'''
  grand_total = 0
  '''Masuk Ke Looping Section'''
  for item in data:
           '''"diskon" menggunakan op. ternary'''
           diskon = f"{item['voucher'] * 100}%"if item['voucher'] > 0 else '-'
           print(f" {item['no']:<6}  {item['tipe']:<12} Rp{item['price']:<13,d}  \
{item['quantity']:<10} {diskon:<10} Rp {item['sub']:,.0f}")
           grand_total += item['sub'] 
       
           
  print(f"{dictionary_nya['heading']}")
  print(f'Total Bayar {"":<47}Rp {grand_total:,.0f}')
  global duit
  duit = int(input('Uang Dibayarkan : ')) 
  '''Function Baru'''
def pembayaran (uang, total):
       if uang < total:
             print('NOMINAL TIDAK CUKUP!')
       elif uang >= total:
             return print(f'Kembalian : {uang - total:,.0f} ')
       

data_pesanan = input_user()
if data_pesanan:
       cetak_input = input('\n Cetak Hasil [y/n] = ').lower()
       if cetak_input == 'y':
              pencetakan(data_pesanan)
              pembayaran(duit, after_discount)
       else:
              print('Terima kasih telah memesan ' "<:")

   
        

