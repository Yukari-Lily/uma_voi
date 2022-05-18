from cmath import rect
import os
import random
from nonebot.exceptions import CQHttpError
from nonebot import MessageSegment
from hoshino import R, Service, priv

sv = Service('uma_voi', enable_on_default=True, visible=False)
   
#定义牡蛎硬拼路径
muli_folder = R.get('uma_voi/muli/').path
def get_muli_folder():
    files = os.listdir(muli_folder)
    filename = random.choice(files)
    rec = R.get('uma_voi/muli',filename)
    return rec

#定义语音路径
voi_folder = R.get('uma_voi/voi').path
def get_voi_folder():
    files = os.listdir(voi_folder)
    filename = random.choice(files)
    rec = R.get('uma_voi/voi',filename)
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
@sv.on_fullmatch('牡蛎DD','DD牡蛎')
async def muli(bot,ev) -> MessageSegment:
    muli_19 = R.get('uma_voi/muli/snd_voi_race_101900_8 -.wav')
    try:
        rec = MessageSegment.record(f'file:///{os.path.abspath(muli_19.path)}')
        await bot.send(ev,rec)
    except CQHttpError:
        sv.logger.erro("发送失败喵")