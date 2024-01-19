import pandas as pd
import streamlit as st
from functions_toclean_data import process_client_master
from corpay_clean import process_file_corpay
from bene_bank import populate_bene_bank_location

st.title("ShipMoney File Processor (Account Management)")
st.subheader("Upload Client Master Excel File by clicking the button below")

uploaded_file = st.file_uploader("Upload here and Process", key="file_uploader_1", type=['xlsx'])
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

st.subheader("Tool to populate Bene Bank location for Corpay")

uploaded_file = st.file_uploader("Upload your main data file", key="file_uploader_3", type=['xlsx'])
key_file = st.file_uploader("Upload your currency-country key file", key="file_uploader_4", type=['xlsx'])

if uploaded_file and key_file:
    # Load the main DataFrame
    df = pd.read_excel(uploaded_file)

    # Load the key DataFrame
    key_df = pd.read_excel(key_file)

    # Process the DataFrame
    processed_df = populate_bene_bank_location(df, key_df)

    # Save the processed DataFrame to a file
    output_file_path = "Populated_BeneBank_File.xlsx"
    processed_df.to_excel(output_file_path, index=False)
    st.success("File processed and saved as 'Populated_BeneBank_File.xlsx'")

    # Provide a download link for the saved file
    with open(output_file_path, "rb") as file:
        st.download_button(
            label="Download Processed File",
            data=file,
            file_name=output_file_path,
            mime="application/vnd.openxmlformats-officedocument.spreadsheetml.sheet"
        )

else:
    st.warning("No files selected")


st.subheader("Upload Card Registration Excel File by clicking the button below")

uploaded_file2 = st.file_uploader("Upload here and Process", key="file_uploader_2", type=['xlsx'])
if uploaded_file2 is not None:
    processed_file_path2 = process_file_corpay(uploaded_file2)
    if processed_file_path2:
        with open(processed_file_path2, "rb") as file:
            st.download_button(
                label="Download Processed File",
                data=file,
                file_name=processed_file_path2,
                mime="application/vnd.openxmlformats-officedocument.spreadsheetml.sheet"
            )
