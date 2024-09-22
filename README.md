
# Youtube Transcript Summarizer  

**Youtube Transcript Summarizer** is a Streamlit application that extracts and summarizes transcripts from YouTube videos using AI. Users can input video URLs or upload transcript files, generating detailed summaries that capture key points and themes discussed in the content.

## Features

- Extracts transcripts from YouTube videos using the YouTube Transcript API.
- Allows users to upload their own transcript files in TXT format.
- Generates detailed summaries using Google’s Gemini AI model.
- User-friendly interface built with Streamlit.

## File Structure

```
SummarizeTube/
├── main.py                # Main application file
├── requirements.txt       # Dependencies for the project
└── README.md              # Project documentation
```

## Code Explanation

### main.py

This file contains the core logic of the application:

1. **Importing Libraries**:
   - Imports necessary libraries such as `streamlit`, `google.generativeai`, and `youtube_transcript_api`.

2. **API Configuration**:
   - Configures the Google API key to access the Gemini model.

3. **Functions**:
   - `extract_transcript_details(youtube_video_url)`: Extracts the transcript from a provided YouTube video URL.
   - `generate_gemini_content(transcript_text, prompt)`: Sends the transcript to the Gemini model for summarization.
   - `extract_video_id(url)`: Extracts the video ID from a given YouTube URL.

4. **Streamlit UI**:
   - Provides options for users to either enter a YouTube video URL or upload a transcript file.
   - Displays the generated summary after processing the input.

## Installation

To run the SummarizeTube application, follow these steps:

1. Clone the repository:

   ```bash
   git clone <repository-url>
   cd SummarizeTube
   ```

2. Install the required dependencies:

   ```bash
   pip install -r requirements.txt
   ```

3. Run the application:

   ```bash
   streamlit run main.py
   ```

4. Open your browser and go to `http://localhost:8501` to use the application.

## Requirements

Create a `requirements.txt` file with the following content:

```
streamlit
google-generativeai
youtube-transcript-api
```

## Disclaimer

This project is built for learning purposes and is not designed from a user perspective. It serves as a demonstration of how to integrate AI with user input for summarizing video content.

