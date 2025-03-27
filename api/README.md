
# AI MindMood API

Welcome to the **AI MindMood API** repository! This project exposes an API to interact with the trained sentiment analysis model. The API allows users to send a text and receive sentiment predictions (either `pos` or `neg`).

## 🔧 API Setup

### Prerequisites

Before you get started, ensure you have the following installed:

- **Python 3.x**
- **pip3** (Python package installer)
- **Flask**
- **joblib**

### 1. Clone the repository

```bash
git clone https://github.com/vijityannapon/ai-mindmood.git
cd ai-mindmood/api
```

### 2. Install dependencies

Run the following command to install the required dependencies:

```bash
pip3 install -r requirements.txt
```

The **requirements.txt** file should contain the necessary libraries, for example:

```
Flask==2.0.1
joblib==1.0.1
```

### 3. Load the trained model

Ensure you have the trained model file `sentiment_model.joblib` in the same directory as your API.

### 4. Start the Flask API

To start the Flask API, run the following command:

```bash
python3 app.py
```

The API will be available at [http://localhost:5000/predict](http://localhost:5000/predict).

### 5. API Usage

To send a POST request with the text to analyze, use the following format:

```bash
curl -X POST http://localhost:5000/predict -H "Content-Type: application/json" -d '{"text": "I love this!"}'
```

The API will respond with the sentiment prediction, for example:

```json
{
  "sentiment": "pos"
}
```

## 💻 Contributing

If you'd like to contribute, feel free to fork the repository and submit pull requests. Here are a few steps to get started:

1. Fork the repository
2. Create a new branch for your feature/bugfix
3. Make your changes and test them
4. Submit a pull request with a description of your changes

## 🔄 License

This project is licensed under the **GNU General Public License v3.0 (GPL-3.0)** - see the [LICENSE](LICENSE) file for details.

