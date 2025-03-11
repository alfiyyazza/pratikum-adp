barang1 = ("tepung", 59000)
barang2 = ("roti", 60000)
barang3 = ("minyak wijen", 75000)
barang4 = ("teh", 55000)
barang5 = ("cincau", 70000)
barang6 = ("pasta", 52000)
barang7 = ("susu formula", 98000)
barang8 = ("garam himalaya", 69000)
barang9 = ("kentang", 88000)
barang10 = ("mozarella", 73000)

print("Daftar Barang yang Tersedia:")
print(f"1. {barang1[0]} - Rp{barang1[1]}")
print(f"2. {barang2[0]} - Rp{barang2[1]}")
print(f"3. {barang3[0]} - Rp{barang3[1]}")
print(f"4. {barang4[0]} - Rp{barang4[1]}")
print(f"5. {barang5[0]} - Rp{barang5[1]}")
print(f"6. {barang6[0]} - Rp{barang6[1]}")
print(f"7. {barang7[0]} - Rp{barang7[1]}")
print(f"8. {barang8[0]} - Rp{barang8[1]}")
print(f"9. {barang9[0]} - Rp{barang9[1]}")
print(f"10. {barang10[0]} - Rp{barang10[1]}")

pilihan = int(input("\nPilih nomor barang yang ingin dibeli: "))
kuantitas = int(input("Pilih jumlah yang ingin dibeli: "))

if pilihan == 1:
    nama_barang, harga_satuan = barang1
elif pilihan == 2:
    nama_barang, harga_satuan = barang2
elif pilihan == 3:
    nama_barang, harga_satuan = barang3
elif pilihan == 4:
    nama_barang, harga_satuan = barang4
elif pilihan == 5:
    nama_barang, harga_satuan = barang5
elif pilihan == 6:
    nama_barang, harga_satuan = barang6
elif pilihan == 7:
    nama_barang, harga_satuan = barang7
elif pilihan == 8:
    nama_barang, harga_satuan = barang8
elif pilihan == 9:
    nama_barang, harga_satuan = barang9
elif pilihan == 10:
    nama_barang, harga_satuan = barang10
else:
    print("Pilihan tidak valid!")
    exit()

harga_total = harga_satuan * kuantitas

if harga_total < 1000000:
    diskon = 0
elif 1000000 <= harga_total <= 1500000:
    diskon = harga_total * 0.10
else:
    diskon = harga_total * 0.15

total_bayar = harga_total - diskon

print("\n========= Struk =========")
print(f"Nama Barang  : {nama_barang}")
print(f"Kuantitas    : {kuantitas}")
print(f"Harga Satuan : Rp{harga_satuan}")
print(f"Harga Total  : Rp{harga_total}")
print(f"Potongan Harga : Rp{diskon}")
print(f"Total Bayar  : Rp{total_bayar}")
print("============================")

