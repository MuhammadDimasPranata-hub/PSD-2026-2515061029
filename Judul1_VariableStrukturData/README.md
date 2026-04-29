Judul Program : Program Pengenalan Variabel Struktur Data
Penjelasan : Program dengan judul “Program Pengenalan Variabel Struktur Data” bertujuan untuk memperkenalkan konsep dasar penggunaan variabel dalam berbagai bentuk struktur data pada pemrograman, khususnya menggunakan bahasa Python. Dalam program ini, pengguna akan memahami bagaimana data dapat disimpan, diolah, dan diakses melalui struktur seperti list satu dimensi (1D) dan dua dimensi (2D). Selain itu, program juga biasanya melibatkan proses input data dari pengguna, penyimpanan ke dalam variabel, serta penampilan kembali data tersebut sebagai output.

Melalui program ini, pengguna dapat mempelajari cara kerja memori sederhana, seperti bagaimana alamat suatu variabel dapat diketahui dan bagaimana setiap elemen dalam struktur data memiliki posisi atau indeks tertentu. Hal ini sangat penting sebagai dasar dalam pemrograman karena struktur data digunakan hampir di semua aplikasi, mulai dari pengolahan data sederhana hingga sistem yang lebih kompleks. Dengan memahami konsep ini, pengguna akan lebih siap untuk mempelajari materi lanjutan seperti array, linked list, maupun struktur data lainnya.

<img width="657" height="521" alt="Screenshot 2026-04-29 192023" src="https://github.com/user-attachments/assets/8e80d37b-31cf-4c61-a33e-19eb388aa289" />
<img width="567" height="810" alt="Screenshot 2026-04-29 192052" src="https://github.com/user-attachments/assets/58c5bc66-19a1-4f27-9837-e05fe36614c3" />
<img width="542" height="550" alt="Screenshot 2026-04-29 192113" src="https://github.com/user-attachments/assets/51a348be-582d-4840-a07e-1e418aa11971" />
<img width="549" height="741" alt="Screenshot 2026-04-29 192159" src="https://github.com/user-attachments/assets/fd4bc483-9649-4ab4-ac01-e3dfcae0f935" />
<img width="528" height="556" alt="Screenshot 2026-04-29 192219" src="https://github.com/user-attachments/assets/fd15df19-fab0-4e8a-bea5-857085439279" />
<img width="549" height="639" alt="Screenshot 2026-04-29 192234" src="https://github.com/user-attachments/assets/81064e21-eb69-447f-a293-b27b8f1a78a1" />
<img width="474" height="629" alt="Screenshot 2026-04-29 192301" src="https://github.com/user-attachments/assets/13ada234-5af7-4a9f-abc0-116905fd19ef" />
<img width="541" height="272" alt="Screenshot 2026-04-29 192324" src="https://github.com/user-attachments/assets/adf5d3c2-167d-4809-8758-10bdbba26b17" />
<img width="495" height="744" alt="Screenshot 2026-04-29 192351" src="https://github.com/user-attachments/assets/efe24b79-7e52-4fd9-9844-5dfeee915cfa" />

Penjelasan logika program per baris :
LIST 1 DIMENSI :
1. Mendefinisikan fungsi untuk menjalankan operasi list 1 dimensi.
2. Membuat sebuah list dengan 5 elemen awal bernilai 0.
3. Menampilkan judul bagian list 1 dimensi.
4. Melakukan perulangan sebanyak 5 kali untuk mengisi setiap indeks.
5. Meminta pengguna memasukkan nilai, lalu menyimpannya ke dalam list sesuai indeks.
6. Menampilkan seluruh isi list setelah diinput.
7. Menampilkan alamat memori dari list tersebut.
8. Melakukan perulangan kembali untuk menampilkan alamat memori tiap elemen dalam list.

LIST 2 DIMENSI :
1. Mendefinisikan fungsi untuk list dua dimensi.
2. Membuat list 2 dimensi berukuran 3 baris dan 2 kolom dengan nilai awal 0.
3. Menampilkan judul bagian list 2 dimensi.
4. Melakukan perulangan untuk setiap baris.
5. Melakukan perulangan lagi untuk setiap kolom di dalam baris.
6. Meminta input dari pengguna untuk setiap posisi array 2D.
7. Menampilkan isi array dalam bentuk per baris.

