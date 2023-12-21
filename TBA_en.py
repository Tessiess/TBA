from builder import *
import logging


logging.disable(logging.DEBUG)
logging.disable(logging.WARNING)


# 操作
def start():
    # 打开软件
    screencap()
    adb_click(image_to_position('ba', 0.5))
    sleep(20)
    # 寻找特定指标
    while True:
        screencap(5)
        cut_image((0, 0.5*y), (0.8*x, y))
        t1 = word_to_position('TOUCH')
        if t1:
            break
        else:
            t2 = word_to_position("Don't", 0.7)
            t3 = word_to_position('Confirm')
            if t2:
                adb_click(t2, (0, 0.5*y))
            if t3:
                adb_click(t3, (0, 0.5*y))

    # 开始唤醒
    screencap()
    cut_image((0.8*x, 0), (x, 0.2*y))
    adb_click(word_to_position("UID"), (0.8*x, 0))
    sleep(10)
    # 做每日签到/叉掉活动
    while True:
        screencap(3)
        cut_image((0.4*x, 0), (x, 0.8*y))
        t1 = word_to_position('Notice')
        if t1:
            break
        else:
            t2 = word_to_position('Attendance')
            t3 = word_to_position('Confirm')
            if t2:
                adb_click(t2, (0.4*x, 0))
            if t3:
                adb_click(t3, (0.4*x, 0))
    adb_click(image_to_position("X"), (0.4*x, 0))
    # 叉掉加速bug
    store_x()
    # 如果有额外的notice，叉掉
    screencap()
    cut_image((0.3*x, 0.5*y), (0.6*x, 0.8*y))
    t3 = word_to_position('Confirm')
    if t3:
        adb_click(t3, (0.3*x, 0.5*y))


def store_x():
    while True:
        screencap()
        cut_image((0.4*x, 0.6*y), (0.6*x, 0.8*y))
        t1 = word_to_position('Confirm')
        if t1:
            break
    adb_click(t1, (0.4*x, 0.6*y))
    screencap()
    print('store_x over')


