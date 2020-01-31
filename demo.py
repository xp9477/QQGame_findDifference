import cv2
import tkinter as tk
import numpy as np
import os
from PIL import ImageGrab


class Diff():

    def adjust(self, img, c, b):
        h, w, r = img.shape
        blank = np.zeros([h, w, r], img.dtype)
        dst = cv2.addWeighted(img, c, blank, 1 - c, b)
        return dst

    def closing(self, frame, n):
        kernel = cv2.getStructuringElement(cv2.MORPH_ELLIPSE, (n, n))
        closing = cv2.morphologyEx(frame, cv2.MORPH_CLOSE, kernel)
        kernel = cv2.getStructuringElement(cv2.MORPH_RECT,(n, n))
        closing = cv2.morphologyEx(frame, cv2.MORPH_CLOSE, kernel)
        return closing

    def get_result(self):
        img = cv2.imread("input.png")
        imgray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
        ret, dst = cv2.threshold(imgray, 127, 255, 0)
        contours, hierarchy = cv2.findContours(dst, cv2.RETR_TREE, cv2.CHAIN_APPROX_SIMPLE)

        cv2.waitKey(0)
        
        picture = []
        for cnt in contours:
            x, y, w, h = cv2.boundingRect(cnt)
            if 90000 < w*h < 130000:
                picture.append([x+10,y+10,w-20,h-20])
        try:
            for i in range(len(picture)):
                for j in range(i+1, len(picture)):
                    if picture[i][2]*picture[i][3] == picture[j][2]*picture[j][3]:
                        pic1 = img[picture[i][1]:picture[i][1]+picture[i][3], picture[i][0]:picture[i][0]+picture[i][2]]
                        pic2 = img[picture[j][1]:picture[j][1]+picture[j][3], picture[j][0]:picture[j][0]+picture[j][2]]
            pic1 = self.adjust(pic1, 1.1, 0)
            pic = cv2.absdiff(pic1, pic2)
        except Exception:
            print("请按要求截图")
            return

        frame = self.adjust(pic, 1.3, 0)
        cls = self.closing(frame, 5)
        picgray = cv2.cvtColor(cls, cv2.COLOR_BGR2GRAY)
        ret, dst = cv2.threshold(picgray, 30, 255, 0)
        dst = self.closing(dst, 8)

        b, g, r = cv2.split(pic1)
        b, g, r = cv2.add(b, dst), cv2.add(g, dst), cv2.add(r, dst)
        res = cv2.merge([b, g, r])

        contours, hierarchy = cv2.findContours(dst, cv2.RETR_TREE, cv2.CHAIN_APPROX_SIMPLE)
        for cnt in contours:
            x, y, w, h = cv2.boundingRect(cnt)
            if w*h < 80000:
                cv2.rectangle(res, (x, y), (x+w, y+h), (0,255,0), 3)
        cv2.imwrite('result.png', res)


class GUI():
    def __init__(self):
        self.root = tk.Tk()
        self.root.title("xp's finder")
        self.root.geometry("450x350")
        button = tk.Button(self.root, text='hit me', font=('Arial', 12), width=10, height=1, command=self.hit_me)
        self.imglabel = tk.Label(self.root)
        button.pack()
        self.root.mainloop()

    def hit_me(self):
        try:
            im = ImageGrab.grab()
            im.save('input.png')
        except Exception:
            print('请保持窗口在最上方')
            return

        diff = Diff()
        diff.get_result()
        img = tk.PhotoImage(file = 'result.png')
        self.imglabel.destroy()
        self.imglabel = tk.Label(self.root, image = img)
        self.imglabel.pack()
        self.root.mainloop()


def main():
    gio = GUI()

if __name__ == '__main__':
    main()