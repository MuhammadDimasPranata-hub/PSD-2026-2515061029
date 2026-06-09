Judul : Sistem Manajemen Kontak Telepon

Deskripsi singkat:
Sistem Manajemen Kontak Telepon merupakan program sederhana yang digunakan
untuk mengelola data kontak menggunakan struktur data HashMap dengan metode
Open Addressing dan Linear Probing. Sistem ini menyimpan data kontak dalam
bentuk pasangan key-value, di mana nomor telepon berperan sebagai key dan nama
kontak sebagai value.

Pada saat program dijalankan, pengguna akan melihat beberapa menu seperti
menambah kontak, mencari kontak, menghapus kontak, dan menampilkan seluruh
kontak yang tersimpan. Sistem memanfaatkan fungsi hash untuk menentukan lokasi
penyimpanan data pada hash table. Jika terjadi collision (tabrakan hash), sistem akan
menggunakan metode Linear Probing untuk mencari slot kosong berikutnya.

Source Code:
<img width="1040" height="862" alt="Screenshot 2026-06-09 184518" src="https://github.com/user-attachments/assets/93ffd56a-5239-4f20-848b-be8cc25d37d9" />
<img width="1046" height="815" alt="Screenshot 2026-06-09 184554" src="https://github.com/user-attachments/assets/c981be9f-b9cb-45a5-b4b9-d98dc5982593" />
<img width="1039" height="801" alt="Screenshot 2026-06-09 184624" src="https://github.com/user-attachments/assets/595f62b9-a7e2-4ecb-93af-d1b19b3e0804" />
<img width="1047" height="802" alt="Screenshot 2026-06-09 184650" src="https://github.com/user-attachments/assets/ecdb2596-e775-4895-9c36-e5bbbb0ebbde" />
<img width="1043" height="252" alt="Screenshot 2026-06-09 184716" src="https://github.com/user-attachments/assets/d3023dee-5bfb-4d19-b092-8d04925bc01f" />

Penjelasan source code per baris:
1. Program dimulai dengan membuat class SlotState untuk mendefinisikan status setiap slot pada hash table.
2. Status EMPTY menunjukkan slot kosong.
3. Status OCCUPIED menunjukkan slot berisi data.
4. Status DELETED menunjukkan data telah dihapus tetapi slot masih digunakan dalam proses pencarian.
5. Class Entry digunakan untuk menyimpan pasangan key dan value.
6. Variabel key digunakan untuk menyimpan nomor telepon.
7. Variabel value digunakan untuk menyimpan nama kontak.
8. Variabel state digunakan untuk menyimpan status slot.
9. Class HashMapOpenAddressing digunakan untuk mengimplementasikan struktur data HashMap.
10. Method __init__() digunakan untuk menentukan ukuran hash table dan membuat array penyimpanan data.
11. Variabel SIZE menyimpan kapasitas maksimum hash table.
12. Variabel table digunakan sebagai tempat penyimpanan seluruh data kontak.
13. Method hash_function() digunakan untuk menghasilkan indeks hash berdasarkan nomor telepon.
14. Method insert() digunakan untuk menambahkan kontak baru ke dalam hash table.
15. Program menghitung indeks awal menggunakan fungsi hash.
16. Program melakukan pengecekan apakah slot yang dituju kosong atau telah terisi.
17. Jika terjadi collision, sistem menggunakan Linear Probing untuk mencari slot kosong berikutnya.
18. Jika key yang sama ditemukan, value akan diperbarui.
19. Data kontak disimpan pada slot yang tersedia.
20. Method search() digunakan untuk mencari data kontak berdasarkan nomor telepon.
21. Program melakukan proses probing hingga data ditemukan atau slot kosong ditemukan.
22. Jika kontak ditemukan, method akan mengembalikan objek kontak tersebut.
23. Method remove_key() digunakan untuk menghapus kontak berdasarkan nomor telepon.
24. Data yang dihapus tidak langsung dikosongkan tetapi diberi status DELETED.
25. Method display() digunakan untuk menampilkan seluruh kontak yang tersimpan.
26. Program melakukan perulangan pada seluruh isi hash table.
27. Kontak yang berstatus OCCUPIED akan ditampilkan ke layar.
28. Fungsi menu() digunakan sebagai pusat jalannya program.
29. Program membuat objek HashMap untuk menyimpan data kontak.
30. Program menampilkan menu utama kepada pengguna.
31. Pengguna dapat memilih menu tambah kontak, cari kontak, hapus kontak, tampilkan kontak, atau keluar.
32. Program menggunakan percabangan if-elif untuk menjalankan menu yang dipilih.
33. Jika pengguna memilih tambah kontak, program meminta nomor telepon dan nama kontak.
34. Jika pengguna memilih cari kontak, program meminta nomor telepon yang ingin dicari.
35. Jika pengguna memilih hapus kontak, program meminta nomor telepon yang akan dihapus.
36. Jika pengguna memilih tampilkan semua kontak, program menampilkan seluruh data kontak yang tersimpan.
37. Program berhenti ketika pengguna memilih menu keluar.

Output Program:
<img width="1095" height="720" alt="Screenshot 2026-06-09 184750" src="https://github.com/user-attachments/assets/42ccefa9-591e-4728-b3e9-e5b8eb980ea5" />
<img width="1091" height="845" alt="Screenshot 2026-06-09 184814" src="https://github.com/user-attachments/assets/054cfd68-2853-49ac-9663-5444fe37c22b" />
<img width="1098" height="182" alt="Screenshot 2026-06-09 184839" src="https://github.com/user-attachments/assets/fbfd6388-eee0-452c-8840-c3bf55a91aab" />

Penjelasan Outout Program:
1. Saat program dijalankan, sistem menampilkan menu utama "SISTEM MANAJEMEN KONTAK TELEPON".
2. Pengguna memilih menu "Tambah Kontak".
3. Program meminta nomor telepon dan nama kontak.
4. Pengguna memasukkan nomor telepon dan nama kontak.
5. Data kontak berhasil disimpan ke dalam HashMap.
6. Pengguna kembali menambahkan beberapa 2 kontak.
7. Setiap kontak disimpan menggunakan nomor telepon sebagai key dan nama kontak sebagai value.
8. Jika terjadi collision pada hash table, sistem akan menggunakan Linear Probing untuk mencari slot kosong berikutnya.
9. Pengguna kemudian memilih menu "Cari Kontak".
10. Program meminta nomor telepon yang ingin dicari.
11. Sistem melakukan proses pencarian pada hash table.
12. Jika data ditemukan, program menampilkan nomor telepon dan nama kontak yang sesuai.
13. Selanjutnya pengguna memilih menu "Hapus Kontak".
14. Program meminta nomor telepon yang akan dihapus.
15. Kontak yang ditemukan akan diberi status DELETED sehingga tidak lagi dianggap sebagai data aktif.
16. Pengguna memilih menu "Tampilkan Semua Kontak".
17. Program menampilkan seluruh kontak yang masih tersimpan dalam hash table.
18. Kontak yang telah dihapus tidak akan ditampilkan.
19. Hal ini menunjukkan bahwa operasi insert, search, delete, dan display pada HashMap berjalan dengan baik.
20. Terakhir pengguna memilih menu "Keluar".
21. Program menampilkan pesan "Program selesai." yang menandakan bahwa program telah berhenti dijalankan.

Link Youtube : https://youtu.be/7IgSOrqPkL8
