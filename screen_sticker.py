# coding: utf-8

import tkinter
from PIL import Image, ImageTk
import random
import argparse

class ScreenSticker:

    def __init__(self):
        self.window = tkinter.Tk()
        self.window.geometry(f"0x0")

    def stick(self, category, sticker):
        
        # タイトルバー削除
        self.window.overrideredirect(True)

        # 画像を表示するための準備
        self.img_raw = Image.open(f'data/{category}/{sticker}.png')
        w, h = self.img_raw.size
        img = ImageTk.PhotoImage(self.img_raw)

        # 画面サイズから位置を出す
        screenwidth = self.window.winfo_screenwidth()
        screenheight = self.window.winfo_screenheight()
        x = random.randint(0, screenwidth)
        y = random.randint(0, screenheight)

        # windowサイズと位置を変更
        self.window.geometry(f"{w}x{h}+{x}+{y}")

        # 画像を表示するためのキャンバスの作成（黒で表示）
        canvas = tkinter.Canvas(self.window, bg = "black", width=w, height=h)
        canvas.place(x=0, y=0) # 左上の座標を指定

        # キャンバスに画像を表示する。第一引数と第二引数は、x, yの座標
        canvas.create_image(0, 0, image=img, anchor=tkinter.NW)

        def destroy_window():
            self.window.quit()
            self.window.destroy()
            exit()
        self.window.after(1500, destroy_window)

        # 最前面に表示
        self.window.lift()
        self.window.attributes('-topmost',True)
        self.window.after_idle(self.window.attributes,'-topmost',False)

        self.window.mainloop()

    def mainloop(self):
        self.window.mainloop()


if __name__ == "__main__":

    parser = argparse.ArgumentParser(description='Just Do It!')
    parser.add_argument('category', help='Just Do It!')
    parser.add_argument('sticker', help='Just Do It!')

    args = parser.parse_args()
    screen_sticker = ScreenSticker()
    screen_sticker.stick(args.category, args.sticker)
