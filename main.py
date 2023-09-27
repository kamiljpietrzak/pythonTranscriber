from gui import GUI
from transcription import Transcription
from file_manager import FileManager

if __name__ == "__main__":
    transcription = Transcription(api_key="TWÓJ_KLUCZ_API", api_url="URL_API_WHISPER")
    file_manager = FileManager()
    gui = GUI(transcription, file_manager)
    gui.run()
