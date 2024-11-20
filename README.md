# Speech to Text Converter

Convert speech to text using microphone input or MP3 files. Uses Google Speech Recognition API for accurate transcription.

## Prerequisites

- Python 3.12
- portaudio
- ffmpeg

### System Requirements Installation

**macOS:**
```bash
brew install portaudio ffmpeg
```

**Linux:**
```bash
sudo apt-get install portaudio19-dev ffmpeg
```

**Windows:**
- Install [PortAudio](http://www.portaudio.com/download.html)
- Install [FFmpeg](https://ffmpeg.org/download.html) and add to PATH

## Setup

1. Create virtual environment:
```bash
python3.12 -m venv .venv
source .venv/bin/activate  # On Unix/macOS
.venv\Scripts\activate     # On Windows
```

2. Install dependencies:
```bash
pip install -r requirements.txt
```

## Usage

### Microphone Recording
```bash
python mic_speech_to_text.py
```
- Speak when prompted
- Press Ctrl+C to stop recording
- Transcription saves to timestamped text file

### MP3 Conversion
```bash
python mp3_speech_to_text.py
```
- Enter path to MP3 file when prompted
- Transcription saves alongside original file

## Notes
- Requires internet connection for Google Speech Recognition
- Supports multiple languages (auto-detection enabled)
- Free API has usage limitations
