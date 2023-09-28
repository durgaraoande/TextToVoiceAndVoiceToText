import elevenlabs
import whisper

class TextToVoiceAndVoiceToText:
    def __init__(self):
        # Initialize Eleven Labs API
        elevenlabs.set_api_key("your-api-key")

    def text_to_voice(self):
        text = input("Enter text: ")
        while not text.strip():  # Check for empty text
            print("Text cannot be empty. Please enter text.")
            text = input("Enter text: ")
        
        voice = "Daniel"
        audio = elevenlabs.generate(text=text, voice=voice)
        elevenlabs.play(audio)

    def voice_to_text(self):
        # Load the Whisper model
        model = whisper.load_model("base")
        audio_file_path = input("Enter audio file path: ")
        
        while True:
            try:
                with open(audio_file_path, "rb") as audio_file:
                    break
            except FileNotFoundError:
                print("File not found. Please enter a valid audio file path.")
                audio_file_path = input("Enter audio file path: ")

        result = model.transcribe(audio_file_path, fp16=False)
        print(result["text"])

if __name__ == "__main__":
    app = TextToVoiceAndVoiceToText()
    while True:
        print("Choose an option:")
        print("1. Text to Voice")
        print("2. Voice to Text")
        print("3. Exit")
        choice = input("Enter your choice (1/2/3): ")

        if choice == "1":
            app.text_to_voice()
        elif choice == "2":
            app.voice_to_text()
        elif choice == "3":
            break
        else:
            print("Invalid choice. Please select 1, 2, or 3.")
