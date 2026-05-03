Judul : Pengurutan Waktu Penggunaan HP Mahasiswa

Deskripsi singkat :
Sistem ini merupakan program sederhana yang digunakan untuk mengurutkan data mahasiswa berdasarkan waktu penggunaan HP (dalam jam). Data yang dimasukkan terdiri dari nama mahasiswa dan lama waktu penggunaan HP, lalu disimpan dalam bentuk list dua dimensi. Program kemudian menampilkan data sebelum diurutkan, sehingga pengguna dapat melihat kondisi awal data yang dimasukkan.

Proses pengurutan dilakukan menggunakan metode Insertion Sort, yaitu dengan membandingkan setiap data dan menyisipkannya ke posisi yang tepat berdasarkan nilai waktu penggunaan HP. Hasil akhirnya adalah data yang sudah terurut dari waktu terkecil ke terbesar atau bisa disebut Ascending. Sistem ini bermanfaat untuk mengetahui pola penggunaan HP mahasiswa dan dapat digunakan sebagai bahan evaluasi kebiasaan sehari-hari.

Source Code:
<img width="460" height="202" alt="Screenshot 2026-05-03 205058" src="https://github.com/user-attachments/assets/0cbeec58-7d48-4189-992b-63a2d1dcc651" />
Baris 1: Fungsi ini digunakan untuk mengurutkan data mahasiswa berdasarkan waktu penggunaan HP (jam) menggunakan metode Insertion Sort.
Baris 2: Perulangan mulai dari elemen ke-2 atau index 1, karena elemen pertama dianggap sudah terurut.
Baris 3: Menyimpan 1 data mahasiswa (nama + waktu)
Baris 4: variabel j menunjuk ke elemen sebelumnya
Baris 5: Selama J maasih dalam batas array dan waktu sebelumnya lebih besar dari waktu sekarang.
Baris 6: Data yang lebih besar digeser ke kanan.
Baris 7: J mundur ke kiri.
Baris 8: Data disisipkan ke posisi yang benar.

<img width="533" height="144" alt="Screenshot 2026-05-03 205856" src="https://github.com/user-attachments/assets/400cb0e2-9ee3-4b98-a359-600798809d19" />
Baris 1: Fungsi utama untuk menjalankan program.
Baris 2: Menjalankan "try"
Baris 3: Meminta user memasukkan jumlah mahasiswa.
Baris 4: Jika error.
Baris 5: Sistem akan menampilkan "Input tidak valid!".
Baris 6: Fungsi akan menampilkan hasil dan berhenti.

<img width="624" height="532" alt="Screenshot 2026-05-03 213807" src="https://github.com/user-attachments/assets/2424ef9d-71c5-4838-8081-624c395436d7" />
Baris 1: Untuk menyimpan data mahasiswa.
Baris 2: menampilkan "Masukkan nama dan waktu penggunaan HP (jam)"
Baris 3: Loop sebanyak jumlah mahasiswa.
Baris 4: Meminta user menulis nama mahasiswa dan menambahkannya ke varibel nama.
Baris 5: Loop agar input tidak salah.
Baris 7: Input angka desimal (misalnya 2.5 jam).
Baris 8: Data disimpan dalam bentuk (Nama, waktu).
Baris 9: Loop berhenti.
Baris 10: Jika error.
Baris 11: sistem akan menampilkan "Input tidak valid, masukkan angka!" lalu meminta memasukkan ulang.
Baris 13: Mencetak "Data sebelum diurutkan:".
Baris 14: Loop sebanyak data yang disimpan.
Baris 15: Menampilkan data yang disimpan sebelum di urut.
Baris 16: Memanggil fungsi insertion_sort untuk mengurutkan data yang sudah disimpan.
Baris 17: Menampilkan "Data setelah diurutkan (terkecil ke terbesar):".
Baris 18: Loop sebanyak data yang disimpan.
Baris 19: Menampilkan data yang disimpan setelah di urut.

<img width="261" height="55" alt="Screenshot 2026-05-03 222152" src="https://github.com/user-attachments/assets/e755b275-fddf-4645-b1c9-b95aa10c5bca" />
Program hanya berjalan jika file dijalankan langsung.

Output Program:
<img width="428" height="595" alt="Screenshot 2026-05-03 225740" src="https://github.com/user-attachments/assets/3699ccea-499b-4e60-b115-86925b165be1" />
Penjelasan Output:
Pada bagian awal, program meminta input jumlah mahasiswa dan user menginput sebanyak 5 orang, lalu setelah itu pengguna diminta memasukkan nama dan waktu penggunaan HP masing-masing mahasiswa.
Data yang dimasukkan oleh pengguna adalah:
* Nina: 3 jam
* Abi: 6 jam
* Lala: 5 jam
* Dian: 4 jam
* Ami: 2 jam
Data ini kemudian disimpan dalam bentuk list.

Selanjutnya, program menampilkan data sebelum diurutkan sesuai dengan urutan input.
Setelah itu, program menjalankan algoritma Insertion Sort untuk mengurutkan data berdasarkan waktu penggunaan HP dari yang terkecil ke terbesar dan terakhir program menampilkan hasil data yang telah diurutkan.

Link Youtube : https://youtu.be/6RTEUJqsVh4
