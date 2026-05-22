class Node:
    def __init__(self, npm, nama, tanggal_lahir, prodi):
        self.npm = npm
        self.nama = nama
        self.tanggal_lahir = tanggal_lahir
        self.prodi = prodi
        self.left = None
        self.right = None


class BSTAkademik:
    def __init__(self):
        self.root = None

    def insert_node(self, root, npm, nama, tanggal_lahir, prodi):
        if root is None:
            return Node(npm, nama, tanggal_lahir, prodi)

        if npm < root.npm:
            root.left = self.insert_node(root.left, npm, nama, tanggal_lahir, prodi)
        elif npm > root.npm:
            root.right = self.insert_node(root.right, npm, nama, tanggal_lahir, prodi)

        return root

    def insert(self, npm, nama, tanggal_lahir, prodi):
        self.root = self.insert_node(self.root, npm, nama, tanggal_lahir, prodi)

    def search_node(self, root, npm):
        if root is None:
            return None

        if root.npm == npm:
            return root

        if npm < root.npm:
            return self.search_node(root.left, npm)

        return self.search_node(root.right, npm)

    def search(self, npm):
        return self.search_node(self.root, npm)

    def inorder(self, root):
        if root is not None:
            self.inorder(root.left)

            print(f"""
NPM            : {root.npm}
Nama           : {root.nama}
Tanggal Lahir  : {root.tanggal_lahir}
Program Studi  : {root.prodi}
_______________________________________
""")

            self.inorder(root.right)


def main():
    bst = BSTAkademik()
    pilih = 0

    while pilih != 4:
        print("\nSistem Pencarian Data Akademik")
        print("1. Tambah Data Mahasiswa")
        print("2. Cari Data Berdasarkan NPM")
        print("3. Tampilkan Semua Data")
        print("4. Keluar")

        try:
            pilih = int(input("Pilih menu: "))
        except ValueError:
            print("Input harus angka!")
            continue

        if pilih == 1:
            try:
                npm = int(input("Masukkan NPM            : "))
                nama = input("Masukkan Nama           : ")
                tanggal_lahir = input("Masukkan Tanggal Lahir  : ")
                prodi = input("Masukkan Program Studi  : ")

                bst.insert(npm, nama, tanggal_lahir, prodi)

                print("Data berhasil ditambahkan")

            except ValueError:
                print("NPM harus angka!")

        elif pilih == 2:
            try:
                npm = int(input("Masukkan NPM yang dicari : "))

                hasil = bst.search(npm)

                if hasil is not None:
                    print("\nData Ditemukan")
                    print(f"NPM            : {hasil.npm}")
                    print(f"Nama           : {hasil.nama}")
                    print(f"Tanggal Lahir  : {hasil.tanggal_lahir}")
                    print(f"Program Studi  : {hasil.prodi}")
                else:
                    print("Data tidak ditemukan")

            except ValueError:
                print("NPM harus angka!")

        elif pilih == 3:
            print("\nData Mahasiswa")
            bst.inorder(bst.root)

        elif pilih == 4:
            print("Program selesai")

        else:
            print("Menu tidak valid")


if __name__ == "__main__":
    main()