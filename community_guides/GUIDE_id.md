# Panduan ke GitHub Code Vault

## Pengantar

Arsip ini, GitHub Code Vault, dibuat oleh Program Arsip GitHub, yang misinya adalah melestarikan perangkat lunak sumber terbuka untuk generasi mendatang. Anda mungkin membaca ini satu tahun dari sekarang, atau seribu, tapi bagaimanapun, kami berharap isinya, dan mungkin konsep open source, bermanfaat bagi Anda.

Ini terutama merupakan arsip perangkat lunak. Perangkat lunak adalah serangkaian perintah yang digunakan untuk mengontrol tindakan komputer. Komputer adalah perangkat yang secara otomatis dapat melakukan fungsi matematika jauh lebih cepat daripada pikiran manusia yang memiliki kekuatan yang jauh melampaui kita. Komputer kami digunakan untuk membantu menjelajahi rahasia alam semesta, untuk menghubungkan seluruh umat manusia dalam jaringan informasi yang ada di mana-mana, untuk memanipulasi sinyal dengan cukup cepat untuk mengirimkan suara dan memproyeksikan gambar bergerak yang mendetail ke layar listrik, dan untuk mengontrol mesin yang sangat kuat yang sejauh ini. melebihi kapasitas dan ketepatan tenaga manusia.

Komputer tanpa perangkat lunak tidak dapat melakukan semua hal ini. Komputer adalah hal yang luar biasa dan menakjubkan, tetapi tanpa perangkat lunak, semua kekuatannya tidak berguna. Tujuan dari arsip ini adalah untuk menyampaikan apa yang kami ketahui tentang perangkat lunak kepada Anda.

Perangkat lunak ditulis sebagai urutan perintah yang kompleks tetapi dapat dibaca manusia, berbagai rasa yang dikenal sebagai bahasa pemrograman, karena unit perangkat lunak yang lengkap sering disebut program. Program-program ini kemudian diubah menjadi bahasa biner satu dan nol yang digunakan oleh komputer. Proses ini dikenal sebagai kompilasi.

Karena perangkat lunak yang dikompilasi sangat sulit untuk diuraikan kembali ke bentuk program aslinya, yang juga dikenal sebagai kode sumbernya, ada kemungkinan bagi orang untuk merahasiakan formulir asli tersebut dan mengklaim kepemilikan atasnya. Perangkat lunak open source bukanlah jenis perangkat lunak yang berbeda, tetapi etos yang berbeda. Etos open source menolak kerahasiaan dan kepemilikan. Program perangkat lunak sumber terbuka tersedia bagi siapa saja dan semua yang ingin menggunakannya, tanpa biaya, sehingga mereka pada gilirannya dapat meningkatkan program tersebut, atau menggunakannya untuk membangun sesuatu yang baru dan lebih baik.

Proyek open source adalah kerja kolektif dari komunitas swakelola yang mungkin berjumlah ribuan. Akumulasi dari semua proyek perangkat lunak sumber terbuka yang diarsipkan di sini adalah hasil kerja dari jutaan komunitas. Meskipun individu tertentu mungkin memiliki hak khusus dalam proyek tertentu, seperti kemampuan untuk menyetujui atau menolak saran perubahan ke versi resmi terbaru dari kode sumbernya, tidak ada yang pernah memilikinya. Setiap orang berhak untuk mengambil dan menggunakan salinan lengkap dari setiap proyek open source kapan saja, tanpa biaya atau penalti. Ini dikenal sebagai forking sebuah proyek.

Ketika banyak orang mengerjakan kode sumber pada saat yang sama, sulit untuk melacak dan mengintegrasikan semua perubahan mereka. Proyek open source yang dikenal sebagai 'Git' dikhususkan untuk memecahkan masalah ini. Ini mengintegrasikan riwayat lengkap semua penambahan dan perubahan pada proyek ke dalam entitas yang dikenal sebagai repositori Git. Arsip ini pada dasarnya adalah arsip dari repositori semacam itu.

Arsip ini dibuat oleh perusahaan bernama 'GitHub', yang menyediakan layanan yang memungkinkan orang di seluruh dunia menyimpan program perangkat lunak yang mereka tulis, melacak perubahan pada program ini, dan berkolaborasi dengan orang lain untuk meningkatkan dan mengembangkannya. GitHub menyediakan layanannya secara gratis untuk pengembang perangkat lunak sumber terbuka publik. Ini memiliki puluhan juta pengguna seperti itu.

Berikut ini adalah uraian tentang apa yang kami yakin perlu Anda ketahui dan miliki untuk memanfaatkan arsip perangkat lunak ini dengan sebaik-baiknya. Jika Anda tidak mengetahui atau memahami beberapa atau semua ini, jangan putus asa! Kami juga menyertakan panduan tentang cara memenuhi persyaratan ini. Jika karena alasan apa pun Anda tidak dapat mencapainya sendiri, maka keturunan Anda bisa.

## Apa yang Anda Butuhkan untuk Menggunakan Arsip

Pada prinsipnya, yang Anda perlukan untuk mengakses konten arsip ini hanyalah sumber penerangan dan semacam kaca pembesar. Namun, sebagian besar (meskipun tidak semua) datanya telah dikemas dengan sangat erat ke gulungan film dalam bentuk yang dikodekan dan dikompresi. Membaca, mendekode, dan membuka kompresi data ini akan membutuhkan komputasi yang cukup besar. Secara teori, hal ini dapat dilakukan tanpa komputer, tetapi akan sangat membosankan dan sulit.

Harapan kami adalah Anda tidak memerlukan definisi kami tentang perangkat lunak, komputer, dan istilah lainnya. Kami membayangkan Anda memiliki komputer sendiri, mungkin jauh lebih canggih daripada milik kami, dan mungkin memiliki arsitektur yang berbeda. Setelah Anda memahami ikhtisar dan panduan di bawah ini, Anda akan dapat dengan mudah mengakses semua data.

