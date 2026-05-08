def sequential_search(data, n, target):
    i = 0
    counter = 0

    while i < n:
        if data[i] == target:
            counter += 1
        i += 1

    return counter


def main():
    data_barang = [
        "Beras", "Gula", "Minyak", "Sabun", "Mie Instan", "Beras",
        "Kopi", "Teh", "Sabun", "Susu", "Gula", "Mie Instan", "Roti",
        "Roti", "Minyak", "Gula", "Telur", "Kopi", "Kecap", "Sabun", "Susu"
    ]

    n = len(data_barang)

    print("PROGRAM PENGECEKAN STOK BARANG DI TOKO")
    print("Daftar Barang:")
    print("1.  Gula\n"
          "2.  Beras\n"
          "3.  Minyak\n"
          "4.  Sabun\n"
          "5.  Mie Instan\n"
          "6.  Kopi\n"
          "7.  Teh\n"
          "8.  Susu\n"
          "9.  Roti\n"
          "10. Telur\n"
          "11. Kecap"
          )

    target = input("\nMasukkan nama barang yang ingin dicari: ")

    counter = sequential_search(data_barang, n, target)

    if counter > 0:
        print(f"\nStok barang '{target}' masih tersedia sebanyak {counter}.")
    else:
        print(f"\nStok barang '{target}' sudah habis.")


if __name__ == "__main__":
    main()