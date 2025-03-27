
# AI MindMood

**AI MindMood** is a sentiment analysis project built with React and Flask, utilizing machine learning models trained on text data in both English and Thai. The application predicts whether a given text expresses a positive or negative sentiment.

## 🔧 Project Structure

The project consists of the following parts:

1. **Frontend**: Built with React and Vite, providing the user interface for inputting text and receiving sentiment predictions.
2. **Model**: The trained sentiment analysis model using **Naive Bayes** classifier.
3. **API**: The backend API, built with Flask, to serve the sentiment model and handle text predictions.

## 🛠️ Prerequisites

Before running the project, ensure you have the following installed:

- **Node.js** (for the frontend)
- **Python 3.x** (for the model and API)
- **pip3** (Python package installer)

## ⚡ Getting Started

### 1. Clone the repository

Clone the project repository to your local machine:

```bash
git clone https://github.com/vijityannapon/ai-mindmood.git
cd ai-mindmood
```

### 2. Setting up Frontend

To set up and run the **frontend**:

```bash
cd frontend
npm install
npm run dev
```

The frontend will be available at [http://localhost:5173](http://localhost:5173).

### 3. Setting up Model

To train and use the **sentiment analysis model**, follow these steps:

```bash
cd model
pip3 install -r requirements.txt
python3 train_model.py
```

This will train the model using the provided datasets and save the trained model to `sentiment_model.joblib`.

### 4. Setting up API

To set up and run the **API** for predictions:

```bash
cd api
pip3 install -r requirements.txt
python3 app.py
```

The API will be available at [http://localhost:5000/predict](http://localhost:5000/predict).

### 5. Environment Variables

You need to configure environment variables before running the project. Create a `.env` file from the `.env.example` template and adjust the values:

```bash
cp .env.example .env
```

Update the `.env` file with the following variables:

```env
VITE_API_URL=http://127.0.0.1:5000
VITE_DEFAULT_LANGUAGE=en
```

### 6. Running the Project

Now, you can run the **frontend** and **API** locally as described above. Ensure both are running to interact with the application.

## 📝 Features

- **Sentiment Analysis**: Input text and get a prediction of whether it's positive, negative, or neutral.
- **Language Switch**: Toggle between Thai and English for the interface.
- **Responsive Design**: The app is fully responsive and works well on both desktop and mobile devices.
- **Stylish UI**: The app uses Tailwind CSS for a clean and modern design.

## 🔧 Technologies Used

- **React**: For building the user interface.
- **Vite**: For faster and modern web development in React.
- **Tailwind CSS**: For styling and responsive design.
- **Flask**: For serving the sentiment analysis model as an API.
- **Scikit-learn**: For training the sentiment analysis model.
- **joblib**: For saving and loading the trained model.

## 🚀 Deployment

For deployment, you can host the frontend on platforms like **Vercel** or **Netlify** and deploy the API on a server such as **Heroku** or **AWS**.

## 💻 Contributing

Feel free to fork the repository, make changes, and submit pull requests. Here’s how you can contribute:

1. Fork the repository
2. Create a new branch for your feature or bugfix
3. Install the dependencies and run the app locally
4. Make your changes and test them
5. Submit a pull request with a description of your changes

## 🔄 License

This project is licensed under the **GNU General Public License v3.0 (GPL-3.0)** - see the [LICENSE](LICENSE) file for details.

---

## 💬 Contact

If you have any questions or feedback, feel free to reach out to the project maintainers.
