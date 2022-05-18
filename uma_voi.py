from cmath import rect
import os
import random
from nonebot.exceptions import CQHttpError
from nonebot import MessageSegment
from hoshino import R, Service, priv

sv = Service('uma_voi', enable_on_default=True, visible=False)
   
#定义牡蛎路径
muli_folder = R.get('uma_voi/muli/').path
def get_muli_folder():
    files = os.listdir(muli_folder)
    filename = random.choice(files)
    rec = R.get('uma_voi/muli',filename)
    return rec

#定义语音路径
voi_1001_folder = R.get('uma_voi/voi/1001特别周').path
def get_1001_folder():
    files = os.listdir(voi_1001_folder)
    filename = random.choice(files)
    rec = R.get('uma_voi/voi/1001特别周',filename)
    return rec

#牡蛎随机发送
@sv.on_fullmatch('牡蛎')
async def muli(bot,ev) -> MessageSegment:
    file = get_muli_folder()
    try:
        rec = MessageSegment.record(f'file:///{os.path.abspath(file.path)}')
        await bot.send(ev,rec)
    except CQHttpError:
        sv.logger.erro("发送失败喵")

#牡蛎指定发送
#成田白仁1016
@sv.on_fullmatch('牡蛎成田白仁','成田白仁牡蛎','白仁牡蛎','牡蛎白仁')
async def muli(bot,ev) -> MessageSegment:
    muli_16 = R.get('uma_voi/muli/snd_voi_race_101600_8 -.wav')
    try:
        rec = MessageSegment.record(f'file:///{os.path.abspath(muli_16.path)}')
        await bot.send(ev,rec)
    except CQHttpError:
        sv.logger.erro("发送失败喵")
   
#爱丽数码1019
@sv.on_fullmatch('牡蛎DD','DD牡蛎','牡蛎dd','dd牡蛎')
async def muli(bot,ev) -> MessageSegment:
    muli_19 = R.get('uma_voi/muli/snd_voi_race_101900_8 -.wav')
    try:
        rec = MessageSegment.record(f'file:///{os.path.abspath(muli_19.path)}')
        await bot.send(ev,rec)
    except CQHttpError:
        sv.logger.erro("发送失败喵")

#玉藻十字1021
@sv.on_fullmatch('tm牡蛎','TM牡蛎','牡蛎TAMA','TAMA牡蛎','牡蛎tama','tama牡蛎')
async def muli(bot,ev) -> MessageSegment:
    muli_21 = R.get('uma_voi/muli/snd_voi_race_102100_8 -.wav')
    try:
        rec = MessageSegment.record(f'file:///{os.path.abspath(muli_21.path)}')
        await bot.send(ev,rec)
    except CQHttpError:
        sv.logger.erro("发送失败喵")

#美妙姿势1022
@sv.on_fullmatch('芝士牡蛎','牡蛎芝士')
async def muli(bot,ev) -> MessageSegment:
    muli_22 = R.get('uma_voi/muli/snd_voi_race_102200_8 -.wav')
    try:
        rec = MessageSegment.record(f'file:///{os.path.abspath(muli_22.path)}')
        await bot.send(ev,rec)
    except CQHttpError:
        sv.logger.erro("发送失败喵")

#曼城茶座1025
@sv.on_fullmatch('牡蛎xcw','xcw牡蛎','XCW牡蛎','牡蛎XCW')
async def muli(bot,ev) -> MessageSegment:
    muli_25 = R.get('uma_voi/muli/snd_voi_race_102500_8 -.wav')
    try:
        rec = MessageSegment.record(f'file:///{os.path.abspath(muli_25.path)}')
        await bot.send(ev,rec)
    except CQHttpError:
        sv.logger.erro("发送失败喵")

#菱曙1028
@sv.on_fullmatch('牡蛎菱曙','菱曙牡蛎')
async def muli(bot,ev) -> MessageSegment:
    muli_28 = R.get('uma_voi/muli/snd_voi_race_102800_8 -.wav')
    try:
        rec = MessageSegment.record(f'file:///{os.path.abspath(muli_28.path)}')
        await bot.send(ev,rec)
    except CQHttpError:
        sv.logger.erro("发送失败喵")

