# coding: utf-8

import tkinter
from PIL import Image, ImageTk
import random
import argparse

class ScreenSticker:

    def __init__(self):
        pass

    def stick(self, category, sticker):
        
        # 新しいウィンドウ作成
        window = tkinter.Tk()

        # タイトルバー削除
        window.overrideredirect(True)

        # 画像を表示するための準備
        self.img_raw = Image.open(f'data/{category}/{sticker}.png')
        w, h = self.img_raw.size
        img = ImageTk.PhotoImage(self.img_raw)

        # 画面サイズから位置を出す
        screenwidth = window.winfo_screenwidth()
        screenheight = window.winfo_screenheight()
        x = random.randint(0, screenwidth)
        y = random.randint(0, screenheight)

        # windowサイズと位置を変更
        window.geometry(f"{w}x{h}+{x}+{y}")

        # 画像を表示するためのキャンバスの作成（黒で表示）
        canvas = tkinter.Canvas(window, bg = "black", width=w, height=h)
        canvas.place(x=0, y=0) # 左上の座標を指定

        # キャンバスに画像を表示する。第一引数と第二引数は、x, yの座標
        canvas.create_image(0, 0, image=img, anchor=tkinter.NW)

        def destroy_window():
            window.quit()
            window.destroy()
            exit()

        # 最前面に表示
        window.lift()
        window.attributes('-topmost',True)
        window.after_idle(window.attributes,'-topmost',False)

        window.after(1500, destroy_window)
        window.mainloop()

if __name__ == "__main__":

    parser = argparse.ArgumentParser(description='Just Do It!')
    parser.add_argument('category', help='Just Do It!')
    parser.add_argument('sticker', help='Just Do It!')

    args = parser.parse_args()
    screen_sticker = ScreenSticker()
    screen_sticker.stick(args.category, args.sticker)

