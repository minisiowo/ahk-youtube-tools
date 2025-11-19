from youtube_transcript_api import YouTubeTranscriptApi
from urllib.parse import urlparse, parse_qs
import tkinter as tk
import pyperclip
import re

video_id = "_WjU5d26Cc4"

transcript = YouTubeTranscriptApi().fetch(
    video_id, languages=["pl", "en"]
)

text = re.sub(r'\s+', ' ', " ".join([snippet.text for snippet in transcript.snippets]))

pyperclip.copy(text)

print(text)