import PyPDF2
import docx
import io

async def extract_text_from_file(file):
    content = await file.read()
    file_extension = file.filename.split('.')[-1].lower()
    text = ""

    if file_extension == 'pdf':
        reader = PyPDF2.PdfReader(io.BytesIO(content))
        for page in reader.pages:
            text += page.extract_text()
    elif file_extension in ['docx', 'doc']:
        doc = docx.Document(io.BytesIO(content))
        for para in doc.paragraphs:
            text += para.text + "\n"
            
    return text