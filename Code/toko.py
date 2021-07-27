# Setup
import database as db
import homepage as hp
import info_produk as ip

# Menetapkan variable yang berisi database katalog produk
list_produk = db.baca_database_produk()

# Membuat list yang mengandung semua toko 
toko = []
for i in list_produk[1:]:
  ada = False

  for j in toko:
    if (j == i[3]):
      ada = True

  if (not ada):
    toko.append(i[3])

# Fungsi Utama
def info_toko(index):
  """
  Menampilkan toko dan informasinya. Menerima variable index untuk variable toko
  """
  
  # Membuat list berisi semua produk toko
  produk_toko = []
  for i in list_produk[1:]:
    if (i[3] == toko[index]):
      produk_toko.append(int(i[0]))
  
  # Subfungsi yang mengatur input
  def it_1():
    console = input("Masukkan nomor aksi yang ingin dilakukan: ")
    
    if ((int(console) > 0) and (int(console) < nomor)):
      ip.info_produk(list_produk[produk_toko[int(console)-1]][1])
    elif (int(console) == nomor):
      hp.homepage()
    else:
      print("Input tidak valid!")
      it_1()

  for i in range(len(list_produk)):
    if toko[index] == list_produk[i][3]:
      deskripsi_toko = list_produk[i][5]
  
  # Bagian yang terlihat di console
  print("""

///////////////////////////////////////////////////////////////
 
Selamat datang di {}

Deskripsi toko {}
{}

Daftar Produk di Toko Ini:""".format(toko[index], toko[index], deskripsi_toko))

  # Mencetak semua produk dan aksi lain
  nomor = 1
  for y in produk_toko:
    print("{}. {}".format(nomor, list_produk[y][1]))
    nomor += 1

  print("\n{}. Pergi ke Homepage".format(nomor))

  print("""
///////////////////////////////////////////////////////////////

  """)

  it_1()

