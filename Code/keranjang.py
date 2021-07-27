# Ini merupakan file fungsi keranjang
import database
import os
import search_produk
import info_produk
import checkout
import locale
locale.setlocale(locale.LC_ALL, '')

# keranjang_produk adalah List yang menyimpan produk-produk apa saja yang masuk keranjang
# keranjang_produk hanya menyimpan Nomor/Nomor ID dari produk
# Dari nomor tersebut, bisa digunakan fungsi cari_barang(nomor_produk)
keranjang_produk = []

# Membuat variable List Matriks global yang berisi database katalog produk
list_produk = database.baca_database_produk()



# Fungsi yang menerima nomor produk dan me-return List detail produk tersebut
def cari_barang(nomor_produk):
  #global list_produk
  for i in range(1, len(list_produk)):
    if int(list_produk[i][0]) == nomor_produk:
      barang = list_produk[i]
  return barang


# Fungsi Menampilkan produk berdasarkan nomor/nomor ID produk
# Hanya menampilkan 1 produk dengan nomor yang dimasukkan
def tampilkan_produk(nomor_produk):
  #global list_produk
  lebar_console = os.get_terminal_size()[0]

  barang = cari_barang(nomor_produk)

  nama_produk = barang[1]
  panjang_dicetak = len('  Nama Produk\t:  '+barang[1])
  if panjang_dicetak > lebar_console:
    nama_produk = nama_produk[:lebar_console-18] + ' .....'
  print(nama_produk, sep='')
  print('  Toko\t: ', barang[3])
  print('  Asal\t: ', barang[7])
  harga = locale.format('%d', int(barang[6]), 1)
  print('  Harga\t: ', harga)



# Fungsi menambah produk ke keranjang belanja (List keranjang_produk)
def tambah_ke_keranjang(nomor_produk):
  keranjang_produk.append(nomor_produk)
  barang = cari_barang(nomor_produk)
  info_produk.info_produk(barang[1], True)  # Menampilkan lagi info produk, dengan isDimasukkanKeranjang = True



# Fungsi untuk menampilkan seluruh produk di keranjang
def tampilkan_keranjang():
  global list_produk
  global keranjang_produk
  print('''

///////////////////////////////////////////////////////////////

[KERANJANG BELANJA]
  ''')
  if len(keranjang_produk) == 0:
    print('[Keranjang Kosong]\n')
  for nomor in keranjang_produk:
    tampilkan_produk(nomor)

  if len(keranjang_produk) != 0: 
    print('\n1 Checkout')
    print('2 Hapus semua di keranjang')
    print('3 Cari produk lagi')
    print('4 Kembali ke Homepage')
    print("""
///////////////////////////////////////////////////////////////

    """)
  else:
    print('1 Cari produk lagi')
    print('2 Kembali ke Homepage')
    print("""
///////////////////////////////////////////////////////////////
  
    """)

  perintah = int(input('Masukkan nomor aksi yang ingin dilakukan: '))
  if perintah == 1 and len(keranjang_produk) != 0:
    checkout.checkout(True, keranjang_produk)
  elif perintah == 2 and len(keranjang_produk) != 0:
    keranjang_produk = []
    tampilkan_keranjang()
  elif perintah == 3 and len(keranjang_produk) != 0:
    search_produk.search_produk()
  elif perintah == 1 and len(keranjang_produk) == 0:
    search_produk.search_produk()
  elif perintah == 4 and len(keranjang_produk) != 0:
    return None
  elif perintah == 2 and len(keranjang_produk) == 0:
    return None
