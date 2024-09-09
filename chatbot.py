import psycopg2
from scripts.query_bot import get_similar_answer

def chatbot():
    # PostgreSQL connection setup
    conn = psycopg2.connect(database="chatbot", user="pankaj8523", password="pankaj", host="localhost", port="5432")
    cur = conn.cursor()
    
    print("Chatbot is ready! Type 'exit' to stop.")
    
    while True:
        print("\n")
        user_input = input("You:")
        
        if user_input.lower() == 'exit':
            print("Goodbye!")
            break
        
        # Get response from the bot
        question, answer = get_similar_answer(cur, user_input)
        if question and answer:
            print(f"Bot: {answer}")
    
    # Clean up
    cur.close()
    conn.close()

if __name__ == "__main__":
    chatbot()
