import nltk
import pickle
import streamlit as st
import re
import tensorflow as tf
from nltk.corpus import stopwords
from nltk.tokenize import word_tokenize
from tensorflow.keras.preprocessing.sequence import pad_sequences
from tensorflow.keras.models import load_model
from tensorflow.keras.layers import LSTM
from nltk.tokenize import RegexpTokenizer

def run():
    # gambar dengan st.image
    st.image('https://upload.wikimedia.org/wikipedia/commons/0/02/TripAdvisor_Logo.svg')

    st.markdown('''
    ###### In the hospitality industry, customer reviews play a very important role in shaping a hotel's reputation. Customers tend to choose hotels based on the experiences of previous guests, which is reflected in the reviews and ratings given on platforms such as TripAdvisor. The TripAdvisor Hotel Reviews dataset contains a collection of customer reviews about the hotels they visited, along with the ratings they gave. This data can be used to analyze customer sentiment, understand customer satisfaction factors, and identify aspects that need improvement in hotel services.
                    ''')



