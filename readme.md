# FastAPI Batch Sentiment Analysis

This project implements a FastAPI endpoint for batch sentiment analysis.

## Endpoint

POST /sentiment

Input format:

{
  "sentences": ["I love this!", "I'm sad."]
}

Output format:

{
  "results": [
    {"sentence": "I love this!", "sentiment": "happy"}
  ]
}

## Run locally

Install dependencies:

pip install -r requirements.txt

Run server:

uvicorn main:app --reload

API runs at:

http://localhost:8000

Swagger docs:

http://localhost:8000/docs