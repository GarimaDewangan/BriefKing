#Importing required libraries
import streamlit as st
import pickle5 as pickle
import base64
import librosa
import torch
from pydub import AudioSegment
from transformers import Wav2Vec2ForCTC, Wav2Vec2Tokenizer,pipeline

#Defining required functions
def mono(x): # TO convert audio from stereo to mono
  sound = AudioSegment.from_mp3(x)
  sound = sound.set_channels(1)
  sound = sound.set_frame_rate(16000)
  t = sound.export(format='wav')
  return(t) 

def create_download(object_to_download):#To create a downloadable link
	b64 = base64.b64encode(object_to_download.encode()).decode()
	return f'<a href="data:file/txt;base64,{b64}" download="result.txt"> Download </a>' #to create a download link

def asr_transcript(audio_file,model,tokenizer):#For speech to text conversion
     transcript = ""
  
     stream = librosa.stream(
         audio_file, block_length=10, frame_length=16000, hop_length=16000
     )
     print(stream)

     for speech in stream:
         print(speech, speech.shape)
         if len(speech.shape) > 1:
           speech = speech[:, 0] + speech[:, 1]

         input_values = tokenizer(speech, return_tensors="pt").input_values
         logits = model(input_values).logits

         predicted_ids = torch.argmax(logits, dim=-1)
         transcription = tokenizer.decode(predicted_ids[0])
         #print(transcription)
         transcript += transcription.lower() + " "
     return transcript#Speech to text conversion 

def summary(text) : #Summarizing text
	summary = summarizer(text)
	return(summary)

# tokenizer = Wav2Vec2Tokenizer.from_pretrained("facebook/wav2vec2-large-960h-lv60-self")
# model = Wav2Vec2ForCTC.from_pretrained("facebook/wav2vec2-large-960h-lv60-self")
# summarizer = pipeline("summarization")

#Loading models
tokenizer = Wav2Vec2Tokenizer.from_pretrained("./")
model = Wav2Vec2ForCTC.from_pretrained('./')
with open('summarize.pickle', 'rb') as handle:
    summarizer = pickle.load(handle)

#Interface
st.title('BriefKing')
st.sidebar.image("briefKing.jpeg")
expander = st.sidebar.beta_expander("About BriefKing")
expander.write("BriefKing is a web app that can be used to convert audio to summarized text" )
expander = st.sidebar.beta_expander("How to use BriefKing")
expander.markdown(" (1) Upload the audio file which you want to summarize ") 
expander.markdown(" (2) Wait for a few seconds") 
expander.markdown("(3) Download the summarized text file")

data = st.file_uploader("Select an audio file", type=["mp3"])

#Conversion (Speech to Text)
if st.button("Brief It!"):
  with st.spinner("Please wait...summarizing...it might take a few minutes......."):
    texted = asr_transcript(mono(data),model,tokenizer)
    print("Speech to Text conversion completed")
    output = summary(texted)
    print("Summarization completed")
    st.success('Done')
    st.markdown("**Full Text**")
    st.write(texted)
    link = create_download(texted)
    st.markdown(link, unsafe_allow_html=True)
    st.markdown("**Summary**")
    st.write(output[0])
    link = create_download(str(output[0]))
    st.markdown(link, unsafe_allow_html=True)
