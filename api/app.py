from flask import Flask, request, jsonify
import joblib
from flask_cors import CORS

app = Flask(__name__)
CORS(app)
model = joblib.load('../model/sentiment_model.joblib')

@app.route('/predict', methods=['POST'])
def predict():
    data = request.get_json()
    text = data['text']
    pred = model.predict([text])[0]
    return jsonify({'sentiment': pred})

if __name__ == '__main__':
    app.run(port=5000)