Namun, mungkin saja Anda memiliki komputer yang lebih rendah dari komputer kami, atau bahkan tidak memiliki komputer sama sekali. Dalam kasus kemungkinan itu, kami telah menyiapkan gulungan data yang tidak terkompresi, tidak terkode, dan dapat dibaca manusia yang kami sebut Pohon Teknologi. Tech Tree berisi informasi tentang teknologi dasar kami, komputer kami, dan perangkat lunak kami, dengan harapan bahwa, seiring waktu, Anda akan dapat Lihat pengetahuan ini untuk membuat ulang komputer yang dapat menggunakan perangkat lunak sumber terbuka dalam arsip ini.

## Ada Apa di Dalam

Arsipnya sangat besar - kira-kira 21 triliun byte (dijelaskan di bawah) - karena sangat inklusif dan demokratis. Jutaan orang membuat perangkat lunak yang mereka tulis tersedia untuk semua orang. Arsip ini mencakup snapshot - yaitu, satu salinan, pada satu waktu - dari semua perangkat lunak publik yang secara aktif dikembangkan oleh pengguna GitHub. Artinya, ini mencakup jutaan repositori terpisah. Harapan kami adalah bahwa pendekatan demokratis yang luas ini akan menarik minat para sejarawan di masa depan.

Repositori yang termasuk dalam arsip ini ditentukan murni oleh waktu komit terakhirnya, yang berarti terakhir kali diperbarui, dan jumlah bintangnya. (Semua pengguna GitHub dapat 'membintangi' repositori publik, untuk menunjukkan bahwa mereka menarik atau penting bagi mereka.) Cuplikan itu dimulai pada 02/02/2020, yaitu, pada hari kedua bulan Februari, di tahun 2020 dari kalender Masehi, saat kita menghitung waktu. Repositori yang termasuk di dalamnya adalah: semua repositori dengan komit apa pun dalam 80 hari sebelumnya; semua repositori dengan setidaknya satu bintang dengan komitmen apa pun dalam 365 hari sebelumnya; dan semua repositori dengan setidaknya 250 bintang, terlepas dari kapan terakhir diperbarui.

Tentu saja, tidak semua repositori ini sama pentingnya dalam hal pengaruh dan ketergantungannya. Tech Tree menyertakan indeks dan deskripsi singkat dari repositori paling signifikan dalam arsip, dan daftar di mana reel masing-masing dapat ditemukan, sehingga mereka dapat diakses tanpa harus mengarungi jutaan repositori ini untuk menentukan mana yang paling praktis berguna.

## Ikhtisar Arsip

Arsip tersebut terdiri dari 188 gulungan film: satu "gulungan panduan" informasi dan panduan yang dapat dibaca manusia, yang kami sebut Tech Tree, dan 187 gulungan perangkat lunak yang diarsipkan. Setiap gulungan mencakup 65.000 bingkai individu. Bingkai di awal setiap gulungan, dan bingkai gulungan panduan, termasuk teks dan gambar yang dapat dibaca manusia. Semua bingkai film lainnya terdiri dari data digital yang disimpan dalam bentuk visual yang dikenal sebagai kode QR.

Data digital berarti data pada akhirnya disimpan dalam format biner, yaitu sebagai 0s dan 1s, karena komputer itu sendiri adalah biner - dikendalikan oleh sinyal listrik yang "on" atau "off", sesuai dengan 1 atau 0 - dan data biner adalah jauh lebih mudah dipahami oleh komputer daripada komputer lainnya.

Metadata yang dapat dibaca manusia yang disimpan di awal setiap gulungan mencakup informasi tentang film itu sendiri, panduan untuk pengkodean QR yang digunakan, program perangkat lunak untuk mendekodekannya, dan indeks. Indeks mencantumkan judul, nomor bingkai awal, dan checksum untuk setiap file yang disimpan pada reel itu.

File adalah entitas data koheren tunggal. Sebuah checksum adalah nilai unik dari perhitungan, yang dikenal sebagai fungsi hash, dijalankan di seluruh konten file, untuk memastikan bahwa isinya tidak rusak atau rusak; fungsi hash yang digunakan dalam arsip dikenal sebagai 'SHA-1'.

Setiap kode QR terdiri dari bidang kotak putih atau hitam kecil yang menempati hampir seluruh bingkai film. Kami menggunakan kode QR karena jauh lebih ringkas dan kuat daripada teks yang dapat dibaca manusia. Kode QR diterjemahkan menjadi data biner, yaitu rangkaian satu dan nol.

Penguraian kode ini hanyalah langkah pertama dalam mengubah data biner menjadi informasi yang bermakna. Ini adalah data terkompresi, artinya telah dipadatkan untuk menghemat ruang, mirip dengan cara menulis "128xA" daripada menulis huruf A 128 kali. Setelah didekodekan, itu harus didekompresi.

Hasil setelah dekompresi dikenal sebagai file arsip: satu file yang berisi seluruh konten repositori proyek perangkat lunak tunggal. Kebanyakan repositori menyertakan banyak file, jadi file arsip ini seperti buku yang berisi banyak bab terpisah, atau kotak yang berisi banyak kotak lain. Umumnya menguntungkan, meskipun tidak mutlak diperlukan, untuk mengekstrak file arsip ke dalam file komponennya sebelum mengaksesnya.

Akhirnya, setiap file komponen adalah kumpulan data binernya sendiri, yaitu satu dan nol. Seseorang dapat memahami data jika Anda mengetahui formatnya. Misalnya, dalam format yang dikenal sebagai 'UTF-8', format paling umum dalam arsip, satu dan nol dibagi menjadi delapan kelompok, yang dikenal sebagai byte, byte 01000001 mewakili huruf A; tiga byte 01101001 01101110 01110100 mewakili kata int; dan dua byte 11000011 10000011 mewakili huruf Ã (A dengan aksen tilde di atasnya.)

