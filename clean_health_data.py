import pandas as pd
import numpy as np

print("Memulai pembersihan data kesehatan Surabaya...")

# 1. Buka file data kotor
df = pd.read_csv('data_kesehatan_surabaya_raw.csv')
initial_rows = len(df)

# 2. Hapus data ganda berdasarkan ID Sampel
df = df.drop_duplicates(subset=['id_sampel'], keep='first')

# 3. Standarisasi format tanggal ke YYYY-MM-DD
df['tanggal_pemeriksaan'] = pd.to_datetime(df['tanggal_pemeriksaan'], format='mixed', errors='coerce')
df = df.dropna(subset=['tanggal_pemeriksaan']) # Hapus baris yang tanggalnya kosong

# 4. Standarisasi penulisan nama Faskes (Puskesmas/RS/Lab)
def bersihkan_faskes(nama):
    if pd.isna(nama):
        return 'Tidak Terdaftar'
    
    teks = str(nama).upper().strip()
    if 'WONOKROMO' in teks:
        return 'Puskesmas Wonokromo'
    elif 'SOETOMO' in teks:
        return 'RSUD Dr. Soetomo'
    elif 'TEGAL' in teks:
        return 'Puskesmas Tegalsari'
    elif 'LABKESDA' in teks:
        return 'Labkesda Surabaya'
    elif 'GUBENG' in teks:
        return 'Puskesmas Gubeng'
    return teks.title()

df['nama_faskes_pengirim'] = df['nama_faskes_pengirim'].apply(bersihkan_faskes)

# 5. Penanganan nilai kosong pada hasil & biaya
df['hasil_pemeriksaan'] = df['hasil_pemeriksaan'].fillna('Pending/Belum Ada')
df['biaya_layanan'] = df['biaya_layanan'].fillna(df['biaya_layanan'].median())

# 6. Simpan hasil data bersih
df.to_csv('data_kesehatan_surabaya_clean.csv', index=False)

print("\n=== RINGKASAN PEMBERSIHAN DATA ===")
print(f"Total baris awal      : {initial_rows}")
print(f"Total baris bersih    : {len(df)}")
print(f"Baris dibuang/dirapikan: {initial_rows - len(df)}")
print("\nFile 'data_kesehatan_surabaya_clean.csv' siap digunakan!")