def lesson():
    screencap()
    cut_image((0, 0.8*y), (x, y))
    # 进入lesson页面
    adb_click(word_to_position('Lesson'), (0, 0.8*y))
    while True:
        screencap()
        cut_image((0.4*x, 0), (0.8*x, y))
        t1 = word_to_position('Location')
        if t1:
            break
    # 注意第一个点击的不要前缀，后面的都要前缀

    # # 赤冬
    adb_swipe((0.8*x, 0.8*y), (0.8*x, 0.2*y))
    screencap()
    cut_image((0.4*x, 0), (0.8*x, y))

    adb_click(word_to_position('Red'), (0.4*x, 0))
    screencap()
    cut_image((0.8*x, 0.8*y), (x, y))
    adb_click(word_to_position('Locations'), (0.8*x, 0.8*y))
    task = ['Building', 'Plaza', 'Dormitory', 'Station', 'Cafeteria']
    for t in task:
        screencap()
        cut_image((0.1*x, 0.2*y), (0.9*x, 0.8*y))
        adb_click(word_to_position(t), (0.1*x, 0.2*y))
        screencap()
        cut_image((0.3*x, 0.7*y), (0.7*x, 0.9*y))
        adb_click(word_to_position('Start'), (0.3*x, 0.7*y))
        while True:
            screencap(3)
            cut_image((0.4*x, 0.6*y), (0.6*x, 0.9*y))
            if word_to_position('Confirm'):
                adb_click(word_to_position('Confirm'), (0.4*x, 0.6*y))
                break
            else:
                adb_click((0.2*x, 0.2*y))
        print(t)
    screencap()
    cut_image((0, 0), (0.1*x, 0.1*y))
    adb_click(image_to_position('return'))
    screencap()
    cut_image((0, 0), (0.1*x, 0.1*y))
    adb_click(image_to_position('return'))

    # DU city
    screencap()
    cut_image((0.4*x, 0), (0.8*x, y))
    adb_click(word_to_position('City'), (0.4*x, 0))
    screencap()
    cut_image((0.8*x, 0.8*y), (x, y))
    adb_click(word_to_position('Locations'), (0.8*x, 0.8*y))
    task = ['Business', 'Plato']
    for t in task:
        screencap()
        cut_image((0.1*x, 0.2*y), (0.9*x, 0.8*y))
        adb_click(word_to_position(t), (0.1*x, 0.2*y))
        screencap()
        cut_image((0.3*x, 0.7*y), (0.7*x, 0.9*y))
        adb_click(word_to_position('Start'), (0.3*x, 0.7*y))
        while True:
            screencap(3)
            cut_image((0.4*x, 0.6*y), (0.6*x, 0.9*y))
            if word_to_position('Confirm'):
                adb_click(word_to_position('Confirm'), (0.4*x, 0.6*y))
                break
            else:
                adb_click((0.2*x, 0.2*y))
        print(t)
    screencap()
    cut_image((0, 0), (0.1*x, 0.1*y))
    adb_click(image_to_position('return'))
    screencap()
    cut_image((0, 0), (0.1*x, 0.1*y))
    adb_click(image_to_position('return'))

    # # Schale Office
    # screencap()
    # adb_click(word_to_position('Office'), (0.4*x, 0))
    # screencap()
    # cut_image((0.8*x, 0.8*y), (x, y))
    # adb_click(word_to_position('Locations'), (0.8*x, 0.8*y))
    # task = ['Laboratory', 'Shooting', 'Hangar']
    # for t in task:
    #     screencap()
    #     cut_image((0.1*x, 0.2*y), (0.9*x, 0.8*y))
    #     adb_click(word_to_position(t), (0.1*x, 0.2*y))
    #     screencap()
    #     cut_image((0.3*x, 0.7*y), (0.7*x, 0.9*y))
    #     adb_click(word_to_position('Start'), (0.3*x, 0.7*y))
    #     while True:
    #         screencap(3)
    #         cut_image((0.4*x, 0.6*y), (0.6*x, 0.9*y))
    #         if word_to_position('Confirm'):
    #             adb_click(word_to_position('Confirm'), (0.4*x, 0.6*y))
    #             break
    #         else:
    #             adb_click((0.2*x, 0.2*y))
    #     print(t)
    # screencap()
    # cut_image((0, 0), (0.1*x, 0.1*y))
    # adb_click(image_to_position('return'))
    # screencap()
    # cut_image((0, 0), (0.1*x, 0.1*y))
    # adb_click(image_to_position('return'))

    # # Schale Residence Hall
    # screencap()
    # cut_image((0.4*x, 0), (0.8*x, y))
    # adb_click(word_to_position('Hall'), (0.4*x, 0))
    # screencap()
    # cut_image((0.8*x, 0.8*y), (x, y))
    # adb_click(word_to_position('Locations'), (0.8*x, 0.8*y))
    # task = ['Arcade', 'Dining', 'Garden']
    # for t in task:
    #     screencap()
    #     cut_image((0.1*x, 0.2*y), (0.9*x, 0.8*y))
    #     adb_click(word_to_position(t), (0.1*x, 0.2*y))
    #     screencap()
    #     cut_image((0.3*x, 0.7*y), (0.7*x, 0.9*y))
    #     adb_click(word_to_position('Start'), (0.3*x, 0.7*y))
    #     while True:
    #         screencap(3)
    #         cut_image((0.4*x, 0.6*y), (0.6*x, 0.9*y))
    #         if word_to_position('Confirm'):
    #             adb_click(word_to_position('Confirm'), (0.4*x, 0.6*y))
    #             break
    #         else:
    #             adb_click((0.2*x, 0.2*y))
    #     print(t)
    # screencap()
    # cut_image((0, 0), (0.1*x, 0.1*y))
    # adb_click(image_to_position('return'))
    # screencap()
    # cut_image((0, 0), (0.1*x, 0.1*y))
    # adb_click(image_to_position('return'))

    # 返回主页面
    screencap()
    cut_image((0, 0), (0.1*x, 0.1*y))
    adb_click(image_to_position('return'))

    store_x()


