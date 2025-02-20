import streamlit as st
import page
import predict

with st.sidebar:
    st.title('Navigation')
    Navigation = st.selectbox('',['Home','Predict Sentiment Analysis'])

    st.write('___')

if Navigation == 'Home':
    page.run()
else:
    predict.run()
