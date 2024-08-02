from flask import Flask, request, jsonify
import openai
from dotenv import load_dotenv
import os

# call .env file
load_dotenv()

app = Flask(__name__)

# OpenAI API key

openai.api_key = os.getenv("OPENAI_API_KEY")

@app.route('/chat', methods=['POST'])
def chat():
    user_input = request.json.get('message')
    response = openai.Completion.create(
        model="text-davinci-003",
        prompt=f"User: {user_input}\nAI:",
        max_tokens=50
    )
    ai_response = response.choices[0].text.strip()
    return jsonify({'response': ai_response})

if __name__ == '__main__':
    app.run(debug=True)