def club():
    screencap()
    cut_image((0, 0.8*y), (x, y))
    # 进入club
    adb_click(word_to_position('Club'), (0, 0.8*y))
    while True:
        screencap()
        cut_image((0, 0), (0.3*x, 0.1*y))
        t1 = word_to_position('Lobby')
        if t1:
            break

    # 返回主页面/领取每日体力
    screencap()
    cut_image((0, 0), (0.1*x, 0.1*y))
    adb_click(image_to_position('return'))

    # 返回主页面
    screencap()
    cut_image((0, 0), (0.1*x, 0.1*y))
    if image_to_position('return'):
        adb_click(image_to_position('return'))

    store_x()

    # 打开邮箱
    screencap()
    cut_image((0.8*x, 0), (x, 0.1*y))
    adb_click(image_to_position('mail'), (0.8*x, 0))
    while True:
        screencap()
        cut_image((0, 0), (0.3*x, 0.1*y))
        t2 = word_to_position('Mailbox')
        if t2:
            break

    screencap()
    cut_image((0.8*x, 0.8*y), (x, y))
    adb_click(word_to_position('Claim All'), (0.8*x, 0.8*y))

    # 返回主页面/领取物品
    screencap()
    cut_image((0, 0), (0.1*x, 0.1*y))
    adb_click(image_to_position('return'))

    # 返回主页面
    screencap()
    cut_image((0, 0), (0.1*x, 0.1*y))
    if image_to_position('return'):
        adb_click(image_to_position('return'))

    store_x()


def cafe():
    screencap()
    cut_image((0, 0.8*y), (x, y))
    # 进入cafe
    adb_click(word_to_position('Cafe'), (0, 0.8*y))
    while True:
        screencap()
        cut_image((0, 0), (0.3*x, 0.1*y))
        t1 = word_to_position('Schale')
        if t1:
            break

    # 避免签到页面
    screencap()
    cut_image((0.4*x, 0.6*y), (0.6*x, 0.8*y))
    if word_to_position('Confirm'):
        adb_click(word_to_position('Confirm'))

    screencap()
    cut_image((0.8*x, 0.8*y), (x, y))
    adb_click(word_to_position('Earnings'), (0.8*x, 0.8*y))
    screencap()
    cut_image((0.4*x, 0.6*y), (0.6*x, 0.8*y))
    adb_click(word_to_position('Claim'), (0.4*x, 0.6*y))

    screencap(4)
    cut_image((0, 0), (0.1*x, 0.1*y))
    adb_click(image_to_position('return'))
    screencap()
    cut_image((0, 0), (0.1*x, 0.1*y))
    adb_click(image_to_position('return'))
    screencap()
    cut_image((0, 0), (0.1*x, 0.1*y))
    adb_click(image_to_position('return'))

    store_x()