Proses pengarsipan data, file biner yang dikemas ke dalam file arsip yang telah dikompresi terlebih dahulu kemudian dikodekan dengan QR, jelas kompleks dibandingkan dengan sekadar menulis teks yang dapat dibaca manusia. Proses pengarsipan yang harus Anda lalui - QR ke biner terkompresi; dikompresi menjadi tidak terkompresi; arsipkan file ke banyak file; file teks ke teks yang dapat dibaca manusia - sama rumitnya. Itu karena kerumitan ini memungkinkan kami menyimpan jauh lebih banyak data daripada yang mungkin dilakukan, dengan cara yang relatif mudah dibaca oleh komputer.

Jika kerumitan ini sulit dan mahal bagi Anda, kami mohon maaf, tetapi harapan kami adalah, jika demikian, panduan ini dan Tech Tree yang dapat dibaca manusia akan meringankan kerumitan ini, dan mungkin lebih berguna bagi Anda daripada arsipnya. konten, setidaknya hingga komputer Anda cukup canggih sehingga kerumitan data arsip mudah ditangani.

## Berkas, Direktori, Repositori, dan Format Data

Mungkin bermanfaat untuk membahas bagaimana arsip dibagi secara logis. Secara khusus, diskusi tentang file, direktori, dan format data kemungkinan besar akan membantu.

File adalah kumpulan data yang dikelompokkan menjadi satu kesatuan yang koheren dengan satu nama: anggap data sebagai pasir, dan file sebagai semacam tas yang dapat menampung pasir, dan hanya pasir. Direktori adalah sekumpulan file: anggap saja sebagai semacam tas yang hanya dapat menampung tas lain. Mengikuti metafora ini, setiap repositori terdiri dari direktori luar, yang dikenal sebagai direktori root, yang berisi sejumlah file dan / atau sejumlah direktori. Setiap direktori dapat, pada gilirannya, berisi file dan direktori itu sendiri.

Struktur ini lebih disukai karena file yang diatur ke dalam grup jauh lebih mudah untuk dikerjakan daripada satu kumpulan file. Pengenal file tertentu dalam direktori terluar terdiri dari nama semua direktori yang melingkupinya, dimulai dengan root, diikuti dengan nama individualnya sendiri, dengan karakter / di antara setiap nama. Misalnya, file bernama README.md di direktori root akan diidentifikasi sebagai /README.md dan file yang diidentifikasi sebagai /public/www/index.html akan menjadi file index.html di direktori 'www' di dalam ' public 'di dalam direktori root.

Setiap repositori memiliki dua nama, dipisahkan oleh pemisah, yang dalam arsip berupa karakter _ atau garis bawah. (Secara historis, ini telah menjadi / atau garis miring, tetapi itu juga digunakan untuk menunjukkan direktori, jadi kami menggunakan _ untuk kejelasan.) Nama depan adalah akun GitHub yang memiliki repositori itu; yang kedua adalah nama repositori individu. Kombinasi repositori dan pengidentifikasi file dapat digunakan untuk mengidentifikasi file individual dalam arsip secara unik. Misalnya, file 'package.json' di direktori 'web' di repositori 'ykarma' dalam akun GitHub 'rezendi' dapat diidentifikasi secara unik sebagai /web/package.json di rezendi_ykarma dalam arsip.

Jenis file yang berbeda memiliki tujuan yang berbeda pula. Arsip GitHub sebagian besar terdiri dari file teks, artinya file yang datanya dimaksudkan untuk mewakili bahasa tertulis. Sebagian besar perangkat lunak ditulis dalam file teks yang berisi teks sangat terstruktur yang dikenal sebagai kode sumber. Program khusus yang dikenal sebagai kompilator mengubah kode sumber yang dapat dibaca manusia menjadi instruksi yang dapat dibaca komputer yang dikenal sebagai kode yang dikompilasi atau kode mesin.

File yang bukan file teks, seperti file yang merepresentasikan gambar visual atau berisi kode yang dikompilasi, sering disebut sebagai file biner. Sayangnya ini istilah yang menyesatkan, karena file teks pada akhirnya juga memiliki angka 1 dan 0. Kami akan merujuk ke file yang bukan file teks sebagai file non-teks.

Ada banyak cara untuk merepresentasikan bahasa tertulis manusia menggunakan 1 dan 0. Karena alasan historis, sebagian besar kode sumber awalnya ditulis dalam apa yang dikenal sebagai skrip Latin. Aksara latin memiliki 26 karakter dasar yang digunakan untuk merepresentasikan kata-kata yang dapat diucapkan, yang masing-masing memiliki dua bentuk, huruf besar dan huruf kecil. Ini juga memiliki 10 digit untuk mewakili angka. Skrip Latin, bersama dengan berbagai simbol terkait lainnya yang digunakan untuk menunjukkan struktur dan konsep lainnya, dikodekan menjadi 1 dan 0 dalam format yang dikenal sebagai 'ASCII', yang dapat mewakili 128 karakter berbeda dan karena alasan historis dominan di sebagian besar perangkat lunak selama bertahun-tahun .

Namun, aksara Latin hanyalah sebagian kecil dari banyak cara manusia mengekspresikan dirinya dalam bahasa tertulis. Untuk mendukung skrip lain, sementara juga memungkinkan semua perangkat lunak yang telah ditulis untuk menggunakan ASCII untuk terus bekerja tanpa perubahan (konsep yang dikenal sebagai kompatibilitas mundur), format data lain yang dikenal sebagai 'UTF-8' diperkenalkan.

ASCII tetap menjadi format kode sumber yang paling umum. Setiap gulungan arsip ini menyertakan panduan untuk karakter ASCII. ASCII adalah bagian dari UTF-8, artinya, semua penyandiaksaraan ASCII juga merupakan penyandiaksaraan UTF-8. Reel panduan juga berisi spesifikasi dari semua karakter UTF-8. Hampir semua file teks dalam arsip ini harus dikodekan sebagai UTF-8.

