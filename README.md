# SMS Spam Detection App  

## Overview  
This project is a **Machine Learning-based SMS Spam Detector** that classifies text messages as either **Spam** or **Not Spam** using **Naive Bayes Classifier**. It includes data preprocessing, model training, evaluation, and deployment via a **Streamlit web app**.  

## Table of Contents  
1. [Introduction](#introduction)  
2. [Installation](#installation)  
3. [Usage](#usage)  
4. [Dataset](#dataset)  
5. [Project Workflow](#project-workflow)  
6. [Model Training & Evaluation](#model-training--evaluation)  
7. [Deployment with Streamlit](#deployment-with-streamlit)  
8. [Requirements](#requirements)  
9. [Future Enhancements](#future-enhancements)  
10. [Contributors](#contributors)  

---

## Introduction  
Spam messages can be annoying and potentially harmful. This project uses **Natural Language Processing (NLP) techniques** to filter out spam messages.  

## Installation  
To run this project locally, follow these steps:  

1. Clone the repository:  
   ```sh
   git clone https://github.com/your-username/sms-spam-detector.git
   cd sms-spam-detector
Here is a `README.md` file for your project:  

2. Create a virtual environment:  
   ```sh
   python -m venv venv
   source venv/bin/activate  # On Windows use: venv\Scripts\activate
   ```  
3. Install dependencies:  
   ```sh
   pip install -r requirements.txt
   ```  

## Usage  
Run the **Streamlit app** with:  
```sh
streamlit run app.py
```  

## Dataset  
The dataset used for training consists of labeled SMS messages:  
- **ham** (not spam)  
- **spam** 

### Dataset sources
- Kaggle - https://www.kaggle.com/datasets/jackksoncsie/spam-email-dataset
- UC Irvine Machine LEarning Repository - https://archive.ics.uci.edu/dataset/228/sms+spam+collection

## Project Workflow  
1. **Data Preprocessing**  
   - Removing duplicates and missing values  
   - Label encoding (spam = 1, not spam = 0)  
   - Adding features like message length and special characters  
2. **Text Processing & Vectorization**  
   - Tokenization  
   - Bag-of-Words (CountVectorizer)  
3. **Model Training**  
   - **Naive Bayes Classifier** (MultinomialNB)  
4. **Evaluation**  
   - Accuracy  
   - F1 Score  
   - Classification Report
   - Confusion Matrix  

## Model Training & Evaluation  
- The trained model is saved using **Pickle** for later use.  
- Performance metrics:  
  - Accuracy, Precision, Recall, F1 Score  
  - Confusion Matrix  

## Deployment with Streamlit  
- The saved model is used in a **Streamlit web app** for real-time spam detection.  

## Requirements  
- Python 3.x  
- Required packages: *(Listed in `requirements.txt`)*  

## Future Enhancements  
- Improve feature extraction using **TF-IDF**  
- Integrate **LSTM-based deep learning models**  
- Deploy as a web API  