def crafting():
    screencap()
    cut_image((0, 0.8*y), (x, y))
    # 进入crafting
    adb_click(word_to_position('Crafting'), (0, 0.8*y))
    while True:
        screencap()
        cut_image((0, 0), (0.3*x, 0.1*y))
        t1 = word_to_position('Chamber')
        if t1:
            break
    # 收获所有物品
    while True:
        screencap()
        cut_image((0.8*x, 0.3*y), (x, 0.9*y))
        t2 = word_to_position('Receive')
        if t2:
            adb_click(t2, (0.8*x, 0.3*y))
            screencap()
            cut_image((0, 0), (0.1*x, 0.1*y))
            adb_click(image_to_position('return'))
        else:
            break
    # 自动生产物品
    while True:
        screencap()
        cut_image((0.6*x, 0.3*y), (0.8*x, 0.9*y))
        t3 = word_to_position('Start')
        if t3:
            # 开始第一轮
            adb_click(t3, (0.6*x, 0.3*y))
            screencap(4)
            cut_image((0.5*x, 0.1*y), (0.8*x, 0.5*y))
            adb_click(image_to_position('stone1'), (0.5*x, 0.1*y))
            screencap()
            cut_image((0.7*x, 0.8*y), (x, y))
            adb_click(word_to_position('Unlock'), (0.7*x, 0.8*y))
            screencap(4)
            cut_image((0.3*x, 0.3*y), (0.75*x, 0.85*y))
            # 优先级是 金色>礼物>其他
            t4 = image_to_position('radiant', 0.7)
            if t4:
                adb_click(t4, (0.3*x, 0.3*y))
            else:
                t5 = image_to_position('flower', 0.7)
                if t5:
                    adb_click(t5, (0.3*x, 0.3*y))
                else:
                    t6 = image_to_position('normal1')
                    t7 = image_to_position('normal2')
                    if t6:
                        adb_click(t6, (0.3*x, 0.3*y))
                    else:
                        adb_click(t7, (0.3*x, 0.3*y))
            screencap()
            cut_image((0.7*x, 0.8*y), (x, y))
            adb_click(word_to_position('Select'), (0.7*x, 0.8*y))

            # 开始第二次
            screencap(4)
            cut_image((0.5*x, 0.8*y), (0.8*x, y))
            adb_click(word_to_position('Add'), (0.5*x, 0.8*y))
            screencap()
            cut_image((0.5*x, 0.1*y), (0.8*x, 0.5*y))
            adb_click(image_to_position('stone1'), (0.5*x, 0.1*y))
            adb_click(image_to_position('stone1'), (0.5*x, 0.1*y))
            screencap()
            cut_image((0.7*x, 0.8*y), (x, y))
            adb_click(word_to_position('Unlock'), (0.7*x, 0.8*y))
            screencap(4)
            cut_image((0.2*x, 0.2*y), (0.6*x, 0.9*y))
            t4 = image_to_position('radiant', 0.7)
            if t4:
                adb_click(t4, (0.2*x, 0.2*y))
            else:
                t5 = image_to_position('flower', 0.7)
                if t5:
                    adb_click(t5, (0.2*x, 0.2*y))
                else:
                    t6 = image_to_position('normal1')
                    t7 = image_to_position('normal2')
                    if t6:
                        adb_click(t6, (0.2*x, 0.2*y))
                    else:
                        adb_click(t7, (0.2*x, 0.2*y))
            screencap()
            cut_image((0.7*x, 0.8*y), (x, y))
            adb_click(word_to_position('Select'), (0.7*x, 0.8*y))
            screencap(4)
            cut_image((0.7*x, 0.8*y), (x, y))
            adb_click(word_to_position('Start'), (0.7*x, 0.8*y))
            screencap()
            cut_image((0.5*x, 0.6*y), (0.7*x, 0.8*y))
            adb_click(word_to_position('Confirm'), (0.5*x, 0.6*y))
            sleep(5)
        else:
            break
    screencap()
    cut_image((0, 0), (0.1*x, 0.1*y))
    adb_click(image_to_position('return'))

    store_x()


