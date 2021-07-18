import pickle
import librosa
import torch
from transformers import Wav2Vec2ForCTC, Wav2Vec2Tokenizer

# Loading models
tokenizer = Wav2Vec2Tokenizer.from_pretrained("./")
model = Wav2Vec2ForCTC.from_pretrained('./')
with open('summarize.pickle', 'rb') as handle:
    summarizer = pickle.load(handle)


# For converting speech to text

def asr_transcript(audio_file, model, tokenizer):

    transcript = ""

    stream = librosa.stream(audio_file, block_length=10, frame_length=16000, hop_length=16000)
    # print(stream)

    for speech in stream:

        # print(speech, speech.shape)
        if len(speech.shape) > 1: speech = speech[:, 0] + speech[:, 1]

        input_values = tokenizer(speech, return_tensors="pt").input_values
        logits = model(input_values).logits

        predicted_ids = torch.argmax(logits, dim=-1)
        transcription = tokenizer.decode(predicted_ids[0])
        # print(transcription)
        transcript += transcription.lower() + " "

    return transcript


# For summarizing

def summarize(text):

    summary = summarizer(text)

    return summary
