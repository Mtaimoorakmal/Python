import yt_dlp

def download_youtube_video(url, save_path="."):
    try:
        ydl_opts = {
            'outtmpl': f"{save_path}/%(title)s.%(ext)s",
            'format': '18',  # MP4 with both audio & video
            'socket_timeout': 60,  # Increase timeout to 60 seconds
            'retries': 10,  # Retry up to 10 times if it fails
        }
        with yt_dlp.YoutubeDL(ydl_opts) as ydl:
            ydl.download([url])
        print("Download complete!")
    except Exception as e:
        print(f"Error: {e}")

if __name__ == "__main__":
    video_url = input("Enter the YouTube video URL: ")
    download_youtube_video(video_url)