# 📘 TDS Virtual TA - Tools in Data Science Project (Jan 2025)

This is a Virtual Teaching Assistant API project for the **Tools in Data Science** course from **IIT Madras Online BSc** (Jan 2025 term). It answers student questions using pre-scraped content from course Discourse posts and content, as per project instructions.

---

## 🔗 API Endpoint

actual one 
http://127.0.0.1:8000


### Method: `POST`

### Request format (JSON):

json
{
  "question": "Should I use gpt-4o-mini which AI proxy supports, or gpt3.5 turbo?",
  "image": "base64-encoded image string "
}

curl command 
curl "https://app.example.com/api/" \
  -H "Content-Type: application/json" \
  -d "{\"question\": \"Should I use gpt-4o-mini which AI proxy supports, or gpt3.5 turbo?\", \"image\": \"$(base64 -w0 project-tds-virtual-ta-q1.webp)\"}"



# response 
{
  "answer": "Your answer string here.",
  "links": [
   {
       "url": "https://discourse.onlinedegree.iitm.ac.in/...",
       "text": "Relevant explanation or reference"
   }
] 
}


# Setup 
pip install -r requirements.txt

# to run locally
uvicorn index:app --host 0.0.0.0 --port 8000 --reload
