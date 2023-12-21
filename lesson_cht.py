from builder import *
import logging


logging.disable(logging.DEBUG)
logging.disable(logging.WARNING)
# 改成append


class Les:
    def __init__(self, tables, tickets):
        self.tables = tables
        self.tickets = tickets

        self.tasks = [
            ['公室', '視聽室', '體育館', '圖書館', '教室', '實驗室', '射擊場', '載具庫'],
            ['居住區', '自習室', '訓練室', '休息室', '便利商店', '游戲中心', '餐廳', '菜園'],
            ['格黑娜', '第一', '大樓', '校園', '中央運動', '第二', '廣場', '委員會本部', '廢校'],
            ['阿拜多斯', '本館', '別館', '運動場', '圖書館', '游泳池', '體育館', '小賣店', '舊校'],
            ['研究區域', '巨塔', '車站', '圖書館', '小賣店', '實習中心', '資料中心', '發電站', '健身中心'],
            ['三一', '大教堂', '廣場', '圖書館', '社團', 'Basis', '美術館', '音樂廳', '古書館'],
            ['赤冬', '赤冬', '革命廣場', '共用', '赤熊', '供給所', '白鯨', '林業', '事務部'],
            ['百鬼夜行', '主樓', '中央廣場', '陰陽部', '大庭園', '商店街', '觀光', '博物館', '神木'],
            ['白鳥區', '學園', '柯基町', '三角廣場', '商業區', '普拉多', '公園', '鐘崎港', '駱馬町'],
            # 没升满D.U.


        ]

    def enter(self):
        screencap()
        cut_image((0, 0.8*y), (x, y))
        # 进入lesson页面
        adb_click(word_to_position_cht('課程表'), (0, 0.8*y))
        while True:
            screencap()
            cut_image((0.4*x, 0), (0.8*x, y))
            t1 = word_to_position('Location')
            if t1:
                break

    def lesson(self):
        for i in range(9):
            if self.tables[i][0] and sum(self.tables[i][1:]):
                if i > 4:
                    adb_swipe((0.8*x, 0.8*y), (0.8*x, 0.2*y))
                screencap()
                cut_image((0.4*x, 0), (0.8*x, y))
                adb_click(word_to_position_cht(
                    self.tasks[i][0]), (0.4*x, 0))
                screencap()
                cut_image((0.8*x, 0.8*y), (x, y))
                adb_click(word_to_position_cht('全體課程表'), (0.8*x, 0.8*y))
                for j in range(1, len(self.tables[i])):
                    if self.tables[i][j]:
                        screencap()
                        cut_image((0.1*x, 0.2*y), (0.9*x, 0.8*y))
                        adb_click(word_to_position_cht(
                            self.tasks[i][j]), (0.1*x, 0.2*y))
                        screencap()
                        cut_image((0.3*x, 0.7*y), (0.7*x, 0.9*y))
                        adb_click(word_to_position_cht('開始'), (0.3*x, 0.7*y))
                        while True:
                            screencap(4)
                            cut_image((0.4*x, 0.6*y), (0.6*x, 0.9*y))
                            if word_to_position_cht('確認'):
                                adb_click(word_to_position_cht(
                                    '確認'), (0.4*x, 0.6*y))
                                break
                            else:
                                adb_click((0.2*x, 0.2*y))
                        print(self.tasks[i][j])
                screencap()
                cut_image((0, 0), (0.1*x, 0.1*y))
                adb_click(image_to_position('return'))
                screencap()
                cut_image((0, 0), (0.1*x, 0.1*y))
                adb_click(image_to_position('return'))
                sleep(2)

    def leave(self):
        # 返回主页面
        screencap()
        cut_image((0, 0), (0.1*x, 0.1*y))
        adb_click(image_to_position('return'))

        store_x()

    def run(self):
        cnt = 0
        for i in self.tables:
            if i[0]:
                cnt += sum(i[1:])
        if cnt > self.tickets:
            print('tasks are more than expected')
            exit(1)

        self.enter()
        self.lesson()
        self.leave()
