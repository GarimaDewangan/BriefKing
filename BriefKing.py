import streamlit as st
import pickle
import base64

#model = pickle.load(open('_____.pkl','rb'))
#def brief(data):
#	pred = model.predict(data)
#	return(pred)

def create_download(object_to_download):
	b64 = base64.b64encode(object_to_download.encode()).decode()
	return f'<a href="data:file/txt;base64,{b64}" download="result.txt"> Download the summary </a>'


st.title('BriefKing')

st.sidebar.image("https://static.streamlit.io/examples/dog.jpg")#will put BriefKing logo instead

expander = st.sidebar.beta_expander("About BriefKing")
expander.write("BriefKing is a web app that can be used to......" )

expander = st.sidebar.beta_expander("How to use BriefKing")
expander.markdown(" (1) Upload the audio/video file which you want to summarize ") 
expander.markdown(" (2) Wait for a few seconds") 
expander.markdown("(3) Download the summarized text file")

st.write('Upload the audio/video')
data = st.file_uploader("Select an audio or video file", type=["mp3","wav", "webm", "mp4"])

import time;

if st.button("Brief It!"):
	with st.spinner("Please wait...summarizing..."):
        #output = brief(data)
		output = 'Lorem ipsum dolor sit amet, consectetur adipiscing elit. Suspendisse dignissim volutpat leo quis porta. Praesent pretium condimentum risus, commodo tempor erat pellentesque ut. Maecenas nec dui ut odio convallis vestibulum. Ut sit amet pellentesque lectus. Pellentesque porttitor maximus tortor, eu aliquam nulla porta ac. Aliquam interdum dapibus turpis nec pharetra. Nullam suscipit vitae mi at porttitor. Sed sit amet libero a ligula tincidunt tempus. Cras porta aliquet quam. Nulla eu malesuada purus.' #temperory till we dont have the model which gives this output
		time.sleep(5)
		st.success('Done')
	#if(len(output)>0):
		st.write(output)
		link = create_download(output)
		st.markdown(link, unsafe_allow_html=True)

#Need to add in the python file
#import pickle
#pickle.dump(____the funcn_____,open('model.pkl','wb'))