# Sitare Chatbot

The **Sitare Chatbot** is an intelligent question-answering system designed to answer queries related to a dataset of Sitare question-answers. It uses the **SBERT model** to compute question embeddings and **PostgreSQL with pgvector** to store and compute similarity scores for efficient matching.

## Features

* Uses **SBERT** for calculating question embeddings.
* Stores question embeddings in **PostgreSQL** using **pgvector**.
* Calculates similarity scores to provide the most relevant answer for a given query.
* Interactive command-line chatbot interface.
  
## Folder Structure

* `chatbot/`: Contains the main chatbot scripts.
* `chatbot.py`: Entry point for running the chatbot.
* `data/`: Stores the Sitare question-answer dataset.
* `requirements.txt`: Lists the Python dependencies for the project.
* `scripts/`: Includes all the custom scripts used in the project.

## Setup

### 1. Clone the repository:
```bash
git clone <repository-url>
cd <repository-name>
