import streamlit as st
from Youtube_Video_Summarizer import yt_analyzer

st.set_page_config(
    page_title="YouTube Video Summarizer",
    layout="centered",

)
st.title("🎥AI youtube Video Summaizer")

@st.cache_resource
def get_agent():
    return yt_analyzer()

agent = get_agent()

video_url= st.text_input("Enter YouTube Video URL:")
button = st.button("Analyze Video")

if video_url and button:
    with st.spinner("Analyzing the video..."):

        try:
            response = agent.run(
            f"""
            Use the YouTube tool to analyze this YouTube video.

            Video URL:
            {video_url}

            Always call the tool before answering.
            """
            ) 

            st.markdown("Analysis Report:")
            st.markdown(response.content)
        except Exception as e:
            st.error(f"An error occurred: {str(e)}")