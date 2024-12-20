import time
import Package

def main():
    Package.Clear_Screen()
    Subtotal = 0
    List_Pesanan = Package.Return_List_Pesanan()
    Package.Check_Data()

    while True:
        Package.Clear_Screen()
        Menu_Kategori = Package.Memilih_Menu_Kategori()

        if Menu_Kategori in ["1", "2"]:
            Package.Clear_Screen()
            Subtotal = Package.Menambahkan_Pesanan(Menu_Kategori, Subtotal)

            while input("Apakah Ada Pesanan Lain? (Y/N): ").upper() == "Y":
                Subtotal = Package.Menambahkan_Pesanan(Menu_Kategori, Subtotal)      
            else:
                pass

        elif Menu_Kategori == "3":
            if not List_Pesanan["Item"]:
                print("\nTidak Ada Pesanan")
                time.sleep(2)
            else:
                List_Pesanan, Subtotal = Package.Hapus_Pesanan(List_Pesanan, Subtotal)
                while input("\nApakah Ada Yang Ingin Di hapus Lagi? (Y/N):  ").upper() == "Y":
                    List_Pesanan, Subtotal = Package.Hapus_Pesanan(List_Pesanan, Subtotal)
                else:
                    pass
        
        elif Menu_Kategori == "4":
            Package.Clear_Screen()
            yakin = input("Are You Sure (Y/N)? : ").upper()

            if yakin == "Y":
                print("Yowesss, Takdirrr...")
                time.sleep(2)
                break
            else:
                print("Lanjutkan...")
                time.sleep(2)
                continue
        
        elif Menu_Kategori == "0":
            
            if Subtotal == 0:
                print("\nPesanan Kosong")
                time.sleep(2)
                continue
            Package.Clear_Screen()
            Nama_Pembeli = input("Masukkan Nama : ").upper()
            
            while True:
                try:
                    Package.Clear_Screen()
                    print(f"Total Harga Pesanan: Rp {Subtotal:,}\n")

                    Input_Uang_User = int(input("Masukkan Uang Pembayaran: "))
                    
                    if Input_Uang_User < Subtotal:
                        print("\nUang Tidak Cukup")
                        time.sleep(2)
                    else:
                        Diskon = 0
                        if Subtotal > 100_000:
                            # Discount 10%
                            Diskon = Subtotal * 0.1
                        elif Subtotal > 50_000:
                            # Discount 5%
                            Diskon = Subtotal * 0.05

                        Uang_Kembali = (Input_Uang_User - Subtotal) + Diskon
                        Package.Membuat_Data(List_Pesanan, Nama_Pembeli, Subtotal)
                        Package.Loading_Animasi("\nMembuat Struk...")
                        Package.Clear_Screen()
                        Package.Menampilkan_Struk(List_Pesanan, Subtotal, Diskon, Input_Uang_User, Uang_Kembali, Nama_Pembeli)
                        
                        break
                
                except Exception as error:
                    print(f"\nError:\n{error}")
                    time.sleep(2)
            break

        else:
            print(f"\nMenu Tidak tersedia")
            time.sleep(2)

main()