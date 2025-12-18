import openai

openai.api_key = "YOUR_API_KEY"

def resume_advice(resume_text):
    prompt = f"improve this resume and suggest missing skills:\n{resume_text}"

    response = openai.chatcompletion.create(
        model="gpt-4",
        messages=[{"role": "user", "content": prompt}]
    )
    return response.choices[0].message.content