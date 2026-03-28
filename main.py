import os, requests
from gtts import gTTS
from moviepy.editor import ImageClip, AudioFileClip

def make_video():
    img_url = os.getenv("IMAGE_URL")
    v_text = os.getenv("VOICE_TEXT")
    v_name = os.getenv("VIDEO_NAME", "output.mp4")

    # ইমেজ ডাউনলোড
    img_data = requests.get(img_url).content
    with open("images/temp_img.jpg", 'wb') as f: f.write(img_data)

    # ভয়েস তৈরি
    tts = gTTS(text=v_text, lang='en')
    tts.save("audio/temp_audio.mp3")

    # ভিডিও এডিটিং
    audio = AudioFileClip("audio/temp_audio.mp3")
    clip = ImageClip("images/temp_img.jpg").set_duration(audio.duration)
    clip = clip.set_audio(audio)
    clip.write_videofile(f"videos/{v_name}", fps=24, codec="libx264")

if __name__ == "__main__":
    make_video()
