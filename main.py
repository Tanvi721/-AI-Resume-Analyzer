import os
import json
import re
from fastapi import FastAPI, UploadFile, File, Form, HTTPException
import google.generativeai as genai
from utils import extract_text_from_file

app = FastAPI()

# Configuration
GENAI_API_KEY = "YOUR_API_KEY" 
genai.configure(api_key=GENAI_API_KEY)
model = genai.GenerativeModel('models/gemini-2.5-flash')

def clean_gemini_json(text):
    cleaned = re.sub(r'```(?:json)?\s*([\s\S]*?)\s*```', r'\1', text)
    return cleaned.strip()

@app.post("/analyze")
async def analyze_resume(file: UploadFile = File(...)):
    try:
        text = await extract_text_from_file(file)
        # Strict prompt to match the frontend keys
        prompt = f"""
        Act as a professional HR Data Parser. Extract data from the following resume text.
        Return ONLY a JSON object with these exact keys:
        "Education": [list of strings including degree and college],
        "Experience": [list of strings including job title and company],
        "Skills": [list of strings],
        "Projects": [list of strings]
        
        Resume Text: {text}
        """
        response = model.generate_content(prompt)
        return json.loads(clean_gemini_json(response.text))
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))

@app.post("/match")
async def match_job(resume_file: UploadFile = File(...), jd_text: str = Form(...)):
    try:
        resume_text = await extract_text_from_file(resume_file)
        
        # We explicitly ask for a numeric value for the percentage to avoid parsing errors
        prompt = f"""
        Analyze the Resume against the Job Description (JD). 
        Return ONLY a JSON object with:
        "Match Percentage": (a number between 0 and 100),
        "Missing Skills": [list of strings],
        "Strength Areas": [list of strings]
        
        Resume: {resume_text}
        JD: {jd_text}
        """
        response = model.generate_content(prompt)
        # Using the clean_gemini_json function we created earlier
        json_data = json.loads(clean_gemini_json(response.text))
        return json_data
    except Exception as e:
        print(f"Match Error: {e}")
        raise HTTPException(status_code=500, detail=str(e))