# Data tarif dalam bentuk array 2D: [tarif_awal, tarif_lanjutan]
tarif_listrik = [
    [1500, 2000],  # Golongan 1
    [2500, 3000],  # Golongan 2
    [4000, 5000],  # Golongan 3
    [5000, 7000]]   # Golongan 4

def hitung_tagihan(pemakaian_kwh, golongan_tarif=3):
    golongan_ke = golongan_tarif - 1  # Menyesuaikan posisi array
    tarif_awal = tarif_listrik[golongan_ke][0]
    tarif_lanjutan = tarif_listrik[golongan_ke][1]
    
    if pemakaian_kwh <= 100:
        total_biaya = pemakaian_kwh * tarif_awal
    else:
        total_biaya = 100 * tarif_awal + (pemakaian_kwh - 100) * tarif_lanjutan
    
    return total_biaya

def program_utama():
    daftar_pelanggan = []

    jumlah = int(input("Masukkan jumlah pelanggan: "))

    for nomor in range(1, jumlah + 1):
        print(f"\nPelanggan ke-{nomor}")
        kwh = int(input("Pemakaian listrik (dalam kWh): "))
        gol_input = input("Masukkan golongan tarif (1-4): ")

        if gol_input == "":
            daftar_pelanggan.append([kwh])  # tanpa golongan, default golongan 3
        else:
            golongan = int(gol_input)
            daftar_pelanggan.append([kwh, golongan])

    print("\n=== Rincian Tagihan Listrik ===")
    urutan = 1
    for pelanggan in daftar_pelanggan:
        if len(pelanggan) == 2:
            kwh = pelanggan[0]
            golongan = pelanggan[1]
        else:
            kwh = pelanggan[0]
            golongan = 3  # default jika tidak diinput

        tagihan = hitung_tagihan(kwh, golongan)
        print(f"Pelanggan {urutan}: {kwh} kWh, Golongan {golongan} => Tagihan: Rp {tagihan:,}")
        urutan += 1

program_utama()
