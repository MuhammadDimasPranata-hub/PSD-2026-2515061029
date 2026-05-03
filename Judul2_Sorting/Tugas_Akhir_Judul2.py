def insertion_sort(arr, n):
    for i in range(1, n):
        temp = arr[i]
        j = i - 1
        while j >= 0 and arr[j][1] > temp[1]:
            arr[j + 1] = arr[j]
            j -= 1
        arr[j + 1] = temp


def main():
    try:
        n = int(input("Masukkan jumlah mahasiswa: "))
    except ValueError:
        print("Input tidak valid!")
        return

    arr = []
    print("\nMasukkan nama dan waktu penggunaan HP (jam):")

    for i in range(n):
        nama = str(input(f"Nama mahasiswa ke-{i+1}: "))
        while True:
            try:
                waktu = float(input("Waktu penggunaan HP (jam): "))
                arr.append([nama, waktu])
                break
            except ValueError:
                print("Input tidak valid, masukkan angka!")

    print("\nData sebelum diurutkan:")
    for d in arr:
        print(f"{d[0]} - {d[1]} jam")

    insertion_sort(arr, n)

    print("\nData setelah diurutkan (terkecil ke terbesar):")
    for d in arr:
        print(f"{d[0]} - {d[1]} jam")


if __name__ == "__main__":
    main()