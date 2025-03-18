


# # Load NLP model
# nlp = spacy.load("en_core_web_sm")
# def extract_keywords(text):
#     doc = nlp(text)
#     keywords = []
#     for token in doc:
#         if token.pos_ in ["NOUN", "PROPN", "VERB"] and not token.is_stop:
#             keywords.append(token.lemma_)
#     for ent in doc.ents:
#         keywords.append(ent.text)
#     return list(set(keywords))  # Remove duplicates

# # def extract_keywords(text):
# #     doc = nlp(text)
# #     keywords = [token.text for token in doc if token.pos_ in ["NOUN", "PROPN", "VERB"]]
# #     return list(set(keywords))  # Remove duplicates

# # # Sample job description


# print("Extracted Keywords:", extract_keywords(job_desc))


# filepath: c:\Users\SUNYLoaner\Desktop\Buddy\keyword_extraction.py
import spacy
try:
    nlp = spacy.load("en_core_web_sm")
except OSError:
    import subprocess
    subprocess.run(["python", "-m", "spacy", "download", "en_core_web_sm"])
    nlp = spacy.load("en_core_web_sm")



def extract_keywords(job_desc):
    doc = nlp(job_desc)
    keywords = []
    for token in doc:
        if token.pos_ in ["NOUN", "PROPN", "VERB"] and not token.is_stop:
            keywords.append(token.lemma_)
    for ent in doc.ents:
        keywords.append(ent.text)
 
    return list(set(keywords))  # Remove duplicates
