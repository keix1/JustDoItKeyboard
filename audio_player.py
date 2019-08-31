# coding: utf-8

import time
from pydub import AudioSegment
from pydub.playback import play
from pydub.utils import ratio_to_db
import threading
import glob
import os
from playsound import playsound

class AudioPlayer:
    def __init__(self, category, filename):
        self.filename = f'data/{category}/{filename}.mp3'

    def play(self):
        playsound(self.filename)
        return

if __name__ == "__main__":
    audio_player = AudioPlayer("ShiaLaBeouf", "DoIt")
    thread = threading.Thread(target=audio_player.play)
    thread.start()
    