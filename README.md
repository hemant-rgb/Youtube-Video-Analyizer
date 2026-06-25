# 🎥 AI YouTube Video Analyzer

An AI-powered web application that analyzes YouTube videos and generates structured summaries using Large Language Models (LLMs). Simply provide a YouTube video URL, and the application extracts the transcript, identifies key topics, and produces an easy-to-read summary with important insights.

Built with **Streamlit**, **Agno**, and **Groq LLM**.

---

## 🚀 Live Demo

🔗 **Application:**
https://youtube-video-analyizer-h9iubc8qnhjhz9evhhxg7m.streamlit.app/

---

# ✨ Features

* 🎥 Analyze YouTube videos using a video URL
* 🤖 AI-generated summaries powered by Groq LLM
* 📚 Extract key concepts and learning points
* 📝 Well-structured markdown output
* ⚡ Fast inference using Groq
* 🌐 Simple and interactive Streamlit interface

---

# 🛠️ Tech Stack

* Python
* Streamlit
* Agno Framework
* Groq API
* YouTube Transcript API
* python-dotenv

---

# 📂 Project Structure

```text
.
├── ui.py
├── Youtube_Video_Summarizer.py
├── requirements.txt
├── .env
└── README.md
```

---

# ⚙️ Local Setup

### 1. Clone the repository

```bash
git clone https://github.com/hemant-rgb/Youtube-Video-Analyizer.git

cd Youtube-Video-Analyizer
```

### 2. Create a virtual environment

**macOS / Linux**

```bash
python3 -m venv .venv
source .venv/bin/activate
```

**Windows**

```bash
python -m venv .venv
.venv\Scripts\activate
```

### 3. Install dependencies

```bash
pip install -r requirements.txt
```

### 4. Create a `.env` file

```env
GROQ_API_KEY=your_groq_api_key
```

### 5. Run the application

```bash
streamlit run ui.py
```

---

# 📖 How It Works

```text
User enters YouTube URL
          │
          ▼
Retrieve video transcript
          │
          ▼
Send transcript to Groq LLM
          │
          ▼
Generate structured summary
          │
          ▼
Display analysis in Streamlit
```

---

# ⚠️ Current Limitations

### • English Videos Only

The application currently supports videos with **English transcripts**.

---

### • Public Captions Required

The analyzer relies on publicly available YouTube captions.

Videos without captions or with disabled transcripts cannot be analyzed.

---

### • YouTube Rate Limiting

The application uses the **YouTube Transcript API** to retrieve transcripts.

Occasionally, transcript requests may fail due to YouTube rate limiting or IP-based restrictions, particularly when many requests originate from the same server.

If this occurs, simply retry after some time or try another video.

---

# 🚀 Future Improvements

* 🌍 Multi-language transcript support
* 🎯 More accurate chapter and timestamp generation
* 📄 Export summaries as PDF or Markdown
* 📌 Key quotes and highlights extraction
* ❓ AI-generated quiz from video content
* 💬 Chat with the video using Retrieval-Augmented Generation (RAG)
* 🔄 Transcript caching to reduce repeated API requests
* 📊 Improved handling of unavailable or rate-limited transcripts

---

# 👨‍💻 Author

**Hemant Machiwar**

B.Tech in Mathematics and Computing
National Institute of Technology Hamirpur

---

## ⭐ If you found this project useful, consider giving it a star!
# 🎥 AI YouTube Video Analyzer

An AI-powered web application that analyzes YouTube videos and generates structured summaries using Large Language Models (LLMs). Simply provide a YouTube video URL, and the application extracts the transcript, identifies key topics, and produces an easy-to-read summary with important insights.

Built with **Streamlit**, **Agno**, and **Groq LLM**.

---

## 🚀 Live Demo

🔗 **Application:**
https://youtube-video-analyizer-h9iubc8qnhjhz9evhhxg7m.streamlit.app/

---

# ✨ Features

* 🎥 Analyze YouTube videos using a video URL
* 🤖 AI-generated summaries powered by Groq LLM
* 📚 Extract key concepts and learning points
* 📝 Well-structured markdown output
* ⚡ Fast inference using Groq
* 🌐 Simple and interactive Streamlit interface

---

# 🛠️ Tech Stack

* Python
* Streamlit
* Agno Framework
* Groq API
* YouTube Transcript API
* python-dotenv

---

# 📂 Project Structure

```text
.
├── ui.py
├── Youtube_Video_Summarizer.py
├── requirements.txt
├── .env
└── README.md
```

---

# ⚙️ Local Setup

### 1. Clone the repository

```bash
git clone https://github.com/hemant-rgb/Youtube-Video-Analyizer.git

cd Youtube-Video-Analyizer
```

### 2. Create a virtual environment

**macOS / Linux**

```bash
python3 -m venv .venv
source .venv/bin/activate
```

**Windows**

```bash
python -m venv .venv
.venv\Scripts\activate
```

### 3. Install dependencies

```bash
pip install -r requirements.txt
```

### 4. Create a `.env` file

```env
GROQ_API_KEY=your_groq_api_key
```

### 5. Run the application

```bash
streamlit run ui.py
```

---

# 📖 How It Works

```text
User enters YouTube URL
          │
          ▼
Retrieve video transcript
          │
          ▼
Send transcript to Groq LLM
          │
          ▼
Generate structured summary
          │
          ▼
Display analysis in Streamlit
```

---

# ⚠️ Current Limitations

### • English Videos Only

The application currently supports videos with **English transcripts**.

---

### • Public Captions Required

The analyzer relies on publicly available YouTube captions.

Videos without captions or with disabled transcripts cannot be analyzed.

---

### • YouTube Rate Limiting

The application uses the **YouTube Transcript API** to retrieve transcripts.

Occasionally, transcript requests may fail due to YouTube rate limiting or IP-based restrictions, particularly when many requests originate from the same server.

If this occurs, simply retry after some time or try another video.

---

# 🚀 Future Improvements

* 🌍 Multi-language transcript support
* 🎯 More accurate chapter and timestamp generation
* 📄 Export summaries as PDF or Markdown
* 📌 Key quotes and highlights extraction
* ❓ AI-generated quiz from video content
* 💬 Chat with the video using Retrieval-Augmented Generation (RAG)
* 🔄 Transcript caching to reduce repeated API requests
* 📊 Improved handling of unavailable or rate-limited transcripts

---

# 👨‍💻 Author

**Hemant Machiwar**

B.Tech in Mathematics and Computing
National Institute of Technology Hamirpur

---

## ⭐ If you found this project useful, consider giving it a star!
