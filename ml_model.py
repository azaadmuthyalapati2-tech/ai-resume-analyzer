import pandas as pd
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.naive_bayes import MultinomialNB
import pickle

data = pd.read_csv("data/resume.csv")

x = data["resume_text"]
y = data["job_role"]

vectorizer = TfidfVectorizer()
x_vec = vectorizer.fit_transform(x)

model = MultinomialNB()
model.fit(x_vec,y)

pickle.dump(model,vectorizer), open("models/job_model.pkl", "wb")