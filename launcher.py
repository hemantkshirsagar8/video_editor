import os
import streamlit as st
# import pandas as pd
from datetime import date
from video_editor import VideoEditor

st.title("Personal video editor")
st.write("Author: Hemant Kshirsagar")

st.set_option('deprecation.showPyplotGlobalUse', False)


def video_parts(video, parts):
    video_editor = VideoEditor()
    video_editor.video = video
    video_editor.divide_into_part = parts
    video_editor.video_cutter()


if st.sidebar.button("Video parts."):
    st.write("Here, you can cut the video into multiple parts in sequence.")

    with st.form('Video Parts'):
        st.markdown('### Video Parts')
        uploaded_file = st.file_uploader("Upload video a file.")
        parts = st.number_input('Number of parts.', min_value=1, max_value=10, step=1)
        if uploaded_file is not None:
            bytes_data = uploaded_file.getvalue()
            st.write(bytes_data)
            filename = uploaded_file.name
            st.write(filename)

        cutter_btn = st.form_submit_button('Start making parts')
        if cutter_btn:
            if parts is not None:
                video_parts(uploaded_file, parts)
            else:
                st.warning("Please enter the number of parts.")
        else:
            st.warning("File not uploaded.")

