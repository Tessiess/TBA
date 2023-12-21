from paddleocr import PaddleOCR
from time import sleep
import logging
from PIL import Image
from builder import screencap

logging.disable(logging.DEBUG)
logging.disable(logging.WARNING)


def cut_image(c1, c2):
    (x1, y1) = c1
    (x2, y2) = c2
    img = Image.open('tmps/tmp.png')
    region = (x1, y1, x2, y2)
    cut_img = img.crop(region)
    cut_img.save('tmps/tmp.png')


def word_to_position_cht(message, val=0.8):
    ocr = PaddleOCR(use_angle_cls=True, lang="chinese_cht")
    screen = 'tmps/tmp.png'
    result = ocr.ocr(screen, cls=True)
    for res in result:
        print(res[1][0], res[1][1])


def word_to_position(message, val=0.8):
    ocr = PaddleOCR(use_angle_cls=True, lang="en")  # chinese_cht or en
    screen = 'tmps/tmp.png'
    result = ocr.ocr(screen, cls=True)
    for res in result:
        print(res[1][0], res[1][1])


x, y = 1920, 1080
screencap()
cut_image((0.3*x,0.1*y),(0.7*x,0.5*y))
word_to_position_cht('')
