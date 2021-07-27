# Modul yang memproses Checkout

import keranjang
import status_pembelian
import random
import login_section
import time
from datetime import datetime


def bayar_shopeepay(pesanan, nominal_pengurangan):
  list_users = login_section.baca_database_users()
  username = login_section.username_login
  list_user = []
  

  for i in range(len(list_users)):
    if list_users[i][1] == username:
      list_user = list_users[i]
      break
  

  list_user[3] = int(list_user[3]) - nominal_pengurangan
  isi_db = list_user[0] + ';' + list_user[1] + ';' + list_user[2] + ';' + str(list_user[3]) +'\n'

  isidb_sementara = ''
  dbread = open('users.csv')
  x = 0
  for j in dbread:
    if x != i:
      isidb_sementara += j
    else:
      isidb_sementara += isi_db
    x += 1

  dbread.close()
  database = open('users.csv', 'w')
  
  database.write(isidb_sementara)
  database.close


def buat_pesanan(metode_pembayaran, alamat, subtotal, jasa_pengiriman, *daftar_barang):
  # Pesanan adalah dictionary yang terdiri atas detail transaksi, yang kemudian disimpan di modul status_pembelian

  # Menghapus seluruh isi keranjang ketika selesai buat pesanan
  keranjang.keranjang_produk = []

  waktu_sekarang = str(datetime.now())[0:16]
  tanggal_tanpa_strip = waktu_sekarang[0:10].replace('-', '')
  angka_random = random.randint(100, 999)

  # Kode pembayaran berformat tanggal hari ini dan 3 angka random
  kode_pembayaran = tanggal_tanpa_strip + str(angka_random)

  # Membuat Dictionary pesanan
  pesanan = { 'daftar_barang': daftar_barang[0],
              'kode_pembayaran': kode_pembayaran,
              'metode_pembayaran':metode_pembayaran,
              'toko': 'a',
              'jasa_pengiriman': jasa_pengiriman,
              'subtotal_produk': subtotal,
              'total_biaya': subtotal + 15000,
              'waktu_pembelian': str(datetime.now())[0:16],
              'status': 'Belum Dibayar' }    
  
  if pesanan['metode_pembayaran'] == 'ShopeePay':
    bayar_shopeepay(pesanan, pesanan['total_biaya'])
    status_pembelian.tambah_list_transaksi(pesanan)
    print("Anda telah memilih metode pembayaran ShopeePay")
    print('Saldo Anda dipotong dan Pembayaran telah selesai')
    pesanan['status'] = 'Sudah Dibayar dengan ShopeePay; Menunggu dikirim Penjual'
    time.sleep(2)
  else:
    status_pembelian.tambah_list_transaksi(pesanan)

  status_pembelian.cetak_pesanan(pesanan)         # Mencetak detail pesanan

  status_pembelian.menu_transaksi()


# Fungsi untuk memproses checkout
def checkout(isDariKeranjang=True, *daftar_barang):
  # Daftar barang opsional (menggunakan *args) karena bisa diakses langsung dari Beli Sekarang tanpa perlu memasukkan argumen daftar barang dari keranjang

  # daftar_barang mempunyai bentuk ([...]) (Tuple yang di dalamnya ada List), karena argumen *args mempack dalam bentuk Tuple, termasuk jika yang dimasukkan ke argumen adalah list

  print("""
  
///////////////////////////////////////////////////////////////


[CHECKOUT]
  """)

  # Menghitung harga total dan mencetak semua barang yang ada do daftar_barang
  # Silakan menuju deskripsi cari_barang() dan tampilkan_produk() untuk melihat maksud fungsi itu
  subtotal_produk = 0
  for i in daftar_barang[0]:
    barangx = keranjang.cari_barang(i) 
    keranjang.tampilkan_produk(i)
    print("")
    subtotal_produk += int(barangx[6])    # indeks 6 = harga
  print("""
///////////////////////////////////////////////////////////////
  
  """)

  # Menerima informasi-informasi seputar pengiriman dan pembelian
  alamat = input("Masukkan alamat pengiriman: ")
  pengiriman_list = ["J&T Express", "SiCepat REG", "JNE Reguler"]
  print('''

///////////////////////////////////////////////////////////////

Pilih opsi pengiriman:
1. J&T Express
2. SiCepat REG
3. JNE Reguler

///////////////////////////////////////////////////////////////

  ''')
  pilihan = int(input("Masukkan nomor aksi yang ingin dilakukan: "))
  jasa_pengiriman = pengiriman_list[pilihan-1]

  print('''

///////////////////////////////////////////////////////////////

Pilih Metode Pembayaran:
1. ShopeePay
2. Transfer Bank
3. COD(Bayar di Tempat)
4. Alfamart
5. Indomaret

///////////////////////////////////////////////////////////////

  ''')
  
  pembayaran_list = ["ShopeePay", "Transfer Bank", "COD(Bayar di Tempat)", "Alfamart", "Indomaret"]
  pilihan = int(input("Masukkan nomor aksi yang ingin dilakukan: "))
  metode_pembayaran = pembayaran_list[pilihan-1]

  console = input("""

///////////////////////////////////////////////////////////////

1. Buat pesanan
2. Batalkan dan kembali ke Homepage

///////////////////////////////////////////////////////////////


Masukkan nomor aksi yang ingin dilakukan: """)

# Konfirmasi apakah jadi buat pesananan atau kembali ke homepage
  if console == "1":
    buat_pesanan(metode_pembayaran, alamat, subtotal_produk, jasa_pengiriman, daftar_barang[0])
    
  elif console == '2':
    return None