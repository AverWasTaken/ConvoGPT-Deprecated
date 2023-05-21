# Text-to-Speech and Speech-to-Text Conversation Analysis Program

## Description

This program is a comprehensive solution that leverages the power of artificial intelligence for text-to-speech and speech-to-text conversions and conversation analysis. The program uses the GPT-3 or GPT-4 language model for conversation analysis and the Eleven Labs API for text-to-speech conversion. 

## Features

1. **Text-to-Speech Conversion**: This feature converts input text into speech using the Eleven Labs API. The generated speech file is saved as an MP3 file.

2. **Speech-to-Text Conversion and Conversation Analysis**: This feature transcribes audio files into text using the OpenAI API. The transcribed text is then analyzed by the GPT-3 or GPT-4 language model to identify people, emotions, meanings of conversations, and other important factors. The transcribed text and its analysis are saved as a text file.

3. **Audio File Analysis**: The user can provide an audio file path, and the program will transcribe the audio, analyze the conversation, and generate a speech file from the analysis text.

## Getting Started

### Prerequisites

- Python 3.x
- OpenAI API key
- Eleven Labs API key
- Required Python packages: `openai`, `os`, `requests`, `json`, `time`, `tqdm`, `colorama`

### Usage

1. Clone the repository.
2. Install the required Python packages using pip: `pip install openai os requests json time tqdm colorama`.
3. Set your OpenAI API key in the `OPENAI_API_KEY` constant.
4. Run the program: `python main.py`.
5. When prompted, provide the path to the audio file you want to transcribe and analyze.

## License

This project is licensed under the MIT License - see the [LICENSE.md](LICENSE.md) file for details.
