
# Frontend: AI MindMood

Welcome to the **AI MindMood** frontend! This project is the user interface for the **AI Sentiment Analysis** application that allows users to input text and receive sentiment predictions. The frontend is built using **React** and **Tailwind CSS**.

## 🔧 Project Setup

### Prerequisites

Before you get started, ensure you have **Node.js** installed. You can download and install it from [here](https://nodejs.org/).

### 1. Clone the repository

```bash
git clone https://github.com/vijityannapon/ai-mindmood.git
cd ai-mindmood/frontend
```

### 2. Install dependencies

Run the following command to install the required dependencies:

```bash
npm install
```

### 3. Set up environment variables

Before running the project, you need to create a `.env` file from the `.env.example` template. Follow these steps:

1. Copy the `.env.example` file and rename it to `.env`:
   ```bash
   cp .env.example .env
   ```

2. Open the newly created `.env` file and update the values with your settings:
   
   ```env
   VITE_API_URL=http://127.0.0.1:5000
   VITE_DEFAULT_LANGUAGE=en
   ```

   - **`VITE_API_URL`**: The URL of the backend API for sentiment analysis.
     - Example: `http://127.0.0.1:5000` (default backend URL).
   
   - **`VITE_DEFAULT_LANGUAGE`**: The default language of the app. You can set it to `en` for English or `th` for Thai.
     - Example: `en` (default language).


### 4. Start the development server

To run the application locally, use:

```bash
npm run dev
```

The app will be available at [http://localhost:5173](http://localhost:5173).

## 📝 Features

- **Sentiment Analysis**: Input text and get a prediction of whether it's positive, negative, or neutral.
- **Language Switch**: Toggle between Thai and English for the interface.
- **Responsive Design**: The app is fully responsive and works well on both desktop and mobile devices.
- **Stylish UI**: The app uses Tailwind CSS for a clean and modern design, with a gradient background.

## 🌐 Live Demo

You can try the live demo of the app here: [AI MindMood Demo](https://your-demo-link.com)

## 🎨 Technologies Used

- **React**: For building the user interface.
- **Tailwind CSS**: For styling and responsive design.
- **Axios**: For making API requests to the backend.

## 🔧 API Integration

The frontend communicates with the **AI Sentiment Analysis API** for text sentiment analysis. Ensure the backend server is running on [http://localhost:5000](http://localhost:5000) (or update the API endpoint in the code if needed).

## 💻 Contributing

If you'd like to contribute, feel free to fork the repository and submit pull requests. Here are a few steps to get started:

1. Fork the repository
2. Create a new branch for your feature/bugfix
3. Install the dependencies and run the app locally
4. Make your changes and test them
5. Submit a pull request with a description of your changes

## 🚀 Deployment

If you want to deploy this app, you can use platforms like **Vercel** or **Netlify**. Simply link the repository and follow their deployment instructions.

---

## 💬 Contact

If you have any questions or feedback, feel free to reach out to the project maintainers.

---

## 🔄 License

This project is licensed under the **GNU General Public License v3.0 (GPL-3.0)** - see the [LICENSE](LICENSE) file for details.
