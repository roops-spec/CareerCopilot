from app.services.ai_client import model

def analyze_resume(text):

    prompt = f"""
Analyze this resume.

Return STRICT JSON only:

{{
  "ats_score": 85,
  "skills_found": ["Python", "Java"],
  "summary": "Strong backend candidate"
}}

Resume:
{text}
"""

    response = model.generate_content(prompt)
    result = response.text

    result = result.replace("```json", "")
    result = result.replace("```", "")
    result = result.strip()

    return result