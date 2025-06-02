import openai
from config import OPENAI_API_KEY

openai.api_key = OPENAI_API_KEY

def summarize_text(text):
    prompt = f"Please provide a concise and clear summary of the following text:\n\n{text}\n\nSummary:"
    
    response = openai.Completion.create(
        engine="text-davinci-003",
        prompt=prompt,
        max_tokens=100,
        temperature=0.5,
        top_p=1,
        frequency_penalty=0,
        presence_penalty=0
    )
    
    summary = response.choices[0].text.strip()
    return summary
