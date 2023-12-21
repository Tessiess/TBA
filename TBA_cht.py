from builder import *
from lesson_cht import Les


# 操作


class Sta:
    def open(self):
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
                t2 = word_to_position_cht("今日", 0.7)
                t3 = word_to_position_cht('確認')
                if t2:
                    adb_click(t2, (0, 0.5*y))
                elif t3:
                    adb_click(t3, (0, 0.5*y))

    def touch(self):
        # 开始唤醒
        screencap()
        cut_image((0.8*x, 0), (x, 0.2*y))
        adb_click(word_to_position("UID"), (0.8*x, 0))
        sleep(10)
        # 做每日签到/叉掉活动
        while True:
            screencap(3)
            cut_image((0.4*x, 0), (x, 0.8*y))
            t1 = image_to_position('mail',0.9)
            if t1:
                adb_click(image_to_position('X'), (0.4*x, 0))
                break
            else:
                t2 = word_to_position_cht('第3天')
                t3 = word_to_position_cht('確認')
                t4 = word_to_position_cht("今日", 0.7)
                if t2:
                    adb_click(t2, (0.4*x, 0))
                elif t3:
                    adb_click(t3, (0.4*x, 0))
                elif t4:
                    adb_click(t4, (0.4*x, 0))

        store_x()

    def dlc(self):
        # 如果有额外的notice，叉掉
        screencap()
        cut_image((0.3*x, 0.5*y), (0.6*x, 0.8*y))
        t3 = word_to_position_cht('確認')
        if t3:
            adb_click(t3, (0.3*x, 0.5*y))


class Caf:
    #  以后做一下invite和touch功能
    def __init__(self,invite_,method=''):
        self.invite_=invite_
        self.method=method
        
    def enter(self):
        screencap()
        cut_image((0, 0.8*y), (x, y))
        # 进入cafe
        adb_click(word_to_position_cht('咖啡廳'), (0, 0.8*y))
        while True:
            screencap()
            cut_image((0, 0), (0.3*x, 0.1*y))
            t1 = word_to_position_cht('夏萊')
            if t1:
                break
        # 学生报道咖啡厅
        screencap()
        cut_image((0.4*x, 0.6*y), (0.6*x, 0.8*y))
        if word_to_position_cht('確認'):
            adb_click(word_to_position_cht('確認'), (0.4*x, 0.6*y))

    def invite(self):
        screencap()
        cut_image((0.5*x,0.8*y),(0.7*x,y))
        adb_click(word_to_position_cht('邀請券'),(0.5*x,0.8*y))
        screencap()
        cut_image((0.4*x, 0.6*y), (0.6*x, 0.8*y))
        t6=word_to_position_cht('確認')
        if t6:
            adb_click(t6,(0.4*x, 0.6*y))
            return 1
        screencap()
        cut_image((0.3*x,0.1*y),(0.7*x,0.5*y))
        t2=word_to_position_cht('羈絆等級')
        if not t2:
            t3=word_to_position_cht('名稱')
            t4=word_to_position_cht('學園')
            t5=word_to_position_cht('精選')
            if t3:
                adb_click(t3,(0.3*x,0.1*y))
            if t4:
                adb_click(t4,(0.3*x,0.1*y))
            if t5:
                adb_click(t5,(0.3*x,0.1*y))
            screencap()
            cut_image((0.3*x,0.1*y),(0.7*x,0.5*y))
            t2=word_to_position_cht('羈絆等級')
            adb_click(t2,(0.3*x,0.1*y))
            screencap()
            cut_image((0.3*x,0.5*y),(0.7*x,0.6*y))
            adb_click(word_to_position_cht('確認'),(0.3*x,0.5*y))
        screencap()
        cut_image((0.3*x,0.1*y),(0.7*x,0.4*y))
        if self.method=='max':
            if image_to_position('max',0.95):
                adb_click(word_to_position_cht('邀請'),(0.3*x,0.1*y))
            else:
                adb_click(image_to_position('min'),(0.3*x,0.1*y))
                sleep(1)
                adb_click(word_to_position_cht('邀請'),(0.3*x,0.1*y))
            screencap()
            cut_image((0.5*x, 0.6*y), (0.7*x, 0.8*y))
            adb_click(word_to_position_cht('確認'), (0.5*x, 0.6*y))
            sleep(4)
        elif self.method=='min':
            if image_to_position('min',0.95):
                adb_click(word_to_position_cht('邀請'),(0.3*x,0.1*y))
            else:
                adb_click(image_to_position('max'),(0.3*x,0.1*y))
                sleep(1)
                adb_click(word_to_position_cht('邀請'),(0.3*x,0.1*y))
            screencap()
            cut_image((0.5*x, 0.6*y), (0.7*x, 0.8*y))
            adb_click(word_to_position_cht('確認'), (0.5*x, 0.6*y))
            sleep(4)


    def get_AP(self):
        screencap(4)
        cut_image((0.8*x, 0.8*y), (x, y))
        adb_click(word_to_position_cht('收益'), (0.8*x, 0.8*y))
        screencap()
        cut_image((0.4*x, 0.6*y), (0.6*x, 0.8*y))
        adb_click(word_to_position_cht('領取'), (0.4*x, 0.6*y))
        screencap(4)
        cut_image((0, 0), (0.1*x, 0.1*y))
        adb_click(image_to_position('return'))
        screencap()
        cut_image((0, 0), (0.1*x, 0.1*y))
        adb_click(image_to_position('return'))

    def leave(self):
        screencap()
        cut_image((0, 0), (0.1*x, 0.1*y))
        adb_click(image_to_position('return'))
        store_x()
        

