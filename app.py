import pandas as pd
import streamlit as st

def upload_and_process(uploaded_file):
    try:
        if uploaded_file:
            df = pd.read_excel(uploaded_file, sheet_name='Sheet1')

            column_types = {
                # Your column types here
            }
            df = df.astype(column_types)
            df = df.sort_values(by='Sub Company', ascending=True)
            df_filtered = df[df['DTCREATEDATE'].notna()]

            output_file_path = "Filtered_Client_Master_File.xlsx"
            df_filtered.to_excel(output_file_path, index=False)

            st.success("File processed and saved as 'Filtered_Client_Master_File.xlsx'")
            return output_file_path
        else:
            st.warning("No file selected")
    except Exception as e:
        st.error("Error: " + str(e))

st.title("ShipMoney File Processor for Client Master")
st.write("Upload Client Master Excel File by clicking the button below")

uploaded_file = st.file_uploader("Upload here and Process", type=['xlsx'])
if uploaded_file is not None:
    processed_file_path = upload_and_process(uploaded_file)
    if processed_file_path:
        with open(processed_file_path, "rb") as file:
            st.download_button(
                label="Download Processed File",
                data=file,
                file_name=processed_file_path,
                mime="application/vnd.openxmlformats-officedocument.spreadsheetml.sheet"
            )