def shop():
    screencap()
    cut_image((0, 0.8*y), (x, y))
    # 进入shop
    adb_click(word_to_position('Shop'),  (0, 0.8*y))
    while True:
        screencap()
        cut_image((0, 0.2*y), (0.2*x, 0.4*y))
        t1 = word_to_position('Eligma')
        if t1:
            break
    shop_list = ['Report', 'Nimrud', 'Aether',
                 'Disc', 'Codex', 'Wolfsegg', 'Mandrake', 'Voynich', 'Nebra', 'Antikythera', 'Crystal', 'Totem', 'Ancient', 'Disco', 'Winnipe']  # Stone
    while True:
        screencap()
        cut_image((0.4*x, 0.1*y), (x, y))
        goods = shop_word_to_position(shop_list)
        for g in goods:
            adb_click(g, (0.4*x, 0.1*y))
        screencap()
        cut_image((0.8*x, 0.8*y), (x, y))
        adb_click(word_to_position('Selected'), (0.8*x, 0.8*y))
        screencap()
        cut_image((0.5*x, 0.6*y), (0.7*x, 0.8*y))
        adb_click(word_to_position('Confirm'), (0.5*x, 0.6*y))
        sleep(2)
        adb_click((0.3*x, 0.2*y))
        screencap(address='pngs/history.png')
        adb_swipe((0.8*x, 0.8*y), (0.8*x, 0.2*y))
        # 对比前后图片判断到底
        screencap()
        if image_to_position('history', 0.9, exchange=False):
            break
    screencap()
    cut_image((0, 0), (0.1*x, 0.1*y))
    adb_click(image_to_position('return'))

    store_x()


def campaign():
    screencap()
    cut_image((0.8*x, 0.8*y), (x, 0.9*y))
    # 进入Campaign
    adb_click(word_to_position('Campaign'), (0.8*x, 0.8*y))
    while True:
        screencap()
        cut_image((0.5*x, 0.2*y), (0.7*x, 0.4*y))
        t1 = word_to_position('Mission')
        if t1:
            break

    # jjc
    screencap()
    cut_image((0.5*x, 0.5*y), (x, y))
    adb_click(word_to_position('Challenge'), (0.5*x, 0.5*y))
    screencap()
    cut_image((0.2*x, 0.4*y), (0.4*x, 0.8*y))
    cla = shop_word_to_position(['Claim'])
    for c in cla:
        adb_click(c, (0.2*x, 0.4*y))
        sleep(2)
        adb_click((0.3*x, 0.2*y))
    screencap()
    cut_image((0, 0), (0.1*x, 0.1*y))
    adb_click(image_to_position('return'))

    # 街道
    screencap()
    cut_image((0.5*x, 0.5*y), (x, y))
    adb_click(word_to_position('Bounty'), (0.5*x, 0.5*y))
    tl = ['Overpass', 'Desert', 'Classroom']
    for t in tl:
        screencap()
        cut_image((0.6*x, 0.2*y), (x, 0.9*y))
        adb_click(word_to_position(t), (0.6*x, 0.2*y))
        screencap()
        cut_image((0.8*x, 0.2*y), (x, y))
        el = shop_word_to_position(['Enter'])
        adb_click(el[-1], (0.8*x, 0.2*y))
        screencap()
        cut_image((0.6*x, 0.35*y), (0.9*x, 0.7*y))
        # 这边可以调整次数
        adb_click(image_to_position('+'), (0.6*x, 0.35*y))
        adb_click(word_to_position('Start Sweep'), (0.6*x, 0.35*y))
        screencap()
        cut_image((0.5*x, 0.6*y), (0.7*x, 0.8*y))
        adb_click(word_to_position('Confirm'), (0.5*x, 0.6*y))
        screencap(6)
        cut_image((0.4*x, 0.5*y), (0.6*x, y))
        adb_click(word_to_position_cht('Confirm'), (0.4*x, 0.5*y))
        screencap()
        cut_image((0, 0), (0.6*x, 0.3*y))
        if word_to_position('Info'):
            adb_click((0.1*x, 0.1*y))
        screencap()
        cut_image((0, 0), (0.1*x, 0.1*y))
        adb_click(image_to_position('return'))
        sleep(2)
    screencap()
    cut_image((0, 0), (0.1*x, 0.1*y))
    adb_click(image_to_position('return'))

    # 学生会
    screencap()
    cut_image((0.5*x, 0.5*y), (x, y))
    adb_click(word_to_position('Scrimmage'), (0.5*x, 0.5*y))
    # paddleocr好像对连续的l识别效果很差，先这样权宜一下
    tl = ['Trinity', 'Gehenna', 'ennium']
    for t in tl:
        screencap()
        cut_image((0.6*x, 0.2*y), (x, 0.9*y))
        adb_click(word_to_position(t), (0.6*x, 0.2*y))
        screencap()
        cut_image((0.8*x, 0.2*y), (x, y))
        el = shop_word_to_position(['Enter'])
        adb_click(el[-2], (0.8*x, 0.2*y))
        screencap()
        cut_image((0.6*x, 0.35*y), (0.9*x, 0.7*y))
        # 这边可以调整次数
        adb_click(image_to_position('+'), (0.6*x, 0.35*y))
        adb_click(word_to_position('Start Sweep'), (0.6*x, 0.35*y))
        screencap()
        cut_image((0.5*x, 0.6*y), (0.7*x, 0.8*y))
        adb_click(word_to_position('Confirm'), (0.5*x, 0.6*y))
        screencap(6)
        cut_image((0.4*x, 0.5*y), (0.6*x, y))
        adb_click(word_to_position_cht('Confirm'), (0.4*x, 0.5*y))
        screencap()
        cut_image((0, 0), (0.6*x, 0.3*y))
        if word_to_position('Info'):
            adb_click((0.1*x, 0.1*y))
        screencap()
        cut_image((0, 0), (0.1*x, 0.1*y))
        adb_click(image_to_position('return'))
        sleep(2)
    screencap()
    cut_image((0, 0), (0.1*x, 0.1*y))
    adb_click(image_to_position('return'))

    screencap()
    cut_image((0, 0), (0.1*x, 0.1*y))
    adb_click(image_to_position('return'))

    store_x()


