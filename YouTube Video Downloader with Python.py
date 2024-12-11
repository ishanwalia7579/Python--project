from pytube import YouTube

# Specify the video URL
video_url = 'your_video_url'

# Create a YouTube object
yt = YouTube(video_url)

# Get the video title
video_title = yt.title

print(f"Video Title: {video_title}")
