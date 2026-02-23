# Praktikum Pengolahan Citra Digital

**Nama:** Muhammad Rafi Fatihul Ihsan  
**NIM:** 24343016  
**Sesi/Kelas:** 202523430039  

Repository ini berisi kumpulan kode program untuk mata kuliah Pengolahan Citra Digital.

## Daftar Isi
1. [Persyaratan Sistem](#persyaratan-sistem)
2. [Instalasi](#instalasi)
3. [Struktur Folder](#struktur-folder)
4. [Deskripsi Program](#deskripsi-program)

---

## Persyaratan Sistem
- Python 3.x
- Pustaka Python yang dibutuhkan:
  - `opencv-python`
  - `numpy`
  - `matplotlib`
  - `requests`
  - `pillow`

## Instalasi
Untuk menginstal semua dependensi yang diperlukan, Anda dapat menjalankan perintah berikut di terminal:

```bash
pip install -r requirements.txt
```

---

## Struktur Folder
Berikut adalah struktur folder dari proyek ini:

```
program/
├── requirements.txt         # Daftar dependensi Python
└── src/
    ├── assignment/
    │   └── assignment.py    # Eksplorasi Digitalisasi Citra
    ├── img/                 # Folder untuk menyimpan citra sampel
    ├── praktikum1/
    │   └── praktikum1.py    # Dasar-dasar Citra Digital
    └── praktikum2/
        ├── latihan1.py      # Analisis Citra & Histogram
        └── latihan2.py      # Simulasi Digitalisasi Sinyal
```

---

## Deskripsi Program

### 1. Eksplorasi Digitalisasi Citra
**File:** `src/assignment/assignment.py`

Program ini merupakan tugas eksplorasi yang mencakup:
- **Akuisisi Citra:** Memuat citra dari penyimpanan lokal.
- **Representasi Matriks:** Menampilkan representasi matriks piksel dan vektor citra.
- **Analisis Parameter:** Menghitung resolusi, bit depth, dan estimasi ukuran memori.
- **Manipulasi Dasar:** Melakukan operasi *cropping* (pemotongan), *resizing* (pengubahan ukuran), dan *flipping* (pembalikan) pada citra.

### 2. Dasar-dasar Citra Digital (Praktikum 1)
**File:** `src/praktikum1/praktikum1.py`

Modul praktikum pertama ini membahas konsep dasar pengolahan citra digital secara komprehensif, meliputi:
- **Analisis Properti Citra:** Resolusi, dimensi, dan channel warna.
- **Konversi Grayscale:** Mengubah citra berwarna menjadi skala abu-abu.
- **Analisis Bit Depth:** Mengamati pengaruh penurunan bit depth (8-bit, 4-bit, 2-bit, 1-bit) terhadap kualitas citra.
- **Aspek Rasio:** Membandingkan berbagai rasio aspek citra (4:3, 16:9, dll).
- **Separasi Channel RGB:** Memisahkan dan menampilkan channel warna Merah, Hijau, dan Biru secara individu.
- **Histogram:** Menampilkan histogram intensitas piksel dan histogram kumulatif.
- **Analisis Memori:** Perbandingan ukuran memori untuk berbagai format resolusi.

### 3. Latihan Praktikum 2

#### Latihan 1: Analisis Citra & Statistik Histogram
**File:** `src/praktikum2/latihan1.py`

Program latihan ini fokus pada:
- Menganalisis citra pribadi (misalnya `kucing_rafi.jpeg`) dan membandingkannya dengan citra standar (Lena).
- Menampilkan visualisasi *side-by-side* antara citra asli dan grayscale.
- Menampilkan histogram intensitas untuk analisis distribusi kecerahan dan warna.
- Menghitung statistik dasar seperti Mean, Standar Deviasi, Min, dan Max nilai piksel.

#### Latihan 2: Simulasi Digitalisasi Sinyal
**File:** `src/praktikum2/latihan2.py`

Program ini mensimulasikan proses konversi sinyal analog ke digital:
- **Sampling:** Mengambil sampel dari sinyal kontinu pada interval waktu tertentu.
- **Quantization:** Memetakan nilai sampel ke level diskrit terdekat.
- Menampilkan grafik visualisasi dari sinyal asli, hasil sampling, dan hasil kuantisasi.

---

**Catatan:**  
Pastikan jalur (path) file gambar pada setiap skrip (`path_citra`) sudah sesuai dengan lokasi file di komputer Anda agar program dapat berjalan dengan benar.
