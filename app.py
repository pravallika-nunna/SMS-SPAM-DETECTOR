import streamlit as st
import pickle

# Load the saved model and vectorizer using pickle
with open('naive_bayes_model.pkl', 'rb') as model_file:
    nb_model = pickle.load(model_file)  # Loading Naive Bayes model

with open('count_vectorizer.pkl', 'rb') as vectorizer_file:
    vectorizer = pickle.load(vectorizer_file)  # Loading the vectorizer

# Streamlit app setup
st.set_page_config(page_title="SMS Spam Detection App", page_icon="📱", layout="centered")

# Streamlit title and instructions
st.title("SMS Spam Detection App")
st.write("Enter an SMS message below to detect if it's spam or not:")

# Input text area for SMS
user_input = st.text_area("Type your message here:")

if st.button("Predict"):
    if user_input.strip():
        # Transform the input message into the same format as the training data
        text_vec = vectorizer.transform([user_input])

        # Predict the label (spam or not spam)
        label = nb_model.predict(text_vec)[0]

        # Display classification result
        if label == 1:
            st.markdown('<p style="color:red;">The message is classified as: <strong>Spam</strong></p>', unsafe_allow_html=True)
        else:
            st.success(f"The message is classified as: **Not Spam**")
    else:
        st.warning("Please enter a message to predict.")