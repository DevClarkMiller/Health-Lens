import streamlit as st
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

st.title("Data Visualization App")

# Generate random data
@st.cache_data
def generate_data():
    return pd.DataFrame(
        np.random.randn(100, 3),
        columns=['A', 'B', 'C']
    )

df = generate_data()

# Sidebar controls
st.sidebar.header("Controls")
column = st.sidebar.selectbox("Select Column", df.columns)
chart_type = st.sidebar.radio("Chart Type", ["Line", "Histogram", "Scatter"])

# Display data
st.subheader("Raw Data")
st.dataframe(df)

# Create visualization
st.subheader(f"{chart_type} Chart for Column {column}")
if chart_type == "Line":
    st.line_chart(df[column])
elif chart_type == "Histogram":
    fig, ax = plt.subplots()
    ax.hist(df[column], bins=20)
    st.pyplot(fig)
else:
    st.scatter_chart(df[column])

