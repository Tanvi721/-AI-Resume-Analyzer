# 📄 AI Resume Analyzer & Job Matcher

An AI-powered web application that parses resumes and intelligently matches them with job descriptions using Generative AI. The system extracts structured resume data and provides a match percentage, missing skills, and strength areas to help candidates improve their job readiness.

---


## 🎥 Project Demo

▶️ **[Watch Full Project Demo](AI_Resume_Analyzer_Demo.mp4.webm)**

This screen recording demonstrates:
- Resume upload (PDF/DOCX)
- AI-based resume parsing
- Extracted education, experience, skills, and projects
- Job description matching
- Match percentage, missing skills, and strength areas

---

## 🚀 Features

- Upload resume in **PDF or DOCX** format  
- AI-based resume parsing:
  - Education
  - Work Experience
  - Skills
  - Projects
- Job description matching with:
  - Overall Match Percentage
  - Missing Skills
  - Strength Areas
- Interactive UI using **Streamlit**
- High-performance backend using **FastAPI**
- Powered by **Google Gemini Generative AI**

---

## 🖼️ Screenshots

| Resume Upload & Parsing | Parsed Resume |
|------------------------|---------------|
| <img width="1920" height="1080" alt="Screenshot (1)" src="https://github.com/user-attachments/assets/1571ffa1-9c3b-4293-9b2f-19d5ca76ba1d" /> | <img width="1920" height="1080" alt="Screenshot (5)" src="https://github.com/user-attachments/assets/adc3725e-93f5-44ca-8742-c68f730dbb28" />
 |

| Skills & Projects | Job Matching | Match percentage, missing skills, and strength areas |
|------------------|--------------|--------------|
| <img width="1920" height="1080" alt="Screenshot (6)" src="https://github.com/user-attachments/assets/cb21c16b-6b27-41df-9505-e11e75c0452a" /> | <img width="1920" height="1080" alt="Screenshot (7)" src="https://github.com/user-attachments/assets/d8f78f32-8d8c-4c85-b425-abcc0ec217df" /> | <img width="1920" height="1080" alt="Screenshot (8)" src="https://github.com/user-attachments/assets/740c9455-9164-4b9d-88d2-e14049c31826" /> |



---

## 🛠️ Tech Stack

### Frontend
- Streamlit

### Backend
- FastAPI
- Uvicorn

### AI / NLP
- Google Generative AI (Gemini)

### Resume Parsing
- PyPDF2
- python-docx

---

## 📁 Project Structure
AI-Resume-Analyzer/
- ├── app.py # Streamlit frontend
- ├── main.py # FastAPI backend
- ├── utils.py # Resume text extraction
- ├── run_all.py # Run frontend & backend together
- ├── check_models.py # Gemini model checker
- ├── requirements.txt # Dependencies



---

## ⚙️ Installation

# 1️⃣ Clone Repository
git clone https://github.com/your-username/AI-Resume-Analyzer.git
cd AI-Resume-Analyzer

# 2️⃣ Create Virtual Environment
python -m venv venv
venv\Scripts\activate     # Windows
source venv/bin/activate # Linux / Mac

# 3️⃣ Install Requirements
pip install -r requirements.txt


# 🔑 API Key Setup

Add your Google Generative AI API Key inside main.py:
GENAI_API_KEY = "YOUR_API_KEY"

# ▶️ Run the Application
Run Everything Together (Recommended)
python run_all.py

OR Run Separately

- Backend
uvicorn main:app --reload --port 8000

- Frontend
  streamlit run app.py

# 🌐 Access URLs

- Frontend (Streamlit): http://localhost:8501

- Backend (FastAPI): http://localhost:8000

# 📊 How It Works

1. Upload resume (PDF/DOCX)

2. AI extracts structured information

3. Paste job description

4. AI calculates:
- Match Percentage
- Missing Skills
- Strength Areas

# 🚀 Future Enhancements

- Resume improvement suggestions

- ATS keyword optimization

- Multiple resume comparison

- User authentication

- Cloud deployment (AWS / Azure / GCP)

# 👩‍💻 Author

# Tanvi Barve
Data Analyst | Data Scientist | AI & ML Enthusiast



