import math
from fractions import Fraction
import sympy as sp

def selesaikan_perbandingan():
    print("\nMenyelesaikan Perbandingan (a/b = c/d)")
    try:
        a = float(input("Masukkan a: "))
        b = float(input("Masukkan b: "))
        c = float(input("Masukkan c: "))
        d = input("Masukkan d (atau 'x' untuk mencari x): ")

        if d.lower() == 'x':
            if a == 0:
                print("Error: Pembagian dengan nol")
                return
            x = (b * c) / a
            print(f"Solusi: x = {x}")
        else:
            d = float(d)
            # Memeriksa apakah a/b sama dengan c/d
            hasil = (a * d) == (b * c)
            print(f"Perbandingan tersebut {'benar' if hasil else 'salah'}")
            if not hasil:
                print(f"Hasil kali silang: {a}*{d} = {a*d} vs {b}*{c} = {b*c}")
    except ValueError:
        print("Input tidak valid. Harap masukkan angka.")

def selesaikan_x():
    print("\nMenyelesaikan persamaan untuk x (ax + b = c)")
    try:
        a = float(input("Masukkan koefisien x (a): "))
        b = float(input("Masukkan konstanta (b): "))
        c = float(input("Masukkan nilai ruas kanan (c): "))

        if a == 0:
            if b == c:
                print("Solusi tak hingga (identitas)")
            else:
                print("Tidak ada solusi (kontradiksi)")
        else:
            x = (c - b) / a
            print(f"Solusi: x = {x}")
    except ValueError:
        print("Input tidak valid. Harap masukkan angka.")

def faktorkan_akar_kuadrat():
    print("\nMemfaktorkan Akar Kuadrat (√n)")
    try:
        n = int(input("Masukkan bilangan bulat positif: "))
        if n < 0:
            print("Harap masukkan bilangan bulat positif.")
            return

        kuadrat_terbesar = 1
        sisa = n

        # Mencari faktor kuadrat sempurna terbesar
        for i in range(int(math.sqrt(n)), 0, -1):
            if n % (i*i) == 0:
                kuadrat_terbesar = i*i
                sisa = n // kuadrat_terbesar
                break

        if kuadrat_terbesar == 1:
            print(f"√{n} tidak dapat disederhanakan lebih lanjut")
        else:
            print(f"√{n} = {int(math.sqrt(kuadrat_terbesar))}√{sisa}")
    except ValueError:
        print("Input tidak valid. Harap masukkan bilangan bulat.")

def konversi_desimal():
    print("\nMengubah Desimal ke Pecahan dan Persen")
    try:
        desimal = float(input("Masukkan bilangan desimal: "))

        # Mengubah ke pecahan
        pecahan = Fraction(desimal).limit_denominator()
        print(f"Pecahan: {pecahan.numerator}/{pecahan.denominator}")

        # Mengubah ke persen
        persen = desimal * 100
        print(f"Persen: {persen}%")
    except ValueError:
        print("Input tidak valid. Harap masukkan angka.")

def konversi_pecahan():
    print("\nMengubah Pecahan ke Desimal dan Persen")
    try:
        pembilang = float(input("Masukkan pembilang: "))
        penyebut = float(input("Masukkan penyebut: "))

        if penyebut == 0:
            print("Error: Penyebut tidak boleh nol")
            return

        desimal = pembilang / penyebut
        persen = desimal * 100

        print(f"Desimal: {desimal}")
        print(f"Persen: {persen}%")
    except ValueError:
        print("Input tidak valid. Harap masukkan angka.")

def konversi_persen():
    print("\nMengubah Persen ke Desimal dan Pecahan")
    try:
        persen = float(input("Masukkan persen (tanpa tanda %): "))

        desimal = persen / 100
        pecahan = Fraction(desimal).limit_denominator()

        print(f"Desimal: {desimal}")
        print(f"Pecahan: {pecahan.numerator}/{pecahan.denominator}")
    except ValueError:
        print("Input tidak valid. Harap masukkan angka.")

def main():
    print("Kalkulator Multi-Fungsi")
    print("=======================")

    while True:
        print("\nPilih operasi:")
        print("1. Menyelesaikan perbandingan")
        print("2. Mencari x dalam persamaan")
        print("3. Memfaktorkan akar kuadrat")
        print("4. Mengubah desimal ke pecahan dan persen")
        print("5. Mengubah pecahan ke desimal dan persen")
        print("6. Mengubah persen ke desimal dan pecahan")
        print("7. Keluar")

        pilihan = input("Masukkan pilihan Anda (1-7): ")

        if pilihan == '1':
            selesaikan_perbandingan()
        elif pilihan == '2':
            selesaikan_x()
        elif pilihan == '3':
            faktorkan_akar_kuadrat()
        elif pilihan == '4':
            konversi_desimal()
        elif pilihan == '5':
            konversi_pecahan()
        elif pilihan == '6':
            konversi_persen()
        elif pilihan == '7':
            print("Sampai jumpa!")
            break
        else:
            print("Pilihan tidak valid. Harap masukkan angka antara 1 dan 7.")

if __name__ == "__main__":
    main()