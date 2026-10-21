# Surabaya Public Health & Lab Test Analytics Pipeline

Proyek simulasi *Data Analyst* berbasis kesehatan masyarakat untuk mengolah, membersihkan, dan menyajikan data sampel laboratorium serta fasilitas kesehatan (Puskesmas, RSUD, Labkesda) di wilayah Surabaya.

---

## Technical Stack
- **Language:** Python
- **Data Processing:** Pandas, NumPy
- **Dashboard & Visualization:** Streamlit
- **Version Control:** Git & GitHub

---

## Key Features & Workflow

1. **Data Cleaning & Standardization (`clean_health_data.py`)**
   - Menghapus rekaman ganda berdasarkan ID sampel.
   - Menyetarakan variasi penulisan nama faskes (misal: "puskesmas wonokromo", "Pusk. Wonokromo" menjadi "Puskesmas Wonokromo").
   - Memperbaiki dan menyelaraskan format tanggal pemeriksaan menjadi `YYYY-MM-DD`.
   - Penanganan *missing values* pada kolom hasil pemeriksaan dan biaya layanan.

2. **Interactive Monitoring Dashboard (`app.py`)**
   - Filter interaktif berdasarkan Faskes Pengirim dan Jenis Pemeriksaan.
   - Metrik ringkasan: Total Sampel, Jumlah Faskes Aktif, dan Total Biaya Layanan.
   - Visualisasi volume sampel per faskes, distribusi jenis pemeriksaan, dan tren harian.
   - Tabel detail data bersih yang siap diunduh untuk kebutuhan pelaporan pimpinan.

---

## How to Run

1. **Clone repository:**
   ```bash
   git clone [https://github.com/USERNAME_KAMU/surabaya-public-health-analytics.git](https://github.com/USERNAME_KAMU/surabaya-public-health-analytics.git)
   cd surabaya-public-health-analytics