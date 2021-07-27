# Deklarasi Import
import login_section as lg
import homepage as hp
import status_program

## Dibuat Bersama Oleh:
# Karma Kunga         / 16520092
# Bryan Amirul Husna  / 16520172
# Shadiq Harwiz       / 16520242
# Gede Sumerta Yoga   / 16520482

## Program Original dibuat dengan mengetik bersama 4 orang selama 12+ jam
# Kami pastikan program ini bukan hasil copy dan paste atau plagiat
# Terima Kasih sangat besar kepada https://repl.it yang menjadi tempat kami berkolaborasi mengetik program. Tanpanya, produktivitas yang tinggi sulit tercapai.
# Disclaimer: data-data produk di sini merupakan hasil dari pencarian di Shopee (https://shopee.co.id) pada November 2020

### Penjelasan Program
# Database Login
# Sesi login menggunakan database users.csv, 
# yang kemudian dikonversi ke List di Python agar lebih mudah diolah 
# Data login akan tetap tersimpan meskipun user telah menutup program
# Format dari Database users.csv (yang sudah dikonversi) adalah:
# [[Nama, Username, Password, Saldo ShopeePay], [...], [...]]
# Untuk fitur Saldo Shopee masih dalam tahap pengembangan

# Database Produk
# Daftar produk, toko, dll. menggunakan database katalog_produk_2.csv (2 karena merupakan versi kedua),
# yang kemudian dikonversi ke List di Python agar lebih mudah diolah
# Formatnya adalah
# [[No, Nama Produk, Kategori, Nama Toko, Nama Toko Lower (keyword dari toko),Deskripsi Toko;Harga;Pengiriman dari;Deskripsi Produk;Terjual;Rating;Testimoni;Pemberi Testimoni], [...], [...]]

# Daftar Transaksi
# Daftar Transaksi menggunakan List dan Dictionary


### FUNGSI-FUNGSI
# Fungsi untuk menampung login, daftar, dan keluar
def masuk_shopee():
  global is_logged        # global, mengambil dari variabel global
  pesan = lg.pesan_awal   # mengambil pesan awal yang ada di modul lg
  
  print(pesan)
  # Menerima masukan dan memprosesnya
  # 1 Login, 2 Daftar, 3 Selesai
  console = int(input('Masukkan nomor aksi yang ingin dilakukan: '))
  if console == 1:
    lg.login()
    is_logged = 1
  elif console == 2:
    lg.daftar()
    is_logged = 1           # Jika memilih daftar, dan berhasil, otomatis logged in
  elif console == 3:
    status_program.ubah(0)  # Variable status_program 0 jika program selesai
    print('Program Selesai') 


### Variabl-Variabel
is_logged = False       # Apakah sudah login atau belum? Atau masuk lewat daftar?

### ALGORTIMA
while status_program.baca() == 1:     # Selama status program tidak 0, jalankan program
   if is_logged == False:             # Jika belum logged in masuk dulu
     masuk_shopee()  
   if status_program.status_program == 0:   # Mengatasi jika memilih menu 3 keluar pada awal, agar homepage tidak tercetak
     break
   hp.homepage()                    # Jika sudah logged in buka homepage
