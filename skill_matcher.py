def match_skills(resume_text, required_skills):
    matched = [skill for skill in required_skills if skill.lower() in resume_text.lower()]
    return matched