import google.generativeai as genai
from youtube_transcript_api import YouTubeTranscriptApi, TranscriptsDisabled
import streamlit as st

# Set your API key here (hidden for GitHub)
GOOGLE_API_KEY = st.secrets["GOOGLE_API_KEY"]

# Configure Google API key for Gemini
genai.configure(api_key=GOOGLE_API_KEY)

# Prompt for summarization
prompt = """Summarize the following transcript in detail, capturing the key points and main ideas discussed.
If it's a podcast, provide an overview of the topics covered, key arguments, and any conclusions made by the speakers.
If it's a lecture, include a structured breakdown of the subject matter, highlighting essential concepts, theories, or lessons taught.
Ensure that all major themes and examples are well explained in an organized manner."""

# Function to extract transcript details from YouTube
def extract_transcript_details(youtube_video_url):
    try:
        video_id = extract_video_id(youtube_video_url)
        transcript_list = YouTubeTranscriptApi.get_transcript(video_id)

        transcript = ""
        for item in transcript_list:
            transcript += " " + item["text"]
        return transcript
    except TranscriptsDisabled:
        st.warning("Subtitles are disabled for this video. You may upload a transcript file instead.")
        return None
    except Exception as e:
        st.error(f"An error occurred while fetching the transcript: {str(e)}")
        return None

# Function to generate summarization using Gemini model
def generate_gemini_content(transcript_text, prompt):
    try:
        model = genai.GenerativeModel("gemini-pro")
        response = model.generate_content(prompt + transcript_text)
        return response.text
    except Exception as e:
        st.error(f"An error occurred while generating the summary: {str(e)}")
        return None

# Function to extract video ID from URL
def extract_video_id(url):
    if "watch?v=" in url:
        return url.split("watch?v=")[1].split("&")[0]
    elif "youtu.be/" in url:
        return url.split("youtu.be/")[1].split("?")[0]
    else:
        st.error("Invalid YouTube URL format.")
        return None

# Streamlit UI
st.title("YouTube Transcript Summarizer")

option = st.selectbox("Choose an option", ["Enter YouTube Video URL", "Upload Transcript File"])

if option == "Enter YouTube Video URL":
    youtube_url = st.text_input("Enter YouTube Video URL", placeholder="https://www.youtube.com/watch?v=example")

    if youtube_url:
        st.write("Fetching transcript...")

        transcript = extract_transcript_details(youtube_url)

        if transcript:
            st.write("Transcript fetched successfully!")

            if st.button("Generate Summary"):
                st.write("Generating summarization using Gemini...")
                summary = generate_gemini_content(transcript, prompt)

                if summary:
                    st.subheader("Summary")
                    st.write(summary)

elif option == "Upload Transcript File":
    uploaded_file = st.file_uploader("Upload a transcript file (TXT format)", type="txt")

    if uploaded_file is not None:
        transcript = uploaded_file.getvalue().decode("utf-8")

        st.write("Transcript uploaded successfully!")

        if st.button("Generate Summary"):
            st.write("Generating summarization using Gemini...")
            summary = generate_gemini_content(transcript, prompt)

            if summary:
                st.subheader("Summary")
                st.write(summary)
