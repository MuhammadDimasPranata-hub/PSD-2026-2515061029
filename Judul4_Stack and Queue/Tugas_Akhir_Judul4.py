class StackBuku:
    def __init__(self, max_size=100):
        self.MAX = max_size
        self.st = [None] * self.MAX
        self.top_idx = -1

    def is_empty(self):
        return self.top_idx == -1

    def is_full(self):
        return self.top_idx == self.MAX - 1

    def tambah_buku(self, judul):
        if self.is_full():
            print("Tumpukan buku penuh")
            return

        self.top_idx += 1
        self.st[self.top_idx] = judul
        print(f'Buku "{judul}" berhasil ditambahkan')

    def ambil_buku(self):
        if self.is_empty():
            print("Tumpukan buku kosong")
            return

        print(f'Buku "{self.st[self.top_idx]}" berhasil diambil')
        self.top_idx -= 1

    def lihat_buku_teratas(self):
        if self.is_empty():
            print("Tumpukan buku kosong")
            return

        print(f'Buku teratas: "{self.st[self.top_idx]}"')

    def tampilkan_buku(self):
        if self.is_empty():
            print("Tumpukan buku kosong")
            return

        print("\nDaftar Tumpukan Buku (atas ke bawah):")
        for i in range(self.top_idx, -1, -1):
            print(f"- {self.st[i]}")


def main():
    stack = StackBuku()
    pilih = 0

    while pilih != 5:
        print("\nSISTEM PENGELOLAAN TUMPUKAN BUKU")
        print("1. Tambah Buku")
        print("2. Ambil Buku")
        print("3. Lihat Buku Teratas")
        print("4. Tampilkan Semua Buku")
        print("5. Keluar")

        try:
            pilih = int(input("Pilih menu: "))
        except ValueError:
            print("Input harus berupa angka!")
            continue

        if pilih == 1:
            judul = input("Masukkan judul buku: ")
            stack.tambah_buku(judul)

        elif pilih == 2:
            stack.ambil_buku()

        elif pilih == 3:
            stack.lihat_buku_teratas()

        elif pilih == 4:
            stack.tampilkan_buku()

        elif pilih == 5:
            print("Program selesai.")

        else:
            print("Pilihan tidak valid!")


if __name__ == "__main__":
    main()