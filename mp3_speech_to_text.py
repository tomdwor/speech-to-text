import argparse
import os

import speech_recognition as sr
from pydub import AudioSegment

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


def convert_mp3_to_text(mp3_path, output_file, language='en'):
    """
    Converts MP3 file to text and saves transcription.
    Returns transcribed text and output filename.
    """
    if language not in SUPPORTED_LANGUAGES:
        return f"Language code '{language}' is not supported", None

    # Convert mp3 to wav (speech_recognition requires wav)
    wav_path = mp3_path.rsplit('.', 1)[0] + '.wav'
    audio = AudioSegment.from_mp3(mp3_path)
    audio.export(wav_path, format="wav")

    recognizer = sr.Recognizer()

    with sr.AudioFile(wav_path) as source:
        audio_data = recognizer.record(source)

        try:
            text = recognizer.recognize_google(audio_data, language=language)
            with open(output_file, 'w', encoding='utf-8') as f:
                f.write(text)

            os.remove(wav_path)  # Clean up temporary wav file
            return text, output_file

        except sr.UnknownValueError:
            return "Speech could not be understood", None
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
    parser = argparse.ArgumentParser(description='Convert MP3 file to text')

    # Create argument groups
    required_args = parser.add_argument_group('required arguments')
    optional_args = parser.add_argument_group('optional arguments')

    # Move --list-languages to parser level (not in any group)
    parser.add_argument('--list-languages', action='store_true',
                        help='List all supported languages')

    # Required arguments (only if not listing languages)
    required_args.add_argument('--input-file', '-i',
                               help='Path to input MP3 file')
    required_args.add_argument('--output-file', '-o',
                               help='Path to output text file (.txt)')

    # Optional arguments
    optional_args.add_argument('--language', '-l', default='en',
                               help='Language code (e.g., en, es, fr). Use --list-languages to see all options')

    args = parser.parse_args()

    if args.list_languages:
        list_supported_languages()
        return

    if not args.input_file or not args.output_file:
        parser.error("--input-file/-i and --output-file/-o are required when not using --list-languages")

    text, output_file = convert_mp3_to_text(args.input_file, args.output_file, args.language)
    if output_file:
        print(f"\nTranscription saved to: {output_file}")
        print(f"Transcribed text: {text}")
    else:
        print(f"Error: {text}")


if __name__ == "__main__":
    main()
