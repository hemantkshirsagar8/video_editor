import os
from os.path import basename
import streamlit as st
from moviepy.editor import *
from time import sleep
from zipfile import ZipFile
from io import BytesIO
import base64
import shutil


class VideoEditor:
    def __init__(self):
        self.video = None
        self.audio = None
        self.divide_into_part = None
        self.unique_id = None
        self.base_path = None

    def del_unwwanted_files(self, f_type):
        files_in_dir = os.listdir("./")
        filtered_files = [file for file in files_in_dir if file.endswith(f_type)]
        for file in filtered_files:
            os.remove("./" + file)

    # Zip the files from given directory that matches the filter
    def zipFilesInDir(self, dirName, zipFileName, filter):
        # create a ZipFile object
        with ZipFile(zipFileName, 'w') as zipObj:
            # Iterate over all the files in directory
            for folderName, subfolders, filenames in os.walk(dirName):
                for filename in filenames:
                    if filter(filename):
                        # create complete filepath of file in directory
                        filePath = os.path.join(folderName, filename)
                        # Add file to zip
                        zipObj.write(filePath, basename(filePath))

    def zip_and_download(self):
        filenames = [entry.name for entry in
                     sorted(os.scandir(os.path.join(self.base_path, self.unique_id, "download")),
                            key=lambda x: x.stat().st_mtime, reverse=True)]
        self.zipFilesInDir(
            "temp/" + self.unique_id + "/download/", "temp/" + self.unique_id + ".zip", lambda name: ".mp4" in name)

        ZipfileDotZip = self.unique_id + ".zip"

        with open(self.base_path + "/" + ZipfileDotZip, "rb") as f:
            bytes = f.read()
            b64 = base64.b64encode(bytes).decode()
            href = f"<a href=\"data:file/zip;base64,{b64}\" download='{ZipfileDotZip}.zip'>\
                        Download all parts\
                    </a>"
        shutil.rmtree(os.path.join(self.base_path, self.unique_id))
        self.del_unwwanted_files(".mp4")
        st.markdown(href, unsafe_allow_html=True)

    def video_cutter(self):
        try:
            st.info("Initiated...")
            current_duration = VideoFileClip(self.video).duration
            single_duration = current_duration/self.divide_into_part
            # current_video = f"{current_duration}.mp4"

            while current_duration > single_duration:
                clip = VideoFileClip(self.video).subclip(current_duration-single_duration, current_duration)
                current_duration -= single_duration
                current_video = f"{self.divide_into_part - 1}.mp4"
        #         clip = clip.resize( (600,750) ) # instagram 4:5 aspect ratio
                clip.to_videofile(os.path.join(self.base_path, self.unique_id, "download") + "/part_" + current_video,
                                  codec="libx264", temp_audiofile='upload-audio.m4a',
                                  remove_temp=True, audio_codec='aac')
                self.divide_into_part = self.divide_into_part - 1
            st.success("Video parts made successfully.")

            self.zip_and_download()
        except Exception as e:
            shutil.rmtree(os.path.join(self.base_path, self.unique_id))
            print(str(e))
            st.error("Something went wrong.")

    def add_audio_to_video(self):
        try:
            st.info("Initiated...")
            video_clip = VideoFileClip(self.video)
            video_duration = video_clip.duration
            background_audio_clip = AudioFileClip(self.audio)
            audio_duration = background_audio_clip.duration
            if audio_duration > video_duration:
                bg_music = background_audio_clip.subclip(0, video_duration)
            else:
                bg_music = background_audio_clip.subclip(0, audio_duration)
            final_clip = video_clip.set_audio(bg_music)
            # final_clip = final_clip.resize( (600,750) ) # instagram 4:5 aspect ratio
            final_clip.write_videofile(os.path.join(self.base_path, self.unique_id, "download") + "/New_Audio_video.mp4",
                                       codec='libx264', audio_codec="aac")
            self.zip_and_download()
        except Exception as e:
            shutil.rmtree(os.path.join(self.base_path, self.unique_id))
            print(str(e))
            st.error("Something went wrong.")

