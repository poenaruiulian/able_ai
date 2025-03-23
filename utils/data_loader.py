import pandas as pd
import streamlit as st

@st.cache_data
def load_dataset(file_path: str) -> pd.DataFrame:
    try:
        df = pd.read_csv(file_path, on_bad_lines='skip', engine='python')
    except pd.errors.ParserError as e:
        print(f"ParserError: {e}")
        # Optionally, you could try other parameters or log the error for further investigation.
        df = pd.DataFrame()  # Return an empty DataFrame or handle accordingly
    return df
