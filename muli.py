import os
import random
import json

from hoshino.typing import MessageSegment
from hoshino import R, Service, priv

current_dir = os.path.join(os.path.dirname(__file__), 'config.json')

sv = Service('muli', enable_on_default=True, visible=False)

@sv.on_prefix('牡蛎')
async def get_single_info(bot, ev):
    alltext = ev.message.extract_plain_text()
    try:
        text_list = alltext.split(' ', 1)
    except:
        msg = f'命令格式输入错误，请参考“马娘数据帮助”发送命令！'
        await bot.finish(ev, msg)
    info_type = text_list[0]

    uma_name_tmp = text_list[1]
    with open(current_dir, 'r', encoding = 'UTF-8') as f:
        f_data = json.load(f)
        f.close()
    with open(os.path.join(os.path.dirname(__file__), 'replace_dict.json'), 'r', encoding = 'UTF-8') as af:
        replace_data = json.load(af)
        af.close()
    name_list = list(f_data.keys())
    name_list.remove('current_chara')
    msg = ''
    for uma_name in name_list:
        other_name_list = list(replace_data[uma_name])
        cn_name = f_data[uma_name]['cn_name'] if f_data[uma_name]['cn_name'] else f_data[uma_name]['jp_name']
        if str(uma_name) == str(uma_name_tmp) or str(cn_name) == str(uma_name_tmp) or str(uma_name_tmp) in other_name_list:
            
            if info_type == '语音':
                voice = f_data[uma_name]['voice']
                if not voice:
                    msg = f'{uma_name_tmp}暂时还没有语音哟'
                    await bot.finish(ev, msg)
                save_path = R.img('uma_voice').path
                mp3_name = uma_name + '.mp3'
                voice_file = os.path.join(save_path, mp3_name)
                msg = MessageSegment.record(f'file:///{os.path.abspath(voice_file)}')
            
    if not msg:
        msg = f'这个角色可能不存在或者角色名称对不上'
    await bot.send(ev, msg)