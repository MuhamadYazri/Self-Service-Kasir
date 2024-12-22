import time, sys, os, csv
from . import Database, View
from tabulate import tabulate
import pandas as pd
from datetime import datetime, timedelta

List_Pesanan = {"Item": [], "Jumlah": [], "Harga_Satuan": [], "Harga_Total": []}

def Clear_Screen():
    os.system('cls')

def Menambahkan_Pesanan(Kategori, Total_Pembayaran):
    global List_Pesanan
    Menu_Kategori = "Makanan" if Kategori == "1" else "Minuman"
    while True:
        try:
            Clear_Screen()
            View.Menampilkan_Menu(Menu_Kategori)
            Memilih_Item = int(input(f"Masukkan nomor {Menu_Kategori.lower()} yang ingin dipesan: "))
            Menu_Data = Database.Menu_Data()

            if Memilih_Item - 1  == -1:
                return Total_Pembayaran

            elif Memilih_Item in Menu_Data[Menu_Kategori]:
                Item, Harga_Item = Menu_Data[Menu_Kategori][Memilih_Item]     
                Jumlah_Item = int(input(f"Masukkan jumlah pesanan untuk {Item}: "))
                
                if Jumlah_Item <= 0:
                    print("Jumlah tidak valid")
                    time.sleep(2)
                    continue

                if str(Item) in List_Pesanan["Item"]:
                    Nama_Barang = str(Menu_Data[Menu_Kategori][Memilih_Item][0])
                    Index = List_Pesanan["Item"].index(str(Nama_Barang))
                    List_Pesanan["Jumlah"][Index] += Jumlah_Item
                    Data_Break = int(List_Pesanan["Harga_Total"][Index][3:].replace(",",""))
                    Data_Break += Jumlah_Item * Harga_Item
                    List_Pesanan["Harga_Total"][Index] = f"Rp {Data_Break:,}"

                else:
                    List_Pesanan["Item"].append(str(Item))
                    List_Pesanan["Harga_Satuan"].append(f"Rp {Harga_Item:,}")
                    List_Pesanan["Jumlah"].append(Jumlah_Item)
                    List_Pesanan["Harga_Total"].append(f"Rp {(Jumlah_Item * Harga_Item):,}")
                    
                Total_Pembayaran += Harga_Item * Jumlah_Item
                View.Loading_Animasi()
                print("\n✅ Pesanan berhasil ditambahkan!\n")
                time.sleep(2)

                break
            else:
                print("\n❌ Pilihan tidak tersedia, silakan coba lagi.\n")
                time.sleep(2)

        except Exception as error :
            print(f"\nInput Tidak Valid")
            time.sleep(5)
            # print("\n❌ Input tidak valid, silakan masukkan lagi.\n")
            # time.sleep(2)
        
    return Total_Pembayaran

def Hapus_Pesanan(List_Pesanan, Subtotal):
    Clear_Screen()
    while True:
        Pandas_List = pd.DataFrame(List_Pesanan, index= range(1, len(List_Pesanan["Item"]) + 1))
        print("\nPesanan Anda: \n")
        print(tabulate(Pandas_List, headers=["No","Item", "Jumlah", "Harga Satuan", "Harga Total"], tablefmt="grid", numalign= "center",stralign="center")) 
        print("0. Cancel\n")
        try:
            Index_Item_Di_Hapus = int(input("Masukkan Nomor Pesanan: "))
            if Index_Item_Di_Hapus - 1 == -1:
                return List_Pesanan, Subtotal
            Hapus_Harga_Total = str(List_Pesanan["Harga_Total"][Index_Item_Di_Hapus-1][3:])
            Hapus_Harga_Total = int(Hapus_Harga_Total.replace(",",""))
            for keys in List_Pesanan:
                List_Pesanan[keys].pop(Index_Item_Di_Hapus-1)
            View.Loading_Animasi("\nProses menghapus pesanan...")
            print("\nPesanan telah dihapus! ✅")
            Subtotal -= Hapus_Harga_Total
            time.sleep(2)
            return List_Pesanan, Subtotal
            
        except ValueError:
            print("\nInput Harus Angka")
            time.sleep(2)
        
        except IndexError:
            print("\nPesanan Tidak Ditemukan")
            time.sleep(2)
        
def Membuat_Data(data_pesanan, nama_pelanggan, total_belanja):
    wib = datetime.utcnow() + timedelta(hours=7)
    waktu = wib.strftime('%H:%M:%S')

    item = data_pesanan["Item"]
    jumlah = data_pesanan["Jumlah"]
    harga_satuan = data_pesanan["Harga_Satuan"]
    harga_total = data_pesanan["Harga_Total"]

    try:
        with open(Database.DB_NAME, 'a', newline='') as csvfile:
            csvwriter = csv.writer(csvfile)
            for indeks in range(len(item)):
                isi_data = [waktu,nama_pelanggan, item[indeks], jumlah[indeks], str(harga_satuan[indeks]), str(harga_total[indeks])]
                csvwriter.writerow(isi_data)

    except Exception as e:
        print(f"\nError Menambahkan Data, Check Program...")
        time.sleep(2)

def Return_List_Pesanan():
    global List_Pesanan
    return List_Pesanan
