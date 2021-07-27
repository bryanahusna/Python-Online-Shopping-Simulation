# Modul sederhana tapi berguna untuk membaca database produk (katalog_produk_2.csv)

def baca_database_produk():
  # Membaca data dari database produk_toko; Mereturn list yang dihasilkan
  # Format list yang dihasilkan:
  # [[No, Nama Produk, Kategori, Nama Toko, Keyword Toko, Deskripsi Toko, Harga, Dikirim dari, Deskripsi Produk, Terjual, Rating, Testimoni], [....], [...], [...]]

  hasil = []

  katalog = open('katalog_produk_2.csv')
  for i in katalog:
    hasil.append(i.split(sep=';'))
  katalog.close()

  return hasil
