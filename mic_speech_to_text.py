import argparse
import io
import signal
import wave

import speech_recognition as sr

# Supported languages with their codes
SUPPORTED_LANGUAGES = {
    'en': 'English',
    'es': 'Spanish',
    'fr': 'French',
    'de': 'German',
    'it': 'Italian',
    'pt': 'Portuguese',
    'ru': 'Russian',
    'zh-CN': 'Chinese (Simplified)',
    'ja': 'Japanese',
    'ko': 'Korean'
}


def transcribe_speech(output_file, language='en'):
    """
    Records speech from microphone and saves transcription to a text file.
    Can be stopped with Ctrl+C.
    """
    if language not in SUPPORTED_LANGUAGES:
        return f"Language code '{language}' is not supported", None

    recognizer = sr.Recognizer()
    recording = True

    def signal_handler(signum, frame):
        nonlocal recording
        print("\nStopping recording...")
        recording = False

    signal.signal(signal.SIGINT, signal_handler)

    with sr.Microphone() as source:
        print("Adjusting for ambient noise... Please wait.")
        recognizer.adjust_for_ambient_noise(source, duration=2)

        print("Listening... Speak now! (Press Ctrl+C to stop)")

        # Create an in-memory audio buffer
        audio_buffer = io.BytesIO()
        wav_buffer = wave.open(audio_buffer, 'wb')
        wav_buffer.setnchannels(1)
        wav_buffer.setsampwidth(2)
        wav_buffer.setframerate(44100)

        while recording:
            try:
                audio_chunk = source.stream.read(4096)
                if audio_chunk:
                    wav_buffer.writeframes(audio_chunk)
            except KeyboardInterrupt:
                break

        wav_buffer.close()

        # Convert buffer to audio data
        audio_buffer.seek(0)
        with sr.AudioFile(audio_buffer) as audio_source:
            audio = recognizer.record(audio_source)

        try:
            text = recognizer.recognize_google(audio, language=language)
            with open(output_file, 'w') as file:
                file.write(text)
            return text, output_file

        except sr.UnknownValueError:
            return "Could not understand audio", None
        except sr.RequestError:
            return "Could not connect to speech recognition service", None


def list_supported_languages():
    """Print a formatted list of supported languages."""
    print("\nSupported Languages:")
    print("-------------------")
    max_code_length = max(len(code) for code in SUPPORTED_LANGUAGES.keys())
    for code, name in sorted(SUPPORTED_LANGUAGES.items()):
        print(f"{code.ljust(max_code_length)} : {name}")
    print()


def main():
    parser = argparse.ArgumentParser(description='Convert microphone speech to text')

    # Create argument groups
    required_args = parser.add_argument_group('required arguments')
    optional_args = parser.add_argument_group('optional arguments')

    # Move --list-languages to parser level (not in any group)
    parser.add_argument('--list-languages', action='store_true',
                        help='List all supported languages')

    # Required argument (only if not listing languages)
    required_args.add_argument('--output-file', '-o',
                               help='Path to output text file (.txt)')

    # Optional arguments
    optional_args.add_argument('--language', '-l', default='en',
                               help='Language code (e.g., en, es, fr). Use --list-languages to see all options')

    args = parser.parse_args()

    if args.list_languages:
        list_supported_languages()
        return

    if not args.output_file:
        parser.error("--output-file/-o is required when not using --list-languages")

    text, filename = transcribe_speech(args.output_file, args.language)
    if filename:
        print(f"\nTranscription saved to: {filename}")
        print(f"Transcribed text: {text}")
    else:
        print(f"Error: {text}")


if __name__ == "__main__":
    main()
