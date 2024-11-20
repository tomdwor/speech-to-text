import speech_recognition as sr
from datetime import datetime
import signal
import io
import wave


def transcribe_speech():
    """
    Records speech from microphone and saves transcription to a text file.
    Can be stopped with Ctrl+C.
    """
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
            text = recognizer.recognize_google(audio)
            filename = f"output/speech_transcript_{datetime.now().strftime('%Y%m%d_%H%M%S')}.txt"

            with open(filename, 'w') as file:
                file.write(text)

            return text, filename

        except sr.UnknownValueError:
            return "Could not understand audio", None
        except sr.RequestError:
            return "Could not connect to speech recognition service", None


if __name__ == "__main__":
    text, filename = transcribe_speech()
    if filename:
        print(f"\nTranscription saved to: {filename}")
        print(f"Transcribed text: {text}")
    else:
        print(f"Error: {text}")
