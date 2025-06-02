import requests
from config import GOOGLE_TRANSLATE_API_KEY

def translate_text(text, source_lang="zh", target_lang="en"):
    url = f"https://translation.googleapis.com/language/translate/v2"
    params = {
        "q": text,
        "source": source_lang,
        "target": target_lang,
        "format": "text",
        "key": GOOGLE_TRANSLATE_API_KEY
    }

    response = requests.post(url, params=params)
    if response.status_code == 200:
        translated_text = response.json()['data']['translations'][0]['translatedText']
        return translated_text
    else:
        raise Exception(f"Translate API error: {response.text}")
