import openai
import os
import requests
import json
import time
from tqdm import tqdm
from colorama import Fore, Style

# Helper function to clear console
def clear_console():
    os.system('cls' if os.name == 'nt' else 'clear')

# Voices
voices = {
    "Rachel": "21m00Tcm4TlvDq8ikWAM",
    "Domi": "AZnzlk1XvdvUeBnXmlld",
    "Bella": "EXAVITQu4vr4xnSDxMaL",
    "Antoni": "ErXwobaYiN019PkySvjV",
    "Elli": "MF3mGyEYCl7XYWbV9V6O",
    "Josh": "TxGEqnHWrfWFTfGW9XjX",
    "Arnold": "VR6AewLTigWG4xSOukaG",
    "Adam": "pNInz6obpgDQGcFmaJgB",
    "Sam": "yoZ06aMxZJJ28mfd3POQ",
}

# OpenAI Models
openai_models = {
    "GPT4": "gpt-4",
    "GPT3": "gpt-3.5-turbo",
}

# Constants
OPENAI_API_KEY = 'API-HERE'
OUTPUT_DIR = "OUTPUT-DIR-HERE"
VOICE_ID = voices['Bella']
ELEVEN_LABS_URL = f"https://api.elevenlabs.io/v1/text-to-speech/{VOICE_ID}"
HEADERS = {
    "xi-api-key": "ELEVENLABS-APIKEY-HERE",
    "Content-Type": "application/json"
}

# Set OpenAI API key
openai.api_key = OPENAI_API_KEY

def sanitize_filename(filename):
    invalid_chars = '<>:"/\\|?*'
    for char in invalid_chars:
        filename = filename.replace(char, '_')
    return filename

def convert_text_to_speech(text):
    first_word = sanitize_filename(text.split(" ")[0])
    output_filename = os.path.join(OUTPUT_DIR, f"{first_word}.mp3")

    payload = {
        "text": text,
        "model_id": "eleven_monolingual_v1",
        "voice_settings": {
            "stability": 1,
            "similarity_boost": 1
        }
    }

    print("\nGenerating speech file from provided text...\n")
    response = requests.post(ELEVEN_LABS_URL, headers=HEADERS, data=json.dumps(payload))

    if response.status_code == 200:
        with open(output_filename, 'wb') as f:
            f.write(response.content)
        print(Fore.GREEN + f"\nSpeech file has been successfully generated and saved to: {output_filename}\n" + Style.RESET_ALL)
    else:
        print(Fore.RED + f"\nError occurred while generating speech: {response.status_code}, {response.text}\n" + Style.RESET_ALL)

def transcribe_audio(file_path):
    print("\nStarting audio transcription. Please wait...\n")
    time.sleep(1)

    with open(file_path, "rb") as audio_file:
        transcript = openai.Audio.transcribe("whisper-1", audio_file)

    text = transcript["text"]
    output_file_path = os.path.join(OUTPUT_DIR, os.path.basename(file_path) + ".txt")

    with open(output_file_path, "w") as output_file:
        output_file.write(text)

    print(Fore.GREEN + f"\nTranscription completed successfully. Transcribed content saved to: {output_file_path}\n" + Style.RESET_ALL)
    time.sleep(2)

    print("\nInitiating conversation analysis...\n")
    time.sleep(2)

    analysis_prompt = f"{text}\n\nAnalyze this conversation:"
    analysis_response = openai.ChatCompletion.create(
      model=openai_models['GPT3'],
      messages=[
            {"role": "system", "content": "You are an AI called ConversationGPT, a large language model trained by OpenAI. Your job is to analyze different parts of this transcribed conversation from a speech to text program. You should identify people, emotions, meaning of conversations, and anything else you deem important. You should identify these factors in an organized manner, so that it is easily read by the user."},
            {"role": "user", "content": analysis_prompt}
        ]
    )

    with open(output_file_path, "a") as output_file:
        output_file.write("\nAnalysis:\n")
        output_file.write(analysis_response['choices'][0]['message']['content'])

    print(Fore.GREEN + f"\nConversation analysis completed. Check the updated file at: {output_file_path}\n" + Style.RESET_ALL)
    time.sleep(2)

    print("\nGenerating speech file from the analysis text...\n")

    convert_text_to_speech(analysis_response['choices'][0]['message']['content'])

if __name__ == "__main__":
    audio_file_path = input("Please provide the path to the audio file: ")
    transcribe_audio(audio_file_path)
