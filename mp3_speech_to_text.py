import speech_recognition as sr
from pydub import AudioSegment
import os


def convert_mp3_to_text(mp3_path):
    """
    Converts MP3 file to text and saves transcription to output folder.
    Returns transcribed text and output filename.
    """
    # Get script directory and create output directory
    script_dir = os.path.dirname(os.path.abspath(__file__))
    output_dir = os.path.join(script_dir, 'output')
    os.makedirs(output_dir, exist_ok=True)

    # Convert mp3 to wav (speech_recognition requires wav)
    wav_path = mp3_path.rsplit('.', 1)[0] + '.wav'
    audio = AudioSegment.from_mp3(mp3_path)
    audio.export(wav_path, format="wav")

    recognizer = sr.Recognizer()

    with sr.AudioFile(wav_path) as source:
        audio_data = recognizer.record(source)

        try:
            text = recognizer.recognize_google(audio_data)
            base_filename = os.path.basename(mp3_path).rsplit('.', 1)[0]
            output_file = os.path.join(output_dir, f'{base_filename}_transcript.txt')

            with open(output_file, 'w', encoding='utf-8') as f:
                f.write(text)

            os.remove(wav_path)  # Clean up temporary wav file
            return text, output_file

        except sr.UnknownValueError:
            return "Speech could not be understood", None
        except sr.RequestError:
            return "Could not connect to speech recognition service", None


if __name__ == "__main__":
    mp3_file = input("Enter path to MP3 file: ")
    text, output_file = convert_mp3_to_text(mp3_file)

    if output_file:
        print(f"\nTranscription saved to: {output_file}")
        print(f"Transcribed text: {text}")
    else:
        print(f"Error: {text}")
