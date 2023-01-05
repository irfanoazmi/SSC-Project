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

![](RackMultipart20230103-1-1pa1y_html_6d063da423c67d01.png)

Tahapan customer dalam menggunakan self-service cassiernya adalah sebagai berikut:
1. Customer akan memulai program dengan membuka script .py yang telah disediakan.
2. Customer akan memasukan ID atau nama customer yang digunakan sebagai ID transaksi.
3. Selanjutnya customer akan memasukan nama item, jumlah dan harganya.
4. customer akan mengecek apakah data yang dimasukan sudah benar atau tidak, jika tidak benar customer dapat melakukan reset dan datanya akan terhapus semua, atau memodifikasi individual antara nama item, jumlah atau harganya.
5. jika sudah benar data yang di input, customer akan melakukan pengecekan total harga, apakah mendapatkan diskon atau tidak.
6. customer membayar belanjaannya
7. program selesai.


# DESKRIPSI TASK
1. Modul transaksi_belanja.py berisikan class Transaction dengan method sebagai berikut :
    - menu() untuk menampilkan pilihan ke method lain
    - add_item() untuk memasukan nama, jumlah dan harga item ke dalam dictionary
    - update_item_name() untuk mengubah nama item yang terdapat dalam dictionary
    - update_item_qty() untuk mengubah jumlah item yang terdapat dalam dictionary
    - update_item_price() untuk mengubah harga item yang terdapat dalam dictionary
    - delete_item() untuk menghapus item spesifik beserta jumlah dan harganya dari dictionary
    - reset_transaction() untuk menghapus semua item dari dictionary
    - check_order() untuk memastikan kelengkapan data pada dictionary belanja, dan menampilkan summary order
    - total_price() untuk menampilkan diskon yang didapat dan total harga setelah diskon
    
2. Modul main_belanja.py merupakan tampilan awal self-service cassier yang terhubung ke modul transaksi_belanja.py

# CARA MENGGUNAKAN PROGRAM
1. Download semua file/module Python ke dalam satu direktori lokal.
2. Anda cukup menjalankan main_belanja.py saja, karena sudah transaksi_belanja.py sudah terimport di module tersebut.

# Hasil Test Case
...

