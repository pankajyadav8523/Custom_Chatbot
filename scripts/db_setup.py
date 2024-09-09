import psycopg2

# PostgreSQL connection setup
conn = psycopg2.connect(database="chatbot", user="pankaj8523", password="pankaj", host="localhost", port="5432")
cur = conn.cursor()

# Create table for storing Q&A and embeddings
cur.execute("""
CREATE EXTENSION IF NOT EXISTS vector;

CREATE TABLE IF NOT EXISTS qa_data (
    id SERIAL PRIMARY KEY,
    question TEXT NOT NULL,
    answer TEXT NOT NULL,
    embedding VECTOR(768) -- SBERT embedding size
);
""")

conn.commit()
cur.close()
conn.close()

print("Database setup complete!")