File non-teks termasuk file yang dimaksudkan untuk mewakili gambar dan dokumen yang diformat. Konvensi yang banyak digunakan adalah untuk nama file yang diakhiri dengan '.' karakter diikuti dengan sufiks yang menunjukkan jenis file. Misalnya, nama file yang diakhiri dengan .jpg kemungkinan besar adalah file gambar JPEG; yang diakhiri dengan .PNG kemungkinan besar adalah file gambar Grafik Jaringan Portabel; dan yang diakhiri dengan .pdf sebuah file Portable Document Format.

Tidak ada sufiks tunggal yang menunjukkan file teks. Sebaliknya, untuk kode sumber, sufiks lebih cenderung menunjukkan bahasa pemrograman atau markup mana kode tersebut ditulis. Bahasa pemrograman dan markup akan dijelaskan lebih detail di bawah ini.

## Cara Mengekstrak Isi Arsip

Di sini kami akan memberikan gambaran umum tentang cara membongkar repositori terarsipkan tertentu ke dalam berbagai file penyusunnya. Sekali lagi, proses ini terdiri dari:

1. Mengidentifikasi reel dan frame spesifik tempat data repositori diarsipkan.

2. Decoding dari kode QR, bidang piksel hitam, putih, dan abu-abu pada bingkai tersebut, menjadi file biner, urutan (setidaknya ribuan, dan seringkali jutaan) 1 dan 0.

3. Membuka ritsleting file biner menjadi file arsip yang lebih panjang dan tidak terkompresi.

4. Membuka file arsip ke dalam subfile terpisah di dalamnya. Namun perlu diperhatikan bahwa data arsip umumnya dapat dipahami, meskipun berantakan, bahkan jika langkah ini dihilangkan.

5. Terakhir, mengubah setiap subfile tersebut - urutan 1 dan 0 itu sendiri yang dapat berkisar dari cukup pendek hingga sangat panjang - menjadi karakter tertulis, jika mereka adalah file teks.

### Mengidentifikasi reel dan frame spesifik tempat data repositori diarsipkan

Setiap gulungan film dimulai dengan pemimpin film kosong, dan kemudian Bingkai Referensi Nol, yang terdiri dari persegi panjang hitam solid di salah satu sudut bingkai kosong. Bingkai yang dapat dibaca manusia berikutnya adalah Bingkai Kontrol, dengan informasi tentang gulungan. Berikut ini adalah Daftar Isi, yang pada gilirannya mencakup daftar File Data Pengguna.

Setiap repositori pada reel ini adalah salah satu dari File Data Pengguna tersebut. Daftar tersebut menyertakan ID unik, ID file, dan nama untuk masing-masing file tersebut. Misalnya, repositori CPython akun Python mungkin memiliki ID file terdaftar sebagai 12345, dan nama terdaftar sebagai python_cpython.tar.

Berikut daftar File Data Pengguna adalah daftar Lokasi Data Digital. Daftar ini mencakup ID file, bingkai awal, byte awal, bingkai akhir, dan byte akhir. Jadi, dengan menggunakan contoh CPython hipotetis, item dalam daftar ini dengan ID 12345 mungkin memiliki bingkai awal 054321, byte awal 03210321, bingkai akhir 054545, dan byte akhir 12321232.

Artinya, untuk mendapatkan data CPython: Buka frame 54321 dari gulungan film ini. Dekode semua frame dari frame awal, 54321, hingga frame akhir, 54545, menjadi nilai biner, dengan cara yang dijelaskan di bawah ini. Ini akan memberi Anda 225 buah data bernomor dari 54321 sampai 54545, yang akan dimulai dengan satu set data kosong tanpa data. Buang 3210320 byte pertama di bagian data tidak kosong pertama. Tambahkan semua data "tengah", secara berurutan. Terakhir, tambahkan 12321232 byte pertama dari potongan data terakhir, 54545. Anda sekarang telah mengumpulkan repositori CPython lengkap, sebagai satu file arsip terkompresi.

### Mendekode dari kode QR menjadi file biner

Detail tentang cara mendekode bingkai film menjadi data biner dapat ditemukan di Informasi Representasi yang dapat dibaca manusia yang dapat ditemukan di Daftar Isi di awal setiap gulungan film di arsip. Informasi ini ditemukan di setiap reel sehingga, meskipun satu reel dipisahkan dari arsip, masih mungkin untuk menguraikan isinya. Informasi Representasi tersebut meliputi, dengan urutan:

1. Panduan untuk Program Arsip GitHub (dokumen ini)

2. Indeks deskriptif GitHub, daftar dan deskripsi singkat dari semua repositori pada reel ini

3. Deskripsi Representasi Informasi

4. Penyimpanan Digital dan Cara Mengambil Data, gambaran umum detail pengambilan data

5. Deskripsi Media Penyimpanan

6. Teknologi Pengambilan Data

7. Struktur Reel Pengawetan Generik (format reel)

8. Deskripsi format Bingkai 4K Generik

9. Deskripsi perpustakaan unboxing (untuk kode QR)

10. Kode sumber perpustakaan membuka kemasan

11. Spesifikasi format data ASCII

12. Spesifikasi bahasa pemograman C

13. Kode sumber file arsip TAR

14. Kode sumber PDF

15. Spesifikasi format file XZ (untuk kompresi / dekompresi, dijelaskan di bawah)

Yang keenam dari item tersebut, dokumen Teknologi Pengambilan Data, menjelaskan persyaratan dan proses untuk menggunakan pemindai untuk menangkap data pada satu bingkai film yang dikodekan secara digital dan mengubahnya menjadi bentuk yang dapat digunakan untuk analisis komputer. Kedelapan di antaranya, deskripsi format Bingkai 4K Generik, memberikan informasi teknis, termasuk kode sumber, yang diperlukan komputer untuk mengambil gambar yang dipindai dan mengubahnya menjadi data biner.

