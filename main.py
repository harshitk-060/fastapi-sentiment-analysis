from fastapi import FastAPI
from pydantic import BaseModel
from typing import List

app = FastAPI()

# Request format
class SentencesInput(BaseModel):
    sentences: List[str]

# Response format
class Result(BaseModel):
    sentence: str
    sentiment: str

class SentimentResponse(BaseModel):
    results: List[Result]

# Simple sentiment logic
def detect_sentiment(sentence: str) -> str:
    sentence = sentence.lower()

    happy_words = ["love", "great", "awesome", "good", "amazing", "happy", "excellent"]
    sad_words = ["terrible", "bad", "sad", "hate", "awful", "worst"]

    if any(word in sentence for word in happy_words):
        return "happy"
    elif any(word in sentence for word in sad_words):
        return "sad"
    else:
        return "neutral"


@app.post("/sentiment", response_model=SentimentResponse)
def sentiment_analysis(data: SentencesInput):

    results = []

    for sentence in data.sentences:
        sentiment = detect_sentiment(sentence)

        results.append({
            "sentence": sentence,
            "sentiment": sentiment
        })

    return {"results": results}