def mission(n):
    for _ in range(n):
        screencap()
        cut_image((0.8*x, 0.2*y), (x, y))
        el = shop_word_to_position(['Enter'])
        adb_click(el[-1], (0.8*x, 0.2*y))
        screencap()
        cut_image((0.6*x, 0.6*y), (0.9*x, 0.8*y))
        adb_click(word_to_position('Start'), (0.6*x, 0.6*y))
        sleep(10)

        screencap()
        cut_image((0.8*x, 0), (x, 0.2*y))
        t2 = word_to_position('Menu')
        if t2:
            adb_click(t2, (0.8*x, 0))
            screencap()
            cut_image((0.8*x, 0), (x, 0.3*y))
            adb_click(image_to_position('skip'), (0.8*x, 0))
            screencap()
            cut_image((0.5*x, 0.6*y), (0.7*x, 0.8*y))
            adb_click(word_to_position('Confirm'), (0.5*x, 0.6*y))
            sleep(5)

        screencap()
        cut_image((0.8*x, 0.8*y), (x, y))
        adb_click(word_to_position('Mobilize'), (0.8*x, 0.8*y))
        sleep(120)
        while True:
            screencap(5)
            cut_image((0.8*x, 0.8*y), (x, y))
            t1 = word_to_position('Confirm')
            if t1:
                adb_click(t1, (0.8*x, 0.8*y))
                break
        sleep(10)

        screencap()
        cut_image((0.8*x, 0), (x, 0.2*y))
        t2 = word_to_position('Menu')
        if t2:
            adb_click(t2, (0.8*x, 0))
            screencap()
            cut_image((0.8*x, 0), (x, 0.3*y))
            adb_click(image_to_position('skip'), (0.8*x, 0))
            screencap()
            cut_image((0.5*x, 0.6*y), (0.7*x, 0.8*y))
            adb_click(word_to_position('Confirm'), (0.5*x, 0.6*y))
            sleep(10)

        screencap()
        cut_image((0.5*x, 0.8*y), (0.7*x, y))
        adb_click(word_to_position('Confirm'), (0.5*x, 0.8*y))
        sleep(10)
        print('event %i is over' % n)


if __name__ == "__main__":
    # 后面考虑一下怎么加条件
    if True:
        start()
        lesson()
        club()
        cafe()
        # crafting()
        shop()
        campaign()

    print('over')
