import pytesseract as T
# import speech_recognition as sr
import cv2 as c,os,gtts
import threading
import tkinter
from tkinter import filedialog

def getAudio(file_path):
    # initialize tesseract software installed separately from pytesseract
    T.pytesseract.tesseract_cmd = r'C:\Program Files\Tesseract-OCR\tesseract.exe'
    # read image with openCv
    img = c.imread(f'{file_path}')
    img = c.resize(img, (720, 480))
    xy = T.image_to_string(img)
    # audio from image text
    audio = gtts.gTTS(text = xy, lang = 'en', slow = False)
    audio.save("saved_audio.wav")
    os.system("saved_audio.wav")

def showText(file_path):
    # initialize tesseract software installed separately from pytesseract
    T.pytesseract.tesseract_cmd = r'C:\Program Files\Tesseract-OCR\tesseract.exe'
    img = c.imread(f'{file_path}')
    img = c.resize(img, (720, 480))
    img_height, img_width, _ = img.shape
    # get the boxes
    boxes = T.image_to_boxes(img)
    # draw boxes and write below text
    for b in boxes.splitlines():
        b = b.split(' ')
        x, y, w, h = int(b[1]), int(b[2]), int(b[3]), int(b[4])
        img = c.rectangle(img, (int(b[1]), img_height - int(b[2])), (int(b[3]), img_height - int(b[4])), (0, 255, 0), 2)
        # write the text in the image
        c.putText(img, b[0], (x, img_height - y + 100), c.FONT_HERSHEY_SIMPLEX, 0.4, (0, 0, 0), 1)
    c.imshow('result',img)
    c.waitKey(0)

# speech recognition for either text or audio
def runApp():
    tkinter.Tk().withdraw() # prevents an empty tkinter window from appearing
    file_path = filedialog.askopenfile()
    first_thread = threading.Thread(target=showText(file_path.name))
    second_thread = threading.Thread(target=getAudio(file_path.name))
    # start th threads
    first_thread.start()
    second_thread.start()
    # join the threads
    first_thread.join()
    second_thread.join()


if __name__ == '__main__':
    runApp()