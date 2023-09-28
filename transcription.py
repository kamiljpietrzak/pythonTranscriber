import urllib.request
import json
from config import API_KEY #Create config.py with your api key inside


class Transcription:
    def __init__(self, api_key, api_url):
        self.api_key = API_KEY
        self.api_url = api_url

    def transcribe_audio(self, file_path):
        data = {
            'audio_file': file_path,
            'api_key': self.api_key
        }
        headers = {'Content-Type': 'application/json'}
        request = urllib.request.Request(self.api_url, data=json.dumps(data).encode(), headers=headers)
        with urllib.request.urlopen(request) as response:
            result = json.loads(response.read().decode())
        return result['text']
