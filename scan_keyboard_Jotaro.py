# coding: utf-8

from audio_player import AudioPlayer
from screen_sticker import ScreenSticker
import keyboard
import threading
import subprocess


class KeyScanner:

    def __init__(self):
        self.category = "Jotaro"
        self.sticker = "ora"

    def key_press(self, key):

        print(key.name)

        if key.name == "enter":
            self.sticker = "ora2"
            thread_sound = threading.Thread(target=AudioPlayer(self.category, self.sticker).play)
            thread_sound.start()
        elif key.name == "¥n¥r":
            pass
        elif key.name == "esc":
            self.sticker = "ToBeContinued"
            thread_sound = threading.Thread(target=AudioPlayer(self.category, self.sticker).play)
            thread_sound.start()
        else:
            self.sticker = "ora"
            thread_sound = threading.Thread(target=AudioPlayer(self.category, self.sticker).play)
            thread_sound.start()

        def stick_process():
            subprocess.call(["python", "screen_sticker.py", f"{self.category}", f"{self.sticker}"])
        stick_thread = threading.Thread(target=stick_process)
        stick_thread.start()

    def start_scan(self):
        keyboard.on_press(self.key_press)

if __name__ == "__main__":
    screen_sticker = ScreenSticker()
    key_scanner = KeyScanner()
    key_scanner.start_scan()
    
    while True:
        pass
