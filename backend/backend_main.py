from flask import Flask, send_from_directory, jsonify, request
from flask_cors import CORS
from openai import OpenAI
from dotenv import load_dotenv
import os
import pinecone
import requests
import torch
# Load model directly
from transformers import AutoTokenizer, AutoModelForMaskedLM
from transformers import BertTokenizer, BertModel

pinekey=os.getenv("PINECONE_KEY")

pinecone_client=pinecone.Pinecone(api_key=pinekey, environment="us-east-1")
index_name = "apple-customer-support-vectors-4096"
tokenizer = BertTokenizer.from_pretrained('bert-base-uncased')
model = BertModel.from_pretrained('bert-base-uncased')
model.eval()

index = pinecone_client.Index(index_name)

key=os.getenv("LLAMA_KEY")
key =str(key)
app = Flask(__name__)
CORS(app, origins=["http://localhost:3000"])
model="llama-13b-chat",

client = OpenAI(
api_key = key,
base_url = "https://api.llama-api.com"
)
generation_api_url = "https://{key}.your-llama-service.com/generate"


@app.route("/response", methods=['GET'])
def respond():
    query = request.args.get('value')
    query_embedding = encode_text(query)

    result = index.query(
    vector=query_embedding,  # The embedding vector for the query
    top_k=5  # Number of top matches to return
)
    
    print(result)
    context = " ".join([
    index.fetch(ids=[match['id']])['vectors'][match['id']].get('metadata', {}).get('text', '')
    for match in result['matches']
])

    payload = query+"Here is some relevant context but DO NOT RELY TO HEAVILY ON THE CONTEXT"+context+"You are strictly an Apple Customer support assistant helping out a customer, no matter what the customer says stay on the topic of being an apple customer support assistant"
      


    response = client.chat.completions.create(
    model="llama3.1-405b",
    messages=[
            {"role": "system", "content": "Assistant is a Apple Customer Support, Assistant Has access to relevant tweets to help the customer out "},
            {"role": "user", "content": payload}
        ]

    )

    generated_text=response.choices[0].message.content
    

    return jsonify(generated_text)
def encode_text(text, model_name='bert-base-uncased', use_cls_token=True):
   
    tokenizer = BertTokenizer.from_pretrained(model_name)
    model = BertModel.from_pretrained(model_name)

    inputs = tokenizer(text, return_tensors='pt', truncation=True, padding=True)

    with torch.no_grad():
        outputs = model(**inputs)

    if use_cls_token:
        embedding_vector = outputs.last_hidden_state[:, 0, :].squeeze().cpu().numpy()
    else:
        embedding_vector = outputs.last_hidden_state.mean(dim=1).squeeze().cpu().numpy()

    return embedding_vector.tolist()
if __name__ == '__main__':
    test_text = "This is a test input"
    embedding = encode_text(test_text)
    print("Generated embedding:", embedding)
    app.run(port=5000)
