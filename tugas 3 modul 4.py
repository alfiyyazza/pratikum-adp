n = int(input("jumlah pendaftar : "))
print()

for i in range (n) :
    print(f"\nMasukkan data pendaftar ke-{i+1}")
    nama = input("Nama : ")
    matakuliah = input("Mata kuliah yang diminati : ")
    wawancara = float(input("Nilai wawancara : "))
    while wawancara > 100 or wawancara < 1 :
        print("Nilai harus berada dalam rentang 1-100, silahkan coba lagi")
        wawancara = float(input("Nilai wawancara : "))

    testulis = float(input("Nilai tes tulis : "))
    while testulis > 100 or testulis < 1 :
        print("Nilai harus berada dalam rentang 1-100, silahkan coba lagi")
        testulis = float(input("Nilai tes tulis : "))

    mengajar = float(input("Nilai mengajar : "))
    while mengajar > 100 or mengajar < 1 :
        print("Nilai harus berada dalam rentang 1-100, silahkan coba lagi")
        mengajar = float(input("Nilai mengajar : "))
    
    total_nilai = wawancara + testulis + mengajar
    rata_rata = total_nilai / 3 
    print(f"{rata_rata}")
    if rata_rata > 80 :
        print("LULUS")
    else :
        print("TIDAK LULUS")
