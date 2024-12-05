# Speech to Text Converter

A versatile Python toolkit that converts spoken words into text using Google's Speech Recognition service. Features both microphone recording and MP3 file conversion capabilities with support for multiple languages. Perfect for transcription, accessibility needs, and content creation.

## Features

- 🎤 Real-time microphone recording with adjustable ambient noise detection
- 🎵 MP3 file conversion support
- 🌍 Support for 10 languages including English, Spanish, French, and more
- 📝 Generates UTF-8 encoded text files
- 🚀 Simple command-line interface
- ⚡ Real-time processing
- 🛑 Graceful recording termination with Ctrl+C

## Requirements

- Python 3.12 or higher
- Internet connection (required for Google Speech Recognition)
- portaudio
- ffmpeg
- pip (Python package installer)

## Installation

1. Clone the repository:
```bash
git clone https://github.com/yourusername/speech-to-text.git
cd speech-to-text
```

2. Install system dependencies:

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

3. Create and activate a virtual environment:
```bash
# On Unix/macOS
python3.12 -m venv .venv
source .venv/bin/activate

# On Windows
python3.12 -m venv .venv
.venv\Scripts\activate
```

4. Install required packages:
```bash
pip install -r requirements.txt
```

## Usage

### List Supported Languages
Both tools support the same set of languages. To see available languages:
```bash
python mic_speech_to_text.py --list-languages
# or
python mp3_speech_to_text.py --list-languages
```

### Microphone Recording

#### Basic Command Structure
```bash
python mic_speech_to_text.py -o <output_file> [-l <language_code>]
```

#### Examples
```bash
# English (default)
python mic_speech_to_text.py -o output/transcription.txt

# Spanish
python mic_speech_to_text.py -o output/transcription.txt -l es
```

#### Command Line Arguments

| Argument | Short | Required | Description |
|----------|--------|----------|-------------|
| --output-file | -o | Yes | Path to output text file (.txt) |
| --language | -l | No | Language code (default: 'en') |
| --list-languages | - | No | Show available language codes |
| --help | -h | No | Show help message |

### MP3 Conversion

#### Basic Command Structure
```bash
python mp3_speech_to_text.py -i <input_file> -o <output_file> [-l <language_code>]
```

#### Examples
```bash
# English (default)
python mp3_speech_to_text.py -i example_data/ibiza_en.mp3 -o output/ibiza_en.txt

# Spanish
python mp3_speech_to_text.py -i example_data/ibiza_es.mp3 -o output/ibiza_es.txt -l es
```

#### Command Line Arguments

| Argument | Short | Required | Description |
|----------|--------|----------|-------------|
| --input-file | -i | Yes | Path to input MP3 file |
| --output-file | -o | Yes | Path to output text file (.txt) |
| --language | -l | No | Language code (default: 'en') |
| --list-languages | - | No | Show available language codes |
| --help | -h | No | Show help message |

### Supported Languages

| Code | Language |
|------|----------|
| de | German |
| en | English |
| es | Spanish |
| fr | French |
| it | Italian |
| ja | Japanese |
| ko | Korean |
| pt | Portuguese |
| ru | Russian |
| zh-CN | Chinese (Simplified) |

## Output

- Text files are saved in UTF-8 encoding
- Output directories are created automatically if they don't exist
- File paths can be relative or absolute

## Project Structure
```
speech-to-text/
├── data/
│   └── .gitignore
├── example_data/
│   ├── ibiza_en.mp3
│   └── ibiza_es.mp3
├── output/
│   └── .gitignore
├── .gitignore
├── LICENSE
├── mic_speech_to_text.py
├── mp3_speech_to_text.py
├── README.MD
└── requirements.txt
```

## Troubleshooting

### Common Issues

1. **Microphone Not Found**: 
   - Ensure your microphone is properly connected
   - Check system permissions for microphone access

2. **MP3 Conversion Errors**:
   - Verify ffmpeg is properly installed
   - Check if the input file is a valid MP3

3. **Language Recognition Issues**:
   - Use correct language codes (check with --list-languages)
   - Ensure clear pronunciation for non-native languages
   - Some languages may have lower recognition accuracy

4. **Internet Connection Error**:
   - The tool requires an active internet connection for Google Speech Recognition
   - Check your network connection if you get recognition errors

### Best Practices

1. **Microphone Recording**:
   - Use in a quiet environment
   - Allow ambient noise calibration to complete
   - Speak clearly and at a moderate pace
   - Use Ctrl+C to stop recording

2. **MP3 Files**:
   - Use high-quality audio recordings
   - Ensure clear speech with minimal background noise
   - Keep files under 10MB for best results

3. **Language Selection**:
   - Choose the correct language code for your audio
   - For better accuracy, use native speakers when possible
   - Consider regional accents when selecting language

## Development

### Contributing

1. Fork the repository
2. Create your feature branch
3. Commit your changes
4. Push to the branch
5. Create a Pull Request

## License

This project is licensed under the MIT License - see the LICENSE file for details.

## Acknowledgments

- [SpeechRecognition](https://github.com/Uberi/speech_recognition) for providing the speech recognition functionality
- [PyAudio](https://people.csail.mit.edu/hubert/pyaudio/) for audio input support
- [pydub](https://github.com/jiaaro/pydub) for audio file processing
- Google Speech Recognition API for multi-language support

## Contact

For bug reports and feature requests, please use the GitHub Issues page.

## Blog article

[Transform Speech into Text with Python: A Versatile Speech Recognition Tool - Tomasz Dworakowski Blog](https://www.tdworakowski.com/2024/11/transform-speech-into-text-with-python.html)
