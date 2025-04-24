# Spam Email Classification model
Built an Email Classification App using streamlit, which is based on trained Logistic Regression Model. User inputs the email in the text area and the app returns whether the email is spam or not.

# Project Details
First of all, dataset was taken from kaggle (dataset in the repo) but the dataset was not balanced, so balanced the dataset using resampling. The features included was text column which consisted the complete email which was then cleaned using NLP. The cleaned text was then converted to vectors using the TFIDF Vectorizer. The Logistic regression model was then trained on the vectors with a train test split of 80-20. The model returned an accuracy score of 99%.

# Libraries Used
Pandas

Scikit-Learn

NLTK

re

streamlit

pickle
