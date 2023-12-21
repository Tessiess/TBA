# TBA使用文档

本项目由Tessiess一时起兴写成(本来想复刻一个低配版maa的，但是还是技术不够，这个项目长期烂尾了)，之后不会进行维护和修补，如果需要更新版本，请自行修补(不过都用这个项目了，应该都会修修补补吧qwq)

## 一·如果你需要使用TBA(碧蓝档案国际服脚本-繁中)
#### 环境方面你需要:
1.拥有一个python环境
2.在创建虚拟环境后(如果库冲突的话)，安装文件夹下requirement.txt中的库(其中paddlepaddle库会出现和numpy版本冲突的报错，这属于正常现象，可以直接搜索解决)
```
pip install requirement.txt
```

3.运行menu.py文件，并且**先设置**需要功能，之后点击*开始运行*执行

#### 含有的功能：
- 开始唤醒
- 咖啡厅
- 课程表
- 社团
- 制造
- 清体力
- 商店
- 自动开荒活动(单独的版块)


**进行了每次修改操作记得点击保存设置，不然还是会执行上一次保存结果**

#### 下面是修改说明：

##### 开始唤醒
打开模拟器设置，查看长度和宽度
谷歌商店连接情况，可以参考每次打开游戏，是否会弹出“谷歌商店未连接”等类型报错，如果未弹出则是良好
连接地址可以查询模拟器的adb连接方面，只要输入类似*127.0.0.1:xxxx*即可

##### 咖啡厅
如果要进行邀请操作，则在选择邀请策略前打钩，这才代表执行下面的操作(之后同，不在赘述)
有两种模式邀请，会自动邀请好感最高的和最低的学生
*注意，在咖啡厅，脚本只会收取体力和邀请，**不会点击**学生增加好感！！*

##### 课程表
课程表的票券数量就是一天可以进行课程表的次数
下面的表格，左侧的地区前有多选框，勾选了才代表访问该地区，只钩后面的是无效的。右侧，多选框的底色代表着邀请所产出的品质(如果勾选了实际未解锁的地区，程序可能会报错卡死)，勾选了指定的多选框，代表着参与了这个节点的课程表

##### 社团
无，就是纯粹的签到并且领取邮件

##### 制造
启动石类型，就是整的启动石(一次1个)或者启动石碎片(一次10个)
制造*追加*次数，0次代表着只制造初始的一次，目前只能制造2次，不能添加金色材料进行第三次制造
制造策略只有优先材料和优先礼物两种，但是识别率比较低，有待优化

##### 清体力
竞技场，打钩表示领取信用货币和青辉石
下面的一行为示例，展现了下面的格式在
扫荡次数代表扫荡前面关卡的次数，后面的多选框按需勾选(如果未通关该关卡的最难难度需要勾选)

##### 商店
狗粮代表经验书，强化石只会全部购买，无法选择品质，材料全买(截止娃娃)
购买体力如果竞技场货币不够，可能会报错(也有可能程序卡住)

##### 自动开荒活动
请将页面切换到需要刷取的界面(最左边一列入场，未解锁的关卡都是锁住的)，剧情关卡依然可以跳过，不挑食qwq

## 二·如果你需要修改文件，下面是对于工程文件的介绍：
TBA(只提及必要介绍文件)
├─database(文件夹)
├─pngs(文件夹)
├─tmps(文件夹)
├─menu.py
├─lesson_cht.py
├─TBA_cht.py
├─TBA_en.py
├─builder.py
├─get.py
└─adb.exe


##### database(文件夹):
充当数据库的功能，可以保存之前设定好的设置

##### pngs(文件夹):
存储图片，供opencv库比对定位点击坐标

##### tmps(文件夹):
临时存储屏幕截图，便于程序识别

##### menu.py
主程序+前端，运行文件，如果要使用该软件运行这个

##### lesson_cht.py
课程表的后端程序，cht代表是繁中版本

##### TBA_cht.py
除了课程表的后端程序，cht代表是繁中版本

##### TBA_en.py
以前做的英文版后端，功能比较简陋，主程序并没有调用这个程序

##### builder.py
搭建脚本的工具， 不分繁中还是英文，内带一个等效于__init__意义的程序

##### get.py
获取图片元素的测试程序，可能对写程序有帮助

##### adb.exe
连接模拟器和脚本的“桥梁”，比较懒，所以就放在这了QAQ

#####目前已存bug
前端偶尔会出现格式问题(具体表现为字体大一号)，但是不影响使用


如果有其他需要沟通的问题，本人邮箱是Tessiess7v7@gmail.com
