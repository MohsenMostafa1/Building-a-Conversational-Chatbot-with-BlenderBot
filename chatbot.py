# -*- coding: utf-8 -*-
"""ChatBot.ipynb

Automatically generated by Colab.

Original file is located at
    https://colab.research.google.com/drive/1K3Nzdgyp5JkcdYmkGbIBvgn1DI0Iepq7
"""

!pip install transformers

from transformers import BlenderbotTokenizer, BlenderbotForConditionalGeneration

# Load the BlenderBot model and tokenizer
model_name = "facebook/blenderbot-400M-distill"
tokenizer = BlenderbotTokenizer.from_pretrained(model_name)
model = BlenderbotForConditionalGeneration.from_pretrained(model_name)

def chat_with_bot(user_input):
    # Encode the input and generate a response
    inputs = tokenizer(user_input, return_tensors='pt')
    reply_ids = model.generate(**inputs)
    response = tokenizer.decode(reply_ids[0], skip_special_tokens=True)
    return response

print("Chatbot is ready! Type 'exit' to stop the conversation.")
while True:
    user_input = input("You: ")
    if user_input.lower() == 'exit':
        break
    bot_response = chat_with_bot(user_input)
    print("Bot:", bot_response)