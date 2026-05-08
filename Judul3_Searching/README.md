Judul : Program Pengecekan Stok Barang Di Toko

Deskripsi singkat :
Program Pengecekan Stok Barang di Toko merupakan program sederhana yang digunakan untuk mencari dan mengecek ketersediaan barang di dalam daftar stok toko. Program ini menerapkan metode Sequential Search atau pencarian berurutan, yaitu proses pencarian data dengan memeriksa setiap elemen pada list satu per satu dari awal hingga akhir sampai data yang dicari ditemukan. Data barang disimpan dalam sebuah list yang berisi beberapa nama barang dengan jumlah tertentu untuk menunjukkan stok yang tersedia.

Pada saat program dijalankan, pengguna akan melihat daftar barang yang tersedia di toko, kemudian diminta memasukkan nama barang yang ingin dicek. Program akan menghitung berapa kali nama barang tersebut muncul di dalam list menggunakan algoritma sequential search. Jika barang ditemukan, program akan menampilkan jumlah stok yang masih tersedia. Namun jika barang tidak ditemukan, maka program akan memberikan informasi bahwa stok barang sudah habis.

Source Code:
<img width="739" height="837" alt="Screenshot 2026-05-08 203515" src="https://github.com/user-attachments/assets/d4680e6d-ce71-40af-944a-51c2537f6134" />
<img width="753" height="297" alt="Screenshot 2026-05-08 203540" src="https://github.com/user-attachments/assets/7ce4bd01-2d40-44dc-9650-2d3a474cf15a" />

Penjelasan source code per baris:
1. Program dimulai dengan membuat fungsi pencarian bernama sequential_search yang digunakan untuk mencari data barang secara berurutan dari awal hingga akhir data.
2. Di dalam fungsi tersebut dibuat variabel i dengan nilai awal 0 sebagai penanda posisi indeks pertama pada list data barang.
3. Program membuat variabel counter dengan nilai awal 0 untuk menghitung jumlah barang yang ditemukan.
4. Program menjalankan perulangan selama indeks i masih lebih kecil dari jumlah data barang.
5. Pada setiap perulangan, program membandingkan data barang pada posisi tertentu dengan barang yang dicari oleh pengguna.
6. Jika nama barang yang dicek sama dengan barang yang dicari, maka nilai counter akan bertambah 1.
7. Setelah pengecekan selesai pada satu data, indeks i ditambah 1 agar program melanjutkan pengecekan ke data berikutnya.
8. Setelah seluruh data selesai diperiksa, fungsi akan mengembalikan jumlah barang yang ditemukan.
9. Program kemudian menjalankan fungsi utama sebagai pusat jalannya program.
10. Program membuat list yang berisi data stok barang toko seperti beras, gula, minyak, sabun, kopi, dan barang lainnya.
11. Beberapa nama barang ditulis lebih dari satu kali untuk menunjukkan jumlah stok barang yang tersedia.
12. Program menghitung jumlah seluruh data barang yang terdapat di dalam list.
13. Selanjutnya program menampilkan judul “PROGRAM PENGECEKAN STOK BARANG DI TOKO”.
14. Program menampilkan daftar barang yang tersedia agar pengguna mengetahui barang apa saja yang dapat dicari.
15. Pengguna diminta memasukkan nama barang yang ingin dicek stoknya.
16. Setelah pengguna memasukkan nama barang, program memanggil fungsi sequential search untuk melakukan pencarian.
17. Fungsi sequential search memeriksa data barang satu per satu sampai seluruh data selesai dicek.
18. Hasil pencarian disimpan dalam variabel counter yang menunjukkan jumlah stok barang ditemukan.
19. Program mengecek apakah nilai counter lebih dari 0.
20. Jika nilai counter lebih dari 0, program menampilkan pesan bahwa stok barang masih tersedia beserta jumlah stoknya.
21. Jika nilai counter sama dengan 0, program menampilkan pesan bahwa stok barang sudah habis atau tidak ditemukan.
22. Program selesai dijalankan setelah hasil pencarian ditampilkan kepada pengguna.

Output Program:
<img width="446" height="375" alt="Screenshot 2026-05-08 204435" src="https://github.com/user-attachments/assets/3562a8b0-4ca2-4bab-a8f1-57a6c89dfd7f" />

Penjelasan output dari source code:
1. Saat program dijalankan, layar akan menampilkan judul program yaitu “PROGRAM PENGECEKAN STOK BARANG DI TOKO” sebagai identitas program.
2. Setelah itu program menampilkan daftar barang yang tersedia di toko, seperti gula, beras, minyak, sabun, mie instan, kopi, teh, susu, roti, telur, dan kecap.
3. Program kemudian meminta pengguna memasukkan nama barang yang ingin dicek dengan tampilan.
4. Pengguna memasukkan nama barang sesuai dengan daftar yang tersedia, misalnya Gula.
5. Program akan melakukan proses pencarian menggunakan metode Sequential Search, yaitu memeriksa data barang satu per satu dari awal hingga akhir list.
6. Jika barang ditemukan, program akan menghitung berapa kali nama barang tersebut muncul di dalam data list. Jumlah kemunculan menunjukkan banyaknya stok barang yang tersedia.
7. Contoh output ketika pengguna memasukkan barang "Minyak".
8. Output menunjukkan bahwa barang Minyak ditemukan sebanyak 2 kali di dalam data stok.
9. Jika pengguna memasukkan nama barang yang tidak ada di dalam data, misalnya Coklat, maka program akan menampilkan "Stok barang Coklat sudah habis."
10. Output tersebut menunjukkan bahwa barang yang dicari tidak ditemukan di dalam daftar stok toko.
11. Setelah hasil pencarian ditampilkan, program selesai dijalankan.

Link YouTube : https://youtu.be/sus2m0ju7co
