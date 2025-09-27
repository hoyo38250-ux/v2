import streamlit as st
options = ('Email', 'Dien thoai ban', 'Dien thoai di dong')
option = st.selectbox('Chon phuong tien lien lac',options)
st.write('Ban da chon:', option)

age= st.slider('How old are you?',0,130,25)
st.write('Im',age,'years old')

s = 'hi'
st.download_button = ('download',s)