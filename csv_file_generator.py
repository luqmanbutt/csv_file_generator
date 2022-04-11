import pandas
import streamlit as st
import pandas as pd
import plotly.express as px
import seaborn as sns
from io import BytesIO
from pyxlsb import open_workbook as open_xlsb
import streamlit as st

def main():
    st.header("Web App")
    
    df = sns.load_dataset('iris')
    # IMPORTANT: Cache the conversion to prevent computation on every rerun
    @st.cache
    def convert_df(df):

        return df.to_csv().encode('utf-8')



    #converting the sample dataframe
    csv = convert_df(df)

    #adding a download button to download csv file
    st.download_button( 

    label="Download data as CSV",

    data=csv,

    file_name='sample_df.csv',

    mime='text/csv',

)





# main
if __name__ == '__main__':
    main()