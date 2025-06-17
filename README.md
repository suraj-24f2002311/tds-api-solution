# TDS Virtual TA - Tools in Data Science Project (Jun 2025) BY *IIT Madras*

This is a Virtual Teaching Assistant API project for the **Tools in Data Science** course from **IIT Madras Online BSc** (Jan 2025 term). It answers student questions using pre-scraped content from course Discourse posts and content, as per project instructions.

---

## API Endpoint

actual one 
http://127.0.0.1:8000
render website 
https://tds-api-solution.onrender.com


### Method: `POST`

## Request format (JSON):

json
{
  "question": "Should I use gpt-4o-mini which AI proxy supports, or gpt3.5 turbo?",
  "image": "base64-encoded image string "
}

# curl command example
curl "https://tds-api-solution.onrender.com" \
  -H "Content-Type: application/json" \
  -d "{\"question\": \"Should I use gpt-4o-mini which AI proxy supports, or gpt3.5 turbo?\", \"image\": \"$(base64 -w0 project-tds-virtual-ta-q1.webp)\"}"



# response 
{
  "answer": "You must use `gpt-3.5-turbo-0125`, even if the AI Proxy only supports `gpt-4o-mini`. Use the OpenAI API directly for this question.",
  "links": [
    {
      "url": "https://discourse.onlinedegree.iitm.ac.in/t/ga5-question-8-clarification/155939/4",
      "text": "Use the model that’s mentioned in the question."
    },
    {
      "url": "https://discourse.onlinedegree.iitm.ac.in/t/ga5-question-8-clarification/155939/3",
      "text": "My understanding is that you just have to use a tokenizer, similar to what Prof. Anand used, to get the number of tokens and multiply that by the given rate."
    }
  ]
}


# Setup 
pip install -r requirements.txt

# To run locally
uvicorn main:app --host 0.0.0.0 --port 8000 --reload 
or you may just simply render the website and use curl command to get the answer because i dont know how to show

# Question this website respond
figuring the aspects to cover students problem into major sub-problems

### Students working with GPT, Docker, etc. might ask:

"Can I use GPT-4o-mini instead of GPT-3.5?" 

"Why does the question say use gpt-3.5-turbo?"

"Can I use Docker instead of Podman?"

"How to install Podman on Windows?"

### Graded Assignment/Dashboard Issues

"If I score 10/10 on GA4 and get the bonus, what will the dashboard show?"

"Why is my GA4 score 110 instead of 100?"

"My GA assignment is missing or not visible."

### Exams and Marks or Technical Assignment 

"When is the end-term exam in September 2025?"

"How are TA marks calculated?"

"Why haven't I received TA evaluation marks yet?"

### Technical and Login Issues

"I'm not able to login to the portal."

"Login issue – keeps saying invalid credentials."

### Recorded Sessions / General Course Info

"When will recorded sessions be uploaded?"

"Where can I find past recordings?"

"How to get started with this course?"

### General Getting Started or Help

"How to start this course?"

"Where do I find the syllabus?"

"Is there a discussion forum?"


## bonus 
MIT LICENCE for public use 