class Clu:
    def enter(self):
        screencap()
        cut_image((0, 0.8*y), (x, y))
        # 进入club
        adb_click(word_to_position_cht('社團'), (0, 0.8*y))
        while True:
            screencap()
            cut_image((0, 0), (0.3*x, 0.1*y))
            t1 = word_to_position_cht('社團大廳')
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

    def mailbox(self):
        # 打开邮箱
        screencap()
        cut_image((0.8*x, 0), (x, 0.1*y))
        adb_click(image_to_position('mail'), (0.8*x, 0))
        while True:
            screencap()
            cut_image((0, 0), (0.3*x, 0.1*y))
            t2 = word_to_position_cht('信箱')
            if t2:
                break

        screencap()
        cut_image((0.8*x, 0.8*y), (x, y))
        adb_click(word_to_position_cht('一次領取'), (0.8*x, 0.8*y))

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



class Cra:
    # 写个加速
    def __init__(self, stone_type, num, method):
        self.stone_type = stone_type
        self.num = num
        self.method = method

    def enter(self):
        screencap()
        cut_image((0, 0.8*y), (x, y))
        # 进入crafting 这边繁中有误，ocr识别有问题
        adb_click(word_to_position_cht('造'), (0, 0.8*y))
        while True:
            screencap()
            cut_image((0, 0), (0.3*x, 0.1*y))
            t1 = word_to_position_cht('工藝室')
            if t1:
                break

    def speed_up(self):
        while True:
            screencap()
            cut_image((0.8*x, 0.3*y), (x, 0.9*y))
            t6 = word_to_position_cht('立即')
            if t6:
                adb_click(t6, (0.8*x, 0.3*y))
                screencap()
                cut_image((0.5*x, 0.6*y), (0.7*x, 0.8*y))
                adb_click(word_to_position_cht('確認'))
            else:
                break

    def receive(self):
        # 收获所有物品
        while True:
            screencap()
            cut_image((0.8*x, 0.3*y), (x, 0.9*y))
            t2 = word_to_position_cht('領取')
            if t2:
                adb_click(t2, (0.8*x, 0.3*y))
                screencap()
                cut_image((0, 0), (0.1*x, 0.1*y))
                adb_click(image_to_position('return'))
            else:
                break

    def create(self):
        # 自动生产物品
        while True:
            screencap()
            cut_image((0.6*x, 0.3*y), (0.8*x, 0.9*y))
            t3 = word_to_position_cht('開始')
            if t3:
                adb_click(t3, (0.6*x, 0.3*y))
                # 开始第一轮
                self.turn1()

                # 开始第二次
                if self.num == '2':
                    self.turn2()

                # 确认
                self.confirm()

            else:
                break

    def leave(self):
        screencap()
        cut_image((0, 0), (0.1*x, 0.1*y))
        adb_click(image_to_position('return'))
        store_x()

    # 识别问题
    def way(self, fir='radiant', sec='flower'):
        screencap()
        cut_image((0.7*x, 0.8*y), (x, y))
        adb_click(word_to_position_cht('開放'), (0.7*x, 0.8*y))
        screencap(6)
        cut_image((0.2*x, 0.2*y), (0.75*x, 0.9*y))
        # 默认优先级是 金色>礼物>其他
        t4 = image_to_position(fir, 0.9)
        if t4:
            adb_click(t4, (0.2*x, 0.2*y))
        else:
            t5 = image_to_position(sec, 0.9)
            if t5:
                adb_click(t5, (0.2*x, 0.2*y))
            else:
                t6 = image_to_position('normal1', 0.3)
                t7 = image_to_position('normal2', 0.3)
                if t6:
                    adb_click(t6, (0.2*x, 0.2*y))
                else:
                    adb_click(t7, (0.2*x, 0.2*y))
        screencap()
        cut_image((0.7*x, 0.8*y), (x, y))
        adb_click(word_to_position_cht('選擇'), (0.7*x, 0.8*y))

    def turn1(self):
        screencap(4)
        cut_image((0.5*x, 0.1*y), (0.8*x, 0.5*y))
        (x1, y1) = image_to_position(self.stone_type)
        adb_swipe((x1+0.5*x, y1+0.1*y), (x1+0.5*x+1, y1+0.1*y+1), 3)

        if self.method == 'rad,flo':
            self.way()
        else:
            self.way('flower', 'radiant')

    def turn2(self):
        screencap(4)
        cut_image((0.5*x, 0.8*y), (0.8*x, y))
        adb_click(word_to_position_cht('追加'), (0.5*x, 0.8*y))

        screencap()
        cut_image((0.5*x, 0.1*y), (0.8*x, 0.5*y))
        (x2, y2) = image_to_position(self.stone_type)
        adb_swipe((x2+0.5*x, y2+0.1*y), (x2+0.5*x+1, y2+0.1*y+1), 5)

        if self.method == 'rad,flo':
            self.way()
        else:
            self.way('flower', 'radiant')

    def confirm(self):
        screencap(4)
        cut_image((0.7*x, 0.8*y), (x, y))
        adb_click(word_to_position_cht('開始'), (0.7*x, 0.8*y))
        screencap()
        cut_image((0.5*x, 0.6*y), (0.7*x, 0.8*y))
        adb_click(word_to_position_cht('確認'), (0.5*x, 0.6*y))
        sleep(5)
        