Secara teoritis dimungkinkan, pada prinsipnya, untuk mengubah repositori dari data yang dikodekan QR menjadi data biner tanpa menggunakan komputer. Namun, ini akan sangat sulit dan mungkin membutuhkan upaya yang cukup besar dari komunitas yang terorganisir dengan baik selama beberapa minggu, jika tidak berbulan-bulan atau bertahun-tahun. Karena konten repositori adalah perangkat lunak yang dimaksudkan untuk dijalankan di komputer, penggunaannya saat tidak ada komputer akan menjadi minimal.

Dalam hal pewaris arsip ini tidak memiliki komputer, mereka harus menyimpan arsip secara utuh dan aman sampai mereka memilikinya. Salah satu tujuan dari Pohon Teknologi yang dapat dibaca manusia adalah untuk membantu mempercepat perkembangan teknologi dan komputer jika terjadi hal ini. (Tujuan lainnya adalah untuk menyusun teknologi kami dan perkembangannya untuk sejarawan masa depan.)

### Membuka file arsip ke dalam subfile terpisah yang dikandungnya

File biner untuk setiap repositori dalam format yang dikenal sebagai TAR, untuk Arsip Pita. File TAR pada dasarnya disusun dengan mengelompokkan sejumlah file bersama-sama dengan menghubungkan ujung satu file ke awal file berikutnya, seperti merekatkan setiap lembar kertas menjadi satu gulungan. File TAR dapat menyertakan sejumlah file, dengan ukuran berapa pun, dibagi menjadi sejumlah direktori dan subdirektori.

Setiap subfile dalam file TAR diawali dengan catatan header 512-byte, yang bertindak seperti pita dalam metafora gulir. Catatan header ini berisi informasi tentang file, seperti nama dan ukurannya. Akhir arsip ditunjukkan oleh setidaknya dua blok 512-byte yang berurutan.

Karena file TAR pada dasarnya hanyalah kumpulan file dengan catatan teks di antara mereka, jika file TAR berisi semua file teks, itu dapat diperlakukan sebagai file teks itu sendiri. Jika berisi campuran, ini dapat diperlakukan sebagai file teks yang berisi campuran teks yang terstruktur dan bermakna (file teks penyusun) dan omong kosong yang tidak dapat dipahami (penyusun file non-teks.)

File TAR dapat disarangkan dalam file TAR, satu wadah di dalam yang lain, dan ini adalah cara sebagian besar data yang diarsipkan disimpan. Untuk repositori tertentu, file TAR luar akan berisi setidaknya:

* satu file metadata tidak terkompresi yang disebut META, yang mencakup nama repositori, nama akun, deskripsi, bahasa, jumlah bintang, dan jumlah garpu
* file terkompresi (lihat di bawah) bernama COMMITS, yang menyertakan log dari perubahan yang dibuat ke repositori dari waktu ke waktu
* file bernama repo.tar.xz, file TAR terkompresi yang berisi konten repositori sebenarnya

Metadata lain, seperti wiki, gh-pages, issues, dan pull request, juga dapat disertakan sebagai file terkompresi yang terpisah.

Rincian spesifik dari file TAR, dan perangkat lunak untuk menyandikan dan mendekodekannya, dapat ditemukan di Informasi Representasi di setiap gulungan arsip.

### Membuka ritsleting file terkompresi menjadi file yang dapat dibaca dan tidak terkompresi

Untuk menyertakan sebanyak mungkin repositori dan data sebanyak mungkin, sebagian besar data telah dikompresi. Kompresi berarti menggunakan sejumlah kecil data untuk mewakili jumlah yang lebih besar, dengan menggunakan pola dan pengulangan dalam jumlah yang lebih besar itu. Misalnya, alih-alih menulis karakter sembilan kali berturut-turut, seseorang bisa saja menulis teks terkompresi 9a, jika seseorang yakin pembaca akan memahami bahwa 9a berarti teks yang tidak terkompresi aaaaaaaaa.

Algoritma kompresi yang efektif jauh lebih kompleks dari itu, tetapi prinsip yang sama berlaku. Arsip ini menggunakan program kompresi yang disebut 'XZ', yang selanjutnya menggunakan algoritme yang disebut 'LZMA'. File data kedua di setiap reel berisi kode sumber dan dokumentasi untuk XZ dalam satu file arsip TAR yang tidak dikompresi, dijelaskan di bawah ini. (File data pertama berisi Deklarasi Universal Hak Asasi Manusia dalam setiap bahasa tertulis yang tersedia.)

LZMA menggabungkan apa yang dikenal sebagai algoritma 'LZ77' dan "pengkodean jangkauan". LZ77 menggantikan data berulang dengan referensi ke tampilan sebelumnya dari data tersebut. Misalnya, untuk menyederhanakan secara berlebihan, jika frase 80 byte muncul dua kali, terpisah 400 byte, kedua kalinya, algoritme pada dasarnya memadatkan data dengan mengatakan "ulangi 80 byte dari 400 byte yang lalu". Pengkodean rentang pada dasarnya mengubah seluruh pesan menjadi satu nomor yang sangat panjang, yang pada gilirannya dapat dikodekan.

Langkah-langkah spesifik dari algoritme yang akan digunakan untuk mendekompresi data dijelaskan oleh kode sumber XZ yang terdapat dalam file data kedua di setiap gulungan. Meskipun secara teoritis mungkin untuk melakukan dekompresi dengan tangan, sekali lagi, ini akan menjadi proses yang sangat memakan waktu dan tenaga. Dalam praktiknya, komputer yang berfungsi akan dipanggil.

### Mengonversi setiap file menjadi karakter tertulis

Umat manusia telah menggunakan banyak karakter tertulis selama ribuan tahun. Pengkodean yang digunakan untuk mewakili karakter ini sebagai 1 dan 0 dalam arsip ini dikenal sebagai 'UTF-8'. Satu karakter UTF-8, yaitu satu simbol tertulis, dapat menempati dari 1 hingga 4 byte data biner.

