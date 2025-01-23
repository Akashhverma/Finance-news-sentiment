# Financial News Sentiment Analysis

## Overview
This project involves building a sentiment analysis model to classify financial news articles as positive, neutral, or negative. The aim is to assist financial analysts, traders, and organizations in making informed decisions based on the sentiment of news articles.
The project uses _LSTM (Long Short-Term Memory)_ and _GRU (Gated Recurrent Unit)_ neural networks for text classification. The trained model is deployed using Streamlit, providing an interactive web interface for real-time sentiment prediction.

## Features
1.Classify financial news into three sentiment categories: Positive, Neutral, and Negative.
2.Interactive UI for real-time predictions using Streamlit.
3.Comparison of LSTM and GRU models to identify the optimal approach for sentiment analysis.
4.Tokenization and preprocessing of text data to handle variable-length sequences.

## Technologies Used
### Programming Languages: Python
### Libraries and Frameworks:
#### TensorFlow: For building and training the deep learning models.
#### NumPy and Pandas: For data preprocessing and manipulation.
#### Scikit-learn: For splitting data into training and testing sets.
#### Streamlit: For deploying the model with a user-friendly web interface.

## Project Workflow
### Data Preprocessing:
Tokenization of text data to convert words into numeric sequences.
Padding sequences to ensure uniform input length for the model.
### Label mapping:
Assigning numeric values to sentiment labels (0: Negative, 1: Neutral, 2: Positive).
### Model Development:
#### LSTM Model:
Embedding layer for converting tokens into dense vectors.
LSTM layer to capture long-term dependencies in text.
Dense layer with softmax activation for multi-class classification.
#### GRU Model:
Similar to the LSTM model but with a GRU layer for faster training and comparable accuracy.

## Evaluation:
Models are evaluated using accuracy and a confusion matrix.
Comparison of LSTM and GRU models based on performance metrics.

## Deployment:
Deployed locally using Streamlit.
Plans for Streamlit Cloud deployment for broader accessibility.

## How to Run the Project
### Prerequisites:
Python 3.7 or higher
Necessary libraries listed in requirements.txt (TensorFlow, Streamlit, etc.)
### Steps:
#### Clone the repository:
git clone <https://github.com/Akashhverma/Finance-news-sentiment>
cd <Akashhverma/Finance-news-sentiment>
#### Install the required libraries:
pip install -r requirements.txt
#### Run the Streamlit app:
streamlit run app.py
Open the local server link (e.g., http://localhost:8501) in your browser to access the web app.

## Results
Achieved 72.90% , 74.00% accuracy with the LSTM model and GRU model.
GRU model provided comparable performance with faster training times.
Insights on the impact of different preprocessing and architectural choices.


![Screenshot 2025-01-23 104342](https://github.com/user-attachments/assets/2e4ca799-4609-428a-a9e8-7f55719cb095)


![image](https://github.com/user-attachments/assets/7bd0354d-251a-4604-926f-d5d6ffc8a4d9)




## Future Improvements
### Use of Pre-trained Embeddings:
Incorporate embeddings like GloVe or Word2Vec for improved context understanding.
### Deployment on Streamlit Cloud:
Make the app accessible online for wider use.
### Multilingual Sentiment Analysis:
Extend the model to handle financial news in multiple languages.
### Integration with Financial Tools:
Link predictions with stock market analysis tools for automated decision-making.

## Contributions
Contributions to this project are welcome! Feel free to fork the repository and raise a pull request with your changes.

##Contact
For questions or feedback, feel free to reach out via:
### Email: akashverma35722@gmail.com
### LinkedIn: https://www.linkedin.com/in/akash-verma-525a88145/

Thank you for checking out this project! If you find it helpful, please give it a star on GitHub! ⭐
