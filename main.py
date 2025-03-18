
from keyword_extraction import extract_keywords
from resume_analyzer import extract_resume_text
from ats import calculate_ats_score
from comparison import find_missing_keywords

def main():
    # Extract keywords from job description
    job_keywords = extract_keywords(job_desc)
    print("Keywords are:",job_keywords)

    # Extract text from resume
    resume_text = extract_resume_text(resume_path)

    missing_keywords=find_missing_keywords(job_keywords, resume_text)
    print("\n\nMissing keywords:",missing_keywords)

    # Calculate ATS score
    ats_score = calculate_ats_score(job_keywords, resume_text)
    print("Your ATS Score:", ats_score, "%")

if __name__ == "__main__":
    main()