Untuk alasan historis, karena mereka paling banyak digunakan pada waktu dan wilayah di mana dan ketika pengembangan perangkat lunak dimulai, sekelompok karakter (dan konsep) yang dikenal sebagai 'ASCII' dikodekan paling efisien, pada 1 byte per karakter. Apa pun yang bukan ASCII dikodekan sebagai 2 atau lebih byte per karakter. Sebagian besar file teks dalam arsip ini adalah ASCII, tetapi sebagian besar bukan. Banyak lagi yang sebagian besar akan menjadi ASCII dengan karakter non-ASCII sesekali.

Spesifikasi terperinci ASCII dapat ditemukan di Informasi Representasi di setiap gulungan arsip. Spesifikasi rinci UTF-8 dapat ditemukan di gulungan panduan. File data pertama pada setiap gulungan arsip akan berisi teks Deklarasi Universal Hak Asasi Manusia dalam setiap bahasa tertulis yang tersedia. Ini akan berfungsi sebagai alat terjemahan dan sebagai contoh ASCII dan UTF-8.

## Jenis Berkas

Ada banyak jenis file teks, dibuat karena berbagai alasan. Jenis utama di sini, alasan arsip ini ada, adalah kode sumber. Kode sumber adalah teks yang sangat padat, sangat terstruktur, dengan simbol seperti '{' dan ';' sangat penting.

Hal utama tentang kode sumber adalah bahwa ia ditulis untuk dibaca oleh kompiler. Karena kompiler adalah perangkat lunak, cara lain untuk mengutarakannya adalah kode sumber ditulis untuk dibaca oleh komputer. Kode yang baik juga ditulis agar manusia lain, jika mereka terampil dan terdidik di bidang perangkat lunak, dapat memahaminya; tetapi ini hanya benar jika kompiler dapat memahaminya.

Kompiler tersebut akan, pada gilirannya, melalui urutan rumit yang dijelaskan di Tech Tree, mengubah kode sumber menjadi urutan satu dan nol yang akan menyebabkan komputer menjalankan fungsi dan aktivitas yang dijelaskan oleh kode. Untuk mengambil contoh yang sangat sederhana, baris kode

    _untuk (int i = 0; i <5; i ++) {} _

akan diubah oleh kompiler menjadi serangkaian instruksi biner yang diumpankan ke komputer, yang akan menyebabkan sebagian kecil dari komputer, yang disebut register, menyetel nilainya menjadi 0, dan kemudian menaikkan nilainya menjadi 1, 2, 3, lalu 4. (Ini tidak dimaksudkan sebagai contoh kode yang berguna; ini hanya ilustrasi dari proses berlapis-lapis untuk mengubah kode sumber menjadi perangkat lunak yang berjalan.)

Jenis file teks lainnya, seperti JSON, XML, dan HTML, digunakan untuk menyimpan data (sebagai lawan dari perintah) untuk komputer. Teks tersebut umumnya juga dapat dibaca oleh manusia, meskipun format terstrukturnya membuatnya lebih sulit dibaca daripada teks mendongeng yang kurang terstruktur seperti file ini.

Sebagian besar jenis file teks lainnya pada akhirnya dimaksudkan untuk dibaca oleh manusia. Beberapa di antaranya sederhana, kebanyakan teks tidak terstruktur, seperti file yang sedang Anda baca ini. Jenis yang akan Anda temui secara luas dalam arsip adalah Penurunan harga, yang ditandai dengan ekstensi .md ke file, yang merupakan jenis bentuk perantara yang dimaksudkan agar dapat dibaca oleh manusia dalam bentuk mentahnya dan juga, pada saat yang sama, terstruktur sehingga komputer dapat memformatnya menjadi tata letak yang lebih menarik dan berguna secara visual. Sebagian besar repositori dalam arsip ini memiliki file README.md Markdown, yang umumnya dimaksudkan sebagai pengantar awal ke repositori, menjelaskan apa itu, mengapa ada, dan bagaimana menggunakannya.

Gambaran singkat tentang bentuk file non-teks yang paling umum mungkin juga berguna. Kode yang dikompilasi adalah non-teks. File JPG dan PNG menyandikan gambar dalam format digital, serta menyandikan audio MP3 dan WAV. File PDF menyandikan dokumen dengan pemformatan yang tepat dan sempurna. Dan file ZIP dan TAR, seperti yang disebutkan sebelumnya, adalah file kontainer yang pada gilirannya dapat menyertakan satu atau banyak file lainnya.

## Bahasa Manusia dan Bahasa Pemrograman

### Bahasa Manusia

Ada ribuan bahasa tertulis yang digunakan oleh umat manusia saat ini, dan bahkan lebih banyak bahasa lisan. Sebagian besar hanya digunakan oleh populasi yang relatif kecil, tetapi setidaknya ada dua puluh bahasa yang digunakan sebagai bahasa pertama atau kedua oleh setidaknya 60 juta orang.

Bahasa yang paling banyak digunakan di dunia adalah bahasa Inggris dan Cina. Karena alasan historis, selama bertahun-tahun sebagian besar pengembangan perangkat lunak terjadi di negara-negara berbahasa Inggris, jadi untuk suatu waktu, bahasa Inggris menjadi bahasa default perangkat lunak. Sebagian besar bahasa pemrograman menggunakan kata-kata bahasa Inggris dalam sintaksnya. Ini adalah bahasa di mana panduan arsip ini pertama kali ditulis.

Tidak ada jaminan bahwa pewaris arsip ini akan tahu bahasa Inggris, meskipun tampaknya bahasa ini kemungkinan besar akan bertahan tanpa batas. Jika beberapa panduan untuk bahasa lain bermanfaat, kami menyertakan lebih dari 500 terjemahan yang tersedia dari Deklarasi Universal Hak Asasi Manusia sebagai file UTF-8 yang tidak terkompresi di awal setiap reel, dan juga di dalam Tech Tree. Deklarasi ini adalah daftar hak dan kebebasan setiap individu manusia di zaman kita, yang tidak boleh dicabut.