class Sho:
    # 在前端append到task中
    def __init__(self, tasks_normal, num_ap, normal_, ap_):
        self.tasks_normal = tasks_normal
        self.num_ap = num_ap
        self.normal_ = normal_
        self.ap_ = ap_

    def enter(self):
        screencap()
        cut_image((0, 0.8*y), (x, y))
        # 进入shop
        adb_click(word_to_position_cht('商店'),  (0, 0.8*y))
        while True:
            screencap()
            cut_image((0, 0.2*y), (0.2*x, 0.4*y))
            t1 = word_to_position_cht('神名')
            if t1:
                break

    def normal(self):
        while True:
            screencap()
            cut_image((0.4*x, 0.1*y), (x, y))
            goods = shop_word_to_position_cht(self.tasks_normal)
            for g in goods:
                adb_click(g, (0.4*x, 0.1*y))
            screencap()
            cut_image((0.8*x, 0.8*y), (x, y))
            adb_click(word_to_position_cht('選擇'), (0.8*x, 0.8*y))
            screencap()
            cut_image((0.5*x, 0.6*y), (0.7*x, 0.8*y))
            adb_click(word_to_position_cht('確認'), (0.5*x, 0.6*y))
            sleep(4)
            adb_click((0.3*x, 0.2*y))
            screencap(address='pngs/history.png')
            adb_swipe((0.8*x, 0.8*y), (0.8*x, 0.2*y))
            # 对比前后图片判断到底
            screencap()
            if image_to_position('history', 0.9, exchange=False):
                break

    def ap(self):
        screencap()
        cut_image((0, 0.5*y), (0.2*x, 0.8*y))
        adb_click(word_to_position_cht('戰術'), (0, 0.5*y))
        shop_list = ['AP']
        for _ in range(self.num_ap):
            screencap()
            cut_image((0.4*x, 0.5*y), (x, y))
            goods = shop_word_to_position(shop_list)
            for g in goods:
                adb_click(g, (0.4*x, 0.5*y))
            screencap()
            cut_image((0.8*x, 0.8*y), (x, y))
            adb_click(word_to_position_cht('選擇購買'), (0.8*x, 0.8*y))
            screencap()
            cut_image((0.5*x, 0.6*y), (0.7*x, 0.8*y))
            adb_click(word_to_position_cht('確認'), (0.5*x, 0.6*y))
            sleep(2)
            adb_click((0.3*x, 0.2*y))
            # 假如体力满了
            screencap()
            cut_image((0.4*x, 0.5*y), (0.7*x, 0.8*y))
            adb_click(word_to_position_cht('確認'), (0.4*x, 0.5*y))
            screencap()
            cut_image((0.8*x, 0.8*y), (x, y))
            adb_click(word_to_position_cht('更新'), (0.8*x, 0.8*y))
            screencap()
            cut_image((0.4*x, 0.5*y), (0.7*x, 0.8*y))
            adb_click(word_to_position_cht('確認'), (0.4*x, 0.5*y))
            sleep(1)

    def leave(self):
        screencap()
        cut_image((0, 0), (0.1*x, 0.1*y))
        adb_click(image_to_position('return'))
        # 重置history.png
        screencap(address='pngs/history.png')
        store_x()


