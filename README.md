# Cara menjalankan

Buka folder project pada Docker dan jalankan perintah berikut pada terminal:

`docker-compose build` 
`docker-compose up`

Jika perintah berhasil dieksekusi tanpa kendala, backend akan berjalan di localhost komputer pada port 8000.

# Fitur/Aksi

## 1. Create

Aksi untuk membuat database PostgreSQL baru di dalam kontainer docker terisolasi. 

Untuk melakukan aksi create, kirim request di bawah ini dengan metode POST (misal menggunakan curl atau postman):

`http://localhost:8000/create` (POST)

## 2. Logs

Aksi untuk menampilkan log aktivitas seluruh user. Setiap pemanggilan create dicatat di dalam log ini.

`http://localhost:8000/logs` (GET)

## 3. List

Aksi untuk menampilkan semua instance database yang sudah dibuat berserta keterangannya.

`http://localhost:8000/logs` (GET) 

