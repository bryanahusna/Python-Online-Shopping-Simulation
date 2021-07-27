import database as db
import search_produk as sp
import keranjang as kr
import checkout as ck
import locale
locale.setlocale(locale.LC_ALL, '')
#locale.setlocale(locale.LC_ALL,'nl_NL.ISO8859-1')

# Membuat variable List Matriks global yang berisi database katalog produk
list_produk = db.baca_database_produk()

def info_produk(nama, isDimasukkanKeranjang=False): 
  # Mencari data produk yang sudah dipilih
  for i in list_produk:
    if nama == i[1]:      # Nama produk berada pada kolom kedua matriks list_produk
      info = i            # info = i = baris detail seputar produk (toko, deskripsi, dsb.)
  print("""

///////////////////////////////////////////////////////////////

{}
  """.format(info[1]))    # Mencetak nama produk
  print(info[3])          # Mencetak nama toko (kolom ke-4 => indeks 3)
  print(info[7])          # Mencetak asal toko (kolom ke-8 => indeks 7)
  print("Harga:", locale.format('%d', int(info[6]), 1))   # Mencetak harga (kolom ke 7 => indeks 6) dengan format
  print("Telah terjual sebanyak", info[9], "unit")  # Banyak unit terjual
  print('\nDeskripsi: ')  
  print(info[8])            # Mencetak deskripsi produk

  print("""
Testimoni""")

  print("Rating: ", end="")
  for i in range(int(info[10])): # mencetak banyak bintang sesuai rating dari produk
    print("*", end="")

  print("")
  print(info[11])       # Mencetak testimoni
  print("by:", info[12]) # Mencetak pennulis testimoni

  if isDimasukkanKeranjang :      # Menandakan barang sudah ditambahkan ke keranjang
    print("""[Produk telah ditambahkan ke keranjang!]
Silakan lanjut berbelanja""")
  print("""
1. Beli sekarang
2. Tambahkan ke Keranjang
3. Tampilkan keranjang
4. Cari produk lagi
5. Kembali ke Homepage

///////////////////////////////////////////////////////////////

  """)
  
  perintah = input("Masukkan nomor aksi yang ingin dilakukan: ")
  if int(perintah) == 1:                    # Beli sekarang
    ck.checkout(False, [int(info[0])])
  elif int(perintah) == 2:                  # Tambah ke keranjang
    kr.tambah_ke_keranjang(int(info[0]))
  elif int(perintah) == 3:                  # Menampilkan keranjang
    kr.tampilkan_keranjang()
  elif int(perintah) == 4:                  # Cari produk lain
    sp.search_produk()
  elif int(perintah) == 5:                  # Kembali ke homepage
    return None