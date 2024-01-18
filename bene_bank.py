import pandas as pd
import streamlit as st

def populate_bene_bank_location(df, key_df):
    try:
        # Merge the main DataFrame with the key DataFrame, keeping all columns from the main DataFrame
        merged_df = df.merge(key_df, left_on='Buy Currency', right_on='Currency', how='left')

        # Update the Bene Bank Location with the Country from the key DataFrame
        df['Bene Bank Location'] = merged_df['Country']

        return df

    except Exception as e:
        st.error("Error: " + str(e))
        return df  # Return the original DataFrame in case of an error
