# coding: utf-8

import sys
import os
import keyboard
import time
import wave
from audio_player import AudioPlayer
import threading
import random
import json
from screen_sticker import ScreenSticker
import subprocess

class KeyScanner:

    def __init__(self):
        self.category = "ShiaLaBeouf"
        self.sticker = "DoIt"

    def key_press(self, key):

        print(key.name)

        if key.name == "enter":
            self.sticker = "JustDoIt"
            thread_sound = threading.Thread(target=AudioPlayer(self.category, self.sticker).play)
            thread_sound.start()
        elif key.name == "¥n¥r":
            pass
        elif key.name == "esc":
            r = random.randint(0,2)
            stickers = ["NoWhatAreYouWatingFor", "NothingIsImpossible", "StopGivingUp", "YesterdayYouSaidTommorow"]
            self.sticker = stickers[r]
            thread_sound = threading.Thread(target=AudioPlayer(self.category, self.sticker).play)
            thread_sound.start()
        elif key.name == "space":
            self.sticker = "YesYouCan"
            thread_sound = threading.Thread(target=AudioPlayer(self.category, self.sticker).play)
            thread_sound.start()
        elif key.name == "shift":
            self.sticker = "MakeYourDreamsComeTrue"
            thread_sound = threading.Thread(target=AudioPlayer(self.category, self.sticker).play)            
            thread_sound.start()
        else:
            self.sticker = "DoIt"
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
    screen_sticker.mainloop()


