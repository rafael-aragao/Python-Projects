from kivy.config import Config
Config.set('graphics', 'width', '414')
Config.set('graphics', 'height', '736')

from kivy.core.audio import SoundLoader
from kivy.uix.boxlayout import BoxLayout
from kivy.lang import Builder
from kivymd.app import MDApp
from kivymd.uix.dialog import MDDialog, MDDialogHeadlineText

AUDIO_FILES = [
    "audios/Rain1.mp3",
    "audios/Forest1.mp3",
    "audios/Campfire1.mp3",
]

class PlayerContent(BoxLayout):
    pass

class ODSConection(MDApp):
    current_index = 0
    sound = None
    dialog = None
    dialog_headline = None

    def build(self):
        self.title = "Conexão ODS"
        return Builder.load_file("main.kv")
    
    def open_player(self, index):
        self.current_index = index
        self.play_sound()

        if self.dialog:
            self.dialog.dismiss()

        self.dialog_headline = MDDialogHeadlineText(
            text = "Playing" + self.get_sound_name(self.current_index),
            theme_font_name = "Custom",
            font_name= "Anton-Regular.ttf",
        )

        self.dialog = MDDialog(
            self.dialog_headline,
            PlayerContent(),
            size_hint=(0.8, 0.4),
            orientation = "vertical", 
        )
        self.dialog.open()

    def get_sound_name(self, index):
        nomes = ["Rain", "Forest", "Camp Fire"]
        return nomes[index]

    def play_sound(self):
        self.stop_sound()
        sound_path = AUDIO_FILES[self.current_index]
        self.sound = SoundLoader.load(sound_path)

        if self.sound:
            self.sound.volume = 0.5
            self.sound.loop = True
            self.sound.play()

    def pause_sound(self):
        if self.sound and self.sound.state == 'play':
            self.sound.stop()

    def stop_sound(self):
        if self.sound:
            self.sound.stop()
            self.sound.unload()
            self.sound = None

    def next_sound(self):
        self.current_index =  (self.current_index + 1) % len(AUDIO_FILES)
        self.play_sound()

        if self.dialog_headline:
            self.dialog_headline.text = "Playing: " + self.get_sound_name(self.current_index)
    
    def previous_sound(self):
        self.current_index =  (self.current_index - 1) % len(AUDIO_FILES)
        self.play_sound()

        if self.dialog_headline:
            self.dialog_headline.text = "Playing: " + self.get_sound_name(self.current_index)

    def set_volume(self, value):
        if self.sound:
            self.sound.volume =  value

    def on_stop(self):
        self.stop_sound()

if __name__ == "__main__":
    ODSConection().run()