class Cam:
    def __init__(self, jjc, bounty, scrimmage):
        self.jjc_ = jjc
        self.bounty = bounty
        self.scrimmage = scrimmage

    def enter(self):
        screencap()
        cut_image((0.8*x, 0.8*y), (x, 0.9*y))
        # 进入Campaign
        adb_click(word_to_position_cht('任務'), (0.8*x, 0.8*y))
        while True:
            screencap()
            cut_image((0.5*x, 0.2*y), (0.7*x, 0.4*y))
            t1 = word_to_position_cht('任務')
            if t1:
                break

    def jjc(self):
        # jjc
        screencap()
        cut_image((0.5*x, 0.5*y), (x, y))
        adb_click(word_to_position_cht('戰術'), (0.5*x, 0.5*y))
        screencap()
        cut_image((0.2*x, 0.4*y), (0.4*x, 0.8*y))
        cla = shop_word_to_position_cht(['獎勵'])
        for c in cla:
            adb_click(c, (0.2*x, 0.4*y))
            sleep(2)
            adb_click((0.3*x, 0.2*y))
            sleep(2)
        screencap()
        cut_image((0, 0), (0.1*x, 0.1*y))
        adb_click(image_to_position('return'))

    def bou(self):
        # 街道
        screencap()
        cut_image((0.5*x, 0.5*y), (x, y))
        adb_click(word_to_position_cht('懸賞'), (0.5*x, 0.5*y))
        tl = ['高架', '沙漠', '教室']
        cnt = 1
        for t in tl:
            if self.bounty[cnt]:
                screencap()
                cut_image((0.6*x, 0.2*y), (x, 0.9*y))
                adb_click(word_to_position_cht(t), (0.6*x, 0.2*y))
                screencap()
                cut_image((0.8*x, 0.2*y), (x, y))
                el = shop_word_to_position_cht(['入場'])
                # 如果是1，取倒数第二个入场，为0则取倒一
                adb_click(el[-self.bounty[cnt+3]-1], (0.8*x, 0.2*y))
                screencap()
                cut_image((0.6*x, 0.35*y), (0.9*x, 0.7*y))
                # 这边可以调整次数
                for _ in range(self.bounty[cnt]-1):
                    adb_click(image_to_position('+'), (0.6*x, 0.35*y))
                adb_click(word_to_position_cht('掃'), (0.6*x, 0.35*y))
                screencap()
                cut_image((0.5*x, 0.6*y), (0.7*x, 0.8*y))
                adb_click(word_to_position_cht('確認'), (0.5*x, 0.6*y))
                screencap(6)
                cut_image((0.4*x, 0.5*y), (0.6*x, y))
                if self.bounty[cnt]-1 > 10:
                    adb_click(word_to_position('SKIP'), (0.4*x, 0.5*y))
                    screencap(4)
                    cut_image((0.4*x, 0.5*y), (0.6*x, y))
                adb_click(word_to_position_cht('確認'), (0.4*x, 0.5*y))
                screencap()
                cut_image((0, 0), (0.6*x, 0.3*y))
                if word_to_position_cht('任務'):
                    adb_click((0.1*x, 0.1*y))
                screencap()
                cut_image((0, 0), (0.1*x, 0.1*y))
                adb_click(image_to_position('return'))
                sleep(2)
            cnt += 1

        screencap()
        cut_image((0, 0), (0.1*x, 0.1*y))
        adb_click(image_to_position('return'))

    def scr(self):
        # 学生会
        screencap()
        cut_image((0.5*x, 0.5*y), (x, y))
        adb_click(word_to_position_cht('學園'), (0.5*x, 0.5*y))
        tl = ['強化', '格黑娜', '年']  # 有点抽象的，三一不被识别为字
        cnt = 1
        for t in tl:
            if self.scrimmage[cnt]:
                screencap()
                cut_image((0.6*x, 0.2*y), (x, 0.9*y))
                adb_click(word_to_position_cht(t), (0.6*x, 0.2*y))
                screencap()
                cut_image((0.8*x, 0.2*y), (x, y))
                el = shop_word_to_position_cht(['入場'])
                # 如果是1，取倒数第二个入场，为0则取倒一
                adb_click(el[-self.scrimmage[cnt+3]-1], (0.8*x, 0.2*y))
                screencap()
                cut_image((0.6*x, 0.35*y), (0.9*x, 0.7*y))
                # 这边可以调整次数
                for _ in range(self.scrimmage[cnt]-1):
                    adb_click(image_to_position('+'), (0.6*x, 0.35*y))
                adb_click(word_to_position_cht('掃'), (0.6*x, 0.35*y))
                screencap()
                cut_image((0.5*x, 0.6*y), (0.7*x, 0.8*y))
                adb_click(word_to_position_cht('確認'), (0.5*x, 0.6*y))
                screencap(6)
                cut_image((0.4*x, 0.5*y), (0.6*x, y))
                if self.scrimmage[cnt]-1 > 10:
                    adb_click(word_to_position('SKIP'), (0.4*x, 0.5*y))
                    screencap(4)
                    cut_image((0.4*x, 0.5*y), (0.6*x, y))
                adb_click(word_to_position_cht('確認'), (0.4*x, 0.5*y))
                screencap()
                cut_image((0, 0), (0.6*x, 0.3*y))
                if word_to_position_cht('任務'):
                    adb_click((0.1*x, 0.1*y))
                screencap()
                cut_image((0, 0), (0.1*x, 0.1*y))
                adb_click(image_to_position('return'))
                sleep(2)
            cnt += 1

        screencap()
        cut_image((0, 0), (0.1*x, 0.1*y))
        adb_click(image_to_position('return'))

    def leave(self):
        screencap()
        cut_image((0, 0), (0.1*x, 0.1*y))
        adb_click(image_to_position('return'))
        store_x()


    


