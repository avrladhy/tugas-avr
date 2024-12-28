#menghitung luas segitiga
def hitung_luas_segitiga(alas, tinggi):
    luas = 0.5 * alas * tinggi
    return luas

#menghitung keliling segitiga
def hitung_keliling_segitiga(sisi1, sisi2, sisi3):
    keliling = sisi1 + sisi2 + sisi3
    return keliling

# Programnya
while True:
    print("Pilih salah satu dari dua fungsionalitas berikut:")
    print("1. Menghitung Luas Segitiga")
    print("2. Menghitung Keliling Segitiga")
    print("3. Keluar dari Program")
    pilihan = int(input("Masukkan pilihan Anda: "))

    if pilihan == 1:
        alas = float(input("Masukkan panjang alas: "))
        tinggi = float(input("Masukkan tinggi: "))
        luas = hitung_luas_segitiga(alas, tinggi)
        print(f"Luas segitiga adalah: {luas}")
    elif pilihan == 2:
        sisi1 = float(input("Masukkan panjang sisi pertama: "))
        sisi2 = float(input("Masukkan panjang sisi kedua: "))
        sisi3 = float(input("Masukkan panjang sisi ketiga: "))
        keliling = hitung_keliling_segitiga(sisi1, sisi2, sisi3)
        print(f"Keliling segitiga adalah: {keliling}")
    elif pilihan == 3:
        print("Good bye")
        print("Terimakasih telah menggunakan program ini")
        break
    else:
        print("Pilihan tidak valid.")