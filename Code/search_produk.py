import database as db
import info_produk as ip

# Membuat variable List Matriks global yang berisi database katalog produk
list_produk = db.baca_database_produk()

produk =[]
for i in list_produk[1:]:   #membuat list seluruh produk
  ada = False
  for j in produk:
    if j == i[1]:
      ada = True
  if(not ada):
    produk.append(i[1])

produk_2 = produk.copy()
for i in range(len(produk_2)):     #membuat seluruh elemen list menjadi huruf kecil
  produk_2[i] = produk_2[i].lower()

def cari(keyword, domain):
  global produk
  terkait = []                      #list yang nantinya akan berisi produk
  keyword = keyword.lower()         #mengubah masukan menjadi huruf kecil
  for i in range(len(domain)):    #mengecek seluruh produk yang sesuai dengan masukan
    if keyword in domain[i]:
      terkait.append(produk[i])     #menambahkan produk yang sesuai ke list terkait
  return terkait


def search_produk():
  def sp_1():
    global hasil
    print('''
    
///////////////////////////////////////////////////////////////

    ''')
    nama = input("Masukkan nama produk: ")      #memasukkan keyword dari produk
    hasil = cari(nama, produk_2) 
    if hasil == []:                             #jika tidak ada produk yang sesuai dengan keyword
      print("Produk tidak ditemukan")
      sp_1()
    else:                                       #jika ada produk yang sesuai dengan keyword
      sp_2()
  
  def sp_2(): #fungsi untuk mencetak seluruh produk di list terkait
    print("""

///////////////////////////////////////////////////////////////

    """)
    nomor = 1
    for i in range(len(hasil)):
      print("{}. {}".format(nomor, hasil[i]))
      nomor += 1
    print("\n{}. Cari lagi".format(nomor))
    print('{}. Kembali ke Homepage'.format(nomor+1))
    print("""

///////////////////////////////////////////////////////////////

    """)

    perintah = input("Masukkan nomor aksi yang diinginkan: ")
    if int(perintah) == nomor:    #jika aksi yang diinginkan adalah cari lagi
      sp_1()
    elif int(perintah) == nomor+1: 
      return None
    elif int(perintah)>0 and int(perintah)<nomor: # jika memilih salah satu produk akan langsung menjalankan fungsi info produk
      ip.info_produk(hasil[int(perintah)-1])
    else: #jika input tidak sesuai
      print("input tidak valid")
      sp_2()
  
  sp_1()

