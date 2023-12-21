from paddleocr import PaddleOCR
import os
from PIL import Image
import cv2
from time import sleep
import logging


logging.disable(logging.DEBUG)
logging.disable(logging.WARNING)
# 截屏


def screencap(time=2, address='tmps/tmp.png'):
    sleep(time)
    os.system("adb shell screencap -p > %s" % address)
    with open(address, "rb") as f:
        bys = f.read()
        bys_ = bys.replace(b"\r\n", b"\n")  # 二进制流中的"\r\n" 替换为"\n"
    with open(address, "bw") as f:
        f.write(bys_)


# 点击

def adb_click(center, offset=(0, 0)):
    sleep(1)
    if center:
        (x, y) = center
        x += offset[0]
        y += offset[1]
        os.system(f"adb shell input tap {x} {y}")
    else:
        print('fail!')


# 得到截屏分辨率
def know_xy():
    screencap()
    screen = cv2.imread('tmps/tmp.png')
    y, x = screen.shape[0:2]
    return x, y


# 滑屏

def adb_swipe(c1, c2, t=1):
    sleep(0.5)
    (x1, y1) = c1
    (x2, y2) = c2
    os.system(f'adb shell input swipe {x1} {y1} {x2} {y2}  {t}000')


# 裁剪图片
def cut_image(c1, c2):
    (x1, y1) = c1
    (x2, y2) = c2
    img = Image.open('tmps/tmp.png')
    region = (x1, y1, x2, y2)
    cut_img = img.crop(region)
    cut_img.save('tmps/tmp.png')


# 查找对应图像位置

def image_to_position(template_address, val=0.5, screen_address='tmps/tmp.png', exchange=True):
    screen = cv2.imread(screen_address)
    template = cv2.imread('pngs/'+template_address+'.png')
    # 如果需要缩放
    if exchange:
        screen = cv2.resize(screen, fx=tdx, fy=tdy, dsize=None,
                            interpolation=cv2.INTER_LINEAR)
    image_y, image_x = template.shape[0:2]
    result = cv2.matchTemplate(screen, template, cv2.TM_CCOEFF_NORMED)
    min_val, max_val, min_loc, max_loc = cv2.minMaxLoc(result)
    # 输出识别概率
    print('%s:%s' % (template_address, max_val))
    if max_val > val:
        # 需要缩放
        if exchange:
            x = (max_loc[0] + image_x / 2)/tdx
            y = (max_loc[1] + image_y / 2)/tdy
            return (x, y)
        else:
            x = max_loc[0] + image_x / 2
            y = max_loc[1] + image_y / 2
            return (x, y)
    else:
        print('fail to find %s' % template_address)
        return False


# 识别文字及坐标

def word_to_position(message, val=0.8):
    ocr = PaddleOCR(use_angle_cls=True, lang="en")  # chinese_cht or en
    screen = 'tmps/tmp.png'
    result = ocr.ocr(screen, cls=True)
    # print(result)
    for res in result:
        if message in res[1][0] and res[1][1] > val:
            # 输出识别概率
            print('%s:%s' % (message, res[1][1]))
            x = (res[0][0][0]+res[0][1][0])/2
            y = (res[0][0][1]+res[0][2][1])/2
            return (x, y)
    else:
        print('fail to find %s' % message)
        return False


def word_to_position_cht(message, val=0.5):
    ocr = PaddleOCR(use_angle_cls=True, lang="chinese_cht")
    screen = 'tmps/tmp.png'
    result = ocr.ocr(screen, cls=True)
    # print(result)
    for res in result:
        if message in res[1][0] and res[1][1] > val:
            # 输出识别概率
            print('%s:%s' % (message, res[1][1]))
            x = (res[0][0][0]+res[0][1][0])/2
            y = (res[0][0][1]+res[0][2][1])/2
            return (x, y)
    else:
        print('fail to find %s' % message)
        return False


def shop_word_to_position(l, val=0.8):
    ocr = PaddleOCR(use_angle_cls=True, lang="en")
    screen = 'tmps/tmp.png'
    result = ocr.ocr(screen, cls=True)
    ans = []
    for res in result:
        for i in l:
            if i in res[1][0] and res[1][1] > val:
                # 输出识别概率
                print(res[1][1])
                x = (res[0][0][0]+res[0][1][0])/2
                y = (res[0][0][1]+res[0][2][1])/2
                ans.append((x, y))
    return ans


def shop_word_to_position_cht(l, val=0.5):
    ocr = PaddleOCR(use_angle_cls=True, lang="chinese_cht")
    screen = 'tmps/tmp.png'
    result = ocr.ocr(screen, cls=True)
    ans = []
    for res in result:
        for i in l:
            if i in res[1][0] and res[1][1] > val:
                # 输出识别概率
                print(res[1][1])
                x = (res[0][0][0]+res[0][1][0])/2
                y = (res[0][0][1]+res[0][2][1])/2
                ans.append((x, y))
    return ans

def store_x():
    if net == 'bad':
        while True:
            screencap()
            cut_image((0.4*x, 0.6*y), (0.6*x, 0.8*y))
            t1 = word_to_position_cht('確認')
            if t1:
                break
        adb_click(t1, (0.4*x, 0.6*y))
        screencap()
        print('store_x over')

def is_main():
    cnt=0
    while True:
        screencap()
        cut_image((0.4*x, 0), (x, 0.8*y))
        t1 = image_to_position('mail',0.9)
        if t1:
            break
        cnt+=1
        if cnt>5:
            print('something wrong')
    sleep(3)

with open('database/start.txt', "rb") as f:
    xy = f.readlines()
    x,y,net=int(xy[0]),int(xy[1]),str(xy[2],encoding='utf-8').replace('\n','')
tdx = 1920/x
tdy = 1080/y