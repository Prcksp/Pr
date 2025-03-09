import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt

day_df = pd.read_csv("Data/day.csv")
hour_df = pd.read_csv("Data/hour.csv")

if 'dteday' in day_df.columns:
    day_df['dteday'] = pd.to_datetime(day_df['dteday'])
    hour_df['dteday'] = pd.to_datetime(hour_df['dteday'])

if 'dteday' not in day_df.columns:
    st.write("Kolom tanggal tidak ditemukan dalam dataset.")
    st.stop()

st.title("Dashboard Penyewaan Sepeda")

st.subheader("Data Penyewaan Sepeda Harian")
st.dataframe(day_df)

st.subheader("Data Penyewaan Sepeda Per Jam")
st.dataframe(hour_df)

st.subheader("Statistik Data Harian")
st.write(day_df.describe())

st.subheader("Statistik Data Per Jam")
st.write(hour_df.describe())

st.subheader("Grafik Penyewaan Sepeda Harian")
selected_day = st.selectbox("Pilih Tanggal", day_df["dteday"].unique())
filtered_hour_df = hour_df[hour_df["dteday"] == selected_day]
fig, ax = plt.subplots()
ax.plot(day_df["dteday"], day_df["cnt"], marker='o', linestyle='-', color='b')
ax.set_xlabel("Tanggal")
ax.set_ylabel("Jumlah Penyewaan")
ax.set_title(f"Jumlah Penyewaan Sepeda per Hari {selected_day}")
plt.xticks(rotation=45)
st.pyplot(fig)

st.subheader("Grafik Penyewaan Sepeda Per Jam")
selected_day = st.selectbox("Pilih jam", day_df["dteday"].unique())
filtered_hour_df = hour_df[hour_df["dteday"] == selected_day]

fig, ax = plt.subplots()
ax.plot(filtered_hour_df["hr"], filtered_hour_df["cnt"], marker='o', linestyle='-', color='r')
ax.set_xlabel("Jam")
ax.set_ylabel("Jumlah Penyewaan")
ax.set_title(f"Jumlah Penyewaan Sepeda per Jam pada {selected_day}")
st.pyplot(fig)

st.write("Dashboard ini menampilkan data penyewaan sepeda berdasarkan data harian dan per jam.")