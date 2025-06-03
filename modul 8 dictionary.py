namafile = "notes.txt"
print("=== APLIKASI CATATAN SEDERHANA ===")

while True:
    print("\nMenu")
    print("1. Lihat Catatan")
    print("2. Buat Catatan Baru")
    print("3. Exit")
    pilihan = input("Pilih menu (1-3): ")

    if pilihan == "1":
        file = open(namafile, "r")
        baris = file.readlines()
        file.close()

        catatan = []
        i = 0
        while i < len(baris)-1:
            judul = ""
            isi = ""

            for huruf in baris[i]:
                if huruf != "\n":
                    judul = judul + huruf
            for huruf in baris[i+1]:
                if huruf != "\n":
                    isi = isi + huruf

            catatan.append([judul, isi])
            i = i + 2

        if len(catatan) == 0:
            print("Catatan Belum Ada!")

        else:
            print("Judul Catatan Yang Ada: ")
            for data in catatan:
                print("-" + data[0])

            cari = input("Masukkan Judul Yang Ingin Dicari:")
            ditemukan = False
            for data in catatan:
                if cari == data[0]:
                    print("\nIsi Catatan:")
                    print(data[1])
                    break
            else:
                print("Data Tidak Ditemukan")

    elif pilihan == "2":
        judul = input("Buat Judul: ")
        isi = input("Masukkan Isi Catatan: ")
        file = open(namafile, "a")
        file.write(judul + "\n")
        file.write(isi + "\n")
        file.close()
        print("Catatan Sudah Disimpan!")

    elif pilihan == "3":
        print("Program Selesai.")
        break

    else:
        print("Pilihan Tidak Diketahui. Silahkan Coba Lagi!")