#艾尼斯风神1031
@sv.on_fullmatch('牡蛎风神','风神牡蛎')
async def muli(bot,ev) -> MessageSegment:
    muli_31 = R.get('uma_voi/muli/snd_voi_race_103100_8 -.wav')
    try:
        rec = MessageSegment.record(f'file:///{os.path.abspath(muli_31.path)}')
        await bot.send(ev,rec)
    except CQHttpError:
        sv.logger.erro("发送失败喵")

#爱慕织姬1033
@sv.on_fullmatch('牡蛎织姬','织姬牡蛎')
async def muli(bot,ev) -> MessageSegment:
    muli_33 = R.get('uma_voi/muli/snd_voi_race_103300_8 -.wav')
    try:
        rec = MessageSegment.record(f'file:///{os.path.abspath(muli_33.path)}')
        await bot.send(ev,rec)
    except CQHttpError:
        sv.logger.erro("发送失败喵")

#荣进闪耀1037
@sv.on_fullmatch('牡蛎阿荣','阿荣牡蛎')
async def muli(bot,ev) -> MessageSegment:
    muli_37 = R.get('uma_voi/muli/snd_voi_race_103700_8 -.wav')
    try:
        rec = MessageSegment.record(f'file:///{os.path.abspath(muli_37.path)}')
        await bot.send(ev,rec)
    except CQHttpError:
        sv.logger.erro("发送失败喵")

#川上公主1039
@sv.on_fullmatch('牡蛎川上','川上牡蛎')
async def muli(bot,ev) -> MessageSegment:
    muli_39 = R.get('uma_voi/muli/snd_voi_race_103900_8 -.wav')
    try:
        rec = MessageSegment.record(f'file:///{os.path.abspath(muli_39.path)}')
        await bot.send(ev,rec)
    except CQHttpError:
        sv.logger.erro("发送失败喵")
    
#超级小海湾1045
@sv.on_fullmatch('牡蛎小海湾','小海湾牡蛎')
async def muli(bot,ev) -> MessageSegment:
    muli_45 = R.get('uma_voi/muli/snd_voi_race_104500_8 -.wav')
    try:
        rec = MessageSegment.record(f'file:///{os.path.abspath(muli_45.path)}')
        await bot.send(ev,rec)
    except CQHttpError:
        sv.logger.erro("发送失败喵")

#醒目飞鹰1046
@sv.on_fullmatch('牡蛎寄寄子','寄寄子牡蛎')
async def muli(bot,ev) -> MessageSegment:
    muli_46 = R.get('uma_voi/muli/snd_voi_race_104600_8 -.wav')
    try:
        rec = MessageSegment.record(f'file:///{os.path.abspath(muli_46.path)}')
        await bot.send(ev,rec)
    except CQHttpError:
        sv.logger.erro("发送失败喵")

#东瀛佐敦1048
@sv.on_fullmatch('牡蛎佐敦','佐敦牡蛎')
async def muli(bot,ev) -> MessageSegment:
    muli_48 = R.get('uma_voi/muli/snd_voi_race_104800_8 -.wav')
    try:
        rec = MessageSegment.record(f'file:///{os.path.abspath(muli_48.path)}')
        await bot.send(ev,rec)
    except CQHttpError:
        sv.logger.erro("发送失败喵")

#成田大进1050
@sv.on_fullmatch('牡蛎大进','大进牡蛎')
async def muli(bot,ev) -> MessageSegment:
    muli_50 = R.get('uma_voi/muli/snd_voi_race_105000_10 -.wav')
    try:
        rec = MessageSegment.record(f'file:///{os.path.abspath(muli_50.path)}')
        await bot.send(ev,rec)
    except CQHttpError:
        sv.logger.erro("发送失败喵")

#西野花1051
@sv.on_fullmatch('牡蛎西野花','西野花牡蛎')
async def muli(bot,ev) -> MessageSegment:
    muli_51 = R.get('uma_voi/muli/snd_voi_race_105100_8 -.wav')
    try:
        rec = MessageSegment.record(f'file:///{os.path.abspath(muli_51.path)}')
        await bot.send(ev,rec)
    except CQHttpError:
        sv.logger.erro("发送失败喵")

#名将怒涛1058
@sv.on_fullmatch('牡蛎怒涛','怒涛牡蛎')
async def muli(bot,ev) -> MessageSegment:
    muli_58 = R.get('uma_voi/muli/snd_voi_race_105800_8 -.wav')
    try:
        rec = MessageSegment.record(f'file:///{os.path.abspath(muli_58.path)}')
        await bot.send(ev,rec)
    except CQHttpError:
        sv.logger.erro("发送失败喵")

