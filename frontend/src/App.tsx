import { useState } from "react";
import axios from "axios";

type Language = "th" | "en";

function App() {
  const apiUrl = import.meta.env.VITE_API_URL;

  const messages = {
    th: {
      title: "🧠 AI ทายอารมณ์จากข้อความ",
      placeholder: "พิมพ์ข้อความ เช่น วันนี้ดีมาก",
      button: "ทายอารมณ์",
      result: "ผลลัพธ์",
    },
    en: {
      title: "🧠 AI Sentiment Analyzer",
      placeholder: "Type something like: I feel great today!",
      button: "Analyze",
      result: "Result",
    },
  };

  const [language, setLanguage] = useState<Language>(
    import.meta.env.VITE_DEFAULT_LANGUAGE
  );
  const t = messages[language];

  const [text, setText] = useState("");
  const [result, setResult] = useState("");

  const handlePredict = async () => {
    const res = await axios.post(`${apiUrl}/predict`, { text });
    setResult(res.data.sentiment);
  };

  return (
    <div className="w-screen h-screen bg-gradient-to-br from-pink-100 via-orange-100 to-blue-100 text-zinc-900 font-notosans flex items-center justify-center px-4">
      <div className="bg-white/80 rounded-2xl shadow-xl p-8 max-w-md w-full text-center backdrop-blur-md relative">
        <div className="absolute top-4 right-4">
          <button
            onClick={() => setLanguage(language === "th" ? "en" : "th")}
            className="px-4 py-2 bg-gray-800 text-white rounded-md text-sm font-semibold hover:bg-gray-700 transition duration-300"
          >
            {language === "th" ? "Switch to English" : "เปลี่ยนเป็นภาษาไทย"}
          </button>
        </div>

        <h1 className="text-3xl font-bold mb-6 mt-12">{t.title}</h1>

        <div className="flex items-stretch w-full">
          <input
            type="text"
            value={text}
            onChange={(e) => setText(e.target.value)}
            placeholder={t.placeholder}
            className="px-4 py-2 text-sm text-black rounded-l-md border border-gray-300 w-full focus:outline-none"
          />
          <button
            onClick={handlePredict}
            className="px-4 py-2 text-sm whitespace-nowrap rounded-r-md bg-zinc-900 text-white font-semibold hover:bg-zinc-800"
          >
            {t.button}
          </button>
        </div>

        {result && (
          <div className="mt-6 text-xl">
            👉 <span className="font-bold">{t.result}:</span>{" "}
            <span
              className={`$\{result === "pos" ? "text-green-500" : result === "neg" ? "text-red-500" : "text-yellow-500"} font-semibold`}
            >
              {result}
            </span>
          </div>
        )}
      </div>
    </div>
  );
}

export default App;
