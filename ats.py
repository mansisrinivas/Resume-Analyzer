

def calculate_ats_score(job_keywords, resume_text):
    matched = [kw for kw in job_keywords if kw.lower() in resume_text.lower()]
    score = len(matched) / len(job_keywords) * 100  # Percentage match
    return round(score, 2)