no_pelanggan = []
nama_pelanggan = []
total_belanja = []

while True:
    print("== Menu Utama ==")
    print("1. Update Data")
    print("2. Hapus Data")
    print("3. Cetak Data")
    print("4. Keluar")

    pilihan = input("Pilih Menu : ")
    print()

    if pilihan == "1":
        print("---- Tambah Data Pelanggan ----")
        # no = input("No. Pelanggan : ")
        # nama = input("Nama Pelanggan : ")
        # total = input("Total Belanja : ")

        # no_pelanggan.append(no)
        # nama_pelanggan.append(nama)
        # total_belanja.append(total)

        no_pelanggan.append(input("No. Pelanggan : "))
        nama_pelanggan.append(input("Nama Pelanggan : "))
        total_belanja.append(input("Total Belanja : "))
        print("\nData sudah ditambah\n")

    elif pilihan == "2":
        print("---- Hapus Data ----")
        hapus = input("Masukkan Nomor Pelanggan yang akan dihapus : ")

        no_baru = []
        nama_baru = []
        total_baru = []
        ditemukan = False

        for i in range(len(no_pelanggan)):
            if no_pelanggan[i] != hapus:
                no_baru.append(no_pelanggan[i])
                nama_baru.append(nama_pelanggan[i])
                total_baru.append(total_belanja[i])
            else:
                ditemukan = True

        if ditemukan == True:
            no_pelanggan = no_baru
            nama_pelanggan = nama_baru
            total_belanja = total_baru
            print("\nData selesai dihapuskan!\n")
        else:
            print("\nData tidak dapat ditemukan!\n")

    elif pilihan == "3":
        print("--- Cetak Data Pelanggan ---")
        if len(no_pelanggan) > 0:
            print(f"{'No':<5} | {'Nama':<15} | {'Total':<10}")
            for i in range(len(no_pelanggan)):
                print(f"{no_pelanggan[i]:<5} | {nama_pelanggan[i]:<15} | {total_belanja[i]:<10}")
        else:
            print("Tidak ada data pelanggan.\n")

    elif pilihan == "4":
        print("Terima kasih")
        break

    else:
        print("Pilihan anda tiidak valid. Silakan pilih ulang antara 1-4.\n")