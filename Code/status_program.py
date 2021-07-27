# Modul untuk menyimpan status program
# Aplikasi berjalan jika status_program == 1, selesai jika status-program == 0

status_program = 1

def ubah(status):
  global status_program
  status_program = status

def baca():
  global status_program
  return status_program