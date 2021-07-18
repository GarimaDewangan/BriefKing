# BriefKing
**Summer Of Code | Implementation Project**  
  
*I was unable to upload some files on github. Please check the drive link:*  
https://drive.google.com/drive/folders/1dpTqg2lhS5CnP_s00b7bSvTwKTErm0Iv?usp=sharing  

  
*Checkpoint1*  
 - Completed a course on ML (Check pdf file [#Week1-2](https://github.com/GarimaDewangan/BriefKing/blob/main/%23WEEK%201-2.pdf)) 
   
   
 *Checkpoint2*    
 - Compared different ML/DL models for speech to text conversion (Check pdf file [ML-Models]())  
 - Best Model I found was espnet
 - Model decided by the group is Transformer wav2vec model    
  
  
*Checkpoint3*
 - Compared different denoising models and libraries(check pdf file [Garima-Audio-denoising](https://github.com/GarimaDewangan/BriefKing/blob/main/Garima_Audio-denoising.pdf)  )
 - Best I found was logmmse
 - Overall model decided by the group is facebook-denoiser
 - Designed a web app on streamlit to deploy the model(Currently running through google colab)  
 - The app takes mp3 audio, converts speech to text and then summarizes the text  
  
    
***Files in the Repository***
 - *BriefKing.py* : The code for streamlit app 
 - *requirements.txt* : Contains the list of required python libraries
 - *input.wav* : The audio file used for testing denoising and speech2text models
 - *SOC-BriefKing.py* : Colab file to run streamlit app BriefKing.py on colab [![Open In Colab](https://colab.research.google.com/assets/colab-badge.svg)](https://colab.research.google.com/drive/1AhWYmXGdHdvu8LbD6Fbe_2ivN_xFt9b9?usp=sharing) (This app only contains speech to text and summarization)
 
 ***References*** 
 >**Speech2Text**  
 >> https://github.com/at16k/at16k  
 >> https://github.com/snakers4/silero-models  
 >> https://pypi.org/project/SpeechRecognition/  
 >> https://github.com/pannous/tensorflow-speech-recognition  
 >> https://github.com/Picovoice/cheetah  
 >> https://github.com/espnet/espnet
 >> https://huggingface.co/transformers/    


 >**Denoising**  
 >> https://github.com/xiph/rnnoise  
 >> https://pypi.org/project/noisereduce/  
 >> https://github.com/dodiku/noise_reduction  
 >> https://pypi.org/project/logmmse/  
 >> https://github.com/N-HANS/N-HANS  
  
 >**Development**  
 >> https://docs.streamlit.io/en/0.65.0/tutorial/index.html  
 >> https://docs.python.org/3/library/pickle.html#module-pickle  
  
 >**Misc.**
 >> https://developers.google.com/machine-learning/crash-course  
 >> https://stackoverflow.com/questions/5120555/how-can-i-convert-a-wav-from-stereo-to-mono-in-python
 
> Used [transformers](https://github.com/huggingface/transformers) library for Speech2Text conversion and summarization

