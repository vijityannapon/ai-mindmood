
# AI MindMood Model

Welcome to the **AI MindMood Model** repository! This project contains the trained sentiment analysis model that predicts whether a given text is positive or negative. The model is trained using **Naive Bayes** classifier and is intended to be used with the **frontend** of the **AI MindMood** application.

## 🔧 Model Setup

### Prerequisites

Before you get started, ensure you have the following installed:

- **Python 3.x**
- **pip3** (Python package installer)
- **scikit-learn**
- **joblib**

### 1. Clone the repository

```bash
git clone https://github.com/vijityannapon/ai-mindmood.git
cd ai-mindmood/model
```

### 2. Install dependencies

Run the following command to install the required dependencies:

```bash
pip3 install -r requirements.txt
```

The **requirements.txt** file should contain the necessary libraries, for example:

```
scikit-learn==0.24.2
joblib==1.0.1
```

### 3. Train the model

To train the sentiment analysis model using the provided dataset, you can run the following script:

```bash
python3 train_model.py
```

This will:
- Train the model using the provided positive and negative text data (both in English and Thai).
- Save the trained model to a file `sentiment_model.joblib`.

### 4. Using the trained model

To load and use the trained model for prediction, use the following code:

```python
import joblib

# Load the trained model
model = joblib.load('sentiment_model.joblib')

# Predict sentiment
text = "I love this!"
prediction = model.predict([text])
print("Predicted sentiment:", prediction[0])
```

## 📝 Model Details

The model is trained using **scikit-learn**'s **Naive Bayes** classifier. The steps for training are as follows:

1. **Data Preprocessing**: The positive and negative text data is tokenized and vectorized using **CountVectorizer**.
2. **Training**: The model is trained using a **Multinomial Naive Bayes** classifier.
3. **Model Serialization**: The trained model is saved using **joblib** for later use.

## 💻 Contributing

If you'd like to contribute, feel free to fork the repository and submit pull requests. Here are a few steps to get started:

1. Fork the repository
2. Create a new branch for your feature/bugfix
3. Make your changes and test them
4. Submit a pull request with a description of your changes

## 🔄 License

This project is licensed under the **GNU General Public License v3.0 (GPL-3.0)** - see the [LICENSE](LICENSE) file for details.

