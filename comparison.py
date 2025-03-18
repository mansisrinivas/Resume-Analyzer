import spacy

# Load NLP model
nlp = spacy.load("en_core_web_sm")

def find_missing_keywords(job_keywords, resume_text):
    # Tokenize and lemmatize resume text
    resume_doc = nlp(resume_text)
    resume_lemmas = {token.lemma_.lower() for token in resume_doc if not token.is_stop and not token.is_digit}

    # Tokenize and lemmatize job keywords
    job_keywords_doc = nlp(" ".join(job_keywords))
    job_keywords_lemmas = {token.lemma_.lower() for token in job_keywords_doc if not token.is_stop and not token.is_digit}

    # Find missing keywords
    missing_keywords = job_keywords_lemmas - resume_lemmas
    return list(missing_keywords)