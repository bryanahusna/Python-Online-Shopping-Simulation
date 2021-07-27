# Modul yang bertanggung jawab untuk menampilkan Homepage
import random
import database as db
import search_toko as st
import search_produk as sp
import keranjang as krj
import status_program
import info_produk as ip
import status_pembelian
import login_section as lg
import locale
locale.setlocale(locale.LC_ALL, '')


# Membuat variable List Matriks global yang berisi database katalog produk
list_produk = db.baca_database_produk()

# Fungsi untuk menetapkan produk yang masuk rekomendasi di Homepage
def recomend(N):
  """
  Memberi N index random dari katalog
  """
  hasil = random.sample([x for x in range(1, len(list_produk))], N)
  return hasil

# Fungsi utama
def homepage():
  rekom = recomend(4)   # Menetapkan barang yang masuk rekomendasi

  # Membaca input.
  # 1. Pencarian Produk; 2. Pencarian Toko; 3. Keranjang; 4. Daftar Transaksi; 5. Keluar
  # 6-9 Daftar produk rekomendasi
  def hp_1():  
    console = input("Masukkan nomor aksi yang ingin dilakukan: ")

    if int(console) == 1:
      sp.search_produk()
    elif int(console) == 2:
      st.search_toko()
    elif int(console) == 3:
      krj.tampilkan_keranjang()

    elif int(console) == 4:
      status_pembelian.tampilkan_transaksi()
    elif int(console) == 5:
      print("Program Selesai")
      status_program.status_program = 0
    elif int(console) == 6:
      ip.info_produk(list_produk[rekom[0]][1])
    elif int(console) == 7:
      ip.info_produk(list_produk[rekom[1]][1])
    elif int(console) == 8:
      ip.info_produk(list_produk[rekom[2]][1])
    elif int(console) == 9:
      ip.info_produk(list_produk[rekom[3]][1])
    else:
      print("Input tidak valid!")
      hp_1()

  nama_depan = lg.info_akun(lg.username_login)[0].split(' ')[0]
  saldo_shopeepay = lg.info_akun(lg.username_login)[3]
  saldo_shopeepay = locale.format('%d', int(saldo_shopeepay), 1)

# Bagian yang dicetak di console
  print("""
  
///////////////////////////////////////////////////////////////
  
[SELAMAT DATANG DI SHOPEE ECERAN '{}']
Saldo ShopeePay Anda {}
ShopeePay dapat digunakan untuk membayar transaksi

Pilih aksi yang ingin dilakukan:
1. Pencarian Produk
2. Pencarian Toko
3. Keranjang
4. Daftar Transaksi
5. Keluar
    """.format(nama_depan, saldo_shopeepay))

  print("""Rekomendasi:
6. {}
7. {}
8. {}
9. {}

//////////////////////////////////////////////////////////////

    """.format(list_produk[rekom[0]][1], list_produk[rekom[1]][1], list_produk[rekom[2]][1], list_produk[rekom[3]][1]))

  # Memanggil fungsi nested hp_1()
  hp_1()