LINKED LIST :
*Node
1. Mendefinisikan class Node sebagai elemen dasar linked list.
2. Menginisialisasi node dengan data.
3. Mengatur pointer next sebagai kosong (None).
*LinkedList
5. Mendefinisikan class LinkedList.
6. Menginisialisasi head sebagai None (list kosong).
*Insert
1. Mendefinisikan fungsi untuk menambah data ke linked list.
2. Membuat node baru dari data yang diberikan.
3. Mengecek apakah list masih kosong.
4. Jika kosong, node baru dijadikan head.
5. Jika tidak kosong, mulai dari head untuk mencari node terakhir.
6. Melakukan perulangan sampai node terakhir ditemukan.
7. Menghubungkan node terakhir dengan node baru.
*Delete
1. Mengecek apakah list kosong.
2. Jika kosong, menampilkan pesan.
3. Jika tidak kosong, menampilkan data yang akan dihapus.
4. Menggeser head ke node berikutnya (menghapus node pertama).
*Display
1. Memulai dari head.
2. Melakukan perulangan selama masih ada node.
3. Menampilkan data setiap node dengan tanda panah.
4. Berpindah ke node berikutnya.
5. Menampilkan penanda akhir list.
*Menu Linked List
1. Membuat objek linked list.
2. Menampilkan menu pilihan secara berulang.
3. Membaca input pilihan pengguna.
4. Jika memilih tambah, meminta input lalu menambahkan data.
5. Jika memilih hapus, menghapus node pertama.
6. Jika memilih tampilkan, menampilkan isi list.
7. Jika memilih kembali, keluar dari menu.
8. Jika input salah, menampilkan pesan error.

DOUBLY LINKED LIST :
*DNode
1. Mendefinisikan node dengan data.
2. Menyimpan pointer ke node sebelumnya.
3. Menyimpan pointer ke node berikutnya.
*DoublyLinkedList
1. Mendefinisikan class doubly linked list.
2. Menginisialisasi head sebagai kosong.
*Insert
1. Membuat node baru.
2. Jika list kosong, node menjadi head.
3. Jika tidak kosong, mencari node terakhir.
4. Menghubungkan node terakhir dengan node baru.
5. Mengatur pointer sebelumnya dari node baru.
*Delete
1. Mengecek apakah list kosong.
2. Jika kosong, menampilkan pesan.
3. Jika tidak kosong, menampilkan data yang dihapus.
4. Menggeser head ke node berikutnya.
5. Jika masih ada node, menghapus hubungan ke node sebelumnya.
*Display Forward
1. Memulai dari head.
2. Menampilkan data dari depan ke belakang.
3. Berpindah ke node berikutnya sampai habis.
*Display Backward
1. Mengecek apakah list kosong.
2. Jika kosong, menampilkan pesan.
3. Jika tidak kosong, mencari node terakhir.
4. Menampilkan data dari belakang ke depan.
5. Berpindah ke node sebelumnya sampai habis.
*Menu Doubly Linked List
1. Membuat objek doubly linked list.
2. Menampilkan menu pilihan.
3. Membaca input pengguna.
4. Menjalankan fungsi sesuai pilihan (tambah, hapus, tampil maju/mundur, keluar).
5. Menampilkan pesan jika input salah.

VECTOR :
1. Mendefinisikan class vector.
2. Menginisialisasi list kosong sebagai penyimpanan data.
*push_back
1. Menambahkan data ke akhir list.
*pop_back
1. Mengecek apakah list tidak kosong.
2. Menghapus elemen terakhir.
*display
1. Menampilkan seluruh isi vector.
*Menu Vector
1. Membuat objek vector.
2. Menampilkan menu pilihan.
3. Membaca input pengguna.
4. Jika pilih tambah, menambahkan data.
5. Jika pilih hapus, menghapus data terakhir.
6. Jika pilih tampil, menampilkan isi.
7. Jika pilih kembali, keluar dari menu.
8. Jika salah, menampilkan pesan error.

MAIN PROGRAM :
1. Mendefinisikan fungsi utama.
2. Menjalankan perulangan menu utama.
3. Menampilkan semua pilihan program (list, linked list, vector).
4. Membaca input pengguna.
5. Menjalankan fungsi sesuai pilihan.
6. Jika memilih keluar, menghentikan program.
7. Jika input tidak valid, menampilkan pesan kesalahan.

ENTRY POINT :
1. Mengecek apakah file dijalankan langsung.
2. Jika iya, maka menjalankan fungsi utama.

