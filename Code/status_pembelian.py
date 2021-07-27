# Status Pembelian atau Daftar Transaksi

import keranjang as kr
import locale
locale.setlocale(locale.LC_ALL, '')

# Membuat variabel List yang menyimpan data Dictionary-Dictionary pesanan

list_transaksi = []

'''
Pesanan adalah Dictionary dengan karakteristik:
pesanan = {   'daftar_barang': daftar_barang[0],
              'kode_pembayaran': kode,
              'metode_pembayaran':metode_pembayaran,
              'jasa_pengiriman': jasa_pengiriman,
              'subtotal_produk': subtotal,
              'total_biaya': subtotal + 15000,
              'waktu_pembelian': str(datetime.now())[0:16],
              'status': 'Belum Dibayar' }    
'''

# Fungsi menampilkan menu pada daftar transaksi
def menu_transaksi():
  print("""
///////////////////////////////////////////////////////////////

1. Kembali ke Homepage

///////////////////////////////////////////////////////////////

""")
  perintah = int(input('Masukkan nomor aksi yang ingin dilakukan: '))
  if perintah == 1:
    return None


# Fungsi mencetak pesanan
def cetak_pesanan(pesanan):
  print("""
  
///////////////////////////////////////////////////////////////
""")
  print('Transaksi pada', pesanan['waktu_pembelian'])
  print('Kode Pembayaran:', pesanan['kode_pembayaran'])
  print('Status: ', pesanan['status'])

  [print('------', end='') for l in range(11)]
  for i in pesanan['daftar_barang']:
    print()
    kr.tampilkan_produk(i)
  [print('------', end='') for l in range(11)]

  print("\nJasa Pengiriman:" ,pesanan['jasa_pengiriman'])
  print("Metode Pembayaran:", pesanan['metode_pembayaran'])
  subtotal = locale.format('%d', int(pesanan['subtotal_produk']), 1)
  print('Subtotal Produk', subtotal)
  print("Ongkos Kirim: 15000")
  [print('------', end='') for x in range(11)]

  print("\nTotal Pembayaran: {}".format(locale.format('%d', int(pesanan['total_biaya']), 1)))


# Fungsi menambah data pesanan ke list_transaksi
def tambah_list_transaksi(pesanan):
  list_transaksi.append(pesanan)

def tampilkan_transaksi():
  print("""
  
///////////////////////////////////////////////////////////////

[INFO TRANSAKSI]
  """)
  if len(list_transaksi) != 0:
    for pesanan in list_transaksi:
      cetak_pesanan(pesanan)
      print()
      [print('======', end='') for i in range(11)]
      print('\n')
    menu_transaksi()
  else:
    print('\n[Anda tidak Memiliki Transaksi Aktif]')
    menu_transaksi()