### Bahasa pemrograman

Bahasa pemrograman adalah bahasa yang digunakan manusia untuk mengkomunikasikan instruksi ke komputer. Mereka adalah bahasa di mana perangkat lunak diekspresikan. Manusia lain (terlatih) juga harus dapat membaca perangkat lunak yang ditulis dalam bahasa pemrograman, tetapi itu adalah tujuan sekunder.

Bahasa pemrograman adalah sekumpulan elemen yang telah ditentukan sebelumnya, yang sebagian besar adalah kata-kata, yang dapat disusun secara terstruktur untuk menginstruksikan komputer untuk melakukan tindakan tertentu dengan cara yang ditentukan. Kumpulan instruksi semacam itu dikenal sebagai program, atau sebagai kode sumber. Kode sumber pada dasarnya adalah perangkat lunak dalam bentuk tertulis yang dibekukan.

Program umumnya dibagi menjadi langkah-langkah terpisah, yang dikenal sebagai pernyataan, yang kemudian dikelompokkan menjadi kolom leksi dikenal sebagai fungsi. Seluruh program dapat dimuat dalam satu file, atau mungkin tersebar di ribuan file.

Ada ratusan bahasa pemrograman yang berbeda, tersebar dalam berbagai bentuk, pendekatan, dan filosofi. Beberapa dikompilasi menjadi file biner terpisah, yang kemudian dieksekusi; beberapa, yang dikenal sebagai bahasa "ditafsirkan", secara efektif disusun dan dijalankan sekaligus, tanpa tahap sementara. Sebagian besar bahasa pemrograman modern menyertakan pustaka fungsi yang telah ditulis sebelumnya, dan pustaka semacam itu bisa sangat banyak dan rumit. Beberapa bahasa pemrograman paling populer saat ini meliputi:

* C, salah satu bahasa tertua dan tercepat, paling universal, dan paling kuat, sederhana dalam beberapa hal tetapi sangat terbatas pada yang lain, dan tidak selalu intuitif, mudah dibaca, atau mudah dipelajari.

* C ++, evolusi C yang lebih kompleks, abstrak, dan kuat.

* C #, evolusi lebih lanjut yang dikompilasi bukan menjadi kode mesin biner tetapi sebuah interpretasi "runtime".

* Java, yang mirip dengan (tapi mendahului) C #, mungkin adalah bahasa yang paling banyak digunakan saat ini.

* JavaScript, tidak seperti Java meskipun memiliki kesamaan nama, dan juga dikenal sebagai 'ECMAScript', adalah bahasa yang awalnya digunakan sepenuhnya dalam browser web, yaitu program yang mengambil, menafsirkan, dan menampilkan data dari komputer jarak jauh yang dikenal sebagai Internet server; hari ini, meskipun, itu banyak digunakan di server-server itu juga.

* TypeScript, suatu bentuk JavaScript dengan aturan yang lebih ketat sehingga kesalahan, juga dikenal sebagai bug, kecil kemungkinannya untuk menemukan jalannya ke dalam program.

* Python, bahasa elegan yang populer di kalangan ilmuwan, kuat dan bahasa pertama yang baik.

* Ruby, bahasa intuitif yang pernyataannya sering dibaca hampir seperti bahasa Inggris tertulis.

* Go, bahasa yang sederhana dan kuat yang khususnya unggul pada program yang diparalelkan, yaitu program yang ditulis sedemikian rupa sehingga beberapa fungsi berjalan secara independen pada waktu yang bersamaan.

* Swift, bahasa baru yang digunakan untuk menulis di ponsel dan perangkat lain yang digunakan oleh satu miliar orang.

* Rust, dimaksudkan sebagai pengganti C, yang membuat bug berbahaya menjadi jauh lebih kecil kemungkinannya.

* PHP, bahasa sederhana yang digunakan untuk server Internet.

* Lisp, bahasa yang sangat lama dengan pendekatan pemrograman yang berbeda secara fundamental dan mengutamakan fungsi.

* SQL, jenis bahasa yang sangat berbeda yang digunakan untuk mengambil data dari penyimpanan data terstruktur dan sangat efisien yang dikenal sebagai database.

* Assembler (atau assembly), rumpun bahasa yang sangat samar, terbatas, tetapi cepat dan kuat di mana terdapat hubungan langsung antara konstruksi bahasa dan kode mesin komputer yang bersangkutan; itu mungkin dianggap kode setengah terkompilasi.

## Pengembangan, Dependensi, dan Sumber Terbuka

### Pengembangan

Proses mengambil satu file kode sumber sederhana dan mengubahnya menjadi impuls listrik di dalam komputer sangatlah rumit. Kami menangani kompleksitas ini menggunakan lapisan abstraksi. Abstraksi yang dikenal sebagai set instruksi memungkinkan output kode mesin dari kompiler tunggal untuk digunakan pada berbagai jenis komputer. Seorang penulis kode sumber biasanya tidak perlu mengetahui atau peduli komputer jenis apa, atau bahkan set instruksi apa, yang akan digunakan untuk menjalankan kode itu; ini disarikan oleh kompiler.

Perangkat lunak modern, pada gilirannya, jauh lebih kompleks daripada seorang penulis tunggal yang mengerjakan satu program untuk satu komputer. Ini terdiri dari banyak penulis yang mengerjakan banyak file dalam satu proyek, secara bersamaan, seringkali menggunakan banyak bahasa pemrograman. Selain itu, setiap proyek bergantung pada proyek lain yang terpisah dan berdiri sendiri sebagai alat dan / atau komponen, sementara proyek ini sendiri sedang dikerjakan secara aktif, dan pada gilirannya bergantung pada proyek lain. Membuat semua bagian yang bergerak ini bekerja bersama secara elegan dan efisien adalah tantangan pengembangan perangkat lunak modern.

