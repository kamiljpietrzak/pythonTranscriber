import os
import csv
from pydub.utils import mediainfo

class FileManager:
    def __init__(self):
        pass

    def get_audio_files(self, folder_path):
        return [os.path.join(folder_path, f) for f in os.listdir(folder_path) if f.endswith('.wav')]

    def save_to_csv(self, data, output_path="output.csv"):
        with open(output_path, 'w', newline='') as csvfile:
            writer = csv.writer(csvfile)
            writer.writerow(['File Path', 'Transcription'])
            for row in data:
                writer.writerow(row)

    def get_file_duration(self, file_path):
        audio_info = mediainfo(file_path)
        return float(audio_info['duration'])
