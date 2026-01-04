import streamlit as st
import requests

st.set_page_config(page_title="AI Resume Analyzer", layout="wide")

# Sidebar to match Screenshot (1)
with st.sidebar:
    st.header("How to use:")
    st.markdown("""
    1. **Upload Resume:** Upload your PDF or DOCX resume
    2. **View Parsed Data:** See structured resume information
    3. **Job Matching:** Enter job description and get match analysis
    """)

st.title("📄 AI Resume Analyzer")
st.write("Upload your resume and match it against job descriptions using AI")

tabs = st.tabs(["🚀 Resume Upload & Parsing", "🎯 Job Matching"])
URL = "http://127.0.0.1:8000"

# TAB 1: UPLOAD & PARSING
with tabs[0]:
    st.header("Resume Upload & Parsing")
    uploaded_file = st.file_uploader("Upload your resume (PDF or DOCX)", type=['pdf', 'docx'])
    
    if uploaded_file:
        if st.button("🔍 Extract & Parse Resume", type="primary"):
            with st.spinner("Processing resume..."):
                files = {"file": (uploaded_file.name, uploaded_file.getvalue())}
                res = requests.post(f"{URL}/analyze", files=files)
                if res.status_code == 200:
                    st.session_state['parsed_data'] = res.json()
                    st.session_state['file_cache'] = uploaded_file.getvalue()
                    st.session_state['file_name'] = uploaded_file.name
                else:
                    st.error("Extraction failed.")

    # DATA DISPLAY (Matches Screenshot 2 and 3)
    if 'parsed_data' in st.session_state:
        data = st.session_state['parsed_data']
        
        # Education Section
        st.subheader("🎓 Education")
        for edu in data.get("Education", []):
            with st.expander(f"❯ {edu}", expanded=True):
                st.write("Parsed from resume.")

        # Work Experience Section
        st.subheader("💼 Work Experience")
        for exp in data.get("Experience", []):
            with st.expander(f"❯ {exp}", expanded=True):
                st.write("Parsed from resume.")

        # Skills Section
        st.subheader("🛠️ Skills")
        skills_list = data.get("Skills", [])
        st.write(" , ".join(skills_list))

        # Projects Section
        st.subheader("🚀 Projects")
        for proj in data.get("Projects", []):
            st.markdown(f"- {proj}")

# TAB 2: MATCHING
with tabs[1]:
    st.header("Job Description Matching")
    jd_input = st.text_area("Paste the Job Description here", height=250, placeholder="Requirements, responsibilities, etc...")
    
    if st.button("🎯 Run Match Analysis", type="primary"):
        # Ensure the user has uploaded a file in Tab 1
        if 'file_cache' not in st.session_state:
            st.error("⚠️ Please upload and parse your resume in the first tab before matching!")
        elif not jd_input.strip():
            st.warning("⚠️ Please paste a Job Description to analyze.")
        else:
            with st.spinner("AI is calculating your match score..."):
                try:
                    # Retrieve file from session state
                    files = {"resume_file": (st.session_state['file_name'], st.session_state['file_cache'])}
                    data = {"jd_text": jd_input}
                    
                    res = requests.post(f"{URL}/match", files=files, data=data)
                    
                    if res.status_code == 200:
                        result = res.json()
                        
                        # Process the Match Percentage safely
                        # We convert to int just in case the AI sent a string
                        raw_score = result.get('Match Percentage', 0)
                        try:
                            score = int(str(raw_score).replace('%', ''))
                        except:
                            score = 0
                        
                        # Display results exactly like the screenshots
                        st.metric("Overall Match Score", f"{score}%")
                        st.progress(score / 100)
                        
                        col1, col2 = st.columns(2)
                        with col1:
                            st.markdown("### ❌ Missing Skills")
                            missing = result.get("Missing Skills", [])
                            if missing:
                                for m in missing: st.write(f"- {m}")
                            else:
                                st.write("None! You have all the required skills.")
                                
                        with col2:
                            st.markdown("### ✅ Strength Areas")
                            strengths = result.get("Strength Areas", [])
                            for s in strengths: st.write(f"- {s}")
                            
                    else:
                        st.error(f"Backend failed: {res.text}")
                except Exception as e:
                    st.error(f"Connection Error: {e}")