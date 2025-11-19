import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt

st.title("Aplikasi Visualisasi Data Sederhana")
st.write("Selamat datang di aplikasi visualisasi data sederhana menggunakan Streamlit!")

data = pd.DataFrame(data={
    "Kampanye": ["Kampanye A", "Kampanye B", "Kampanye C", "Kampanye D"],
    "Total Donasi (Juta Rupiah)": [50, 75, 30, 90],
})

st.subheader("Data Kampanye Donasi")
st.dataframe(data)

# Bar Chart
st.bar_chart(data.set_index(keys = "Kampanye"))

# Line Chart
st.line_chart(data.set_index("Kampanye"))

# Matplotlib Plot

fig, ax = plt.subplots()
ax.pie(data["Total Donasi (Juta Rupiah)"], labels=data["Kampanye"], autopct='%1.1f%%', colors=['green', 'blue', 'red', 'orange'])
ax.set_title("Pie Chart Donasi")
st.pyplot(fig)

# Dropdown
tipe = st.selectbox("Jenis Grafik", ["Bar Chart", "Line Chart", "Pie Chart"])

if tipe == "Bar Chart":
    st.bar_chart(data.set_index(keys="Kampanye"))
elif tipe == "Line Chart":
    st.line_chart(data.set_index(keys="Kampanye"))
else:
    fig, ax = plt.subplots()
    ax.pie(data["Total Donasi (Juta Rupiah)"], labels=data["Kampanye"], autopct='%1.1f%%')
    st.pyplot(fig)

# Slider
nilai = st.slider("Tampilkan data dengan donasi minimum:", 0, 150, 50)
st.dataframe(data[data["Total Donasi (Juta Rupiah)"] >= nilai])

# Geospasial
st.title("Peta Lokasi Penanaman")

data_peta = pd.DataFrame(data={
    'lokasi': ['Balikpapan', 'Samboja', 'Mahakam'],
    'lat': [-1.27, -1.10, 0.50],
    'lon': [116.83, 117.00, 117.25]
})

st.map(data_peta)

# Dashboard
st.title("Dashboard Donasi Lingkungan")

data = pd.DataFrame(data={
    "Kampanye": ["Mangrove Balikpapan", "Pantai Samboja", "Delta Mahakam"],
    "Donasi": [120, 85, 60],
    "Target": [150, 100, 90]
})

kampanye = st.selectbox("Pilih Kampanye:", data["Kampanye"])
row = data[data["Kampanye"] == kampanye].iloc[0]

st.metric("Donasi Saat Ini", f"{row['Donasi']} juta", delta=row['Donasi'] - row['Target'])
st.progress(row['Donasi'] / row['Target'])

fig, ax = plt.subplots()
ax.bar(data["Kampanye"], data["Donasi"])
ax.set_ylabel("Donasi (Juta Rupiah)")
# ax.set_title("Perbandingan Donasi per Kampanye")
st.pyplot(fig)

# Masukkan Image
st.image("varrel.jpg", caption="Menanam Varrel di Pantai Samboja")
st.markdown("Gambar di atas menunjukkan proses penanaman varrel di Pantai Samboja sebagai bagian dari upaya pelestarian lingkungan.")
