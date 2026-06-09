class SlotState:
    EMPTY = 0
    OCCUPIED = 1
    DELETED = 2


class Entry:
    def __init__(self):
        self.key = None  # Nomor Telepon
        self.value = None  # Nama Kontak
        self.state = SlotState.EMPTY


class HashMapOpenAddressing:
    def __init__(self, size=20):
        self.SIZE = size
        self.table = [Entry() for _ in range(self.SIZE)]

    def hash_function(self, key):
        return (key % self.SIZE + self.SIZE) % self.SIZE

    def insert(self, key, value):
        idx = self.hash_function(key)
        first_deleted = -1

        for step in range(self.SIZE):
            i = (idx + step) % self.SIZE

            if self.table[i].state == SlotState.OCCUPIED:
                if self.table[i].key == key:
                    self.table[i].value = value
                    return True

            elif self.table[i].state == SlotState.DELETED:
                if first_deleted == -1:
                    first_deleted = i

            else:
                if first_deleted != -1:
                    i = first_deleted

                self.table[i].key = key
                self.table[i].value = value
                self.table[i].state = SlotState.OCCUPIED
                return True

        if first_deleted != -1:
            self.table[first_deleted].key = key
            self.table[first_deleted].value = value
            self.table[first_deleted].state = SlotState.OCCUPIED
            return True

        return False

    def search(self, key):
        idx = self.hash_function(key)

        for step in range(self.SIZE):
            i = (idx + step) % self.SIZE

            if self.table[i].state == SlotState.EMPTY:
                return None

            if (self.table[i].state == SlotState.OCCUPIED and
                    self.table[i].key == key):
                return self.table[i]

        return None

    def remove_key(self, key):
        entry = self.search(key)

        if entry is None:
            return False

        entry.state = SlotState.DELETED
        return True

    def display(self):
        print("\nDAFTAR KONTAK")

        ada_data = False

        for i in range(self.SIZE):
            if self.table[i].state == SlotState.OCCUPIED:
                print(
                    f"Nomor Telepon : {self.table[i].key}\n"
                    f"Nama Kontak   : {self.table[i].value}\n"
                )
                ada_data = True

        if not ada_data:
            print("Belum ada kontak tersimpan.")


def menu():
    kontak = HashMapOpenAddressing()

    while True:
        print("\nSISTEM MANAJEMEN KONTAK TELEPON")
        print("1. Tambah Kontak")
        print("2. Cari Kontak")
        print("3. Hapus Kontak")
        print("4. Tampilkan Semua Kontak")
        print("5. Keluar")

        pilihan = input("Pilih menu: ")

        if pilihan == "1":
            nomor = int(input("Masukkan Nomor Telepon: "))
            nama = input("Masukkan Nama Kontak: ")

            if kontak.insert(nomor, nama):
                print("Kontak berhasil disimpan.")
            else:
                print("HashMap penuh!")

        elif pilihan == "2":
            nomor = int(input("Masukkan Nomor Telepon yang dicari: "))

            hasil = kontak.search(nomor)

            if hasil:
                print("\nKontak ditemukan")
                print(f"Nomor : {hasil.key}")
                print(f"Nama  : {hasil.value}")
            else:
                print("Kontak tidak ditemukan.")

        elif pilihan == "3":
            nomor = int(input("Masukkan Nomor Telepon yang akan dihapus: "))

            if kontak.remove_key(nomor):
                print("Kontak berhasil dihapus.")
            else:
                print("Kontak tidak ditemukan.")

        elif pilihan == "4":
            kontak.display()

        elif pilihan == "5":
            print("Program selesai.")
            break

        else:
            print("Pilihan tidak valid!")


if __name__ == "__main__":
    menu()