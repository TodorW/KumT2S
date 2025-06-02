from speech_to_text import transcribe_audio
from translate_text import translate_text
from summarize_text import summarize_text

def main():
    print("Dobrodošao u Kineski-Engleski glasovni prevodilac sa sažetkom!")
    print("------------------------------------------------------------")
    audio_path = input("Unesi putanju do audio fajla sa kineskim govorom (WAV 16kHz): ")

    try:
        print("\nPrepoznavanje govora...")
        chinese_text = transcribe_audio(audio_path)
        print(f"\nPrepoznat kineski tekst:\n{chinese_text}")

        print("\nPrevođenje na engleski...")
        english_text = translate_text(chinese_text)
        print(f"\nPrevedeni tekst:\n{english_text}")

        print("\nSažimanje teksta...")
        summary = summarize_text(english_text)
        print(f"\nSažetak:\n{summary}")

    except Exception as e:
        print(f"\nDošlo je do greške: {e}")

if __name__ == "__main__":
    main()
