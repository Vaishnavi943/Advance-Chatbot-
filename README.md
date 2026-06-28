# 🚀 Advance-Chatbot

A **production-ready AI chatbot** built using **LangGraph**, **FastAPI**, and **React (Vite)**. This project demonstrates how to build an intelligent conversational AI system with advanced features such as memory, streaming responses, RAG (Retrieval-Augmented Generation), persistent chat history, human-in-the-loop workflows, and tool integration.

> **Note:** This project is currently under active development. Additional features and improvements will be added over time.

---

## ✨ Features

* 💬 AI-powered conversational chatbot
* ⚡ Real-time streaming responses (ChatGPT-like typing effect)
* 🧠 Conversation memory using LangGraph MemorySaver
* 💾 Persistent chat history with resume chat support
* 📚 Retrieval-Augmented Generation (RAG) *(Coming Soon)*
* 🔍 Document upload and retrieval *(Coming Soon)*
* 🛠️ Tool integration
* 👤 Human-in-the-loop workflow
* 🔄 Retry logic for fault tolerance
* 📊 LangSmith integration for monitoring and debugging
* 🗂️ Multiple conversation support
* 🌙 Modern responsive React UI
* ⚙️ FastAPI backend with REST APIs

---

## 🏗️ Tech Stack

### Frontend

* React (Vite)
* JavaScript
* HTML5
* CSS3

### Backend

* FastAPI
* LangGraph
* LangChain
* OpenAI
* Uvicorn

### Database

* SQLite *(default)*
* Easily configurable for PostgreSQL or MySQL

### AI & LLM

* OpenAI GPT Models
* LangGraph
* LangChain
* LangSmith

---

## 📂 Project Structure

```text
Advance-Chatbot/
│
├── backend/
│   ├── main.py
│   ├── graph.py
│   ├── database.py
│   ├── config.py
│   ├── requirements.txt
│   └── .env
│
├── frontend/
│   ├── src/
│   │   ├── components/
│   │   ├── pages/
│   │   ├── App.jsx
│   │   ├── main.jsx
│   │   └── index.css
│   │
│   ├── package.json
│   └── vite.config.js
│
├── README.md
└── .gitignore
```

---

## ⚙️ Installation

### 1. Clone the repository

```bash
git clone <repository-url>
cd Advance-Chatbot
```

---

### 2. Backend Setup

```bash
cd backend

python -m venv venv
```

#### Windows

```bash
venv\Scripts\activate
```

#### Linux / macOS

```bash
source venv/bin/activate
```

Install dependencies:

```bash
pip install -r requirements.txt
```

Create a `.env` file:

```env
OPENAI_API_KEY=your_openai_api_key
LANGCHAIN_API_KEY=your_langchain_api_key
LANGSMITH_API_KEY=your_langsmith_api_key
DATABASE_URL=sqlite:///chat.db
```

Run the backend:

```bash
uvicorn main:app --reload
```

Backend runs at:

```
http://localhost:8000
```

---

### 3. Frontend Setup

```bash
cd frontend

npm install

npm run dev
```

Frontend runs at:

```
http://localhost:5173
```

---

## 📡 Backend APIs

| Method | Endpoint               | Description                              |
| ------ | ---------------------- | ---------------------------------------- |
| POST   | `/chat`                | Send a message to the chatbot            |
| GET    | `/history/{thread_id}` | Retrieve chat history                    |
| POST   | `/new-chat`            | Create a new conversation                |
| POST   | `/resume-chat`         | Resume an existing conversation          |
| POST   | `/upload`              | Upload documents for RAG *(Coming Soon)* |
| GET    | `/health`              | Health check                             |

---

## 🚀 Current Features

* AI Chat
* Conversation Memory
* Streaming Responses
* Persistent Chat Sessions
* Resume Previous Chats
* Tool Calling
* LangSmith Monitoring
* Retry Logic
* Human-in-the-loop Workflow

---

## 🔮 Upcoming Features

* Retrieval-Augmented Generation (RAG)
* PDF & Document Upload
* Vector Database Integration
* Authentication
* User Profiles
* Multi-Model Support
* Voice Input & Output
* Image Understanding
* Docker Support
* Cloud Deployment
* Conversation Search
* Export Chat History

---

## 💻 Development Workflow

Start the backend:

```bash
cd backend
uvicorn main:app --reload
```

Start the frontend:

```bash
cd frontend
npm run dev
```

Open your browser:

```
http://localhost:5173
```

---

## 🤝 Contributing

Contributions are welcome!

1. Fork the repository.
2. Create a feature branch.
3. Commit your changes.
4. Push the branch.
5. Open a Pull Request.

---

## 📜 License

This project is licensed under the MIT License.

---

## 👨‍💻 Author

**Kumari Vaishnavi**

Computer Science Engineering Student

Passionate about Artificial Intelligence, Agentic AI, Full-Stack Development, and Large Language Models.

---

## ⭐ Support

If you found this project helpful, consider giving it a **⭐ Star** on GitHub. It helps others discover the project and motivates further development.

---

> **Disclaimer:** This project is under active development. Some features mentioned above are planned and will be added in future updates.

