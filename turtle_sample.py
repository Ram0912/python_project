# import turtle
# turtle.speed(0)
# turtle.bgcolor("black")
# for i in range(30):
#     for color in ("red", "blue", "purple", "white"):
#         turtle.color(color)
#         turtle.pensize(3)
#         turtle.left(4)
#         turtle.forward(200)
#         turtle.left(90)
#         turtle.forward(200)
#         turtle.left(90)
#         turtle.forward(200)
#         turtle.left(90)
#         turtle.forward(200)
#         turtle.left(90)

# import pyautogui as pg
# pg.getInfo()
# pg.write("sample")
# pg.press("Enter")

# import cv2
# import winsound
#
# cam = cv2.


# a =[10,20]
# b=a
# b+=[30, 40]
# print(a)
#
# a=2*2//2
# b = 3//2*3
# print(a,b)
# print(1//2)
import pyttsx3
import PyPDF2
book = open('sample.pdf', 'rb')
pdfReader = PyPDF2.PdfFileReader(book)
pages = pdfReader.numPages
print(pages)
speaker = pyttsx3.init()
pages = pdfReader.getPage(1)
text = pages.extractText()
speaker.say(text)
speaker.runAndWait()
