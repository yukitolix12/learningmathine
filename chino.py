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

#ファイルダイアログを開く
def openfile():
    fpath = fd.askopenfilename()
    if fpath:
        #画像ファイルを数値リストに変換する
        data = imageToData(fpath)

#アプリのウィンドウを作る
root = tk.Tk()
root.geometry("400x400")

btn = tk.Button(root, text="ファイルを開く", command = openFile)
imageLabel = tk.Label()
