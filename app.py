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

# Function to get Gemini explanation (or your explanation logic)
def get_explanation(text, model, vectorizer):
    # Transform the input message into the same format as the training data
    text_vec = vectorizer.transform([text])
    
    # Predict the label (spam or not spam)
    prediction = model.predict(text_vec)
    
    # Get explanation for the classification (this is a placeholder for the Gemini method)
    explanation = "The model detected specific keywords related to spam, such as 'free', 'win', or 'urgent'."
    
    return prediction[0], explanation

if st.button("Predict"):
    if user_input.strip():
        # Step 1: Get prediction and explanation
        label, explanation = get_explanation(user_input, nb_model, vectorizer)
        
        # Step 2: Display classification result
        if label == 1:
            st.markdown('<p style="color:red;">The message is classified as: <strong>Spam</strong></p>', unsafe_allow_html=True)
        else:
            st.success(f"The message is classified as: **Not Spam**")
        
        # Step 3: Display explanation
        st.write("### Reason for classification:")
        st.write(explanation)  # Display the reason behind the classification
    else:
        st.warning("Please enter a message to predict.")