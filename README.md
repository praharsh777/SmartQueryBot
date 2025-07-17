# 🤖 SmartQueryBot

SmartQueryBot is an intelligent chatbot that can:

- 💬 Chat like a traditional bot
- 📂 Accept and read input files to answer questions from them
- 🌐 Search the web when the answer isn’t found in the file

It combines **natural conversation**, **document understanding**, and **web search** in a single simple web app built with **Flask** and **HTML**.

---

## 🛠️ Tech Stack

- **Backend:** Python + Flask  
- **Frontend:** HTML (Jinja template)  
- **Search & File Parsing:** Custom Python logic (you can add NLP, SerpAPI, etc.)

---

## 📁 Project Structure

SmartQueryBot/
├── app.py # Main Flask application
├── requirements.txt # Python dependencies
├── templates/
│ └── index.html # Frontend HTML interface
└── README.md # Project documentation

## 🚀 How to Run the Project

### 1. Clone the repository

git clone https://github.com/praharsh777/SmartQueryBot.git
cd SmartQueryBot
2. Create a virtual environment (optional but recommended)

python -m venv venv
venv\Scripts\activate      # On Windows
# OR
source venv/bin/activate   # On macOS/Linux
3. Install dependencies

pip install -r requirements.txt
4. Run the Flask app

python app.py
5. Open in browser
Visit: http://127.0.0.1:5000

📌 Features
Upload a file (e.g., .txt, .pdf, .csv) and ask questions about its content

Ask general questions and the bot will search the web

Clean and minimal UI built with HTML + Flask templating

📄 Requirements (from requirements.txt)
Flask
(Add others like requests, PyPDF2, bs4, openai, or serpapi if you're using them)

📦 Future Improvements
 Integrate NLP or LLMs (like GPT) for deeper answers

 Add support for PDFs, Excel, and other formats

 Improve UI with Tailwind or Bootstrap

 Add chat history and file preview

🧠 Example Use Case
Upload a product spec file → Ask: “What is the warranty period?”
Bot reads it and answers.
If not found, it searches online and gives a relevant response.

📄 License
This project is open-source and available under the MIT License.

Built by Praharsh – making chatbots smarter, one feature at a time.
