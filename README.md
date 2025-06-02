# KumT2S

**KumT2S** is a Python-based application that listens to spoken conversations, transcribes the speech into text, and translates it into a target language in real-time. It's designed to facilitate seamless multilingual communication, making it ideal for meetings, interviews, or everyday conversations.

## Features

* 🎙️ Real-time speech recognition
* 🌐 Automatic translation between languages
* 📄 Text summarization capabilities
* 🧩 Modular architecture for easy customization
* 🛠️ Configurable settings via `config.py`

## Installation

1. **Clone the repository:**

   ```bash
   git clone https://github.com/TodorW/KumT2S.git
   cd KumT2S
   ```



2. **Create and activate a virtual environment (optional but recommended):**

   ```bash
   python -m venv venv
   source venv/bin/activate  # On Windows: venv\Scripts\activate
   ```



3. **Install the required dependencies:**

   ```bash
   pip install -r requirements.txt
   ```



## Usage

1. **Configure settings:**

   Edit the `config.py` file to set your preferred source and target languages, as well as other parameters like microphone input and translation settings.

2. **Run the application:**

   ```bash
   python main.py
   ```



3. **Interact:**

   Speak into your microphone. The application will transcribe your speech, translate it into the target language, and display the translated text.

## File Structure

* `main.py` – Entry point of the application
* `config.py` – Configuration settings
* `speech_to_text.py` – Handles speech recognition
* `translate_text.py` – Manages text translation
* `summarize_text.py` – Performs text summarization
* `requirements.txt` – Lists Python dependencies

## Dependencies

The application relies on several Python libraries, including but not limited to:

* `speechrecognition`
* `googletrans`
* `transformers`
* `torch`

Ensure all dependencies are installed via the provided `requirements.txt` file.

## License

This project is licensed under the MIT License. See the [LICENSE](LICENSE) file for details.

## Contributing

Contributions are welcome! Please fork the repository and submit a pull request with your enhancements.

## Acknowledgements

Developed by [TodorW](https://github.com/TodorW).

---
