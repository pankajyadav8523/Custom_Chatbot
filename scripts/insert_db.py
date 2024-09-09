import psycopg2
import pandas as pd
import numpy as np

# Define the desired dimension
DESIRED_DIMENSION = 768

# Load Q&A dataset with embeddings
df = pd.read_csv('/home/pankaj/Desktop/chatbot/data/qa_with_embeddings.csv')

# PostgreSQL connection setup
conn = psycopg2.connect(database="chatbot", user="pankaj8523", password="pankaj", host="localhost", port="5432")
cur = conn.cursor()

# Insert data into PostgreSQL
for _, row in df.iterrows():
    question = row['question']
    answer = row['answer']
    embedding_str = row['question_embedding']  # This is a string representation of a list

    # Convert the string to a numpy array
    embedding = np.fromstring(embedding_str.strip('[]'), sep=' ').tolist()

    # Pad or truncate the embedding to the desired dimension
    if len(embedding) < DESIRED_DIMENSION:
        embedding += [0] * (DESIRED_DIMENSION - len(embedding))
    elif len(embedding) > DESIRED_DIMENSION:
        embedding = embedding[:DESIRED_DIMENSION]

    # Ensure embedding dimensions match
    if len(embedding) != DESIRED_DIMENSION:
        print(f"Warning: Skipping entry with incorrect embedding dimension: {len(embedding)}")
        continue

    cur.execute("INSERT INTO qa_data (question, answer, embedding) VALUES (%s, %s, %s)", 
                (question, answer, embedding))

conn.commit()
cur.close()
conn.close()

print("Data and embeddings inserted into the database!")
