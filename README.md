# catatan-inventory-gudang
buat sebuah daftar barang keluar/masuknya barang yang dimana disertakan dengan foto barang tersebut

# step
1. pull git
2. jalankan docker compose up -d --build
3. cek di http://ip:5000
4. dasboard
   <img width="2880" height="1800" alt="image" src="https://github.com/user-attachments/assets/be42bda7-7497-4148-b6c4-3f336df1eedf" />
5. tambah barang
   <img width="2880" height="1800" alt="image" src="https://github.com/user-attachments/assets/99d5b2f6-e07c-4e46-a4e4-fac71112c656" />
6. edit barang
   <img width="2880" height="1800" alt="image" src="https://github.com/user-attachments/assets/f606c99f-85d3-4f4e-bcba-bfa4fc7096a4" />

# HTTP -> HTTPS
kalau saran saya pakai ngrock untuk yang free, cuman minus url link httpsnya berganti-ganti setiap up docker container dan juga urlnya menyesuaikan dengan code container yang ada di docker dan tidak bisa diedit untuk nama url domainnya. Agar url tidak berubah terus menerus saran saya kirim notif lewat email arag dapat update terbaru dengan mudah tanpa harus cek dari log ngroknya atau kalau mau bisa beli sertifikat ssl untuk https-nya agar lebih mudah konfigurasinya dan namanya nya bisa disesuaikan dengan kemauan sendiri
