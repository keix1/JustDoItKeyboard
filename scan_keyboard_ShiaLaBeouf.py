# coding: utf-8

from audio_player import AudioPlayer
from screen_sticker import ScreenSticker
import keyboard
import threading
import subprocess
import random


class KeyScanner:

    def __init__(self, mute_flag=False):
        self.category = "ShiaLaBeouf"
        self.sticker = "DoIt"
        self.mute_flag = mute_flag 

    def key_press(self, key):

        print(key.name)

        if key.name == "enter":
            self.sticker = "JustDoIt"
            if not self.mute_flag:
                thread_sound = threading.Thread(target=AudioPlayer(self.category, self.sticker).play)
                thread_sound.start()
        elif key.name == "¥n¥r":
            pass
        elif key.name == "esc":
            r = random.randint(0,2)
            stickers = ["NoWhatAreYouWatingFor", "NothingIsImpossible", "StopGivingUp", "YesterdayYouSaidTommorow"]
            self.sticker = stickers[r]
            if not self.mute_flag:
                thread_sound = threading.Thread(target=AudioPlayer(self.category, self.sticker).play)
                thread_sound.start()
        elif key.name == "space":
            self.sticker = "YesYouCan"
            if not self.mute_flag:
                thread_sound = threading.Thread(target=AudioPlayer(self.category, self.sticker).play)
                thread_sound.start()
        elif key.name == "shift":
            self.sticker = "MakeYourDreamsComeTrue"
            if not self.mute_flag:
                thread_sound = threading.Thread(target=AudioPlayer(self.category, self.sticker).play)            
                thread_sound.start()
        else:
            self.sticker = "DoIt"
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

def justdoit():
    key_scanner = KeyScanner(mute_flag=False)
    key_scanner.start_scan()
    _loop()
        
def justdoit_mute():
    key_scanner = KeyScanner(mute_flag=True)
    key_scanner.start_scan()
    _loop()


if __name__ == "__main__":
    justdoit()
