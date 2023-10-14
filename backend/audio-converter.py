import os

import openai

os.environ['OPENAI_API_KEY'] = "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"
openai.api_key = os.environ['OPENAI_API_KEY']
# Iterate over the data/db/audio directory
# For each file, transcribe it and save the transcription to a file in the data/db/transcriptions directory
files = os.listdir("/Users/tim/Documents/Sage AI Stanford/people-recommender/data/db/audio")
for file in files:
    audio_file = open(f"/Users/tim/Documents/Sage AI Stanford/people-recommender/data/db/audio/{file}", "rb")
    transcript = openai.Audio.transcribe("whisper-1", audio_file)
    with open(f"/Users/tim/Documents/Sage AI Stanford/people-recommender/data/db/transcriptions/{file}.txt", 'w') as file:
        file.write(transcript)
    print(f"Transcribed {file}")
