# Dataset Putusan Pengadilan Narkotika - PN Samarinda 2025

Selamat datang di repository **Dataset Putusan Pengadilan Narkotika**. Dataset ini merupakan kumpulan putusan pengadilan dari **Pengadilan Negeri (PN) Samarinda** tahun **2025** dengan fokus pada kasus **Narkotika dan Psikotropika**. Dataset ini dapat digunakan untuk penelitian di bidang **Temu Kembali Informasi (TKI)**, **analisis hukum**, **data mining**, maupun **Natural Language Processing (NLP)**.

---

## 📂 Struktur Repository

Dataset-Narkotika_278_298/
│
├── Dataset/
│ └── Narkotika.zip # Folder berisi 50 dokumen putusan pengadilan (*.pdf)
│
├── Overview/
│ └── Overview.xlsx # Ringkasan informasi 50 putusan
│
└── README.md # Dokumentasi dataset

---

## 📝 Deskripsi Dataset

Dataset ini berisi **50 dokumen putusan pengadilan** yang diambil secara manual dari direktori putusan Mahkamah Agung RI ([Direktori Putusan MA](https://putusan3.mahkamahagung.go.id/direktori.html)) dengan ketentuan:

- Pengadilan Negeri: **Samarinda**
- Klasifikasi: **Pidana Khusus – Narkotika dan Psikotropika**
- Tahun putusan: **2025**
- Status putusan: **Belum berkekuatan hukum tetap**
- Format file: **PDF**

### Tujuan Pengumpulan
Dataset ini dikumpulkan untuk mendukung:

1. **Penelitian Temu Kembali Informasi (TKI)**: Memungkinkan ekstraksi informasi penting dari dokumen hukum.
2. **Analisis Hukum**: Mempermudah analisis kasus narkotika berdasarkan barang bukti, amar putusan, dan pidana yang dijatuhkan.
3. **Pengembangan NLP**: Dataset cocok untuk **text mining**, **named entity recognition (NER)**, dan **classification tasks**.

---

## 📄 Overview.xlsx

File `Overview.xlsx` berisi **ringkasan 50 putusan** dengan struktur kolom sebagai berikut:

| No | No Putusan | Lembaga Peradilan | Barang Bukti | Amar Putusan |
|----|------------|-----------------|-------------|--------------|

- **No Putusan:** Nomor resmi putusan pengadilan.
- **Lembaga Peradilan:** Nama pengadilan (PN Samarinda).
- **Barang Bukti:** Detail barang bukti narkotika dan psikotropika, beserta jumlah atau beratnya.
- **Amar Putusan:** Ringkasan amar putusan, termasuk vonis pidana penjara, denda, serta ketentuan terkait barang bukti.

Contoh isi kolom `Amar Putusan`:

> Menyatakan Terdakwa telah terbukti secara sah dan meyakinkan melakukan tindak pidana tanpa hak atau melawan hukum memiliki Narkotika Golongan I bukan tanaman jenis sabu dengan berat 7,42 gram; Menjatuhkan pidana penjara selama 7 tahun; Menghukum denda sebesar Rp 1.000.000.000; Menetapkan barang bukti dirampas untuk dimusnahkan.

---

## ⚙️ Cara Menggunakan Dataset

1. **Download Dataset**
   - Unduh `Narkotika.zip` dari folder `Dataset/` dan ekstrak ke direktori lokal.
2. **Buka Overview**
   - Gunakan Excel atau Python (`pandas`) untuk membaca `Overview.xlsx`:
     ```python
     import pandas as pd
     df = pd.read_excel("Overview/Overview.xlsx")
     print(df.head())
     ```
3. **Analisis**
   - Dataset dapat digunakan untuk:
     - Ekstraksi informasi barang bukti dan amar putusan
     - Analisis pola hukum dan pidana
     - NLP, text mining, atau pembuatan model klasifikasi

---

## ⚖️ Hak Cipta dan Lisensi

- Dokumen ini **bersifat publik** dan **tidak terikat Hak Kekayaan Intelektual (HaKI)**.
- Dataset dapat digunakan untuk penelitian, pembelajaran, maupun pengembangan model AI dengan **mencantumkan sumber**.

---

## 📚 Referensi

- [Direktori Putusan Mahkamah Agung RI](https://putusan3.mahkamahagung.go.id/direktori.html)
- Panduan Tugas Temu Kembali Informasi - Dokumentasi Dataset Putusan Pengadilan

---

## 👥 Kontributor

- **Andi Fathir Muzakki Diningrat** – NIM: 202210370311278
- **Achmal Farhan Ashidiqy** – NIM: 202210370311298  

---

> Repository ini dibuat untuk memenuhi tugas Mata Kuliah **Temu Kembali Informasi (TKI)** dan bersifat **open source**.

