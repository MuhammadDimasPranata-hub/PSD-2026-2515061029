Judul : Sistem Pencarian Data Akademik Berdasarkan NPM

Deskripsi singkat:
Sistem Pencarian Data Akademik Berdasarkan NPM merupakan program sederhana yang digunakan untuk
mengelola dan mencari data mahasiswa menggunakan struktur data Binary Search Tree (BST). Sistem ini
menyimpan data mahasiswa seperti NPM, nama, tanggal lahir, dan program studi ke dalam node-node yang
tersusun secara terurut berdasarkan NPM.

Pada saat program dijalankan, pengguna dapat menambahkan data mahasiswa, mencari data mahasiswa
berdasarkan NPM, dan menampilkan seluruh data mahasiswa. Struktur Binary Search Tree memungkinkan
proses pencarian data menjadi lebih cepat karena data disusun secara terurut. Jika NPM yang dicari lebih
kecil dari node saat ini maka pencarian bergerak ke kiri, sedangkan jika lebih besar maka pencarian bergerak ke kanan.

Source Code:
<img width="842" height="883" alt="Screenshot 2026-05-22 223849" src="https://github.com/user-attachments/assets/efbea399-ab6c-4526-98b3-02db69d62cd5" />
<img width="793" height="442" alt="Screenshot 2026-05-22 224004" src="https://github.com/user-attachments/assets/06c1e175-62a5-4f18-be75-932658e6570d" />
<img width="666" height="864" alt="Screenshot 2026-05-22 224045" src="https://github.com/user-attachments/assets/b1bffa14-b606-4059-ab40-3410f5dabb18" />
<img width="677" height="602" alt="Screenshot 2026-05-22 224321" src="https://github.com/user-attachments/assets/570b83a5-66f4-4d27-ae3f-62f88ede1702" />

Penjelasan source code per baris:
1. Program dimulai dengan membuat class Node untuk menyimpan data mahasiswa.
2. Method __init__ digunakan sebagai constructor pada class Node.
3. Variabel npm digunakan untuk menyimpan NPM mahasiswa.
4. Variabel nama digunakan untuk menyimpan nama mahasiswa.
5. Variabel tanggal_lahir digunakan untuk menyimpan tanggal lahir mahasiswa.
6. Variabel prodi digunakan untuk menyimpan program studi mahasiswa.
7. Variabel left digunakan untuk menunjuk child kiri pada BST.
8. Variabel right digunakan untuk menunjuk child kanan pada BST.
9. Program membuat class BSTAkademik untuk mengelola Binary Search Tree.
10. Method __init__ pada class BST digunakan untuk menginisialisasi root BST.
11. Variabel root diatur bernilai None karena BST masih kosong.
12. Method insert_node() digunakan untuk menambahkan data mahasiswa ke dalam BST.
13. Parameter root digunakan sebagai node saat ini yang sedang diperiksa.
14. Parameter npm, nama, tanggal_lahir, dan prodi digunakan sebagai data mahasiswa yang akan dimasukkan.
15. Program mengecek apakah node saat ini kosong.
16. Jika kosong maka program membuat node baru menggunakan class Node.
17. Program membandingkan NPM baru dengan NPM pada root.
18. Jika NPM lebih kecil maka data dimasukkan ke subtree kiri.
19. Program memanggil method insert_node() secara rekursif ke child kiri.
20. Jika NPM lebih besar maka data dimasukkan ke subtree kanan.
21. Program memanggil method insert_node() secara rekursif ke child kanan.
22. Method mengembalikan node root setelah proses insert selesai.
23. Method insert() digunakan untuk mempermudah pemanggilan proses insert.
24. Root BST diperbarui dengan hasil method insert_node().
25. Method search_node() digunakan untuk mencari data mahasiswa berdasarkan NPM.
26. Program mengecek apakah node saat ini kosong.
27. Jika kosong maka data tidak ditemukan dan method mengembalikan None.
28. Program mengecek apakah NPM pada root sama dengan NPM yang dicari.
29. Jika sama maka node mahasiswa ditemukan dan dikembalikan.
30. Jika NPM lebih kecil maka pencarian dilanjutkan ke subtree kiri.
31. Program memanggil method search_node() secara rekursif ke child kiri.
32. Jika NPM lebih besar maka pencarian dilanjutkan ke subtree kanan.
33. Program memanggil method search_node() secara rekursif ke child kanan.
34. Method search() digunakan untuk memanggil proses pencarian data.
35. Method search() mengembalikan hasil dari search_node().
36. Method inorder() digunakan untuk menampilkan seluruh data mahasiswa secara terurut.
37. Program mengecek apakah root tidak kosong.
38. Program terlebih dahulu menampilkan subtree kiri.
39. Program menampilkan data mahasiswa pada node saat ini.
40. Data yang ditampilkan meliputi NPM, nama, tanggal lahir, dan program studi.
41. Garis pemisah digunakan agar tampilan data lebih rapi.
42. Setelah itu program menampilkan subtree kanan.
43. Fungsi main() digunakan sebagai pusat jalannya program.
44. Program membuat objek BST bernama bst.
45. Variabel pilih digunakan untuk menyimpan pilihan menu pengguna.
46. Program menggunakan perulangan while agar menu terus berjalan sampai pengguna keluar.
47. Program menampilkan judul “Sistem Pencarian Data Akademik”.
48. Program menampilkan menu tambah data mahasiswa.
49. Program menampilkan menu pencarian data berdasarkan NPM.
50. Program menampilkan menu tampilkan semua data.
51. Program menampilkan menu keluar.
52. Program meminta pengguna memasukkan pilihan menu.
53. try-except digunakan untuk menangani kesalahan input.
54. Jika input bukan angka maka program menampilkan pesan kesalahan.
55. Jika pengguna memilih menu 1 maka program menjalankan tambah data mahasiswa.
56. Program meminta input NPM mahasiswa.
57. Program meminta input nama mahasiswa.
58. Program meminta input tanggal lahir mahasiswa.
59. Program meminta input program studi mahasiswa.
60. Program memanggil method insert() untuk menyimpan data ke BST.
61. Program menampilkan pesan bahwa data berhasil ditambahkan.
62. Jika input NPM bukan angka maka program menampilkan pesan kesalahan.
63. Jika pengguna memilih menu 2 maka program menjalankan pencarian data.
64. Program meminta input NPM yang ingin dicari.
65. Program memanggil method search() untuk mencari data mahasiswa.
66. Hasil pencarian disimpan ke variabel hasil.
67. Program mengecek apakah data ditemukan.
68. Jika ditemukan maka program menampilkan informasi mahasiswa.
69. Informasi yang ditampilkan meliputi NPM, nama, tanggal lahir, dan program studi.
70. Jika data tidak ditemukan maka program menampilkan pesan “Data tidak ditemukan”.
71. Jika input NPM salah maka program menampilkan pesan kesalahan.
72. Jika pengguna memilih menu 3 maka program menampilkan seluruh data mahasiswa.
73. Program menampilkan judul “Data Mahasiswa”.
74. Program memanggil method inorder() untuk menampilkan data secara terurut berdasarkan NPM.
75. Jika pengguna memilih menu 4 maka program berhenti dijalankan.
76. Program menampilkan pesan “Program selesai”.
77. Jika pengguna memasukkan pilihan menu yang tidak tersedia maka program menampilkan pesan “Menu tidak valid”.
78. Baris if __name__ == "__main__": digunakan untuk memastikan program dijalankan langsung.
79. Fungsi main() dipanggil untuk menjalankan seluruh program.

