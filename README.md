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

### Contoh create

Pemanggilan aksi create dari postman menggunakan metode POST, aksi ini membuat kontainer database baru dengan nama pg_5986.
<img width="2596" height="856" alt="image" src="https://github.com/user-attachments/assets/165f41bb-9563-4fe9-b689-8605b1f56144" />

Tampilan kontainer baru di docker:
<img width="2268" height="250" alt="image" src="https://github.com/user-attachments/assets/a6f8b361-91c5-4c25-b0a3-431dc6fd2b60" />


## 2. Logs

Aksi untuk menampilkan log aktivitas seluruh user. Setiap pemanggilan create dicatat di dalam log ini.

`http://localhost:8000/logs` (GET)

### Contoh logs

Pemanggilan aksi logs dari browser Chrome:
<img width="2879" height="682" alt="image" src="https://github.com/user-attachments/assets/de9a70e9-ace4-42ca-8954-c615467faa73" />

## 3. List

Aksi untuk menampilkan semua instance database yang sudah dibuat berserta keterangannya.

`http://localhost:8000/list` (GET) 

### Contoh list

Pemanggilan aksi list dari browser Chrome:
<img width="2879" height="784" alt="image" src="https://github.com/user-attachments/assets/f054d789-1645-4dff-9e0a-0b7147877d27" />
