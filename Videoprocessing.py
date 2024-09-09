import cv2
import librosa
from moviepy.editor import VideoFileClip
import numpy as np

def extract_video_data(video_path):
    # Load the video
    video = VideoFileClip(video_path)
    
    # Extract video frames for visual analysis
    frames = []
    for frame in video.iter_frames(fps=1):
        frames.append(frame)

    # Extract audio for audio analysis
    audio_path = video_path.replace(".mp4", ".wav")
    video.audio.write_audiofile(audio_path)
    audio, sr = librosa.load(audio_path, sr=None)

    return frames, audio, sr


