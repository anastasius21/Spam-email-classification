import streamlit as st
import pickle
import re
from nltk.stem import PorterStemmer
from nltk.corpus import stopwords

model = pickle.load(open('model.pkl','rb'))
vect = pickle.load(open('vector.pkl','rb'))

stop_words = set(stopwords.words('english'))
ps = PorterStemmer()

def stemming(content):
    cleaned_text = re.sub('[^a-zA-Z]', ' ',content)
    cleaned_text = cleaned_text.lower()
    cleaned_text = cleaned_text.split()
    cleaned_text = [ps.stem(txt) for txt in cleaned_text if not txt in stop_words]
    cleaned_text = ' '.join(cleaned_text)
    return cleaned_text

st.header('Spam Email Classification App')
t_ext = st.text_area('Enter the email below')
but = st.button('Predict')

if but:
    cleanText = stemming(t_ext)
    vectorized = vect.transform([cleanText])
    Prediction = model.predict(vectorized)[0]
    if Prediction == [0]:
        st.success('The given email is not spam')
    if Prediction == [1]:
        st.warning('The given email is spam')

    