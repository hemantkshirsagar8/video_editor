import streamlit as st
from moviepy.editor import *
from time import sleep


class VideoEditor:
    def __init__(self):
        self.video = None
        self.audio = None
        self.divide_into_part = None

    def video_cutter(self):
        st.info("Video cutter initiated...")
        current_duration = VideoFileClip(self.video).duration
        single_duration = current_duration/self.divide_into_part
        current_video = f"{current_duration}.mp4"

        while current_duration > single_duration:
            clip = VideoFileClip(self.video).subclip(current_duration-single_duration, current_duration)
            current_duration -= single_duration
            current_video = f"{current_duration}.mp4"
    #         clip = clip.resize( (600,750) ) # instagram 4:5 aspect ratio
            clip.to_videofile("new_" + current_video, codec="libx264", temp_audiofile='temp-audio.m4a', remove_temp=True, audio_codec='aac')
        st.success("Video parts made successfully.")

    def add_audio_to_video(self):
        video_clip = VideoFileClip(self.video)
        video_duration = video_clip.duration
        background_audio_clip = AudioFileClip(self.audio)
        audio_duration = background_audio_clip.duration
        if audio_duration > video_duration:
            bg_music = background_audio_clip.subclip(0, video_duration)
        else:
            bg_music = background_audio_clip.subclip(0, audio_duration)
        final_clip = video_clip.set_audio(bg_music)
    #     final_clip = final_clip.resize( (600,750) ) # instagram 4:5 aspect ratio
        final_clip.write_videofile("new_" + self.video, codec='libx264', audio_codec="aac")
    #     final_clip.ipython_display(width=280)

