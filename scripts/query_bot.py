import numpy as np
from sentence_transformers import SentenceTransformer

# Initialize SBERT model
model = SentenceTransformer('paraphrase-MiniLM-L6-v2')

def get_similar_answer(cur, user_query):
    """
    Retrieve the most similar answer from the database based on the user query.

    Parameters:
    - cur: The database cursor.
    - user_query: The input query from the user.

    Returns:
    - Tuple containing the most similar question and answer from the database.
    """
    # Generate embedding for user input
    original_embedding = model.encode(user_query)
    
    # Define the desired length of the embedding
    target_length = 768
    
    # Pad or truncate the embedding as needed
    if len(original_embedding) < target_length:
        # Pad the embedding with zeros
        processed_embedding = np.zeros(target_length)
        processed_embedding[:len(original_embedding)] = original_embedding
    elif len(original_embedding) > target_length:
        # Truncate the embedding
        processed_embedding = original_embedding[:target_length]
    else:
        # Use the original embedding if it matches the target length
        processed_embedding = original_embedding
    
    # Convert to list and format for pgvector
    query_embedding_list = processed_embedding.tolist()
    vector_embedding = f'[{", ".join(map(str, query_embedding_list))}]'
    
    # Perform vector similarity search in the database
    cur.execute("""
    SELECT question, answer 
    FROM qa_data
    ORDER BY embedding <=> %s::vector LIMIT 1;
    """, (vector_embedding,))
    
    result = cur.fetchone()
    return result