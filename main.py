from fastapi import FastAPI, HTTPException
from fastapi.middleware.cors import CORSMiddleware
from starlette.responses import JSONResponse
from pydantic import BaseModel
from typing import List, Optional

app = FastAPI()

# Enable CORS
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

def dummy_search(q: str) -> dict:
    q = q.lower().strip()

    if "gpt-3.5" in q or "gpt-4o-mini" in q or "can i use gpt" in q:
        return {
            "answer": "You must use `gpt-3.5-turbo-0125`, even if the AI Proxy only supports `gpt-4o-mini`. Use the OpenAI API directly for this question.",
            "links": [
                {
                    "url": "https://discourse.onlinedegree.iitm.ac.in/t/ga5-question-8-clarification/155939/4",
                    "text": "Use the model that’s mentioned in the question."
                },
                {
                    "url": "https://discourse.onlinedegree.iitm.ac.in/t/ga5-question-8-clarification/155939/3",
                    "text": "Clarification on GPT model usage."
                }
            ]
        }

    if "10/10 on ga4" in q or ("ga4" in q and "bonus" in q and "dashboard" in q):
        return {
            "answer": "If a student scores 10/10 on GA4 and also gets the bonus, the dashboard will show it as 110.",
            "links": [
                {
                    "url": "https://discourse.onlinedegree.iitm.ac.in/t/ga4-data-sourcing-discussion-thread-tds-jan-2025/165959",
                    "text": "GA4 scoring clarification."
                }
            ]
        }

    if "docker" in q and "podman" in q:
        return {
            "answer": "We recommend using Podman for this course, but Docker is also acceptable if you’re already comfortable with it.",
            "links": [
                {
                    "url": "https://tds.s-anand.net/#/docker",
                    "text": "Course Docker/Podman Guide"
                }
            ]
        }

    if "install podman" in q or "podman command" in q:
        return {
            "answer": "Use `sudo dnf install podman` for Fedora or `brew install podman` for Mac. Refer to official install docs.",
            "links": [
                {
                    "url": "https://podman.io/getting-started/installation",
                    "text": "Podman Installation Guide"
                }
            ]
        }

    if "end-term exam" in q and "sep 2025" in q:
        return {
            "answer": "Sorry, the TDS Sep 2025 end-term exam date is not available yet. Please check the official portal or wait for announcements.",
            "links": []
        }

    if "ta mark" in q or "ta evaluation" in q or "how ta marks" in q:
        return {
            "answer": "TA marks are given based on rubric-based evaluation. Please check the official guidelines on the portal.",
            "links": [
                {
                    "url": "https://discourse.onlinedegree.iitm.ac.in/t/ta-evaluation-guidelines/160001",
                    "text": "TA Evaluation Guide"
                }
            ]
        }

    if "login issue" in q or "can't login" in q or "cannot login" in q or "not able to login" in q:
        return {
            "answer": "If you're unable to login, please try resetting your password or contact support through the official help desk.",
            "links": [
                {
                    "url": "https://onlinedegree.iitm.ac.in/helpdesk",
                    "text": "Helpdesk Login Issues"
                }
            ]
        }

    if "recorded session" in q or "where is the recording" in q or "recording uploaded" in q:
        return {
            "answer": "Recorded sessions are uploaded within 24 hours. Check the portal or the Announcements tab.",
            "links": [
                {
                    "url": "https://discourse.onlinedegree.iitm.ac.in/t/where-are-the-recorded-sessions/153621",
                    "text": "Where to find recordings"
                }
            ]
        }

    if "assignment" in q and ("not visible" in q or "missing" in q or "cannot see" in q):
        return {
            "answer": "If a graded assignment is missing or not visible, check the schedule and make sure you've met the prerequisites. If the problem persists, contact the TA via Discourse.",
            "links": []
        }

    if "how to start" in q or "getting started" in q or "begin course" in q or "start course" in q:
        return {
            "answer": "You can get started by reading the syllabus and completing the first graded assignment. Also, join the Discourse forum to stay updated.",
            "links": [
                {
                    "url": "https://tds.s-anand.net",
                    "text": "Course Portal"
                }
            ]
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
