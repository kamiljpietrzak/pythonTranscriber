import tkinter as tk
from tkinter import filedialog, Label, Button
from PIL import Image, ImageTk
class GUI:
    def __init__(self, transcription, file_manager):
        self.transcription = transcription
        self.file_manager = file_manager
        self.window = tk.Tk()
        #LOGO
        image = Image.open("images/DataLabLogo.png")
        image = image.resize((100, 100))
        self.logo = ImageTk.PhotoImage(image)
        logo_label = tk.Label(self.window, image=self.logo)
        logo_label.pack(pady=20, side=tk.LEFT)
        self.window.title("Speech to Text")

    def choose_directory(self):
        return filedialog.askdirectory()

    def show_summary(self, total_files, total_duration):
        summary_window = tk.Tk()
        summary_window.title("Podsumowanie")

        tk.Label(summary_window, text=f"Przetworzono {total_files} plików.").pack(pady=10)
        tk.Label(summary_window, text=f"Łączny czas trwania plików: {total_duration} sekund.").pack(pady=20)


        def close_program():
            summary_window.destroy()
            self.window.quit()

        tk.Button(summary_window, text="Zakończ program", command=close_program).pack(pady=20)
        summary_window.mainloop()

    def start_transcription(self):
        folder_path = self.choose_directory()
        audio_files = self.file_manager.get_audio_files(folder_path)
        total_files = len(audio_files)
        total_duration = sum([self.file_manager.get_file_duration(f) for f in audio_files])

        data = []
        for file_path in audio_files:
            transcription_text = self.transcription.transcribe_audio(file_path)
            data.append((file_path, transcription_text))

        self.file_manager.save_to_csv(data)
        self.show_summary(total_files, total_duration)

    def run(self):
        label = Label(self.window, text="Wybierz katalog w którym\n znajdują się pliki do transkrypcji!")
        label.pack(pady=20, side=tk.RIGHT)

        btn = Button(self.window, text="Zacznij transkrypcję!", command=self.start_transcription)
        btn.pack(pady=20,side=tk.RIGHT)
        self.window.mainloop()