#目白多伯1059
@sv.on_fullmatch('牡蛎多勃','多勃牡蛎','牡蛎多啵','多啵牡蛎','牡蛎多伯','多伯牡蛎')
async def muli(bot,ev) -> MessageSegment:
    muli_59 = R.get('uma_voi/muli/snd_voi_race_105900_8 -.wav')
    try:
        rec = MessageSegment.record(f'file:///{os.path.abspath(muli_59.path)}')
        await bot.send(ev,rec)
    except CQHttpError:
        sv.logger.erro("发送失败喵")

#待兼诗歌剧1062
@sv.on_fullmatch('牡蛎诗宝','诗宝牡蛎')
async def muli(bot,ev) -> MessageSegment:
    muli_62 = R.get('uma_voi/muli/snd_voi_race_106200_8 -.wav')
    try:
        rec = MessageSegment.record(f'file:///{os.path.abspath(muli_62.path)}')
        await bot.send(ev,rec)
    except CQHttpError:
        sv.logger.erro("发送失败喵")

#里见光钻1067
@sv.on_fullmatch('牡蛎钻宝','钻宝牡蛎')
async def muli(bot,ev) -> MessageSegment:
    muli_67 = R.get('uma_voi/muli/snd_voi_race_106700_8 -.wav')
    try:
        rec = MessageSegment.record(f'file:///{os.path.abspath(muli_67.path)}')
        await bot.send(ev,rec)
    except CQHttpError:
        sv.logger.erro("发送失败喵")

#北部玄驹1068
@sv.on_fullmatch('牡蛎小北','小北牡蛎')
async def muli(bot,ev) -> MessageSegment:
    muli_68 = R.get('uma_voi/muli/snd_voi_race_106800_8 -.wav')
    try:
        rec = MessageSegment.record(f'file:///{os.path.abspath(muli_68.path)}')
        await bot.send(ev,rec)
    except CQHttpError:
        sv.logger.erro("发送失败喵")

#樱花千代王1069
@sv.on_fullmatch('牡蛎小千代','小千代牡蛎')
async def muli(bot,ev) -> MessageSegment:
    muli_69 = R.get('uma_voi/muli/snd_voi_race_106900_8 -.wav')
    try:
        rec = MessageSegment.record(f'file:///{os.path.abspath(muli_69.path)}')
        await bot.send(ev,rec)
    except CQHttpError:
        sv.logger.erro("发送失败喵")

#目白阿尔丹1071
@sv.on_fullmatch('牡蛎中国媳妇','中国媳妇牡蛎','牡蛎阿尔丹','阿尔丹牡蛎')
async def muli(bot,ev) -> MessageSegment:
    muli_71 = R.get('uma_voi/muli/snd_voi_race_107100_8 -.wav')
    try:
        rec = MessageSegment.record(f'file:///{os.path.abspath(muli_71.path)}')
        await bot.send(ev,rec)
    except CQHttpError:
        sv.logger.erro("发送失败喵")

#八重无敌1072
@sv.on_fullmatch('牡蛎八重','八重牡蛎')
async def muli(bot,ev) -> MessageSegment:
    muli_72 = R.get('uma_voi/muli/snd_voi_race_107200_8 -.wav')
    try:
        rec = MessageSegment.record(f'file:///{os.path.abspath(muli_72.path)}')
        await bot.send(ev,rec)
    except CQHttpError:
        sv.logger.erro("发送失败喵")

#目白光明1074
@sv.on_fullmatch('牡蛎光明','光明牡蛎')
async def muli(bot,ev) -> MessageSegment:
    muli_74 = R.get('uma_voi/muli/snd_voi_race_107400_8 -.wav')
    try:
        rec = MessageSegment.record(f'file:///{os.path.abspath(muli_74.path)}')
        await bot.send(ev,rec)
    except CQHttpError:
        sv.logger.erro("发送失败喵")

#语音部分
@sv.on_keyword("特别渣", "特别肥", "特别胖", "特别能吃", "小特", "斯佩酱", "斯佩夏尔维特")
async def muli(bot,ev) -> MessageSegment:
    file = get_1001_folder
    try:
        rec = MessageSegment.record(f'file:///{os.path.abspath(file.path)}')
        await bot.send(ev,rec)
    except CQHttpError:
        sv.logger.erro("发送失败喵")