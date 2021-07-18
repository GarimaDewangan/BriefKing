# BriefKing
**Summer Of Code | Implementation Project**  
  
*I was unable to upload some files on github. Please check the drive link for all files:*  
https://drive.google.com/drive/folders/1dpTqg2lhS5CnP_s00b7bSvTwKTErm0Iv?usp=sharing  

***Work Distribution over checkpoints***  

*Checkpoint1*  
 - Completed a course on ML (Check pdf file [#Week1-2](https://github.com/GarimaDewangan/BriefKing/blob/main/%23WEEK%201-2.pdf)) 
   
   
 *Checkpoint2*    
 - Compared different ML/DL models for speech to text conversion (Check pdf file [ML-Models](https://github.com/GarimaDewangan/BriefKing/blob/main/ML-Models.pdf))  
 - Best Model I found was espnet
 - Model decided by the group is Transformer wav2vec model    
  
  
*Checkpoint3*
 - Compared different denoising models and libraries(check pdf file [Garima-Audio-denoising](https://github.com/GarimaDewangan/BriefKing/blob/main/Garima_Audio-denoising.pdf)  )
 - Best I found was logmmse
 - Overall model decided by the group is facebook-denoiser
 - Designed a web app on streamlit to deploy the model(Currently running through google colab)  
 - The app takes mp3 audio, converts speech to text and then summarizes the text  
  
    
***Files in the Repository***
 - *BriefKing.py* : The code for streamlit app [Speech2Text and Summarize]
 - *requirements.txt* : Contains the list of required python libraries
 - *input.wav* : The audio file used for testing denoising and speech2text models
 - *SOC-BriefKing.py* : Colab file to run BriefKing.py on colab [![Open In Colab](https://colab.research.google.com/assets/colab-badge.svg)](https://colab.research.google.com/drive/1AhWYmXGdHdvu8LbD6Fbe_2ivN_xFt9b9?usp=sharing)  
 - *BriefKing_FinalApp.py* : Colab file to run final code integrating denoiser-speech2text-summarizer [![Open In Colab](https://colab.research.google.com/assets/colab-badge.svg)](https://colab.research.google.com/drive/1fcO8QmGLq0t_mMVtIMgfBmRd_E3TETEU?usp=sharing)
 - *Audio_denoising.py* : Denoises the audio
 - *Speech_to_Text.py*: Converts speech to text  
 - *BriefKing.jpeg* : Logo of BriefKing  
   
 **Extra Files on Google Drive**
 - Pre trained Models  
    - *pytorch_model.bin*  
    - *config.json*  
    - *special_tokens_map.json*  
    - *tokenizer_config.json*  
    - *vocab.json*  
    - *summarize.pickle*
 - *download.py* : Running this file downloads the above models
 - *input_file.wav* : A sample audio for testing
 
 ***How to run the app locally***  
 
 - Download the drive folder on you computer  
 - Open the command terminal
 - Navigate to the folder
 - `pip install -r requirements.txt` 
 - `streamlit run BriefKing_FinalApp.py`   
  
***How to run the app on colab***  

 [![Open In Colab](https://colab.research.google.com/assets/colab-badge.svg)](https://colab.research.google.com/drive/1fcO8QmGLq0t_mMVtIMgfBmRd_E3TETEU?usp=sharing)
  
***How to use the app***  

(1) Upload the audio file which you want to summarize  
(2) Press "Brief It!" and wait for a few seconds  
(3) Download the summarized text file"
 
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
> Used [facebook-denoiser](https://github.com/facebookresearch/denoiser) model for denoising  

All the assets/resources/libraries used in BriefKing were, to the best of our knowledge, taken from copyleft material. Incase of any inadvertent copyright infringement by us, please contact the team.

 *License of the models used*  
  https://github.com/huggingface/transformers/blob/master/LICENSE  
  https://github.com/facebookresearch/denoiser/blob/master/LICENSE

