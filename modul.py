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
