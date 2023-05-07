import requests
import os
from gtts import gTTS

API_KEY = os.getenv('API_KEY')

def get_chatbot_response(user_input):
    url = 'https://api.cohere.ai/v1/generate'
    headers = {
        'Content-Type': 'application/json',
        'Authorization': 'Bearer ' + API_KEY,
    }
    
    data = {
        "model": "command-xlarge-nightly",
        'prompt': user_input,
        'num_completion': 1,
        'max_tokens': 300,
        'temperature': 0.9,
    }
    response = requests.post(url, headers=headers, json=data)
    response_data = response.json()
    # print(response_data)
    # completion = response_data
    # return completion
    completion = response_data['generations'][0]['text']
    if completion is None:
        completion = response_data['generations'][0]['message']['content']
    return completion

def summerizer(user_input):
    url = 'https://api.cohere.ai/v1/summarize'
    headers = {
        'Content-Type': 'application/json',
        'Authorization': 'Bearer ' + API_KEY,
    }
    
    data = {
            'model':'summarize-xlarge', 
            'length':'medium',
            'extractiveness':'medium',
            'text' : user_input
        }
    
    response = requests.post(url, headers=headers, json=data)
    response_data = response.json()
    # print(response_data)
    # completion = response_data
    # return completion
    completion = response_data['summary']
    # tts = gTTS(text=completion, lang='en')
    # tts.save('./summary.mp3')
    if completion is None:
        pass
    return completion


