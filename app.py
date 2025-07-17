import os
import pandas as pd
import requests
from flask import Flask, render_template, request, session

app = Flask(__name__)
app.secret_key = 'supersecretkey'  # Needed for session

# SerpAPI Key
SERPAPI_KEY = 'ba64149463cecd5908058abcf7249e9fe9b89c24e0d16563807183bbed71b0b6'

# Function to get answers from SerpAPI
def get_answer_from_serpapi(question):
    url = "https://serpapi.com/search"
    params = {
        "q": question,
        "api_key": SERPAPI_KEY,
        "engine": "google",
        "num": 1
    }

    try:
        response = requests.get(url, params=params)
        if response.status_code != 200:
            print(f"SerpAPI Error [{response.status_code}]: {response.text}")
            return "Could not fetch answer (API error)."

        data = response.json()
        return data.get('answer_box', {}).get('answer') or \
               data.get('answer_box', {}).get('snippet') or \
               data.get('organic_results', [{}])[0].get('snippet', "No answer found.")
    except Exception as e:
        print(f"Exception: {e}")
        return "Something went wrong while fetching the answer."

@app.route('/', methods=['GET', 'POST'])
def index():
    # Initialize chat history in session if not already present
    if 'chat_history' not in session:
        session['chat_history'] = []

    chat_history = session['chat_history']
    file_answers = []

    # Handle POST request for question and file input
    if request.method == 'POST':
        # Handle question submission
        if 'question' in request.form:
            question = request.form['question']
            answer = get_answer_from_serpapi(question)
            chat_history.append((question, answer))
            session['chat_history'] = chat_history

        # Handle file upload
        elif 'file' in request.files:
            file = request.files['file']
            if file.filename.endswith('.csv'):
                df = pd.read_csv(file)
            elif file.filename.endswith('.xlsx'):
                df = pd.read_excel(file)
            elif file.filename.endswith('.txt'):
                lines = file.read().decode('utf-8').splitlines()
                df = pd.DataFrame(lines, columns=['Question'])
            else:
                return "Unsupported file format."

            # Process the questions in the file and get answers
            df['Answer'] = df['Question'].apply(get_answer_from_serpapi)
            file_answers = list(zip(df['Question'], df['Answer']))

    # Render the template with chat history and file answers
    return render_template('index.html', chat_history=chat_history, file_answers=file_answers)

if __name__ == '__main__':
    app.run(debug=True)
