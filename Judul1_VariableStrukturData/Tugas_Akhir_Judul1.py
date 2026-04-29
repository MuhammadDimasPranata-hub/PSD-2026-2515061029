#List 1D dan 2D
def list_1d():
    a = [0] * 5
    print("\nLIST 1 DIMENSI")
    for i in range(5):
        a[i] = int(input(f"Masukkan nilai a[{i}]: "))
    print("Isi array:", a)
    print("Address array:", id(a))
    for i in range(5):
        print(f"Address a[{i}]: {id(a[i])}")


def list_2d():
    b = [[0 for _ in range(2)] for _ in range(3)]
    print("\nLIST 2 DIMENSI")
    for i in range(3):
        for j in range(2):
            b[i][j] = int(input(f"Masukkan b[{i}][{j}]: "))
    print("Isi array:")
    for row in b:
        print(row)


#LINKED LIST
class Node:
    def __init__(self, data):
        self.data = data
        self.next = None


class LinkedList:
    def __init__(self):
        self.head = None

    def insert(self, data):
        new_node = Node(data)
        if self.head is None:
            self.head = new_node
        else:
            current = self.head
            while current.next:
                current = current.next
            current.next = new_node

    def delete(self):
        if self.head is None:
            print("List kosong")
        else:
            print(f"Menghapus: {self.head.data}")
            self.head = self.head.next

    def display(self):
        current = self.head
        while current:
            print(current.data, end=" -> ")
            current = current.next
        print("None")


def linked_list_menu():
    ll = LinkedList()
    print("\nLINKED LIST")

    while True:
        print("\n1. Tambah data")
        print("2. Hapus data depan")
        print("3. Tampilkan")
        print("4. Kembali")
        pilih = input("Pilih: ")

        if pilih == "1":
            data = int(input("Masukkan data: "))
            ll.insert(data)
        elif pilih == "2":
            ll.delete()
        elif pilih == "3":
            ll.display()
        elif pilih == "4":
            break
        else:
            print("Pilihan salah!")


# 3. DOUBLY LINKED LIST
class DNode:
    def __init__(self, data):
        self.data = data
        self.prev = None
        self.next = None


class DoublyLinkedList:
    def __init__(self):
        self.head = None

    def insert(self, data):
        new_node = DNode(data)
        if self.head is None:
            self.head = new_node
        else:
            current = self.head
            while current.next:
                current = current.next
            current.next = new_node
            new_node.prev = current

    def delete(self):
        if self.head is None:
            print("List kosong")
        else:
            print(f"Menghapus: {self.head.data}")
            self.head = self.head.next
            if self.head:
                self.head.prev = None

    def display_forward(self):
        current = self.head
        print("Maju: ", end="")
        while current:
            print(current.data, end=" <-> ")
            current = current.next
        print("None")

    def display_backward(self):
        current = self.head
        if current is None:
            print("List kosong")
            return

        # ke node terakhir
        while current.next:
            current = current.next

        print("Mundur: ", end="")
        while current:
            print(current.data, end=" <-> ")
            current = current.prev
        print("None")


def doubly_linked_list_menu():
    dll = DoublyLinkedList()
    print("\nDOUBLY LINKED LIST")

    while True:
        print("\n1. Tambah data")
        print("2. Hapus data depan")
        print("3. Tampilkan maju")
        print("4. Tampilkan mundur")
        print("5. Kembali")

        pilih = input("Pilih: ")

        if pilih == "1":
            data = int(input("Masukkan data: "))
            dll.insert(data)
        elif pilih == "2":
            dll.delete()
        elif pilih == "3":
            dll.display_forward()
        elif pilih == "4":
            dll.display_backward()
        elif pilih == "5":
            break
        else:
            print("Pilihan salah!")


# 4. VECTOR
class Vector:
    def __init__(self):
        self.data = []

    def push_back(self, value):
        self.data.append(value)

    def pop_back(self):
        if self.data:
            self.data.pop()

    def display(self):
        print(self.data)


def vector_menu():
    v = Vector()
    print("\nVECTOR")

    while True:
        print("\n1. Tambah data")
        print("2. Hapus data terakhir")
        print("3. Tampilkan")
        print("4. Kembali")
        pilih = input("Pilih: ")

        if pilih == "1":
            data = int(input("Masukkan data: "))
            v.push_back(data)
        elif pilih == "2":
            v.pop_back()
        elif pilih == "3":
            v.display()
        elif pilih == "4":
            break
        else:
            print("Pilihan salah!")

def main():
    while True:
        print("\nPilih Program")
        print("1. List 1D")
        print("2. List 2D")
        print("3. Linked List")
        print("4. Double Linked List")
        print("5. Vector")
        print("6. Keluar")

        pilihan = input("Pilih menu: ")

        if pilihan == "1":
            list_1d()
        elif pilihan == "2":
            list_2d()
        elif pilihan == "3":
            linked_list_menu()
        elif pilihan == "4":
            doubly_linked_list_menu()
        elif pilihan == "5":
            vector_menu()
        elif pilihan == "6":
            print("Program selesai.")
            break
        else:
            print("Pilihan tidak valid!")


if __name__ == "__main__":
    main()