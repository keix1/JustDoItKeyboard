# coding: utf-8

from audio_player import AudioPlayer
from screen_sticker import ScreenSticker
import keyboard
import threading
import subprocess


class KeyScanner:

    def __init__(self, mute_flag=False):
        self.category = "Jotaro"
        self.sticker = "ora"
        self.mute_flag = mute_flag 

    def key_press(self, key):

        print(key.name)

        if key.name == "enter":
            self.sticker = "ora2"
            if not self.mute_flag:
                thread_sound = threading.Thread(target=AudioPlayer(self.category, self.sticker).play)
                thread_sound.start()
        elif key.name == "¥n¥r":
            pass
        elif key.name == "esc":
            self.sticker = "ToBeContinued"
            if not self.mute_flag:
                thread_sound = threading.Thread(target=AudioPlayer(self.category, self.sticker).play)
                thread_sound.start()
        else:
            self.sticker = "ora"
            if not self.mute_flag:
                thread_sound = threading.Thread(target=AudioPlayer(self.category, self.sticker).play)
                thread_sound.start()

        def stick_process():
            subprocess.call(["python", "screen_sticker.py", f"{self.category}", f"{self.sticker}"])
        stick_thread = threading.Thread(target=stick_process)
        stick_thread.start()

    def start_scan(self):
        keyboard.on_press(self.key_press)

def _loop():
    while True:
        pass

def jojo():
    key_scanner = KeyScanner(mute_flag=False)
    key_scanner.start_scan()
    _loop()
        
def jojo_mute():
    key_scanner = KeyScanner(mute_flag=True)
    key_scanner.start_scan()
    _loop()

if __name__ == "__main__":
    jojo()
