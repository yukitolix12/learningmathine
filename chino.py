import tkinter as tk
import tkinter.filedialog as fd
import PIL.Image
import PIL.ImageTk

#画像ファイルを数値リストに変換する
def imageToData(filename):
    #画像を8*8のグレースケールに変換
    grayImage = PIL.Image.open(filename).convert("L")
    grayImage = grayImage.resize((8,8),PIL.Image.ANTIALIAS)
    #その画像を表示する
    dispImage = PIL.ImageTk.PhotoImage(grayImage.resize((300,300)))
    imageLabel.configure(image = dispImage)
    imageLabel.image = dispImage