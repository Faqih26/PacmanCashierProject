
## Proyek overview

Seorang kasir memiliki tanggung jawab untuk mengelola transaksi dan mengelola pembayaran, baik dalam bentuk uang tunai maupun giro. Pekerjaan kasir mencakup beberapa tugas, seperti mencatat data penjualan, menyelesaikan transaksi penjualan, membuat laporan secara berkala, dan merangkum laporan transaksi penjualan. Tujuan proyek ini adalah untuk membantu supermarket mengurangi biaya yang dikeluarkan untuk pekerjaan kasir sehingga dana tersebut dapat digunakan untuk hal-hal yang lebih penting, seperti meningkatkan kualitas produk yang ditawarkan, menambah variasi produk, dan meningkatkan kampanye produk.

## Pemahaman Bisnis
Bagian ini akan menjelaskan proses pemahaman masalah secara lebih rinci.

## Pernyataan Masalah
Bagaimana cara mengurangi biaya yang dikeluarkan untuk pekerjaan kasir di sebuah supermarket?
Bagaimana supermarket dapat mencapai pelanggan di luar wilayah fisik mereka?
## Tujuan
Mengurangi kesalahan dan masalah dalam program sehingga pelanggan dapat berbelanja dengan lancar.
Membuat program yang dapat diakses melalui internet tanpa harus mengunjungi fisik supermarket.
## Pernyataan Solusi
Kami akan menggunakan bahasa pemrograman Python dengan prinsip-prinsip seperti pemrograman berorientasi objek, kode modular, penanganan kesalahan, dan kode bersih.
## Tujuan
Membangun sebuah program yang dapat melakukan operasi Create, Read, Update, dan Delete (CRUD).

<b>Create</b>

Pelanggan dapat memasukkan ID transaksi ke dalam sistem.
Pelanggan dapat menambahkan nama item, jumlah item, dan harga per item, dan sistem akan secara otomatis menghitung total harga berdasarkan informasi tersebut.

<b>Read</b>

Pelanggan dapat melihat data transaksi dalam format tabel.
Pelanggan dapat melakukan pemeriksaan kebenaran data transaksi.
Pelanggan dapat melihat total biaya transaksi dan memeriksa apakah ada diskon yang diberikan.

<b>Update</b>

Pelanggan dapat mengubah nama item yang sudah dimasukkan sebelumnya dengan menyebutkan nama item.
Pelanggan dapat mengubah jumlah item yang sudah dimasukkan sebelumnya dengan menyebutkan nama item, dan total harga akan diperbarui sesuai dengan jumlah yang baru.
Pelanggan dapat mengubah harga per item yang sudah dimasukkan sebelumnya dengan menyebutkan nama item, dan total harga akan diperbarui sesuai dengan harga baru.

<b>Delete</b>

Pelanggan dapat menghapus item tertentu dari daftar transaksi dengan menyebutkan nama item.
Pelanggan dapat menghapus seluruh daftar transaksi mereka.
Ini akan membantu dalam mengotomatisasi dan menyederhanakan proses penjualan di supermarket serta memungkinkan pelanggan untuk berbelanja dengan lebih efisien.
    
## Flowchart

