import streamlit as st
import pandas as pd
from PIL import Image

# Charts
df=pd.read_csv("retail_sales_data.csv")
df['Date']=pd.to_datetime(df['Date'])

# Set page configuration
st.set_page_config(page_title="Miracle App", page_icon="✨", layout="centered")

# Add a hero section with a title and subheader
st.markdown("<h1 style='text-align: center; color: #4B8BBE;'>🌟 Miracle App 🌟</h1>", unsafe_allow_html=True)
st.markdown("<h3 style='text-align: center; color: #306998;'>A beautiful Streamlit demo</h3>", unsafe_allow_html=True)

# Add a decorative horizontal line
st.markdown("---")

# Use columns to add better layout
col1, col2 = st.columns(2)

with col1:
    st.subheader("📌 Description")
    st.write("Welcome to the **Miracle App**! This is a simple yet elegant example of what Streamlit can do.")

with col2:
    st.subheader("🚀 Quick Code")
    st.code("print('Hello World')", language='python')

# Add a callout box
st.success("✨ Tip: You can expand this app with charts, inputs, and much more!")

# Dataframe
st.markdown("---")
st.subheader("💻 Retail Sales Data")
st.dataframe(df)
st.markdown("---")

# Charts
st.subheader("📶 Charts")
st.bar_chart(data=df, x="Date",y="Total Amount")

# Footer or bottom section
st.markdown("---")
st.markdown("<p style='text-align: center; color: gray;'>Made with ❤️ using Streamlit</p>", unsafe_allow_html=True)
