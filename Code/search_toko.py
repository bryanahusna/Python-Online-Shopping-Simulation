# Setup
import database as db
import toko as it

# Menetapkan variable yang berisi database katalog produk
list_produk = db.baca_database_produk()

# Membuat list yang mengandung semua toko dalam bentuk index
toko = []
for i in list_produk[1:]:
  ada = False
  for j in toko:
    if (j == i[3]):
      ada = True
  if (not ada):
    toko.append(i[3])


def search(keyword, domain):
  """
  Membuat sebuah list yang berisi object-object dari list domain dengan keyword
  """
  domainlow = domain.copy()
  for i in range(len(domain)-1):
    domainlow[i] = domainlow[i].lower()

  hasil = []
  for j in range(len(domainlow)-1):
    if (keyword in domainlow[j]):
      hasil.append(domain[j])

  return hasil


def search_toko():

  def st_1():
    global hasil_search
    console = input("\nKetik nama toko yang ingin dicari: ")
    hasil_search = search(str(console), toko)

    if (hasil_search == []):
      print("Nama toko tidak ditemukan!")
      st_1()
    else:
      st_2()


  def st_2():
    print("""
    
///////////////////////////////////////////////////////////////
    """)
    nomor = 1
    for i in hasil_search:
      print("{}. {}".format(nomor, i))
      nomor += 1
    print("""
{}. Cari lagi\n{}. Kembali ke Homepage

///////////////////////////////////////////////////////////////

    """.format(nomor, nomor+1))

    console = input("Masukkan nomor aksi yang ingin dilakukan: ")
    if (int(console) == nomor):
      st_1()
    elif int(console) == nomor+1:
      return None
    elif ((int(console) < nomor) and (int(console) > 0)):
      it.info_toko(toko.index(hasil_search[int(console)-1]))
    else:
      print("Input tidak valid!")
      st_2()
  
  st_1()
