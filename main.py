# from src.text_cleaner import clean_text
# from src.skill_matcher import match_skills
# import pickle



# resume = "python ml nlp sql"
# resume = clean_text(resume)

# model, vectorizer = pickle.load(open("models/job_model.pkl", "rb"))

# prediction = model.predict(vectorizer.transform([resume]))
# print("predicted jon role:", prediction[0])

# skills = ["python", "machine learning", "deep learning", "sql"]
# print("matched skills:", match_skills(resume,skills))

import pickle
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.linear_model import LogisticRegression

texts = [
    "Python developer with machine learning experience",
    "Civil engineer with site supervision experience",
    "Data scientist with NLP background"
]

labels = [1, 0, 1]

vectorizer = TfidfVectorizer()
X = vectorizer.fit_transform(texts)

model = LogisticRegression()
model.fit(X, labels)

with open("models/job_model.pkl", "wb") as f:
    pickle.dump((model, vectorizer), f)

print("Model trained and saved successfully")
