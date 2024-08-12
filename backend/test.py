import pytorch
from openai import OpenAI


def query_pinecone(query_text, index, model, tokenizer, top_k=5):
    # Convert the query text into a vector using the same model used for vectorization
    inputs = tokenizer(query_text, return_tensors='pt', truncation=True, padding=True)
    with torch.no_grad():
        query_vector = model(**inputs).last_hidden_state.mean(dim=1).squeeze().cpu().numpy().tolist()
    
    # Query Pinecone to retrieve the top_k most relevant vectors
    results = index.query(queries=[query_vector], top_k=top_k)
    
    return results['matches']
def combine_context_and_query(matches, original_query):
    # Extract the text from the retrieved matches
    retrieved_texts = [match['metadata']['text'] for match in matches]
    
    # Combine the retrieved context with the original query
    context = " ".join(retrieved_texts)
    combined_input = f"Context: {context}\n\nQuery: {original_query}"
    
    return combined_input


model="llama-13b-chat",

client = OpenAI(
api_key = 'LL-KUWuBk3MKbIlnfGMnrBWhJrpr3oN8uqacr48nfXlUGP6HNTbE12vOOCAXLNmaF5Z',
base_url = "https://api.llama-api.com"
)
response = client.chat.completions.create(
    model="llama-13b-chat",
    messages=[
            {"role": "system", "content": "Assistant is a Technical Support Agent"},
            {"role": "user", "content": 'hello'}
        ]

    )