Output Program :
<img width="252" height="623" alt="Screenshot 2026-04-29 200945" src="https://github.com/user-attachments/assets/4e27fec1-637f-4d7b-8ba9-40d718808b44" />
<img width="237" height="304" alt="Screenshot 2026-04-29 200932" src="https://github.com/user-attachments/assets/61510709-be2b-4a78-bd52-6bdb3bfae339" />
<img width="235" height="702" alt="Screenshot 2026-04-29 200918" src="https://github.com/user-attachments/assets/3fb9199d-d821-48d0-9fdf-3b5ede5d3402" />
<img width="415" height="677" alt="Screenshot 2026-04-29 200903" src="https://github.com/user-attachments/assets/1fff4054-9bb9-4b2e-8cea-42fada30ffb9" />
<img width="200" height="522" alt="Screenshot 2026-04-29 200849" src="https://github.com/user-attachments/assets/d6b6080a-3ca5-4f7c-bbd0-bffef215ebe0" />
<img width="211" height="762" alt="Screenshot 2026-04-29 200838" src="https://github.com/user-attachments/assets/353a1fab-53f7-4c9d-8520-27e0e608f549" />
<img width="216" height="429" alt="Screenshot 2026-04-29 200826" src="https://github.com/user-attachments/assets/fbda03e1-a4d9-4faa-a3e3-0ce18a4af839" />
<img width="196" height="148" alt="Screenshot 2026-04-29 200817" src="https://github.com/user-attachments/assets/c303099a-45a3-46de-a97e-9015ab27f928" />
<img width="213" height="697" alt="Screenshot 2026-04-29 200802" src="https://github.com/user-attachments/assets/a2d67ffd-d0b2-46f6-b705-5e59209f5439" />
<img width="203" height="452" alt="Screenshot 2026-04-29 200748" src="https://github.com/user-attachments/assets/93a81350-ce9c-4663-be71-c26a76a87487" />
<img width="278" height="294" alt="Screenshot 2026-04-29 200731" src="https://github.com/user-attachments/assets/37d9f2cb-0c68-4280-8955-4f2cefb781e1" />
<img width="212" height="189" alt="Screenshot 2026-04-29 200724" src="https://github.com/user-attachments/assets/dfd1ae9a-3533-4c3d-9687-92d5bde7a8f5" />

Penjelasan Output :
1. Tampilan Menu Utama
Saat program dijalankan, pengguna akan melihat menu pilihan berisi beberapa jenis struktur data:
List 1 Dimensi, List 2 Dimensi, Linked List, Doubly Linked List, Vector, dan Keluar.
Pengguna diminta memasukkan angka sesuai menu. Jika input tidak sesuai, program akan menampilkan pesan bahwa pilihan tidak valid.

2. Output List 1 Dimensi
Program meminta pengguna memasukkan 5 buah nilai.
Setelah semua nilai diinput:
* Program menampilkan isi array dalam bentuk list.
* Menampilkan alamat memori dari array tersebut.
* Menampilkan alamat memori masing-masing elemen dalam array.
Tujuannya adalah untuk menunjukkan bagaimana data disimpan di memori.

3. Output List 2 Dimensi
Program meminta pengguna mengisi data dalam bentuk tabel (3 baris dan 2 kolom).
Setelah semua data dimasukkan:
* Program menampilkan isi array dalam bentuk baris per baris.
* Setiap baris berisi 2 nilai.
Ini menggambarkan struktur data matriks sederhana.

4. Output Linked List
Program menampilkan menu operasi Linked List:
* Tambah data
* Hapus data depan
* Tampilkan data
* Kembali
Penjelasan output:
* Saat menambah data, nilai akan dimasukkan ke akhir list.
* Saat menghapus, data paling depan akan dihapus dan ditampilkan.
* Saat ditampilkan, data akan terlihat berurutan dengan tanda panah (→) dan diakhiri dengan “None”.
* Jika list kosong dan dilakukan penghapusan, akan muncul pesan bahwa list kosong.

5. Output Doubly Linked List
Program menampilkan menu:
* Tambah data
* Hapus data depan
* Tampilkan maju
* Tampilkan mundur
* Kembali
Penjelasan output:
* Data yang ditambahkan akan tersusun berurutan.
* Tampilkan maju akan menampilkan data dari depan ke belakang menggunakan simbol dua arah (<->).
* Tampilkan mundur akan menampilkan data dari belakang ke depan.
* Jika list kosong, akan muncul pesan bahwa list kosong.

6. Output Vector
Program menyediakan menu:
* Tambah data
* Hapus data terakhir
* Tampilkan data
* Kembali
Penjelasan output:
* Data yang ditambahkan akan disimpan dalam vector.
* Jika data dihapus, elemen terakhir akan dihilangkan.
* Saat ditampilkan, data akan muncul dalam bentuk list.

7. Keluar Program
Jika pengguna memilih keluar:
* Program akan menampilkan pesan bahwa program selesai
* Kemudian program berhenti.

Link Youtube : 