Output Program:
<img width="427" height="776" alt="Screenshot 2026-05-22 224356" src="https://github.com/user-attachments/assets/e2e9970e-fa54-4889-95e1-f00afb3d4781" />
<img width="421" height="723" alt="Screenshot 2026-05-22 224420" src="https://github.com/user-attachments/assets/9a392ceb-cf8c-4dfa-8f61-aa3ed60a2788" />
<img width="388" height="814" alt="Screenshot 2026-05-22 224440" src="https://github.com/user-attachments/assets/a60004d0-16c5-401b-9212-196c8432fb91" />

Penjelasan Output Program:
1. Saat program dijalankan, sistem menampilkan menu utama Sistem Pencarian Data Akademik.
2. Pengguna memilih menu tambah data mahasiswa.
3. Program meminta input NPM, nama, tanggal lahir, dan program studi mahasiswa.
4. Data mahasiswa disimpan ke dalam Binary Search Tree berdasarkan NPM.
5. Pengguna menambahkan beberapa data mahasiswa ke dalam sistem.
6. Setelah data dimasukkan, program menampilkan pesan bahwa data berhasil ditambahkan.
7. Pengguna kemudian memilih menu pencarian data berdasarkan NPM.
8. Program meminta NPM mahasiswa yang ingin dicari.
9. BST melakukan proses pencarian dengan membandingkan NPM input dengan node pada tree.
10. Jika data ditemukan maka program menampilkan seluruh informasi mahasiswa.
11. Pengguna juga dapat memilih menu tampilkan semua data mahasiswa.
12. Program menggunakan traversal inorder untuk menampilkan data secara terurut berdasarkan NPM.
13. Output menunjukkan bahwa data dengan NPM terkecil ditampilkan lebih dahulu.
14. Terakhir pengguna memilih menu keluar.
15. Program menampilkan pesan “Program selesai” yang menandakan program telah berhenti dijalankan.

Link Youtube:
