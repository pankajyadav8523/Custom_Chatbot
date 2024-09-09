import pandas as pd
from sentence_transformers import SentenceTransformer

# Load Q&A dataset
df = pd.read_csv('/home/pankaj/Desktop/chatbot/data/qa_dataset.csv')

# Initialize SBERT model
model = SentenceTransformer('paraphrase-MiniLM-L6-v2')

# Generate embeddings for each question
df['question_embedding'] = df['question'].apply(lambda x: model.encode(x))

# Save embeddings to CSV (optional)
df.to_csv('/home/pankaj/Desktop/chatbot/data/qa_with_embeddings.csv', index=False)

print("Embeddings generated and saved!")
