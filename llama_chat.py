import json
import os

from pyllamacpp.model import Model
model_path = 'C:/path/to/models/'
model = Model(ggml_model=model_path+ 'model_file_name.bin', n_ctx=512)


def open_file(filepath):
    with open(filepath, 'r', encoding='utf-8') as infile:
        return infile.read()


def textgen(prompt, n_predict=50, new_text_callback=None, verbose=False, top_p=1.0, temp=0.7, repeat_penalty=1):
    prompt = prompt.encode(encoding='ASCII',errors='ignore').decode()
    response = model.generate(prompt=prompt, n_predict=n_predict)
    text = response
    return text


if __name__ == '__main__':
    conversation = list()
    while True:
        user_input = input('USER: ')
        conversation.append('USER: %s' % user_input)
        text_block = '\n'.join(conversation)
        prompt = open_file('prompt_chat.txt').replace('<<BLOCK>>', text_block) # prompt_chat.txt = text file with prompt for AI
        prompt = prompt + '\nJAX:'
        response = textgen(prompt)
        print('JAX:', response)
        conversation.append('JAX: %s' % response)
        
# For the original code, visit David Shapiro's github (https://github.com/daveshap/PythonGPT3Tutorial) and PyLLaMaCpp's repo (https://github.com/abdeladim-s/pyllamacpp).