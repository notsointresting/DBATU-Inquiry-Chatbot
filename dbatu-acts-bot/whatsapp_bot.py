from flask import Flask, request
from twilio.twiml.messaging_response import MessagingResponse
import os
from dotenv import load_dotenv
import google.generativeai as genai
from main import user_input

load_dotenv()

# Init the Flask App
app = Flask(__name__)

# Initialize the OpenAI API key
genai.configure(api_key=os.getenv("API_KEY"))




# Define a function to generate answers using GPT-3
def generate_answer(question):
    answer = user_input(question)['output_text']
    return answer


# Define a route to handle incoming requests
@app.route('/gemini', methods=['POST'])
def chatgpt():
    incoming_que = request.values.get('Body', '').lower()
    print("Question: ", incoming_que)
    # Generate the answer using GPT-3
    answer = generate_answer(incoming_que)
    print("BOT Answer: ", answer)
    bot_resp = MessagingResponse()
    msg = bot_resp.message()
    msg.body(answer)
    return str(bot_resp)


# Run the Flask app
if __name__ == '__main__':
    app.run(host='0.0.0.0', debug=False, port=5000)