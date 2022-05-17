from cmath import rect
import os
import random
from nonebot.exceptions import CQHttpError
from nonebot import MessageSegment
from hoshino import R, Service, priv

sv = Service(
    name = '马娘全语音'
    use_priv = priv.NORMAL, #使用权限   
    manage_priv = priv.ADMIN, #管理权限
    visible = False, #False隐藏
    enable_on_default = True, #是否默认启用
    bundle = 'uma_voi', #属于哪一类
)
   
#牡蛎部分路径
muli_folder = R.get('uma_voi/muli/').path

def get_muli_folder ():
    files = os.listdir(muli_folder)
    filename = random.choice(files)
    rec = R.get('uma_voi/muli',filename)
    return rec

@sv.on_keyword('牡蛎')
async def muli(bot,ev) -> MessageSegment:
    file = get_muli_folder()
    try:
        rec = MessageSegment.record(f'file:///{os.path.abspath(file.path)}')
        await bot.send(ev,rec)
    except CQHttpError:
        sv.logger.erro("发送失败喵")
