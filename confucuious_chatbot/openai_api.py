import json
import openai

with open('confucuious_chatbot\secret.json') as file:
    secrets = json.load(file)
openai.api_key = secrets["OPENAI_API_KEY"]

with open('C:\lab\우학연\confucuious_chatbot\confucius.txt', 'r', encoding='utf-8') as file:
    confucius_text = file.read()

def confucius_reply(question):
    prompt = f"Given the teachings of Confucius:\n{confucius_text}\n\nQuestion: {question}\nAnswer:"
    response = openai.ChatCompletion.create(
        model="gpt-3.5-turbo",
        messages=[
            {"role": "system", "content": "You are a wise sage knowledgeable in the teachings of Confucius."},
            {"role": "user", "content": question}
        ]
    )
    return response['choices'][0]['message']['content']

question = "부모님께 효도해야 하는 이유는 무엇인가요?"
answer = confucius_reply(question)
print(answer)