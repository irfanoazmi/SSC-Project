# SSC Project
Self Service Cashier (SSC) sederhana dengan menggunakan bahasa pemrograman Python.

# OBJECTIVE
Pada project python ini, saya diminta oleh pacmann untuk membuat system kasir self-service menggunakan python, diharapkan system kasir yang dibuat dapat membantu siapapun yang sedang mengembangkan warung jujur yang customernya milih barang sendiri, bayar sendiri dan ambil kembaliannya sendiri.
Objective yang harus dipenuhi dari system kasir ini adalah sebagai berikut:

1. Customer dapat membuat ID transaksinya (class Transaction)
2. Customer dapat memasukan nama, jumlah dan harga barang
3. Customer dapat melakukan perubahan nama, jumlah dan harga barang
4. Customer dapat membatalkan salah satu item yang akan dibeli dan juga dapat menghapus semua pesanan dengan fitur reset transaction
5. Customer dapat melakukan pengecekan total orderan secara keseluruhan
6. Customer dapat menghitung total belanja yang akan dibeli dengan diskon yang sudah ditetapkan oleh took

# FLOWCHART
Berikut flowchart / alur system kasir online yang akan dibuat:

![flow chart](https://user-images.githubusercontent.com/119559428/210802519-2b2e6409-9995-45a2-b181-3ee2775a7c12.png)

Tahapan customer dalam menggunakan self-service cashier-nya adalah sebagai berikut:
1. Customer akan memulai program dengan membuka script .py yang telah disediakan.
2. Customer akan memasukan ID atau nama customer yang digunakan sebagai ID transaksi.
3. Selanjutnya customer akan memasukan nama item, jumlah dan harganya.
4. customer akan mengecek apakah data yang dimasukan sudah benar atau tidak, jika tidak benar customer dapat melakukan reset dan datanya akan terhapus semua, atau memodifikasi individual antara nama item, jumlah atau harganya.
5. jika sudah benar data yang di input, customer akan melakukan pengecekan total harga, apakah mendapatkan diskon atau tidak.
6. customer membayar belanjaannya
7. program selesai.


# DESKRIPSI TASK
### A. Modul transaksi_belanja.py berisikan class Transaction dengan penjelasan sebagai berikut:

1. Membuat dictionary kosong untuk menampung item nama, jumlah dan harga yang nanti akan diinput oleh user, serta membuat class Transaction yang berisi beberapa method.
```python
# membuat dictionary kosong :
belanja = {}
# membuat class Transaction :
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
```
***

2. Membuat method table() yang digunakan untuk mengkonversi dictionary belanja menjadi table dengan library tabulate dan pandas. method table ini akan selalu di panggil method lainnya.
```python
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
```
***
3. Membuat method repeat() untuk memberikan kepada user agar pergi ke menu utama atau tidak.
```python
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
 ```
***
4. membuat method menu() untuk menampilkan pilihan kepada user dan akan terhubung ke method lainnya.
```python
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

      # Jika user pilih 0, maka akan menutup aplikasi:  
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
 ```
 ***
5. Membuat method add_item() untuk memasukan nama, jumlah dan harga item ke dalam dictionary belanja.
```python
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
 ```
 ***
6. Membuat methode update_item_name() untuk mengubah nama item yang terdapat dalam dictionary.
 ```python
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
```
***
7. Membuat method update_item_qty() untuk mengubah jumlah item yang terdapat dalam dictionary.
```python
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
```
***
8. Membuat method update_item_price() untuk mengubah harga item yang terdapat dalam dictionary.
```python
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
```
***
9. membuat method delete_item() untuk menghapus item spesifik beserta jumlah dan harganya dari dictionary.
```python
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
```
***
10. Membuat method reset_transaction() untuk menghapus semua item dari dictionary.
```python
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
```
***

11. Membuat method check_order() untuk memastikan kelengkapan data pada dictionary belanja, dan menampilkan summary order.
```python
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
```
***

12. membuat method total_price() untuk menampilkan diskon yang didapat dan total harga setelah diskon.
```python
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
 ```
 ***

    
### B. Modul main_belanja.py merupakan tampilan awal self-service cashier yang terhubung ke modul transaksi_belanja.py.
```python
# Masukan module transaksi_belanja
import transaksi_belanja as tb

# Masukan library lain yang akan digunakan
import os
from time import sleep


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
```
***

# CARA MENGGUNAKAN PROGRAM
1. Download semua file/module Python ke dalam satu direktori lokal.
2. Anda cukup menjalankan main_belanja.py saja, karena transaksi_belanja.py sudah terimport di module main_belanja.py. Perhatikan gambar dibawah ini :
![simpan kedua file dalam satu directory yang sama](https://user-images.githubusercontent.com/119559428/210802861-67f5a83f-8b32-4302-b648-ade75ceb8455.png)

# Hasil Test Case
1. **TEST 1 :** Buka file main_belanja.py, maka akan muncul tampilan menu utama program. user hanya perlu memasukan nama nya sebagai ID transaksi,

![tampilan halaman utama program, masukan ID atau nama user](https://user-images.githubusercontent.com/119559428/210803265-976c3440-f4ff-40b2-adae-19d51dafef8a.png)

![Setelah memasukan nama](https://user-images.githubusercontent.com/119559428/210803443-127689d0-21be-4f0f-b6a8-822bb49e036f.png)
***

- Pilih Y jika ingin melanjutkan menggunakan program dan N jika ingin menghentikannya.

- Setelah pilih Y, maka user akan diarahkan ke menu utama program. Pada menu ini user dapat memilih action apa yang ingin dilakukan selanjutnya. Tabel belanjaan juga ditampilkan sebagai summary dan mempermudah user untuk memilih action apa yang ingin dilakukan.
Namun pada saat pertama dibuka, tabel belanja masih kosong.

![tampilan menu utama](https://user-images.githubusercontent.com/119559428/210804144-dbe4b62c-d161-4e87-9028-da9e201153ac.png)
***

2. **TEST 2 :** Pilih menu 1 untuk menambahkan item belanja / add item. maka akan muncul perintah untuk Memasukan nama, jumlah dan harga item.

![memasukan input secara manual](https://user-images.githubusercontent.com/119559428/210804727-e378f7fe-c35b-4a75-a470-13e4b037919e.png)
***

- setelah itu maka akan terupdate automatis di tabel belanjaan user.

![setelah menambahkan 1 item](https://user-images.githubusercontent.com/119559428/210804839-242a9d99-669e-48af-adc6-3e97a2dfb52f.png)
***

3. **TEST 3 :** Pilih menu 2 untuk mengupdate / modifikasi item belanja, terdapat pilihan menu yang disediakan untuk user. 

![menu pilihan update item](https://user-images.githubusercontent.com/119559428/210805697-57c4ac90-ab8c-454d-9efb-d54c61a3c27b.png)
***

- Pilih menu 1 untuk **update nama** belanjaan, maka akan diarahkan untuk memasukan nama yang ingin diganti dan nama barunya.

![input nama sebelum d
an sesudah](https://user-images.githubusercontent.com/119559428/210806029-338a45cf-95a5-43f0-bfe5-f19ef592c89a.png)
***

setelah itu klik **ENTER**, maka nama item berhasil di update.

![setelah diganti namanya](https://user-images.githubusercontent.com/119559428/210806134-8335d86b-e758-4dd5-8105-4f77a85d53b0.png)
***

- Pilih menu 2 untuk **update jumlah** item belanjaan, dan diarahkan untuk memasukan nama item yang akan diganti jumlahnya.

![input nama dan jumah update](https://user-images.githubusercontent.com/119559428/210807214-830040a6-a075-4fa6-9cdd-6eb73dc8af4a.png)
***

setelah itu klik **ENTER**, maka nama item berhasil di update.

![tampilan setelah update jumlah](https://user-images.githubusercontent.com/119559428/210807310-9834e060-c9be-4b35-b4fd-1807968435da.png)
***

- Pilih menu 3 untuk **update harga** item belanjaan, dan diarahkan untuk memasukan nama item yang ingin diganti harganya.

![input nama dan harga update](https://user-images.githubusercontent.com/119559428/210808159-d06e38fa-1ac3-4ec2-9b84-46b8670254d4.png)
***

setelah itu klik **ENTER**, maka nama item berhasil di update.

![tampilan setelah update harga](https://user-images.githubusercontent.com/119559428/210808348-8c4c57d4-3d35-436e-b993-10cb60c6d2fa.png)
***

- Pilih menu 4 untuk **delete item** belanjaan, dan diarahkan untuk memasukan nama item yang ingin di hapus dari tabel.

![input item yang akan di delete](https://user-images.githubusercontent.com/119559428/210815337-f45d02ea-fd3d-4c6e-8a31-0b9aee50442a.png)
***

setelah itu klik **ENTER**, maka nama item berhasil di hapus.

![tampilan setelah delete item](https://user-images.githubusercontent.com/119559428/210815442-b02083cc-47df-46bc-ae7a-54dec72fe360.png)
***

4. **TEST 4 :** Pilih menu 3 untuk reset transaction, maka seluruh item yang terdapat pada tabel akan terhapus.

![halaman utama reset transaction](https://user-images.githubusercontent.com/119559428/210817502-ccf98a25-8d2e-467e-81be-08c1bcd7e6ca.png)
***

5. **TEST 5 :** Pilih menu 4 untuk check order, maka akan dilakukan pengcekan apakah input pada tabel sudah sesuai atau tidak.

![tampilan awal check order](https://user-images.githubusercontent.com/119559428/210817900-6507999c-0c85-40a0-b67f-ee20d1a47a55.png)
***

6. **TEST 6 :** Pilih menu 5 untuk menampilkan total pembayaran dan termasuk perhitungan diskon yang didapatkan.

![halaman awal total belanjaan](https://user-images.githubusercontent.com/119559428/210818304-4e037348-1fb7-409e-8962-645a42afe1f4.png)
***

# KESIMPULAN
1. Pada project ini telah diterapkan prinsip DRY (Dont Repeat Yourself) dan Re-using Code dengan menggunakan function / method seperti add_item(), update_item_name(), check_order(), table() dll. Sehingga program menjadi mudah dipahami, terstruktur, ringkas dan memperkecil terjadinya bug / eror.
2. Pada project ini sudah diatur untuk eror handlingnya dengan menggunakan try dan except.
3. Pada project ini sudah menerapkan Clean Code PEP 8, sehingga program mejadi lebih rapi, mudah dibaca dan dipahami

# FUTURE WORK
1. input item dengan scan barcode, sehingga tidak perlu memasukan nama dan harga secara manual.
2. Merapihkan tampilan agar tidak membingungkan user.
3. Dapat menyimpan item belanjaan user kedalam keranjang. sehingga dapat dipanggil kembali jika dibutuhkan.
