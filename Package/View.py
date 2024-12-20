from tabulate import tabulate
import pandas as pd
from . import Database
import time

def Memilih_Menu_Kategori():
    List_Menu = [
    ["1", "Makanan"],
    ["2", "Minuman"],
    ["3", "Hapus Pesanan"],
    ["4", "Batalkan"],
    ["0", "Selesai"]
    ]
    print("\n" + "="*30)
    print("📜  MENU UTAMA 📜".center(30))
    print("="*30)
    print(tabulate(List_Menu, headers=["No", "Pilihan"], tablefmt="double_grid",colalign=("center", "left")))
    Menu = input("Masukkan Pilihan [1/2/3/4/0]: ")
    return Menu

def Menampilkan_Menu(kategori):
    print("="*40)
    print(f"🍴  MENU {kategori.upper()}  🍴".center(40))
    print("="*40)
    Menu_Data = Database.Menu_Data()
    Menu_Kategori = Menu_Data[kategori]
    data_menu = [
        [nomor, item, f"Rp {harga:,}"] 
        for nomor, (item, harga) in Menu_Kategori.items()
    ]
    print(tabulate(data_menu, headers=["No.", "Nama Item", "Harga"], tablefmt="fancy_grid", numalign="center",stralign="e"))
    print("\n0. Cancel untuk kembali ke menu utama")
    print("="*40)


def Menampilkan_Struk(data_pesanan, subtotal, dics, uang_user, kembalian, nama_pelanggan):
    tanggal = Database.Return_Tanggal()
    print("\n\n","="*59, "\n\n")
    print("*** 🧾  STRUK STRUKAN  🧾 ***".center(59))
    print("WARUNG MAKAN SEDERHANA".center(59))
    print("JL. PASMOD MARS".center(59))
    print("".center(59))
    print("-"*59)
    
    print(f"\nNama    : {nama_pelanggan}")
    print(f"Tanggal : {tanggal}\n")

    print("Rincian Pesanan :\n")
    print((tabulate(data_pesanan, headers=["Item", "Jumlah", "Harga Satuan", "Harga Total"], numalign="center",stralign="center", showindex=False)))
    print("\n")
    print("-"*59)
    
    if subtotal > 100_000:
        print(f"\n\t\t\t\t{'Subtotal    :':<15} Rp {int(subtotal):,}")
        print(f"\t\t\t\t{'Disc 10%    :':<15} Rp {int(dics):,}")
    elif subtotal > 50_000:
        print(f"\n\t\t\t\t{'Subtotal    :':<15} Rp {int(subtotal):,}")
        print(f"\t\t\t\t{'Disc 5%     :':<15} Rp {int(dics):,}")
    
    print("\t\t\t\t-----------------------")
    print(f"\t\t\t\t{'Total       :':<10} Rp {int(subtotal - dics):,}")
    print(f"\t\t\t\t{'Pembayaran  :':<10} Rp {int(uang_user):,}")
    print(f"\t\t\t\t{'Kembali     :':<10} Rp {int(kembalian):,}")

    print("\n\n","🤝 Terima Kasih Telah Memesan! 🤝".center(59))
    print("🙏 Silahkan Ditunggu Pesanannya 🙏".center(59))
    print("\n\n","="*59, "\n\n")

def Loading_Animasi(task="\nProses Menambahkan pesanan..."):
    panjang_bar = 30
    print(f"{task}")
    for i in range(panjang_bar + 1):
        time.sleep(0.03)  # Delay setiap langkah
        percent = int((i / panjang_bar) * 100)
        bar = "■" * i + "□" * (panjang_bar - i)
        print(f"\r[{bar}] {percent}%", end="")