Ketika beberapa penulis kode sumber, juga dikenal sebagai pengembang perangkat lunak, mengerjakan satu proyek, masing-masing memiliki komputer sendiri, dan salinan keseluruhan proyek di komputer mereka. Jika masing-masing membuat perubahan, masing-masing memiliki versi berbeda dari proyek yang sama. Proses rekonsiliasi beberapa versi proyek dikenal sebagai kontrol versi. Dikelola oleh perangkat lunak kontrol versi; dalam arsip ini, dengan perangkat lunak bernama Git, yang kemudian dinamai GitHub. Setiap repositori dalam arsip ini adalah repositori Git.

Git dapat secara otomatis menggabungkan berbagai versi perangkat lunak menjadi satu bentuk yang koheren dengan sedikit campur tangan manusia. Git juga menyimpan riwayat lengkap yang memungkinkan Anda untuk kembali ke versi sebelumnya jika diperlukan. Namun, untuk menghemat ruang, repositori arsip ini umumnya tidak menyertakan riwayat Git.

Ketika beberapa pengembang mengambil proyek di beberapa jalur berbeda secara bersamaan, ini dikenal sebagai proyek bercabang, dan jalur tersebut dikenal sebagai cabang. Cabang utama proyek yang disepakati dikenal sebagai trunk, atau cabang induk. Git menyediakan fasilitas yang dapat digunakan pengembang untuk meringkas perbedaan antara dua cabang dan usulkan untuk menggabungkan cabang mereka ke cabang lainnya. Ini dikenal sebagai permintaan tarik. Pengembangan perangkat lunak modern sebagian besar terdiri dari percabangan proyek, menulis atau mengedit perangkat lunak di cabang Anda, dan, setelah selesai, mengirimkan permintaan tarik agar pekerjaan Anda digabungkan kembali ke cabang master.

### Dependensi

Pada dasarnya setiap bahasa pemrograman mendukung pembangunan di atas pekerjaan orang lain. Tanpa menggunakan kembali pekerjaan orang lain, setiap proyek akan menjadi jauh lebih sulit, dan jauh lebih lambat, dan semakin sedikit proyek yang akan pernah melihat penggunaan aktual di dunia nyata.

Jika proyek A perlu menyertakan proyek B agar A dapat melakukan tugasnya, maka A dikenal sebagai tergantung pada proyek B, dan B dikenal sebagai ketergantungan proyek A. A dapat memiliki banyak ketergantungan, yang masing-masing dapat memiliki banyak ketergantungan mereka sendiri, dan lain sebagainya. Selain itu, setiap ketergantungan adalah untuk versi tertentu, atau rentang versi, dari proyek tertentu. Perincian lengkap dari semua lapisan beberapa proyek dependensi dikenal sebagai pohon ketergantungannya.

Umumnya, dependensi diperinci di dalam file kode sumber, biasanya di paling atas, dan setiap kali compiler atau interpreter menemukan dependensi, ia akan mencarinya dalam sekumpulan direktori yang telah ditentukan. Karena pohon ketergantungan untuk sebuah proyek bisa sangat kompleks, terkadang pohon itu diperinci secara keseluruhan dalam satu file dalam proyek yang dikenal sebagai daftar paket. Misalnya, proyek Ruby mungkin memiliki Gemfile untuk tujuan ini, dan proyek JavaScript mungkin memiliki file package.json. Ini memungkinkan sejenis alat yang dikenal sebagai perangkat lunak manajemen paket untuk mengambil semua dependensi untuk suatu proyek sekaligus, dari satu atau lebih server Internet.

Dalam kasus arsip ini, kemungkinan dependensi untuk setiap proyek ada di tempat lain dalam arsip. Untuk menemukan ketergantungan dalam arsip, pertama-tama kita harus menemukan nama ketergantungan dalam kode sumber atau daftar paket, detail persisnya berbeda-beda menurut bahasa dan kerangka kerja, lalu gunakan indeks master di gulungan panduan, atau, jika tidak ada, indeks di depan setiap gulungan, untuk menentukan di mana gulungan dan bingkai tempat penyimpanan yang dimaksud dapat ditemukan.

### Sumber terbuka

Karena menjalankan program di komputer hanya membutuhkan kode mesin yang dikompilasi, maka dimungkinkan untuk mendistribusikannya sambil menjaga kerahasiaan kode sumber. Ini dikenal sebagai model sumber tertutup. Pada masa-masa awal komputasi, kode sumber biasanya didistribusikan bersama dengan kode mesinnya, tetapi kemudian, karena perangkat lunak menjadi industri yang menguntungkan, model sumber tertutup menjadi lebih umum.

Sejak itu telah dipelajari bahwa membuat kode sumber menjadi publik, bagi siapa saja untuk disalin, dicabangkan, dan ditingkatkan, adalah pendekatan yang jauh lebih efektif untuk pengembangan perangkat lunak. Lebih banyak orang yang dapat membaca kode sumber proyek berarti lebih banyak orang untuk mengidentifikasi kemungkinan kebutuhan dan fitur baru yang berguna, lebih banyak orang yang cukup memahami proyek untuk berkontribusi, lebih banyak orang yang mungkin melihat bug dan mengirimkan perbaikan, dan lebih banyak orang untuk menguji dan memverifikasi kode baru itu berfungsi.

Secara umum, sumber tertutup mengarah pada komunitas yang lebih kecil, sempit, dan terfragmentasi yang berjuang untuk menemukan dan mengadopsi ide-ide baru dan lebih baik. Sumber terbuka mengarah ke komunitas yang besar dan saling berhubungan, masing-masing membantu proyek satu sama lain tumbuh dan berkembang dan berhasil, menggunakan pekerjaan satu sama lain sebagai ketergantungan dan / atau menggunakan kembali kode mereka, dan belajar dari satu sama lain. Perangkat lunak sumber terbuka adalah perangkat untuk penggunaan kolektif seluruh umat manusia, dan semakin banyak alat yang kita miliki, semakin cepat dan lebih baik kita dapat berkembang sebagai suatu spesies.
