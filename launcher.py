import os
import streamlit as st
# import pandas as pd
from datetime import date
from video_editor import VideoEditor
from moviepy.editor import *
import uuid

st.title("Personal video editor")
st.write("Author: Hemant Kshirsagar")

st.set_option('deprecation.showPyplotGlobalUse', False)


def video_join(videos, unique_id, base_path):
    video_editor = VideoEditor()
    video_editor.video = videos
    video_editor.unique_id = unique_id
    video_editor.base_path = base_path
    video_editor.video_cutter()


def video_parts(video, parts, unique_id, base_path):
    video_editor = VideoEditor()
    video_editor.video = video
    video_editor.divide_into_part = parts
    video_editor.unique_id = unique_id
    video_editor.base_path = base_path
    video_editor.video_cutter()


def add_audio_in_video(video, audio, unique_id, base_path):
    video_editor = VideoEditor()
    video_editor.video = video
    video_editor.audio = audio
    video_editor.unique_id = unique_id
    video_editor.base_path = base_path
    video_editor.add_audio_to_video()


# with st.expander("Join Videos"):
#     with st.form('Join Videos'):
#         st.markdown('### Join Videos')
#         st.write("Here, you can join the multiple videos into single video in sequence.")
#         uploaded_file = st.file_uploader("Upload video a files.", type="mp4")
#         cutter_btn = st.form_submit_button('Join')
#
#         if cutter_btn and uploaded_file is not None:
#             bytes_data = uploaded_file.getvalue()
#             unique_id = uuid.uuid4().hex
#             if not os.path.isdir(os.path.join(os.getcwd(), "temp")):
#                 os.mkdir(os.path.join(os.getcwd(), "temp"))
#             os.mkdir(os.path.join(os.getcwd(), "temp", unique_id))
#             os.mkdir(os.path.join(os.getcwd(), "temp", unique_id, "upload"))
#             os.mkdir(os.path.join(os.getcwd(), "temp", unique_id, "download"))
#             base_path = os.path.join(os.getcwd(), "temp")
#             with open(os.path.join(os.getcwd(), "temp", unique_id, "upload") + "/input_video.mp4", "wb") as video_file:
#                 video_file.write(bytes_data)
#             input_video_files_path = os.path.join(os.getcwd(), "temp", unique_id, "upload") + "/input_video.mp4"
#             video_join(input_video_files_path, unique_id, base_path)

with st.expander("Audio in Video"):
    with st.form('Audio in Video'):
        st.markdown('### Audio in Video')
        st.write("Here, you can add any mp3 audio into video file.")
        uploaded_video_file = st.file_uploader("Upload video a file.", type="mp4")
        uploaded_audio_file = st.file_uploader("Upload audio a file.", type="mp3")

        start_btn = st.form_submit_button('Start process')
        if start_btn:
            if uploaded_video_file is not None and uploaded_audio_file is not None:
                video_bytes_data = uploaded_video_file.getvalue()
                audio_bytes_data = uploaded_audio_file.getvalue()
                unique_id = uuid.uuid4().hex
                if not os.path.isdir(os.path.join(os.getcwd(), "temp")):
                    os.mkdir(os.path.join(os.getcwd(), "temp"))
                os.mkdir(os.path.join(os.getcwd(), "temp", unique_id))
                os.mkdir(os.path.join(os.getcwd(), "temp", unique_id, "upload"))
                os.mkdir(os.path.join(os.getcwd(), "temp", unique_id, "download"))
                base_path = os.path.join(os.getcwd(), "temp")
                with open(os.path.join(os.getcwd(), "temp", unique_id, "upload") + "/input_video.mp4", "wb") as video_file:
                    video_file.write(video_bytes_data)
                with open(os.path.join(os.getcwd(), "temp", unique_id, "upload") + "/input_audio.mp3", "wb") as audio_file:
                    audio_file.write(audio_bytes_data)
                video_file_path = os.path.join(os.getcwd(), "temp", unique_id, "upload") + "/input_video.mp4"
                audio_file_path = os.path.join(os.getcwd(), "temp", unique_id, "upload") + "/input_audio.mp3"
                add_audio_in_video(video_file_path, audio_file_path, unique_id, base_path)


with st.expander("Make Video Parts"):
    with st.form('Video Parts'):
        st.markdown('### Video Parts')
        st.write("Here, you can cut the video into multiple parts in sequence.")
        uploaded_file = st.file_uploader("Upload video a file.", type="mp4")
        parts = st.number_input('Number of parts.', min_value=1, max_value=10, step=1)
        parts = parts + 1
        cutter_btn = st.form_submit_button('Start making parts')
        if cutter_btn and parts is not None:
            if uploaded_file is not None:
                bytes_data = uploaded_file.getvalue()
                unique_id = uuid.uuid4().hex
                if not os.path.isdir(os.path.join(os.getcwd(), "temp")):
                    os.mkdir(os.path.join(os.getcwd(), "temp"))
                os.mkdir(os.path.join(os.getcwd(), "temp", unique_id))
                os.mkdir(os.path.join(os.getcwd(), "temp", unique_id, "upload"))
                os.mkdir(os.path.join(os.getcwd(), "temp", unique_id, "download"))
                base_path = os.path.join(os.getcwd(), "temp")
                with open(os.path.join(os.getcwd(), "temp", unique_id, "upload") + "/input_video.mp4", "wb") as video_file:
                    video_file.write(bytes_data)
                input_video_file_path = os.path.join(os.getcwd(), "temp", unique_id, "upload") + "/input_video.mp4"
                video_parts(input_video_file_path, parts, unique_id, base_path)

