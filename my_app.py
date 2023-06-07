import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt

st.set_page_config(page_title='Kevin Liu Participation Project', page_icon=':alien:', layout='wide')
st.title('A simple EDA application')

file = st.file_uploader('Upload CSV file', type='csv')
if file is not None:
    df = pd.read_csv(file)

    st.write('Rows:', df.shape[0])
    st.write('Columns:', df.shape[1])
    st.write('Categorical variables:', df.select_dtypes(include='object').shape[1])
    st.write('Numerical variables:', df.select_dtypes(include='number').shape[1])
    st.write('Boolean variables:', df.select_dtypes(include='bool').shape[1])

    selected_col = st.selectbox('Select column', df.columns)

    if selected_col:
        col_type = df[selected_col].dtype

        if col_type in ['int64', 'float64']:
            five_num = df[selected_col].describe()[['min', '25%', '50%', '75%', 'max']]
            st.write('Five number summary:', five_num)

            fig, ax = plt.subplots()
            ax.hist(df[selected_col], color='green', alpha=0.5)
            ax.set_title('Histogram of ' + selected_col)
            ax.set_xlabel(selected_col)
            ax.set_ylabel('Frequency')
            st.pyplot(fig)
        
        if col_type == 'object':
            category_props = df[selected_col].value_counts(normalize=True)
            st.write('Proportions of each category: ', category_props)

            fig, ax = plt.subplots()
            ax.bar(df[selected_col].value_counts().keys(), df[selected_col].value_counts(), color='green', alpha=0.5)
            ax.set_title('Bar plot of ' + selected_col)
            ax.set_xlabel(selected_col)
            ax.set_ylabel('Frequency')
            st.pyplot(fig)