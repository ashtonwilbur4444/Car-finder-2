import streamlit as st
import pandas as pd

# Dummy vehicle data with MMR estimates
dummy_data = [
    {"Make": "Honda", "Model": "Civic", "Year": 2020, "Price (CAD)": 22000, "MMR (USD)": 18000},
    {"Make": "Toyota", "Model": "Corolla", "Year": 2021, "Price (CAD)": 21000, "MMR (USD)": 17500},
    {"Make": "Ford", "Model": "Escape", "Year": 2019, "Price (CAD)": 19000, "MMR (USD)": 16000}
]

exchange_rate = st.number_input("Enter CAD to USD exchange rate", value=1.35)
st.title("🚗 Car Finder – Dummy MMR Test")

data = pd.DataFrame(dummy_data)
data["Price (USD)"] = data["Price (CAD)"] / exchange_rate
data["Profit (USD)"] = data["MMR (USD)"] - data["Price (USD)"]

st.write("All Listings with Dummy MMR:")
st.dataframe(data)

filtered = data[data["Profit (USD)"] > 2000]
st.subheader("Profitable Vehicles (Profit > $2,000 USD):")
st.dataframe(filtered)
