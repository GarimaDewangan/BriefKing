# Importing required libraries
import streamlit as st
import base64
import time

# Importing modules
import Audio_Processing as Ap
import Speech_to_text as Stt


# Function to create a downloadable link
def create_download(object_to_download):
    b64 = base64.b64encode(object_to_download.encode()).decode()
    return f'<a href="data:file/txt;base64,{b64}" download="result.txt"> Download </a>'  # to create a download link


# Interface
st.title('BriefKing')
st.sidebar.image("briefKing.jpeg")
expander = st.sidebar.beta_expander("About BriefKing")
expander.write("BriefKing is a web app converts audio to text and summarizes the text")
expander = st.sidebar.beta_expander("How to use BriefKing")
expander.markdown(" (1) Upload the audio file which you want to summarize ")
expander.markdown(" (2) Wait for a few minutes")
expander.markdown("(3) Download the text file as well as the summary")

audio_data = st.file_uploader("Select an audio file", type=["mp3"])

# Processing of Speech, Conversion to text and, Summarization
if st.button("Brief It!"):
    with st.spinner("Please wait for a few minutes......."):

        time.sleep(0.5)
        t = st.empty()
        t.write("Audio processing started...")
        processed_audio = Ap.process(audio_data)
        t.write("Audio processing started... Done!")

        time.sleep(0.5)
        t = st.empty()
        t.write("Converting into text...")
        texted = Stt.asr_transcript(processed_audio, Stt.model, Stt.tokenizer)
        t.write("Converting into text... Done!")

        time.sleep(0.5)
        t = st.empty()
        t.write("Summarizing...")
        output = Stt.summarize(texted)
        t.write("Summarizing... Done!")

        time.sleep(1)
        st.success("Finished")

        # Display text
        time.sleep(0.5)
        st.markdown("**Full Text**")
        time.sleep(0.2)
        st.write(texted)
        link = create_download(texted)
        st.markdown(link, unsafe_allow_html=True)

        # Display Summary
        time.sleep(0.5)
        st.markdown("**Summary**")
        time.sleep(0.2)
        st.write(str(output[0]))
        link = create_download(str(output[0]))
        st.markdown(link, unsafe_allow_html=True)

        # Message
        time.sleep(1)
        st.write("Thanks for using BriefKing :)")
