import openai 
from flask import Flask,request, jsonify
from twilio.twiml.messaging_response import MessagingResponse
import os


app = Flask(__name__)

openai.api_key = os.environ.get ('YOUR_OPENAI_API_KEY')
def generate_answer(question):
    model_engine = 'text-davinci-002'
    prompt = f"Q: {question}\nA:"
    
    response = openai.Completion.create(
        engine=model_engine,
        prompt=prompt,
        max_tokens=1024,
        n=1,
        stop = None,
        temperature=0.9,
    )
    
    answer = response.choices[0].text.strip()
    return answer
@app.route('/chatgpt', methods=['POST'])
def chatgpt():
    incoming_question = request.values.get('Body','').lower()
    print(incoming_question)
    
    answer = generate_answer(incoming_question)
    print(answer)
    bot_res = MessagingResponse()
    msg = bot_res.message()
    msg.body(answer)
    
    return str(bot_res)

if __name__ == '__main__':
    app.run(host = '0.0.0.0', debug=False, port=5000)

