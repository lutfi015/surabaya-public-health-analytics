import pandas as pd
import streamlit as st

st.set_page_config(page_title="Surabaya Health Analytics", layout="wide")

st.title("Surabaya Public Health & Lab Test Monitoring Dashboard")
st.write("Dashboard pemantauan sampel pemeriksaan laboratorium dan kesehatan masyarakat wilayah Surabaya.")

@st.cache_data
def load_data():
    df = pd.read_csv('data_kesehatan_surabaya_clean.csv')
    df['tanggal_pemeriksaan'] = pd.to_datetime(df['tanggal_pemeriksaan'])
    return df

df = load_data()

# Sidebar Filter
st.sidebar.header("Filter Data")
list_faskes = ["Semua"] + sorted(df['nama_faskes_pengirim'].unique().tolist())
selected_faskes = st.sidebar.selectbox("Pilih Faskes Pengirim", list_faskes)

list_tes = ["Semua"] + sorted(df['jenis_pemeriksaan'].unique().tolist())
selected_tes = st.sidebar.selectbox("Pilih Jenis Pemeriksaan", list_tes)

# Apply Filter
df_filtered = df.copy()
if selected_faskes != "Semua":
    df_filtered = df_filtered[df_filtered['nama_faskes_pengirim'] == selected_faskes]
if selected_tes != "Semua":
    df_filtered = df_filtered[df_filtered['jenis_pemeriksaan'] == selected_tes]

# Key Metrics
col1, col2, col3 = st.columns(3)
with col1:
    st.metric("Total Sampel Diuji", f"{len(df_filtered)}")
with col2:
    st.metric("Faskes Aktif", df_filtered['nama_faskes_pengirim'].nunique())
with col3:
    total_biaya = df_filtered['biaya_layanan'].sum()
    st.metric("Total Biaya Layanan", f"Rp {total_biaya:,.0f}".replace(",", "."))

st.markdown("---")

# Visualisasi Utama
col_chart1, col_chart2 = st.columns(2)

with col_chart1:
    st.subheader("Volume Sampel per Faskes")
    faskes_counts = df_filtered['nama_faskes_pengirim'].value_counts()
    st.bar_chart(faskes_counts)

with col_chart2:
    st.subheader("Distribusi Jenis Pemeriksaan")
    tes_counts = df_filtered['jenis_pemeriksaan'].value_counts()
    st.bar_chart(tes_counts)

st.subheader("Tren Pemeriksaan Harian")
daily_counts = df_filtered.groupby('tanggal_pemeriksaan').size()
st.line_chart(daily_counts)

# Tabel Data
st.subheader("Tabel Detail Sample")
st.dataframe(df_filtered, use_container_width=True)