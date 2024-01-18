import pandas as pd
import streamlit as st
from functions_toclean_data import process_client_master
from corpay_clean import process_file_corpay

st.title("ShipMoney File Processor for Client Master")
st.write("Upload Client Master Excel File by clicking the button below")

uploaded_file = st.file_uploader("Upload here and Process", type=['xlsx'])
if uploaded_file is not None:
    processed_file_path = process_client_master(uploaded_file)
    if processed_file_path:
        with open(processed_file_path, "rb") as file:
            st.download_button(
                label="Download Processed File",
                data=file,
                file_name=processed_file_path,
                mime="application/vnd.openxmlformats-officedocument.spreadsheetml.sheet"
            )
st.write("Upload Card Registration Excel File by clicking the button below")

uploaded_file = st.file_uploader("Upload here and Process", type=['xlsx'])
if uploaded_file is not None:
    processed_file_path2 = process_file_corpay(uploaded_file)
    if processed_file_path2:
        with open(processed_file_path2, "rb") as file:
            st.download_button(
                label="Download Processed File",
                data=file,
                file_name=processed_file_path2,
                mime="application/vnd.openxmlformats-officedocument.spreadsheetml.sheet"
            )