from fastapi import FastAPI, UploadFile, File
from app.services.resume_analyzer import analyze_resume
import fitz
import json
import os

app =FastAPI()

@app.get("/")
def home():
    return {"message": "Career Copilot Running"}

@app.post("/upload-resume")
async def uplaod_resume(file: UploadFile = File(...)):

    uploads_dir = "uploads"
    os.makedirs(uploads_dir, exist_ok=True)

    file_path = os.path.join(uploads_dir, file.filename)
    with open(file_path, "wb") as buffer:
        content = await file.read()
        buffer.write(content)
    text = extract_text(file_path)
    result = analyze_resume(text)
    result = json.loads(result)

    return {
        "filename": file.filename,
        "saved_to": file_path,
        "preview": text[:500],
        "analysis": result
    }
def extract_text(pdf_path):
    
    doc = fitz.open(pdf_path)

    text = ""

    for page in doc:
        text += page.get_text()

    return text