![flowchart drawio](https://github.com/Faqih26/PacmanCashierProject/blob/main/Untitled%20Diagram.jpg?raw=true)

Gambar 1. Flowchart super cashier

## Teknikal

proyek ini terdiri dari 2 file yaitu main.py dan modul.py yang masing-masing memiliki kegunaan.
- file modul.py digunakan sebagai modul yang berisi *class, function dan attributes*. penjelasan dari isi file sebagai berikut:


    import pandas as pd
    
    class SupermarketCashier:
        def __init__(self):
            self.transaction_id = self.get_transaction_id()
            self.items = []
    
        @staticmethod
        def get_transaction_id():
            while True:
                try:
                    return int(input("Masukkan ID Transaksi Anda: "))
                except ValueError:
                    print("ID Transaksi tidak valid!")
    
        def menu(self):
            while True:
                print("\n<----------------------- Menu ----------------------->")
                print("1. Tambah entri pesanan")
                print("2. Edit Nama Barang pesanan")
                print("3. Edit Jumlah Barang pesanan")
                print("4. Edit Harga per Barang pesanan")
                print("5. Konfirmasi pesanan")
                print("6. Hapus pesanan tertentu")
                print("7. Hapus semua pesanan")
                print("8. Total biaya semua pesanan")
                print("9. Keluar dari program")
                print("\n")
    
                choice = input("Masukkan perintah = ")
    
                if choice == "1":
                    self.add_item()
                elif choice == "2":
                    self.edit_item_name()
                elif choice == "3":
                    self.edit_item_quantity()
                elif choice == "4":
                    self.edit_item_price()
                elif choice == "5":
                    self.confirm_order()
                elif choice == "6":
                    self.remove_item()
                elif choice == "7":
                    self.clear_transaction()
                elif choice == "8":
                    self.calculate_total_price()
                elif choice == "9":
                    print("Terima kasih telah menggunakan layanan kami.")
                    break
                else:
                    print("Perintah tidak valid. Silakan coba lagi.")
                    
    
        def add_item(self):
            nama_barang = input("Nama Barang: ")
            while True:
                try:
                    jumlah_item = int(input("Jumlah Barang: "))
                    harga = int(input("Harga per Barang: "))
                    total_harga = jumlah_item * harga
                    self.items.append({
                        "Nama Barang": nama_barang,
                        "Jumlah Barang": jumlah_item,
                        "Harga per Barang": harga,
                        "Total Harga": total_harga
                    })
                    print("Barang berhasil ditambahkan ke keranjang.")
                    break
                except ValueError:
                    print("Input harus berupa angka.")
                    
    
        def edit_item_name(self):
            nama_barang = input("Nama Barang yang ingin diubah: ")
            for item in self.items:
                if item["Nama Barang"] == nama_barang:
                    new_name = input("Masukkan Nama Barang yang baru: ")
                    item["Nama Barang"] = new_name
                    print("Nama Barang berhasil diubah.")
                    return
            print("Barang tidak ditemukan.")
    
    
        def edit_item_quantity(self):
            nama_barang = input("Nama Barang yang ingin diubah jumlahnya: ")
            for item in self.items:
                if item["Nama Barang"] == nama_barang:
                    while True:
                        try:
                            new_quantity = int(input("Masukkan jumlah barang yang baru: "))
                            item["Jumlah Barang"] = new_quantity
                            item["Total Harga"] = new_quantity * item["Harga per Barang"]
                            print("Jumlah Barang berhasil diubah.")
                            return
                        except ValueError:
                            print("Input harus berupa angka.")
            print("Barang tidak ditemukan.")
    
    
        def edit_item_price(self):
            nama_barang = input("Nama Barang yang ingin diubah harga per barangnya: ")
            for item in self.items:
                if item["Nama Barang"] == nama_barang:
                    while True:
                        try:
                            new_price = int(input("Masukkan harga per Barang yang baru: "))
                            item["Harga per Barang"] = new_price
                            item["Total Harga"] = item["Jumlah Barang"] * new_price
                            print("Harga per Barang berhasil diubah.")
                            return
                        except ValueError:
                            print("Input harus berupa angka.")
            print("Barang tidak ditemukan.")
    
    
        def confirm_order(self):
            if not self.items:
                print("Tidak ada data transaksi.")
            else:
                print("\n<-------- List Order Barang -------->")
                df = pd.DataFrame(self.items)
                print(df)
                print("Data transaksi telah diverifikasi dengan benar.")
    
    
        def remove_item(self):
            nama_barang = input("Nama Barang yang ingin dihapus: ")
            for item in self.items:
                if item["Nama Barang"] == nama_barang:
                    self.items.remove(item)
                    print("Barang berhasil dihapus.")
                    return
            print("Barang tidak ditemukan.")
    
    
        def clear_transaction(self):
            self.items = []
            print("Transaksi berhasil dihapus.")
    
    
        def calculate_total_price(self):
            if not self.items:
                print("Tidak ada data transaksi.")
            else:
                df = pd.DataFrame(self.items)
                total_harga = df["Total Harga"].sum()
    
                print("\n<-------- Total Biaya -------->")
                print(f"Total biaya: Rp.{total_harga}")
    
                if total_harga > 500000:
                    diskon = total_harga * 0.10
                    total_harga_setelah_diskon = total_harga - diskon
                    print(f"Diskon 10%: Rp.{diskon}")
                    print(f"Total biaya setelah diskon: Rp.{total_harga_setelah_diskon}")
                elif total_harga > 300000:
                    diskon = total_harga * 0.08
                    total_harga_setelah_diskon = total_harga - diskon
                    print(f"Diskon 8%: Rp.{diskon}")
                    print(f"Total biaya setelah diskon: Rp.{total_harga_setelah_diskon}")
                elif total_harga > 200000:
                    diskon = total_harga * 0.05
                    total_harga_setelah_diskon = total_harga - diskon
                    print(f"Diskon 5%: Rp.{diskon}")
                    print(f"Total biaya setelah diskon: Rp.{total_harga_setelah_diskon}")
        if __name__ == "__main__":
            cashier = SupermarketCashier()
            cashier.menu()

## Test Case

Pada bagian ini program akan dilakukan beberapa testing berbeda untuk memastikan bahwa program berjalan dengan lancar.

1. Test pertama
    Customer ingin menambahkan dua item baru menggunakan *method add_item()*. item yang ditambahkan adalah sebagai berikut:
    - Nama item: Ayam Goreng, Qty: 2 dan harga per item: 20000
    - Nama item: Pasta Gigi, Qty: 3 dan harga per item: 15000

    Hasil:
    
    ![test1](https://github.com/Faqih26/PacmanCashierProject/assets/74944172/14e7a21e-fbe8-4914-aab2-dbde7c31c00c)
    
    Gambar 2. Output test pertama
 
2. Test kedua
    Ternyata Customer salah membeli salah satu item dari belanjaan yang sudah ditambahkan, maka customer menggunakan *method delete_item()* untuk menghapus item.   Item yang ingin dihapus adalah <b>Pasta Gigi</b>.

    Hasil:
    
    ![test24](https://github.com/Faqih26/PacmanCashierProject/assets/74944172/4ec6b377-1559-4e09-b99a-f677e4597210)
    
    Gambar 3. Output test kedua

3. Test ketiga
    Ternyata setelah dipikir-pikir Customer salah memasukkan item yang ingin dibelanjakan! Daripada menghapusnya satu-satu, maka Customer cukup menggunakan *method reset_transaction()* untuk menghapus semua item yang sudah ditambahkan.

    Hasil:
    
    ![test3](https://github.com/Faqih26/PacmanCashierProject/assets/74944172/5b839301-6a59-4f59-a4b7-2f264d48a1a2)
    
    Gambar 4. Output test ketiga

4. Test keempat
    Setelah Customer selesai berbelanja, akan menghitung total belanja yang harus dibayarkan menggunakan *method total_price()*. Sebelum mengeluarkan output total belanja akan menampilkan item-item yang dibeli.

    Hasil:
    
    ![test444](https://github.com/Faqih26/PacmanCashierProject/assets/74944172/322605c5-eb8e-4d66-9857-92da37068325)
    
    Gambar 5. Output test keempat

## Kesimpulan: 

Kebanyakan orang sangat mengandalkan supermarket untuk memenuhi kebutuhan sehari-hari, karena di sana tersedia berbagai barang yang dibutuhkan dalam satu tempat. Supermarket membantu efisiensi berbelanja bagi pelanggan. Program yang diusulkan akan meningkatkan efisiensi pelanggan dan supermarket dengan memungkinkan transaksi tanpa harus secara fisik datang ke toko, cukup dengan menggunakan smartphone dan internet.

Harapan untuk program ini adalah dapat mengembangkannya menjadi sebuah aplikasi mobile atau situs web yang menarik dan interaktif. Beberapa fitur tambahan yang bisa dipertimbangkan adalah pemberian poin kepada pelanggan setiap kali mereka bertransaksi, yang nantinya bisa digunakan untuk mendapatkan barang gratis di supermarket. Juga, penyimpanan seluruh data pelanggan, transaksi, dan inventaris barang ke dalam database untuk manajemen yang lebih efisien.

