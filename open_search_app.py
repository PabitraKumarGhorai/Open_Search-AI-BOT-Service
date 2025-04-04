from flask import Flask, render_template, request, jsonify
import openai
import os
from dotenv import load_dotenv
app = Flask(__name__)

# Set your OpenAI API key
load_dotenv()

openai.api_key = os.getenv("api_key")

@app.route('/')
def index():
    return render_template('app_home.html')

@app.route('/ask', methods=['POST'])
def ask():
    user_message = request.json.get('message')
    print(user_message)

    if not user_message:
        return jsonify({'error': 'No message provided'}), 400

    response = openai.chat.completions.create(
            model="gpt-3.5-turbo", 
            messages=[{"role": "user", "content": user_message}]
        )
    bot_reply = response.choices[0].message.content
    print(bot_reply)
    return jsonify({'reply': bot_reply})
    
    
 
    
    
if __name__ == '__main__':
    app.run(debug=True)
