import streamlit as st
import pandas as pd

upload_file = st.file_uploader('', type='csv')

if upload_file is not None:
    data = pd.read_csv(upload_file)
    st.write(data)