def mission():
    screencap()
    cut_image((0.8*x, 0.2*y), (x, y))
    el = shop_word_to_position_cht(['入場'])
    adb_click(el[-1], (0.8*x, 0.2*y))
    screencap()
    cut_image((0.4*x, 0.6*y), (0.9*x, 0.8*y))
    t1 = word_to_position_cht('進入章節')
    t2 = word_to_position_cht('任務開始')
    if t1:
        adb_click(t1, (0.4*x, 0.6*y))
        sleep(15)

        screencap()
        cut_image((0.8*x, 0), (x, 0.2*y))
        t3 = word_to_position('MENU')
        if t3:
            adb_click(t3, (0.8*x, 0))
            screencap()
            cut_image((0.8*x, 0), (x, 0.3*y))
            adb_click(image_to_position('skip'), (0.8*x, 0))
            screencap()
            cut_image((0.5*x, 0.6*y), (0.7*x, 0.8*y))
            adb_click(word_to_position_cht('確認'), (0.5*x, 0.6*y))
            sleep(5)
            adb_click((0.2*x, 0.2*y))
            sleep(2)
    else:
        adb_click(t2, (0.4*x, 0.6*y))
        sleep(15)

        screencap()
        cut_image((0.8*x, 0), (x, 0.2*y))
        t3 = word_to_position('MENU')
        if t3:
            adb_click(t3, (0.8*x, 0))
            screencap()
            cut_image((0.8*x, 0), (x, 0.3*y))
            adb_click(image_to_position('skip'), (0.8*x, 0))
            screencap()
            cut_image((0.5*x, 0.6*y), (0.7*x, 0.8*y))
            adb_click(word_to_position_cht('確認'), (0.5*x, 0.6*y))
            sleep(5)

        screencap()
        cut_image((0.8*x, 0.8*y), (x, y))
        adb_click(word_to_position_cht('出擊'), (0.8*x, 0.8*y))
        sleep(100)
        while True:
            screencap(5)
            cut_image((0.8*x, 0.8*y), (x, y))
            t1 = word_to_position_cht('確認')
            if t1:
                adb_click(t1, (0.8*x, 0.8*y))
                break
        sleep(10)

        screencap()
        cut_image((0.8*x, 0), (x, 0.2*y))
        t3 = word_to_position('MENU')
        if t3:
            adb_click(t3, (0.8*x, 0))
            screencap()
            cut_image((0.8*x, 0), (x, 0.3*y))
            adb_click(image_to_position('skip'), (0.8*x, 0))
            screencap()
            cut_image((0.5*x, 0.6*y), (0.7*x, 0.8*y))
            adb_click(word_to_position_cht('確認'), (0.5*x, 0.6*y))
            sleep(10)

        screencap()
        cut_image((0.3*x, 0.8*y), (0.7*x, y))
        adb_click(word_to_position_cht('確認'), (0.3*x, 0.8*y))
        sleep(5)
        screencap()
        cut_image((0.3*x, 0.8*y), (0.7*x, y))
        adb_click(word_to_position_cht('確認'), (0.3*x, 0.8*y))
        sleep(10)




