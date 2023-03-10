# masukan library yang dibutuhkan
import os
from time import sleep

# membuat dictionary kosong untuk menampung item belanjaan yang akan di input oleh user :
belanja = {}

class Transaction:      
  """
  Pada class Transaction terdapat beberapa method, yaitu :
  1. menu() untuk menampilkan pilihan ke method lain
  2. add_item() untuk memasukan nama, jumlah dan harga item ke dalam dictionary
  3. update_item_name() untuk mengubah nama item yang terdapat dalam dictionary
  4. update_item_qty() untuk mengubah jumlah item yang terdapat dalam dictionary
  5. update_item_price() untuk mengubah harga item yang terdapat dalam dictionary
  6. delete_item() untuk menghapus item spesifik beserta jumlah dan harganya dari dictionary
  7. reset_transaction() untuk menghapus semua item dari dictionary
  8. check_order() untuk memastikan kelengkapan data pada dictionary belanja, dan menampilkan summary order
  9. total_price() untuk menampilkan diskon yang didapat dan total harga setelah diskon
  10. table() untuk membuat table dari dictionary belanja
  11. repeat() untuk memberikan pilihan kepada user untuk ke menu utama
  """
  def table():
    """
    Method ini digunakan untuk membuat table dari dictionary belanja
    """
    print('Item belanjaan anda : ')
    # Masukan library yang dibutuhkan, tabulate untuk membuat table, pandas untuk konversi ke Dataframe
    from tabulate import tabulate
    import pandas as pd

    # Mengubah dictionary menjadi dataframe
    df = pd.DataFrame(belanja)
    df = df.astype('str')

    # print tablenya
    print(tabulate(df.T, headers = ['Jumlah', 'Harga', 'Total Harga']))
  
  def repeat():
    """
    Method ini digunakan untuk memberikan pilihan kepada user untuk pergi menu utama atau tidak
    """
    # try except dibuat untuk mengetahui apakah user sudah menginput dengan benar atau tidak :
    try:
      repeat = str(input('Kembali ke menu utama? (Y / N) ')).lower()
      if repeat == 'y':
        os.system('cls')
        Transaction.menu()
      elif repeat == 'n':
        print('Layanan simpan belanja belum dibuat, anda kembali ke menu utama dalam 2 detik :)')
        sleep(2)
        os.system('cls')
        Transaction.menu()
    
    except:
      print('\n')
      print('Format input anda salah, anda akan kembali ke menu utama dalam 2 detik!')
      print('\n----------------------\n')
      sleep(2)
      os.system('cls')
      Transaction.menu()
      
  def menu():
    """
    Method ini seperti homepage aplikasi untuk mempermudah user.
    Terdapat pilihan menu yang sudah terhubung ke method lain seperti add_item, update_item, dan lainnya.
    Tabel belanjaan user juga akan muncul di sisi atas menu pilihan untuk mempermudah user dalam menentukan pilihannya, 
    sehingga terlihat apakah ada salah input dan harus diubah nilainya.
    """
    # Menampilkan Tabel Belanjaan User :
    print('-------------------------------------------------')
    print('Selamat Datang di Kasir Online PACMANN')
    print('-------------------------------------------------')
    print('\n')
    Transaction.table()

    # Menampilkan Pilihan Menu :
    print('\n')
    print('Silahkan Pilih Salah Satu Menu Dibawah: ')
    print('Pilih 1 untuk add item')
    print('pilih 2 untuk update/modifikasi item')
    print('pilih 3 untuk reset transaksi')
    print('pilih 4 untuk check order')
    print('pilih 5 untuk menghitung total pembayaran')
    print('pilih 0 untuk close app')

    # try except dibuat untuk mengetahui apakah user sudah menginput dengan benar atau tidak :
    try:
      # Membuat variable input untuk memilih pilihan pada menu:
      nilai = int(input('\nPilih Salah Satu Menu: '))
      
      # Jika user pilih 1, maka akan menuju method add_item():
      if nilai == 1: 
        os.system('cls')
        # Menampilkan Tabel Belanjaan User :
        Transaction.table() 
        print('\n----------------------\n')
        Transaction.add_item()

      # Jika user pilih 2, maka user akan mengupdate / modifikasi item belanjaan :  
      elif nilai == 2:

        # Check terlebih dahulu, jika dictionary belanja masih kosong, maka beri peringatan dan kembali ke menu utama :
        if len(belanja) == 0:
          print('Tidak ada item yang bisa dimodifikasi, anda akan kembali ke menu utama dalam 5 detik')
          sleep(5)
          os.system('cls')
          print('\n----------------------\n')
          Transaction.menu()

        # Jika dictionary belanja sudah ada isinya, maka tampilkan pilihan modifikasi apa yang diinginkan user :
        else:
          print('\n----------------------\n')
          print('Silahkan Pilih Salah Satu Menu Dibawah: ')
          print('pilih 1 untuk update nama')
          print('pilih 2 untuk update jumlah')
          print('pilih 3 untuk update harga')
          print('pilih 4 untuk menghapus item belanja')
          print('pilih 0 untuk kembali ke menu utama')
          # Buat variable input untuk memasukan pilihan user dengan format int :
          update = int(input('\nPilih salah satu update: '))

          # Jika user pilih 1, maka akan menuju method update_item_name():
          if update == 1:
            os.system('cls')
            # Menampilkan Tabel Belanjaan User :
            Transaction.table() 
            print('\n----------------------\n')
            Transaction.update_item_name()

          # Jika user pilih 2, maka akan menuju method update_item_qty():
          elif update == 2:
            os.system('cls')
            # Menampilkan Tabel Belanjaan User :
            Transaction.table()
            print('\n----------------------\n')
            Transaction.update_item_qty()

          # Jika user pilih 3, maka akan menuju method update_item_price():
          elif update == 3:
            os.system('cls')
            # Menampilkan Tabel Belanjaan User :
            Transaction.table()
            print('\n----------------------\n')
            Transaction.update_item_price()

          # Jika user pilih 4, maka akan menuju method delete_item():
          elif update == 4:
            os.system('cls')
            # Menampilkan Tabel Belanjaan User :
            Transaction.table()
            print('\n----------------------\n')
            Transaction.delete_item()

          # Jika user pilih 0, maka akan menuju menu utama:
          elif update == 0:
            os.system('cls')
            print('\n----------------------\n')
            Transaction.menu()
          
      # Jika user pilih 3, maka akan menuju method reset_transaction(): 
      elif nilai == 3:
        os.system('cls')
        print('\n----------------------\n')
        Transaction.reset_transaction()
      
      # Jika user pilih 4, maka akan menuju method check_order():   
      elif nilai == 4:
        os.system('cls')
        Transaction.check_order()

      # Jika user pilih 5, maka akan menuju method total_price():   
      elif nilai == 5:
        os.system('cls')

      # Menampilkan Tabel Belanjaan User :
        Transaction.table()

        print('\n----------------------\n')
        Transaction.total_price()

      # Jika user pilih 0, maka akan menuju menu utama:  
      elif nilai == 0:
        os.system('cls')
        print('\n----------------------\n')
        pass
      
      # Jika user memilih diluar angka pada pilihan, maka tampilan peringatan!
      else:
        print('Pilih menu yang sesuai!')
        print('Input tidak sesuai, anda akan kembali ke menu utama dalam 3 detik!')
        sleep(3)
        os.system('cls')

    # Jika user memasukan input dengan format str, contoh : 'a', maka tampilkan peringatan!
    except:
      print('Input tidak sesuai, anda akan kembali ke menu utama dalam 5 detik!')
      sleep(5)
      os.system('cls')
      print('\n----------------------\n')
      Transaction.menu()

  def add_item():
    """
    Pada method ini user akan memasukan item belanjaan mereka dengan rincinan nama, jumlah dan harganya.
    tabel list belanjaan juga akan ditampilkan untuk mengetahui apa saja yang sudah user input.
    """
    # try except dibuat untuk mengetahui apakah user sudah menginput dengan benar atau tidak :
    try:
      # Buat variable input untuk memasukan nama item, jumlah item, dan harga item dengan format tertentu :
      nama = str(input('Masukan item yang akan dibeli: '))
      jumlah = int(input(f'Masukan jumlah {nama} yang akan dibeli: '))
      harga = int(input(f'Masukan Harga {nama} yang akan dibeli: '))
      os.system('cls')
      
      # Masukan variable yang sudah di input ke dalam dictionary baru, dan update ke dictionary belanja :
      # variable yang dimasukan adalah nama, jumlah, harga, serta perkalian antara jumlah dan harga.
      item = {nama : [jumlah, harga, jumlah * harga]}
      belanja.update(item)

      # Tampilkan kembali list belanjaan user dalam bentuk tabel :
      Transaction.table()
      print('\n----------------------\n')
      print(f'Item belanja {nama} berhasil di tambahkan!')
      print('\n')

      # Beri pilihan kepada user apakah ingin melanjutkan untuk input item atau kembali ke menu utama :
      repeat = str(input('Apakah akan menginput item selanjutnya? (Y / N) ')).lower()
      if repeat == 'y':
        Transaction.add_item()
      elif repeat == 'n':
        os.system('cls')
        Transaction.menu()

    # Jika user memasukan input dengan format str pada variable jumlah dan harga, maka beri peringatan :
    except:
      print('\n')
      print('Format input anda salah, anda akan kembali ke menu utama dalam 5 detik!')
      print('\n----------------------\n')
      sleep(5)
      os.system('cls')
      Transaction.menu()

      

  def update_item_name():
    """
    Pada method ini user dapat mengubah nama item yang telah di input sebelumnya
    """
    # try except dibuat untuk mengetahui apakah user sudah menginput dengan benar atau tidak :
    try:
      # Buat variable untuk memasukan nama item yang ingin diganti dan nama item yang baru
      nama = str(input('Masukan nama item yang ingin diganti: '))
      nama_update = str(input('Masukan nama item yang baru: '))
      os.system('cls')

      # Masukan variable yang sudah di input ke dalam dictionary baru, dan update ke dictionary belanja :
      dict_baru = {nama_update : belanja[nama]}
      belanja.update(dict_baru)
      belanja.pop(nama)

      # Tampilkan kembali list belanjaan user dalam bentuk tabel :
      Transaction.table()
      print('\n----------------------\n')
      print(f'Item belanja {nama} telah diganti menjadi {nama_update}!')
      print('\n')

      # Beri pilihan kepada user apakah ingin kembali ke menu utama atau tidak :
      Transaction.repeat()

    # Jika user salah memasukan input nama item yang ingin diganti, maka beri peringatan :  
    except:
      print('\n')
      print(f'item {nama} tidak terdapat pada list belanjaan anda!')
      print('anda akan kembali ke menu utama dalam 5 detik!')
      sleep(5)
      os.system('cls')
      Transaction.menu()
      

  def update_item_qty():
    """
    Pada method ini user dapat mengubah jumlah item yang telah di input sebelumnya
    """
    # try except dibuat untuk mengetahui apakah user sudah menginput dengan benar atau tidak :
    try:
      # Buat variable untuk memasukan nama item yang ingin diganti jumlahnya
      nama = str(input('Masukan nama item yang ingin diganti jumlahnya: '))
      jumlah_update = int(input('Masukan jumlah item yang baru: '))
      os.system('cls')

      # Masukan variable yang sudah di input ke dalam dictionary baru, dan update ke dictionary belanja :
      belanja[nama][0] = jumlah_update
      belanja[nama][2] = belanja[nama][0] * belanja[nama][1]
      # Tampilkan kembali list belanjaan user dalam bentuk tabel :
      Transaction.table()
      print('\n----------------------\n')
      print(f'Item belanja {nama} berhasil diubah jumlahnya menjadi {jumlah_update}!')
      print('\n')
      
      # Beri pilihan kepada user apakah ingin kembali ke menu utama atau tidak :
      Transaction.repeat() 

    # Jika user salah memasukan input nama item yang ingin diganti, maka beri peringatan :  
    except:
      print('\n')
      print(f'item {nama} tidak terdapat pada list belanjaan anda!')
      print('anda akan kembali ke menu utama dalam 5 detik!')
      sleep(5)
      os.system('cls')
      Transaction.menu()


  def update_item_price():
    """
    Pada method ini user dapat mengubah harga item yang telah di input sebelumnya
    """
    # try except dibuat untuk mengetahui apakah user sudah menginput dengan benar atau tidak :
    try:
      # Buat variable untuk memasukan nama item yang ingin diganti harganya
      nama = str(input('Masukan nama item yang ingin diganti harganya: '))
      harga_update = int(input('Masukan harga item yang baru: '))
      os.system('cls')

      # Masukan variable yang sudah di input ke dalam dictionary baru, dan update ke dictionary belanja :
      belanja[nama][1] = harga_update
      belanja[nama][2] = belanja[nama][0] * belanja[nama][1]

      # Tampilkan kembali list belanjaan user dalam bentuk tabel :
      Transaction.table()
      print('\n----------------------\n')
      print(f'Item belanja {nama} berhasil diubah harganya menjadi Rp {harga_update}!')
      print('\n')

      # Beri pilihan kepada user apakah ingin kembali ke menu utama atau tidak :
      Transaction.repeat()

    # Jika user salah memasukan input nama item yang ingin diganti, maka beri peringatan :
    except:
      print('\n')
      print(f'item {nama} tidak terdapat pada list belanjaan anda!')
      print('anda akan kembali ke menu utama dalam 5 detik!')
      sleep(5)
      os.system('cls')
      Transaction.menu()
 
  def delete_item():
    """
    Pada method ini user dapat menghapus item yang telah di input sebelumnya
    """
    # try except dibuat untuk mengetahui apakah user sudah menginput dengan benar atau tidak :
    try:
      # Buat variable untuk memasukan nama item yang ingin diganti harganya
      nama = str(input('Masukan nama item yang ingin dihapus: '))
      belanja.pop(nama)
      os.system('cls')

      # Tampilkan kembali list belanjaan user dalam bentuk tabel :
      Transaction.table()

      print('\n----------------------\n')
      print(f'Item belanja {nama} berhasil di delete!')
      print('\n')

      # Beri pilihan kepada user apakah ingin kembali ke menu utama atau tidak :
      Transaction.repeat()

    # Jika user salah memasukan input nama item yang ingin diganti, maka beri peringatan :
    except:
      print('\n')
      print(f'item {nama} tidak terdapat pada list belanjaan anda!')
      print('anda akan kembali ke menu utama dalam 5 detik!')
      sleep(5)
      os.system('cls')
      Transaction.menu()
    
  def reset_transaction():
    """
    Pada method ini user dapat menghapus semua item yang telah di input sebelumnya
    """
    # hapus dictionary dengan .clear()
    belanja.clear()
    os.system('cls')
    
    # Tampilkan kembali list belanjaan user dalam bentuk tabel :
    Transaction.table()

    print('\n----------------------\n')
    print('Semua item belanja berhasil di delete!')
    print('\n')

    # Beri pilihan kepada user apakah ingin kembali ke menu utama atau tidak :
    Transaction.repeat()
    
  def check_order():
    """
    Pada method ini user dapat melihat item apa saja yang sudah di input, serta kelengkapan datanya.
    Jika sudah benar / lengkap, maka akan trigger 'Pemesanan anda sudah benar'
    """
    # Tampilkan table belanjaan user
    Transaction.table()

    print('\n')
    print('Pemesanan anda sudah benar')
    print(f'Total item yang dibeli sebanyak : {len(belanja)} item')

    # Hitung total belanjaan user sebelum dikurangin diskon
    total = 0
    for key in belanja: 
      total = total + belanja[key][2]
    print(f'Total biaya sebelum diskon : Rp {total}')
   
   # Beri pilihan kepada user apakah ingin kembali ke menu utama atau tidak :
    print('\n')
    Transaction.repeat() 
    
  def total_price():
    """
    Pada method ini user dapat melihat total harga beserta besar diskon yang didapatkannya.
    """
    ## Menghitung total harga
    total = 0
    total_belanja = 0
    for key in belanja: 
      total = total + belanja[key][2]
        
    # Klasifikasi besar diskon yang didapat berdasarkan total harga
    if total >= 500000:

      # 10% diskon untuk pembelian diatas 500,000
      diskon = 0.1 
      total_belanja = total - (total*diskon)

      ('\n----------------------\n')
      print('Selamat anda mendapatkan diskon 10%!')
      print(f'Total belanjaan anda adalah : Rp {int(total_belanja)}')
      ('\n----------------------\n')

    elif total >= 300000:

      # 8% diskon untuk pembelian diatas 300,000
      diskon = 0.08
      total_belanja = total - (total*diskon)

      ('\n----------------------\n')
      print('Selamat anda mendapatkan diskon 8%!')
      print(f'Total belanjaan anda adalah : Rp {int(total_belanja)}')
      ('\n----------------------\n')

    elif total >= 200000:

      # 5% diskon untuk pembelian diatas 200,000
      diskon = 0.05
      total_belanja = total - (total*diskon)

      ('\n----------------------\n')
      print('Selamat anda mendapatkan diskon 5%!')
      print(f'Total belanjaan anda adalah : Rp {int(total_belanja)}')
      ('\n----------------------\n')

    else:
      # jika dibawah 200,000 tidak akan mendapatkan diskon
      ('\n----------------------\n')
      print('Mohon maaf anda tidak mendapatkan diskon!')
      print(f'Total belanjaan anda adalah : Rp {int(total)}')
      ('\n----------------------\n')
    
    print('\n')
    # Beri pilihan kepada user apakah ingin kembali ke menu utama atau tidak :
    Transaction.repeat()
