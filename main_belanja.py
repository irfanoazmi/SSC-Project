# Masukan module transaksi_belanja
import transaksi_belanja as tb

# Masukan library lain yang akan digunakan
import os
from time import sleep

# buat tampilan awal aplikasi
print('-------------------------------------------------')
print('Selamat Datang di Kasir Online PACMANN')
print('-------------------------------------------------')

# buat variable untuk meyimpan input nama user, dan gunakan sebagai id transaksi
nama = str(input('Silahkan Masukan Nama Anda : '))

os.system('cls')
print('-------------------------------------------------')
print('Selamat Datang di Kasir Online PACMANN')
print('-------------------------------------------------')
print(f'Selamat Datang {nama}!')
print('\n')

# Beri pilihan kepada user, apakah sudah siap untuk input atau belum
ready = str(input('Apakah kamu sudah siap untuk input belanjaan kamu? (Y / N): ')).lower()

# try except digunakan untuk mengontrol eror
try:

  # Jika ready, jalankan class Transaction, dan masuk ke method menu()
  if ready == 'y':
    os.system('cls')
    nama = tb.Transaction
    nama.menu()

  # Jika tidak, maka close aplikasi dalam 3 detik
  elif ready == 'n':
    print('-------------------------------------------------')
    print('Silahkan datang kembali ketika sudah siap input belanjaan :)')
    print('Aplikasi akan automatis tertutup dalam 3 detik!')
    sleep(3)
    pass

  # Jika user memasukan selain Y dan N, maka program akan tertutup
  else:
    print('-------------------------------------------------')
    print('Input anda salah, silahkan restart program!')
    print('Aplikasi akan automatis tertutup dalam 3 detik!')
    sleep(3)
    pass

# Jika terjadi eror pada saat input data, maka program akan tertutup.
except:
  print('-------------------------------------------------')
  print('Input anda salah, silahkan restart program!')
  print('Aplikasi akan automatis tertutup dalam 3 detik!')
  sleep(3)
