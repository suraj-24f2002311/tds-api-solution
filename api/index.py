
from fastapi import FastAPI, HTTPException
from pydantic import BaseModel
from typing import Optional, List
from fastapi.middleware.cors import CORSMiddleware
from starlette.responses import JSONResponse

app = FastAPI()

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

class QuestionRequest(BaseModel):
    question: str
    image: Optional[str] = None

def dummy_search(question: str) -> dict:
    if "gpt-3.5-turbo-0125" in question:
        return {
            "answer": "You must use `gpt-3.5-turbo-0125`, even if the AI Proxy only supports `gpt-4o-mini`. Use the OpenAI API directly for this question.",
            "links": [
                {
                    "url": "https://discourse.onlinedegree.iitm.ac.in/t/ga5-question-8-clarification/155939/4",
                    "text": "Use the model that’s mentioned in the question."
                },
                {
                    "url": "https://discourse.onlinedegree.iitm.ac.in/t/ga5-question-8-clarification/155939/3",
                    "text": "Tokenizer clarification from Prof. Anand."
                }
            ]
        }
    elif "dashboard" in question.lower():
        return {
            "answer": "The dashboard will show '110' if you score 10/10 on GA4 and the bonus is applied.",
            "links": [
                {
                    "url": "https://discourse.onlinedegree.iitm.ac.in/t/ga4-data-sourcing-discussion-thread-tds-jan-2025/165959/388",
                    "text": "GA4 bonus discussion on Discourse."
                }
            ]
        }
    elif "docker" in question.lower() and "podman" in question.lower():
        return {
            "answer": "We recommend using Podman for this course, although Docker will also work.",
            "links": [
                {
                    "url": "https://tds.s-anand.net/#/docker",
                    "text": "Docker and Podman info in the course."
                }
            ]
        }
    elif "end-term" in question.lower():
        return {
            "answer": "We don't have that information at the moment. Please refer to the course announcements.",
            "links": []
        }
    return {
        "answer": "Sorry, I couldn't find a direct answer to your question. Please check the course Discourse or syllabus.",
        "links": []
    }

@app.post("/api/")
async def answer_question(request: QuestionRequest):
    try:
        response = dummy_search(request.question)
        return JSONResponse(content=response)
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))

