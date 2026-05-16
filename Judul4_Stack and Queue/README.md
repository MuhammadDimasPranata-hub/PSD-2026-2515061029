Judul : Sistem Pengelolaan Tumpukan Buku

Deskripsi singkat :
Sistem Pengelolaan Tumpukan Buku merupakan program sederhana yang digunakan untuk mengelola 
data buku menggunakan struktur data Stack berbasis Array. Sistem ini menerapkan konsep LIFO (Last In 
First Out), yaitu data buku yang terakhir dimasukkan akan menjadi data pertama yang diambil. Data buku 
disimpan dalam sebuah array/list dengan indeks teratas (top) sebagai penanda posisi buku paling 
atas pada tumpukan.

Pada saat program sistem dijalankan, pengguna akan melihat beberapa menu seperti menambah buku, mengambil 
buku, melihat buku teratas, dan menampilkan seluruh tumpukan buku. Sistem akan memproses data 
menggunakan operasi stack seperti push, pop, dan peek. Jika pengguna menambahkan buku, maka buku 
akan ditempatkan di posisi paling atas. Jika pengguna mengambil buku, maka buku paling atas akan 
dihapus terlebih dahulu. Program juga dapat menampilkan seluruh isi tumpukan buku dari atas ke bawah.

Source Code:

<img width="657" height="840" alt="Screenshot 2026-05-16 210933" src="https://github.com/user-attachments/assets/70a37787-3541-4e65-8f42-ac75a27e5d47" />

<img width="559" height="210" alt="Screenshot 2026-05-16 210959" src="https://github.com/user-attachments/assets/8fe24959-df50-4275-9737-d9cf798a02ff" />

<img width="511" height="796" alt="Screenshot 2026-05-16 211016" src="https://github.com/user-attachments/assets/5b8658a3-b37c-4816-86ab-0a182a827f09" />
____________________________________________________
<img width="416" height="154" alt="Screenshot 2026-05-16 211031" src="https://github.com/user-attachments/assets/d4310214-5592-46bb-8154-91f156d0ae66" />

Penjelasan source code per baris:
1. Program dimulai dengan membuat class bernama StackBuku untuk mengelola tumpukan buku menggunakan struktur data stack.
2. Method __init__ digunakan untuk menginisialisasi ukuran maksimum stack, array penyimpanan data, dan indeks top.
3. Variabel MAX digunakan untuk menentukan kapasitas maksimal tumpukan buku.
4. Variabel st digunakan sebagai list/array penyimpanan data buku.
5. Variabel top_idx digunakan untuk menandai posisi buku paling atas pada stack.
6. Method is_empty() digunakan untuk mengecek apakah stack kosong.
7. Method is_full() digunakan untuk mengecek apakah stack penuh.
8. Method tambah_buku() digunakan untuk menambahkan buku ke dalam stack.
9. Program akan mengecek terlebih dahulu apakah stack penuh.
10. Jika stack belum penuh, indeks top akan bertambah satu.
11. Judul buku akan disimpan pada posisi top terbaru.
12. Program menampilkan pesan bahwa buku berhasil ditambahkan.
13. Method ambil_buku() digunakan untuk mengambil buku paling atas dari stack.
14. Program mengecek apakah stack kosong.
15. Jika stack tidak kosong, buku paling atas akan ditampilkan sebagai buku yang diambil.
16. Setelah itu indeks top dikurangi satu untuk menghapus buku teratas.
17. Method lihat_buku_teratas() digunakan untuk melihat buku yang berada di posisi paling atas.
18. Program akan menampilkan judul buku paling atas tanpa menghapusnya.
19. Method tampilkan_buku() digunakan untuk menampilkan seluruh isi stack.
20. Program menggunakan perulangan dari indeks top sampai indeks pertama.
21. Buku ditampilkan dari atas ke bawah sesuai konsep stack.
22. Fungsi main() digunakan sebagai pusat jalannya program.
23. Program membuat objek stack dari class StackBuku.
24. Program menampilkan menu pilihan kepada pengguna.
25. Pengguna dapat memilih menu tambah buku, ambil buku, melihat buku teratas, menampilkan semua buku, atau keluar.
26. Program menggunakan percabangan if-elif untuk menjalankan menu yang dipilih pengguna.
27. Jika pengguna memilih tambah buku, program meminta input judul buku.
28. Jika pengguna memilih ambil buku, program menjalankan method ambil_buku().
29. Jika pengguna memilih lihat buku teratas, program menjalankan method lihat_buku_teratas().
30. Jika pengguna memilih tampilkan semua buku, program menjalankan method tampilkan_buku().
31. Program akan berhenti ketika pengguna memilih menu keluar.

Output Program:

<img width="405" height="846" alt="Screenshot 2026-05-16 212102" src="https://github.com/user-attachments/assets/b0a570d2-1b33-4da0-84bb-f721b6dd6156" />
_______________________________________________
<img width="360" height="645" alt="Screenshot 2026-05-16 212201" src="https://github.com/user-attachments/assets/b8c245d6-fd94-4a19-8559-52fe1da78489" />

Penjelasan Output Program:
1. Saat program dijalankan, layar menampilkan menu utama "SISTEM PENGELOLAAN TUMPUKAN BUKU" 
   yang berisi beberapa pilihan menu seperti tambah buku, ambil buku, melihat buku teratas, menampilkan semua buku, dan keluar program.
2. Pengguna pertama kali memilih menu "Tambah Buku" kemudian memasukkan judul buku "Amalan Sholat".
3. Program menjalankan proses push pada stack sehingga buku “Amalan Sholat” berhasil dimasukkan ke dalam tumpukan buku dan menjadi buku paling atas.
4. Setelah itu pengguna kembali memilih menu tambah buku dan memasukkan judul buku "Tips Hemat".
5. Buku “Tips Hemat” berhasil ditambahkan ke dalam stack dan berada di atas buku "Amalan Sholat".
6. Pengguna kembali memilih menu tambah buku dan memasukkan judul buku "Rajin Menabung"
7. Program menambahkan buku “Rajin Menabung” ke posisi paling atas stack karena struktur data stack menggunakan konsep LIFO (Last In First Out).
8. Selanjutnya pengguna memilih menu "Ambil Buku".
9. Program mengambil buku yang berada di posisi paling atas yaitu "Rajin Menabung" karena buku tersebut adalah data terakhir yang dimasukkan ke dalam stack.
10. Setelah buku "Rajin Menabung" diambil, posisi buku paling atas berubah menjadi "Tips Hemat".
11. Pengguna kemudian memilih menu "Lihat Buku Teratas".
12. Program menampilkan buku teratas saat ini yaitu "Tips Hemat" tanpa menghapusnya dari dalam stack.
13. Setelah itu pengguna memilih menu "Tampilkan Semua Buku".
14. Program menampilkan seluruh isi tumpukan buku dari atas ke bawah sesuai urutan stack.
15. Output menunjukkan bahwa buku "Tips Hemat" berada di posisi paling atas dan buku "Amalan Sholat" berada di bawahnya.
16. Hal tersebut menunjukkan bahwa stack bekerja menggunakan konsep LIFO, di mana data terakhir yang masuk akan menjadi data pertama yang keluar.
17. Terakhir pengguna memilih menu "Keluar"
18. Program menampilkan pesan "Program selesai." yang menandakan bahwa program telah berhenti dijalankan.

Link Youtube: https://youtu.be/O4SnBQPzuLQ
