import pandas as pd
def process_client_master(uploaded_file):
    try:
        if uploaded_file:
            df = pd.read_excel(uploaded_file, sheet_name='Sheet1')

            column_types = {
                "DTCREATEDATE": "datetime64[ns]",
                "DTLASTUPDATE": "datetime64[ns]",
                "CardRange": "int64",
                "BIN": "int64",
                "CurrencyCode": "str",
                "NBSUBCOMPANY": "int64",
                "NBCOMPANY": "int64",
                "Sub Company": "str",
                "Company": "str",
                "MV_SHIPMONEY_PARTNERS.PARTNER_ID": "str",  
                "SEGMENT": "str",
                "COMPANY NAME": "str",
                "Referring Account Name -AFEX": "str",
                "Referring Account Number-AFEX": "str",
                "Distribution Account": "int64",
                "Ticket Company Master": "str",
                "Western Union Master": "str",
                "Spend Company Master": "str",
                "KAM": "str",
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