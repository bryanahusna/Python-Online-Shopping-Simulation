import time
import status_program
import homepage


username_login = ''

pesan_awal = '''
///////////////////////////////////////////////////////////////
  
[SELAMAT DATANG DI SHOPEE]
  
Pilih aksi yang ingin dilakukan
Untuk pengguna baru, pilih Sign Up
1. Login
2. Sign up
3. Keluar

///////////////////////////////////////////////////////////////
  '''


# Kalau tadi ada fungsi baca baca_database_produk(), sekarang ada baca_database_users()
# Fungsi membaca database users dan me-return hasilnya dalam list
def baca_database_users():
  # [[Nama, Email, Password, Saldo ShopeePay], [...], [...]]
  hasil = []
  users = open('users.csv')
  for i in users:
    hasil.append(i.split(sep=';'))
  users.close()
  return hasil


# Fungsi menuliskan akun baru (nama, username, password) ke database users.csv sehingga tidak hilang jika program selesai
def tulis_database_users(nama, email, password):
  saldo_awal = 1000000000
  placeholder = open('users.csv', 'a')
  placeholder.seek(len(list_users))
  placeholder.write(nama + ';' + email + ';' + password + ';')
  placeholder.write(str(saldo_awal))
  placeholder.write('\n')
  placeholder.close()


# Menerima username dan mengeluarkan satu baris detail akun tersebut
def info_akun(username):
  list_users = baca_database_users()
  for i in range(len(list_users)):
    if list_users[i][1] == username:
      return list_users[i]


# Fungsi login
def login():
  pesan = '''
///////////////////////////////////////////////////////////////
  
[Halaman Login]
  '''
  global list_users
  global username_login
  list_users = baca_database_users()

  isLanjutDaftar = False
  isBerhasil = False
  while(isBerhasil == False):
    print(pesan)
    email = input('Masukkan Email Anda\t: ')
    password = input('Masukkan Password Anda\t: ')

    isDitemukan = False
    i = 0
    while i < len(list_users) and isDitemukan == False:
      if email == list_users[i][1] and password == list_users[i][2]: 
        isDitemukan = True
      i += 1


    for j in range(10):
      print('------', end='')
      time.sleep(0.1)

    if isDitemukan == True:
      isBerhasil = True
      nama_depan = list_users[i-1][0].split(' ')[0]
      username_login = email

      print('\nEmail dan Password Ditemukan!')
      print('Selamat Menikmati Fitur-Fitur Shopee', nama_depan)
      time.sleep(2)

    else:
      print('\nAKUN TIDAK DITEMUKAN ATAU SALAH')
      print('Silakan coba lagi atau pilih menu Sign up untuk mendaftar')
      print('\n1. Coba lagi\n2. Sign up\n3. Keluar')
      print('''
///////////////////////////////////////////////////////////////
''')
      console = int(input('Masukkan nomor aksi yang ingin dilakukan: '))
      if console == 1:
        pass
      elif console == 2:
        isLanjutDaftar = True
        isBerhasil = True
      elif console == 3:
        status_program.ubah(0)
        print("Program Selesai")
        return

  if isLanjutDaftar == True:
    daftar()
  homepage.homepage()


# Fungsi daftar
def daftar():
  pesan = '''

///////////////////////////////////////////////////////////////
  
[Halaman Sign Up]
  '''
  global list_users
  global username_login
  list_users = baca_database_users()
  print(pesan)
  print('Daftar Sekarang dan Dapatkan Saldo ShopeePay 1.000.000.000')
  nama = input('Silakan Masukkan Nama Anda\t\t: ')

  isTersedia = False  
  while isTersedia == False:
    email = input('Silakan Masukkan Email Anda\t\t: ')
    i = 0
    isKetemu = False
    while i <= len(list_users)-1 and isKetemu == False:
      if list_users[i][1] == email:
        isKetemu = True
      i += 1
    if isKetemu == True:
      isTersedia = False
      print('USERNAME YANG ANDA MASUKKAN SUDAH ADA!')
      print('Silakan coba yang lain')
    else:
      isTersedia = True

  password = input('Silakan Masukkan Password Anda\t: ')
  
  tulis_database_users(nama, email, password)
  username_login = email

  for j in range(10):
    print('------', end='')
    time.sleep(0.1)

  print('\nSelamat! Anda sudah terdaftar')
  print('Anda mendapat saldo promo ShopeePay 1.000.000.000')
  print('Selamat menikmati fitur-fitur Shopee!')
  time.sleep(3)
  homepage.homepage()

list_users = baca_database_users()