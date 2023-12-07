import cv2
import os
import numpy as np


class ColorBars():

    def __init__(self, blue_level, green_level, red_level):
        self.blue_level = blue_level
        self.green_level = green_level
        self.red_level = red_level
        self.blue_dir  = 1
        self.green_dir = 1
        self.red_dir   = 1
        self.image = None
        self.level = None

    def set_image(self, Image):
        self.image = Image
        self.level = np.zeros_like(Image, dtype = "uint8")

    def blue_modify(self, *args):
        self.blue_level = args[0]
        print(self.blue_level * self.blue_dir)
        self.level[:, :, 0] = np.zeros_like(self.image[:, :, 0], dtype = "uint8") + (self.blue_level * self.blue_dir)
        self.show_changes()

    def green_modify(self, *args):
        self.green_level = args[0]
        self.level[:, :, 1] = np.zeros_like(self.image[:, :, 1], dtype = "uint8") + (self.green_level * self.green_dir)
        self.show_changes()

    def red_modify(self, *args):
        self.red_level = args[0]
        self.level[:, :, 2] = np.zeros_like(self.image[:, :, 2], dtype = "uint8") + (self.red_level * self.red_dir)
        self.show_changes()

    def change_blue_dir(self, *args):
        if self.blue_dir == 1:
            self.blue_dir = -1
        else:
            self.blue_dir = 1

    def change_green_dir(self, *args):
        if self.green_dir == 1:
            self.green_dir = -1
        else:
            self.green_dir = 1

    def change_red_dir(self, *args):
        if self.red_dir == 1:
            self.red_dir = -1
        else:
            self.red_dir = 1

    def show_changes(self):
        if self.blue_dir == 1:
            B = cv2.add(self.image[:, :, 0], self.level[:, :, 0])
        else:
            B = cv2.subtract(self.image[:, :, 0], self.level[:, :, 0])
        if self.green_dir == 1:
            G = cv2.add(self.image[:, :, 1], self.level[:, :, 1])
        else:
            G = cv2.subtract(self.image[:, :, 1], self.level[:, :, 1])
        if self.red_dir == 1:
            R = cv2.add(self.image[:, :, 2], self.level[:, :, 2])
        else:
            R = cv2.subtract(self.image[:, :, 2], self.level[:, :, 2])
        cv2.imshow(window, cv2.merge((B, G, R)))


window = "Flag"
max_bar = 255
blue_bar  = 0
green_bar = 0
red_bar   = 0

bars = ColorBars(blue_level  = 0,
                 green_level = 0,
                 red_level   = 0)

cv2.namedWindow(window, cv2.WINDOW_AUTOSIZE)
cv2.createTrackbar("Blue ", window, blue_bar,  max_bar, bars.blue_modify)
cv2.createTrackbar("Blue dir", window, 0, 1, bars.change_blue_dir)
cv2.createTrackbar("Green", window, green_bar, max_bar, bars.green_modify)
cv2.createTrackbar("Green dir", window, 0, 1, bars.change_green_dir)
cv2.createTrackbar("Red  ", window, red_bar,   max_bar, bars.red_modify)
cv2.createTrackbar("Red dir", window, 0, 1, bars.change_red_dir)

file_path = "./images"
file_name = "ukraine_flag.jpg"
I = cv2.imread(os.path.join(file_path, file_name), cv2.IMREAD_UNCHANGED)

bars.set_image(I)

cv2.imshow(window, I)
c = cv2.waitKey(0)
cv2.destroyAllWindows()
