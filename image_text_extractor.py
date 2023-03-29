import pytesseract as T
import playsound,speech_recognition as sr,pyttsx3
import cv2 as c,os,gtts
def getAudio():
    # initialize tesseract software installed separately from pytesseract
    T.pytesseract.tesseract_cmd = r'C:\Program Files\Tesseract-OCR\tesseract.exe'
    # read image with openCv
    img = c.imread('test.jpg')
    img = c.resize(img, (720, 480))
    xy = T.image_to_string(img)

    # audio from image text
    audio = gtts.gTTS(text = xy, lang = 'en', slow = False)
    audio.save("saved_audio.wav")
    os.system("saved_audio.wav")
    # play audio
    # playsound.playsound('saved_audio.wav')


def showText():
    # initialize tesseract software installed separately from pytesseract
    T.pytesseract.tesseract_cmd = r'C:\Program Files\Tesseract-OCR\tesseract.exe'
    img = c.imread('test.jpg')
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
        c.putText(img, b[0], (x, img_height - y + 13), c.FONT_HERSHEY_SIMPLEX, 0.4, (50, 205, 50), 1)

    c.imshow('result',img)
    c.waitKey(0)

# speech recognition for either text or audio
def runApp():
    r = sr.Recognizer()
    with sr.Microphone() as source:
        print('what feature do you want: \n audio or \n text')
        r.adjust_for_ambient_noise(source=source)
        audio = r.listen(source,timeout=3)
        data = ''
        try :
            data = r.recognize_google(audio)
            if data =='audio':
                getAudio()
            elif data == 'text':
                showText()
            else:
                print('you said ' + data)
        except sr.UnknownValueError:
            print(" Error")
        except sr.RequestError as e:
            print("Request Error")

if __name__ == '__main__':
    runApp()