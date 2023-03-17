import requests
import json
import os


# Token

def open_file(filepath):
    with open(filepath, 'r', encoding='utf-8') as infile:
        return infile.read()

token = open_file('token_nai.txt')


# API

tx_url = "https://api.novelai.net/ai/generate"
headers = {"accept": "application/json","Content-Type": "application/json"}
h_auth = {"Authorization":  f"Bearer {token}"}


# Definitions

def tx_gen(content):
    content = content.encode(encoding='ASCII', errors='ignore').decode()
    model = "krake-v2"
    params = {"stop_sequences": [[27]], "use_string":True, "temperature":1, "min_length":10, "max_length":30}
    data = {"input": content, "model": model, "parameters":params}
    response = requests.post(url=tx_url, json=data, headers=h_auth)
    #print(response)
    response_data = response.json()
    #print(response_data)
    text = response_data["output"].strip()
    #print(text)
    return text

# Main Function

if __name__ == '__main__':
    conversation = list()
    while True:
        user_input = input('USER: ')
        conversation.append('USER: %s' % user_input)
        text_block = '\n'.join(conversation)
        content = open_file('chat_history.txt').replace('<<BLOCK>>', text_block)
        content = content + '\nHANA:'
        response = tx_gen(content)
        print('HANA:', response)
        conversation.append('HANA: %s' % response)