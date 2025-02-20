# 🚀 Sentiment Analysis of TripAdvisor Hotel Reviews

## 📌 Project Overview

This project focuses on **Sentiment Analysis of TripAdvisor Hotel Reviews** using **Deep Learning**. Customer reviews play a crucial role in shaping a hotel's reputation. By leveraging **Natural Language Processing (NLP)** and **Deep Learning**, we analyze customer sentiment to understand satisfaction factors and identify areas that need improvement in hotel services.

🔗 **Dataset Source:** [Kaggle - TripAdvisor Hotel Reviews](https://www.kaggle.com/datasets/andrewmvd/trip-advisor-hotel-reviews/data)\
🔗 **Application Deployment:** [Hugging Face Spaces](https://huggingface.co/spaces/AzkaIrsyad/SentimenAnalysist_TripAdvisor)\
🔗 **Model Improvements:** [Google Drive](https://drive.google.com/drive/folders/1MHjBiDE4f1jlib2fVPLhY99iDoiSqamQ?usp=sharing)

---

## 📂 Project Structure

```
|-- app.py          # Main Streamlit application file
|-- predict.py      # Sentiment prediction logic
|-- page.py         # Home page UI
|-- sentiment_model.h5  # Pre-trained sentiment analysis model
|-- tokenizer.pkl   # Tokenizer for text preprocessing
|-- tripadvisor_hotel_reviews.csv  # Dataset
|-- requirements.txt  # Required dependencies
```

---

## 🔍 Implementation Details

### 🔹 Sentiment Analysis Model

- **Model:** LSTM-based Deep Learning model
- **Preprocessing Steps:**
  - Tokenization, stopword removal, text cleaning
  - Padding sequences to standardize input length
- **Training Data:** TripAdvisor Hotel Reviews dataset
- **Evaluation Metrics:** Accuracy, Precision, Recall
- **Deployment:** Implemented using Streamlit for an interactive interface

### 🔹 Model Training & Evaluation

- **Architecture:**
  - Embedding Layer → LSTM Layer → Dense Layer
  - Dropout Regularization to prevent overfitting
- **Optimization:**
  - Adam Optimizer with a learning rate of 0.001
  - Categorical Cross-Entropy Loss Function
- **Evaluation Results:**
  - **Accuracy:** 85.3%
  - **Precision:** 83.7%
  - **Recall:** 84.5%

### 🔹 Model Deployment & Features

- **Home Page (`page.py`)** → Displays project overview and dataset description.
- **Prediction Page (`predict.py`)** → Users can enter hotel reviews and get sentiment predictions.
- **Sentiment Categories:**
  - **Positive** (Good reviews)
  - **Neutral** (Moderate reviews)
  - **Negative** (Bad reviews)

---

## 🏗️ How to Run the Application

### 🔹 1. Install Dependencies

Ensure **Python & Streamlit** are installed, then run:

```bash
# Install required dependencies
$ pip install -r requirements.txt
```

### 🔹 2. Run the Streamlit Application

```bash
# Run sentiment analysis application
$ streamlit run app.py
```

### 🔹 3. Navigate the Application

- **Home Page:** Project overview.
- **Sentiment Analysis Prediction:** Enter a review and analyze its sentiment.

---

## 🚀 Challenges & Future Improvements

### 🔹 Challenges Faced

- Handling **sarcasm and implicit sentiment** in hotel reviews
- Addressing **class imbalance**, where positive reviews dominate
- Optimizing the model to **reduce inference time** without sacrificing accuracy

### 🔹 Potential Enhancements

- **Improve Sentiment Classification:**
  - Experiment with **Transformer-based models** like BERT for better accuracy
  - Implement **Aspect-Based Sentiment Analysis (ABSA)** for deeper insights
- **Expand Data Sources:**
  - Integrate reviews from multiple platforms (e.g., Yelp, Google Reviews)
- **Deploy as an API:**
  - Provide the sentiment analysis model as a **REST API** for easier integration with other applications

---

## 📊 Results & Insights

✅ **Real-time sentiment prediction** based on hotel reviews.\
✅ **Deep Learning-powered model** for better accuracy.\
✅ **Deployed and accessible** to the public.\
✅ **Potential future improvements** with advanced NLP techniques.

---

## 👤 Author
**Azka Irsyad Choir**  
📧 Email: [azkairsyad24@gmail.com](mailto:azkairsyad24@gmail.com)  
🔗 LinkedIn: [linkedin.com/in/azkairsyad](https://www.linkedin.com/in/azka-irsyad-aa2509191/)  
🐱 GitHub: [github.com/azka irsyad](https://github.com/Azka24-ui)  
