import time, csv

def Return_Tanggal():
    tanggal = time.strftime("%d-%m-%Y", time.gmtime())
    return tanggal

DB_NAME = f"data ( {Return_Tanggal()} ).csv"

def Check_Data():
    print("\n\nCheck file untuk laporan hari ini...")
    try:
        with open(DB_NAME, "r") as csvfile:
            pass
    except:
        print("\nData hari ini belum tersedia, Membuat data...")
        time.sleep(2)
        with open(DB_NAME, 'w', newline='') as csvfile:
            csvwriter = csv.writer(csvfile)
            header = ["Jam","Nama Pembeli", "Nama Item", "Jumlah", "Harga Item", "Subtotal"]
            csvwriter.writerow(header)
            
def Menu_Data():
    menu_data = {
    "Makanan": {
        1: ("Nasi Ayam", 15_000),
        2: ("Nasi Ikan + Telur", 20_000),
        3: ("Nasi Goreng", 20_000),
        4: ("Soto Ayam", 18_000),
        5: ("Pecel Lele", 22_000),
        6: ("Bakso", 25_000),
        7: ("Tahu-Tempe Goreng", 10_000),
        8: ("Lontong Sayur", 15_000),
        9: ("Ikan Bakar", 30_000),
        10: ("Ayam Goreng", 20_000),
    },
    "Minuman": {
        1: ("Es Teh Manis", 5_000),
        2: ("Es Jeruk", 7_000),
        3: ("Kopi Hitam", 8_000),
        4: ("Teh Tawar Hangat", 3_000),
        5: ("Air Mineral", 5_000),
        6: ("Susu Jahe", 10_000),
        7: ("Susu Kedelai", 8_000),
    }
    }
    return menu_data
        