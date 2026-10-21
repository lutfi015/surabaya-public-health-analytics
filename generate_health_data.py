import pandas as pd
import numpy as np
import random
from datetime import datetime, timedelta

print("Membuat data kotor simulasi laboratorium kesehatan Surabaya...")

np.random.seed(42)
random.seed(42)

n_rows = 600

# Variasi nama faskes yang berantakan (typo & beda penulisan)
faskes_list = [
    'Puskesmas Wonokromo', 'puskesmas wonokromo', 'Pusk. Wonokromo',
    'RSUD Dr. Soetomo', 'RSUD DR SOETOMO', 'RS Soetomo',
    'Puskesmas Tegalsari', 'Puskesmas Tegal Sari',
    'Labkesda Surabaya', 'LABKESDA SBY',
    'Puskesmas Gubeng', 'Pusk. Gubeng'
]

jenis_tes = ['PCR TBC', 'Uji Kualitas Air', 'Darah Lengkap', 'Demam Berdarah (NS1)', 'Pemeriksaan Makanan']
hasil_options = ['Positif', 'Negatif', 'Normal', 'Abnormal', 'Layak', 'Tidak Layak']

data = []
for i in range(1, n_rows + 1):
    # ID Sampel (sebagian sengaja duplikat buat simulasi data ganda)
    sample_id = f"SMPL-2024-{random.randint(1000, 1450)}"
    
    # Format tanggal ngacak
    base_date = datetime(2024, 1, 1) + timedelta(days=random.randint(0, 180))
    date_format_choice = random.choice([1, 2, 3, 4])
    if date_format_choice == 1:
        tgl = base_date.strftime("%Y-%m-%d")
    elif date_format_choice == 2:
        tgl = base_date.strftime("%d/%m/%Y")
    elif date_format_choice == 3:
        tgl = base_date.strftime("%d-%b-%Y")
    else:
        tgl = None  # Missing value
        
    faskes = random.choice(faskes_list) if random.random() > 0.05 else None # 5% missing
    tes = random.choice(jenis_tes)
    hasil = random.choice(hasil_options) if random.random() > 0.08 else None # 8% missing
    biaya = random.choice([50000, 75000, 150000, 200000, 350000]) if random.random() > 0.1 else np.nan

    data.append({
        'id_sampel': sample_id,
        'tanggal_pemeriksaan': tgl,
        'nama_faskes_pengirim': faskes,
        'jenis_pemeriksaan': tes,
        'hasil_pemeriksaan': hasil,
        'biaya_layanan': biaya
    })

df = pd.DataFrame(data)

# Simpan ke CSV
df.to_csv('data_kesehatan_surabaya_raw.csv', index=False)
print("Sukses! File 'data_kesehatan_surabaya_raw.csv' berhasil dibuat (600 baris data kotor).")