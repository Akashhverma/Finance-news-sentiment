import streamlit as st
import pickle
import time
import tensorflow as tf
from tensorflow.keras.preprocessing.sequence import pad_sequences

# Cache model and tokenizer loading to avoid reloading each time
@st.cache_resource
def load_model():
    model = tf.keras.models.load_model('lstm_model.keras')  # Path to your trained model
    tokenizer = pickle.load(open('tokenizer.pkl', 'rb'))  # Path to your tokenizer
    return model, tokenizer

# Load the trained model and tokenizer once
model, tokenizer = load_model()

# Function to preprocess text input
def preprocess_input(text):
    sequence = tokenizer.texts_to_sequences([text])
    padded_sequence = pad_sequences(sequence, maxlen=71, padding='post')  # Ensure maxlen=71
    return padded_sequence

st.title('Financial News Sentiment Analysis')

tweet = st.text_input('Enter your News')

submit = st.button('Predict')

if submit:
    start = time.time()
    preprocessed_input = preprocess_input(tweet)
    prediction = model.predict(preprocessed_input)
    end = time.time()

    st.write('Prediction time taken: ', round(end-start, 2), 'seconds')
    
    # Decode prediction (if using softmax output with 3 classes)
    predicted_class = ['Negative', 'Neutral', 'Positive'][prediction.argmax()]
    st.write(f"Sentiment: {predicted_class}")

