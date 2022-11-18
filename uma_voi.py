from cmath import rect
import os
import random
from nonebot.exceptions import CQHttpError
from nonebot import MessageSegment
from hoshino import R, Service, priv

sv = Service('uma_voi', enable_on_default=True, visible=False)

yada_folder = R.get('uma_voi/yada/').path
def get_yada_folder():
    files = os.listdir(yada_folder)
    filename = random.choice(files)
    rec = R.get('uma_voi/yada',filename)
    return rec

koba_folder = R.get('uma_voi/koba/').path
def get_koba_folder():
    files = os.listdir(koba_folder)
    filename = random.choice(files)
    rec = R.get('uma_voi/koba',filename)
    return rec
   
muli_folder = R.get('uma_voi/muli/').path
def get_muli_folder():
    files = os.listdir(muli_folder)
    filename = random.choice(files)
    rec = R.get('uma_voi/muli',filename)
    return rec

voi_1001_folder = R.get('uma_voi/voi/1001特别周/').path
def get_1001_folder():
    files = os.listdir(voi_1001_folder)
    filename = random.choice(files)
    rec = R.get('uma_voi/voi/1001特别周/',filename)
    return rec

voi_1002_folder = R.get('uma_voi/voi/1002无声铃鹿/').path
def get_1002_folder():
    files = os.listdir(voi_1002_folder)
    filename = random.choice(files)
    rec = R.get('uma_voi/voi/1002无声铃鹿/',filename)
    return rec

voi_1003_folder = R.get('uma_voi/voi/1003东海帝王/').path
def get_1003_folder():
    files = os.listdir(voi_1003_folder)
    filename = random.choice(files)
    rec = R.get('uma_voi/voi/1003东海帝王/',filename)
    return rec

voi_1004_folder = R.get('uma_voi/voi/1004丸善斯基/').path
def get_1004_folder():
    files = os.listdir(voi_1004_folder)
    filename = random.choice(files)
    rec = R.get('uma_voi/voi/1004丸善斯基/',filename)
    return rec

voi_1005_folder = R.get('uma_voi/voi/1005富士奇迹/').path
def get_1005_folder():
    files = os.listdir(voi_1005_folder)
    filename = random.choice(files)
    rec = R.get('uma_voi/voi/1005富士奇迹/',filename)
    return rec

voi_1006_folder = R.get('uma_voi/voi/1006小栗帽/').path
def get_1006_folder():
    files = os.listdir(voi_1006_folder)
    filename = random.choice(files)
    rec = R.get('uma_voi/voi/1006小栗帽/',filename)
    return rec

voi_1007_folder = R.get('uma_voi/voi/1007黄金船/').path
def get_1007_folder():
    files = os.listdir(voi_1007_folder)
    filename = random.choice(files)
    rec = R.get('uma_voi/voi/1007黄金船/',filename)
    return rec

voi_1008_folder = R.get('uma_voi/voi/1008伏特加/').path
def get_1008_folder():
    files = os.listdir(voi_1008_folder)
    filename = random.choice(files)
    rec = R.get('uma_voi/voi/1008伏特加/',filename)
    return rec

voi_1009_folder = R.get('uma_voi/voi/1009大和赤骥/').path
def get_1009_folder():
    files = os.listdir(voi_1009_folder)
    filename = random.choice(files)
    rec = R.get('uma_voi/voi/1009大和赤骥/',filename)
    return rec

voi_1010_folder = R.get('uma_voi/voi/1010大树快车/').path
def get_1010_folder():
    files = os.listdir(voi_1010_folder)
    filename = random.choice(files)
    rec = R.get('uma_voi/voi/1010大树快车/',filename)
    return rec

voi_1011_folder = R.get('uma_voi/voi/1011草上飞/').path
def get_1011_folder():
    files = os.listdir(voi_1011_folder)
    filename = random.choice(files)
    rec = R.get('uma_voi/voi/1011草上飞/',filename)
    return rec

voi_1012_folder = R.get('uma_voi/voi/1012菱亚马逊/').path
def get_1012_folder():
    files = os.listdir(voi_1012_folder)
    filename = random.choice(files)
    rec = R.get('uma_voi/voi/1012菱亚马逊/',filename)
    return rec

voi_1013_folder = R.get('uma_voi/voi/1013目白麦昆/').path
def get_1013_folder():
    files = os.listdir(voi_1013_folder)
    filename = random.choice(files)
    rec = R.get('uma_voi/voi/1013目白麦昆/',filename)
    return rec

voi_1014_folder = R.get('uma_voi/voi/1014神鹰/').path
def get_1014_folder():
    files = os.listdir(voi_1014_folder)
    filename = random.choice(files)
    rec = R.get('uma_voi/voi/1014神鹰/',filename)
    return rec

voi_1015_folder = R.get('uma_voi/voi/1015好歌剧/').path
def get_1015_folder():
    files = os.listdir(voi_1015_folder)
    filename = random.choice(files)
    rec = R.get('uma_voi/voi/1015好歌剧/',filename)
    return rec

voi_1016_folder = R.get('uma_voi/voi/1016成田白仁/').path
def get_1016_folder():
    files = os.listdir(voi_1016_folder)
    filename = random.choice(files)
    rec = R.get('uma_voi/voi/1016成田白仁/',filename)
    return rec

voi_1017_folder = R.get('uma_voi/voi/1017鲁道夫象征/').path
def get_1017_folder():
    files = os.listdir(voi_1017_folder)
    filename = random.choice(files)
    rec = R.get('uma_voi/voi/1017鲁道夫象征/',filename)
    return rec

voi_1018_folder = R.get('uma_voi/voi/1018气槽/').path
def get_1018_folder():
    files = os.listdir(voi_1018_folder)
    filename = random.choice(files)
    rec = R.get('uma_voi/voi/1018气槽/',filename)
    return rec

voi_1019_folder = R.get('uma_voi/voi/1019爱丽数码/').path
def get_1019_folder():
    files = os.listdir(voi_1019_folder)
    filename = random.choice(files)
    rec = R.get('uma_voi/voi/1019爱丽数码/',filename)
    return rec

voi_1020_folder = R.get('uma_voi/voi/1020星云天空/').path
def get_1020_folder():
    files = os.listdir(voi_1020_folder)
    filename = random.choice(files)
    rec = R.get('uma_voi/voi/1020星云天空/',filename)
    return rec

voi_1021_folder = R.get('uma_voi/voi/1021玉藻十字/').path
def get_1021_folder():
    files = os.listdir(voi_1021_folder)
    filename = random.choice(files)
    rec = R.get('uma_voi/voi/1021玉藻十字/',filename)
    return rec

voi_1022_folder = R.get('uma_voi/voi/1022美妙姿势/').path
def get_1022_folder():
    files = os.listdir(voi_1022_folder)
    filename = random.choice(files)
    rec = R.get('uma_voi/voi/1022美妙姿势/',filename)
    return rec

voi_1023_folder = R.get('uma_voi/voi/1023琵琶晨光/').path
def get_1023_folder():
    files = os.listdir(voi_1023_folder)
    filename = random.choice(files)
    rec = R.get('uma_voi/voi/1023琵琶晨光/',filename)
    return rec

voi_1024_folder = R.get('uma_voi/voi/1024重炮/').path
def get_1024_folder():
    files = os.listdir(voi_1024_folder)
    filename = random.choice(files)
    rec = R.get('uma_voi/voi/1024重炮/',filename)
    return rec

voi_1025_folder = R.get('uma_voi/voi/1025曼城茶座/').path
def get_1025_folder():
    files = os.listdir(voi_1025_folder)
    filename = random.choice(files)
    rec = R.get('uma_voi/voi/1025曼城茶座/',filename)
    return rec

voi_1026_folder = R.get('uma_voi/voi/1026美浦波旁/').path
def get_1026_folder():
    files = os.listdir(voi_1026_folder)
    filename = random.choice(files)
    rec = R.get('uma_voi/voi/1026美浦波旁/',filename)
    return rec

voi_1027_folder = R.get('uma_voi/voi/1027目白赖恩/').path
def get_1027_folder():
    files = os.listdir(voi_1027_folder)
    filename = random.choice(files)
    rec = R.get('uma_voi/voi/1027目白赖恩/',filename)
    return rec

voi_1028_folder = R.get('uma_voi/voi/1028菱曙/').path
def get_1028_folder():
    files = os.listdir(voi_1028_folder)
    filename = random.choice(files)
    rec = R.get('uma_voi/voi/1028菱曙/',filename)
    return rec

voi_1029_folder = R.get('uma_voi/voi/1029雪之美人/').path
def get_1029_folder():
    files = os.listdir(voi_1029_folder)
    filename = random.choice(files)
    rec = R.get('uma_voi/voi/1029雪之美人/',filename)
    return rec

voi_1030_folder = R.get('uma_voi/voi/1030米浴/').path
def get_1030_folder():
    files = os.listdir(voi_1030_folder)
    filename = random.choice(files)
    rec = R.get('uma_voi/voi/1030米浴/',filename)
    return rec

voi_1031_folder = R.get('uma_voi/voi/1031艾尼斯风神/').path
def get_1031_folder():
    files = os.listdir(voi_1031_folder)
    filename = random.choice(files)
    rec = R.get('uma_voi/voi/1031艾尼斯风神/',filename)
    return rec

voi_1032_folder = R.get('uma_voi/voi/1032爱丽速子/').path
def get_1032_folder():
    files = os.listdir(voi_1032_folder)
    filename = random.choice(files)
    rec = R.get('uma_voi/voi/1032爱丽速子/',filename)
    return rec

voi_1033_folder = R.get('uma_voi/voi/1033爱慕织姬/').path
def get_1033_folder():
    files = os.listdir(voi_1033_folder)
    filename = random.choice(files)
    rec = R.get('uma_voi/voi/1033爱慕织姬/',filename)
    return rec

voi_1034_folder = R.get('uma_voi/voi/1034稻荷一/').path
def get_1034_folder():
    files = os.listdir(voi_1034_folder)
    filename = random.choice(files)
    rec = R.get('uma_voi/voi/1034稻荷一/',filename)
    return rec

voi_1035_folder = R.get('uma_voi/voi/1035胜利奖券/').path
def get_1035_folder():
    files = os.listdir(voi_1035_folder)
    filename = random.choice(files)
    rec = R.get('uma_voi/voi/1035胜利奖券/',filename)
    return rec

voi_1036_folder = R.get('uma_voi/voi/1036空中神宫/').path
def get_1036_folder():
    files = os.listdir(voi_1036_folder)
    filename = random.choice(files)
    rec = R.get('uma_voi/voi/1036空中神宫/',filename)
    return rec

voi_1037_folder = R.get('uma_voi/voi/1037荣进闪耀/').path
def get_1037_folder():
    files = os.listdir(voi_1037_folder)
    filename = random.choice(files)
    rec = R.get('uma_voi/voi/1037荣进闪耀/',filename)
    return rec

voi_1038_folder = R.get('uma_voi/voi/1038真机伶/').path
def get_1038_folder():
    files = os.listdir(voi_1038_folder)
    filename = random.choice(files)
    rec = R.get('uma_voi/voi/1038真机伶/',filename)
    return rec

voi_1039_folder = R.get('uma_voi/voi/1039川上公主/').path
def get_1039_folder():
    files = os.listdir(voi_1039_folder)
    filename = random.choice(files)
    rec = R.get('uma_voi/voi/1039川上公主/',filename)
    return rec

voi_1040_folder = R.get('uma_voi/voi/1040黄金城/').path
def get_1040_folder():
    files = os.listdir(voi_1040_folder)
    filename = random.choice(files)
    rec = R.get('uma_voi/voi/1040黄金城/',filename)
    return rec

voi_1041_folder = R.get('uma_voi/voi/1041樱花进王/').path
def get_1041_folder():
    files = os.listdir(voi_1041_folder)
    filename = random.choice(files)
    rec = R.get('uma_voi/voi/1041樱花进王/',filename)
    return rec

voi_1042_folder = R.get('uma_voi/voi/1042采珠/').path
def get_1042_folder():
    files = os.listdir(voi_1042_folder)
    filename = random.choice(files)
    rec = R.get('uma_voi/voi/1042采珠/',filename)
    return rec

voi_1043_folder = R.get('uma_voi/voi/1043"新光风"/').path
def get_1043_folder():
    files = os.listdir(voi_1043_folder)
    filename = random.choice(files)
    rec = R.get('uma_voi/voi/1043新光风/',filename)
    return rec

voi_1044_folder = R.get('uma_voi/voi/1044东商变革/').path
def get_1044_folder():
    files = os.listdir(voi_1044_folder)
    filename = random.choice(files)
    rec = R.get('uma_voi/voi/1044东商变革/',filename)
    return rec

voi_1045_folder = R.get('uma_voi/voi/1045超级小海湾/').path
def get_1045_folder():
    files = os.listdir(voi_1045_folder)
    filename = random.choice(files)
    rec = R.get('uma_voi/voi/1045超级小海湾/',filename)
    return rec

voi_1046_folder = R.get('uma_voi/voi/1046醒目飞鹰/').path
def get_1046_folder():
    files = os.listdir(voi_1046_folder)
    filename = random.choice(files)
    rec = R.get('uma_voi/voi/1046醒目飞鹰/',filename)
    return rec

voi_1047_folder = R.get('uma_voi/voi/1047荒漠英雄/').path
def get_1047_folder():
    files = os.listdir(voi_1047_folder)
    filename = random.choice(files)
    rec = R.get('uma_voi/voi/1047荒漠英雄/',filename)
    return rec

voi_1048_folder = R.get('uma_voi/voi/1048东瀛佐敦/').path
def get_1048_folder():
    files = os.listdir(voi_1048_folder)
    filename = random.choice(files)
    rec = R.get('uma_voi/voi/1048东瀛佐敦/',filename)
    return rec

voi_1049_folder = R.get('uma_voi/voi/1049中山庆典/').path
def get_1049_folder():
    files = os.listdir(voi_1049_folder)
    filename = random.choice(files)
    rec = R.get('uma_voi/voi/1049中山庆典/',filename)
    return rec

voi_1050_folder = R.get('uma_voi/voi/1050成田大进/').path
def get_1050_folder():
    files = os.listdir(voi_1050_folder)
    filename = random.choice(files)
    rec = R.get('uma_voi/voi/1050成田大进/',filename)
    return rec

voi_1051_folder = R.get('uma_voi/voi/1051西野花/').path
def get_1051_folder():
    files = os.listdir(voi_1051_folder)
    filename = random.choice(files)
    rec = R.get('uma_voi/voi/1051西野花/',filename)
    return rec

voi_1052_folder = R.get('uma_voi/voi/1052春乌拉拉/').path
def get_1052_folder():
    files = os.listdir(voi_1052_folder)
    filename = random.choice(files)
    rec = R.get('uma_voi/voi/1052春乌拉拉/',filename)
    return rec

voi_1053_folder = R.get('uma_voi/voi/1053青竹回忆/').path
def get_1053_folder():
    files = os.listdir(voi_1053_folder)
    filename = random.choice(files)
    rec = R.get('uma_voi/voi/1053青竹回忆/',filename)
    return rec

voi_1054_folder = R.get('uma_voi/voi/1054周日宁静/').path
def get_1054_folder():
    files = os.listdir(voi_1054_folder)
    filename = random.choice(files)
    rec = R.get('uma_voi/voi/1054周日宁静/',filename)
    return rec

voi_1055_folder = R.get('uma_voi/voi/1055微光飞驹/').path
def get_1055_folder():
    files = os.listdir(voi_1055_folder)
    filename = random.choice(files)
    rec = R.get('uma_voi/voi/1055微光飞驹/',filename)
    return rec

voi_1056_folder = R.get('uma_voi/voi/1056待兼福来/').path
def get_1056_folder():
    files = os.listdir(voi_1056_folder)
    filename = random.choice(files)
    rec = R.get('uma_voi/voi/1056待兼福来/',filename)
    return rec

voi_1057_folder = R.get('uma_voi/voi/1057千明代表/').path
def get_1057_folder():
    files = os.listdir(voi_1057_folder)
    filename = random.choice(files)
    rec = R.get('uma_voi/voi/1057千明代表/',filename)
    return rec

voi_1058_folder = R.get('uma_voi/voi/1058名将怒涛/').path
def get_1058_folder():
    files = os.listdir(voi_1058_folder)
    filename = random.choice(files)
    rec = R.get('uma_voi/voi/1058名将怒涛/',filename)
    return rec

voi_1059_folder = R.get('uma_voi/voi/1059目白多伯/').path
def get_1059_folder():
    files = os.listdir(voi_1059_folder)
    filename = random.choice(files)
    rec = R.get('uma_voi/voi/1059目白多伯/',filename)
    return rec

voi_1060_folder = R.get('uma_voi/voi/1060优秀素质/').path
def get_1060_folder():
    files = os.listdir(voi_1060_folder)
    filename = random.choice(files)
    rec = R.get('uma_voi/voi/1060优秀素质/',filename)
    return rec

voi_1061_folder = R.get('uma_voi/voi/1061帝王光辉/').path
def get_1061_folder():
    files = os.listdir(voi_1061_folder)
    filename = random.choice(files)
    rec = R.get('uma_voi/voi/1061帝王光辉/',filename)
    return rec

voi_1062_folder = R.get('uma_voi/voi/1062待兼诗歌剧/').path
def get_1062_folder():
    files = os.listdir(voi_1062_folder)
    filename = random.choice(files)
    rec = R.get('uma_voi/voi/1062待兼诗歌剧/',filename)
    return rec

voi_1063_folder = R.get('uma_voi/voi/1063生野狄杜斯/').path
def get_1063_folder():
    files = os.listdir(voi_1063_folder)
    filename = random.choice(files)
    rec = R.get('uma_voi/voi/1063生野狄杜斯/',filename)
    return rec

voi_1064_folder = R.get('uma_voi/voi/1064目白善信/').path
def get_1064_folder():
    files = os.listdir(voi_1064_folder)
    filename = random.choice(files)
    rec = R.get('uma_voi/voi/1064目白善信/',filename)
    return rec

voi_1065_folder = R.get('uma_voi/voi/1065大拓太阳神/').path
def get_1065_folder():
    files = os.listdir(voi_1065_folder)
    filename = random.choice(files)
    rec = R.get('uma_voi/voi/1065大拓太阳神/',filename)
    return rec

voi_1066_folder = R.get('uma_voi/voi/1066双涡轮/').path
def get_1066_folder():
    files = os.listdir(voi_1066_folder)
    filename = random.choice(files)
    rec = R.get('uma_voi/voi/1066双涡轮/',filename)
    return rec

voi_1067_folder = R.get('uma_voi/voi/1067里见光钻/').path
def get_1067_folder():
    files = os.listdir(voi_1067_folder)
    filename = random.choice(files)
    rec = R.get('uma_voi/voi/1067里见光钻/',filename)
    return rec

voi_1068_folder = R.get('uma_voi/voi/1068北部玄驹/').path
def get_1068_folder():
    files = os.listdir(voi_1068_folder)
    filename = random.choice(files)
    rec = R.get('uma_voi/voi/1068北部玄驹/',filename)
    return rec

voi_1069_folder = R.get('uma_voi/voi/1069樱花千代王/').path
def get_1069_folder():
    files = os.listdir(voi_1069_folder)
    filename = random.choice(files)
    rec = R.get('uma_voi/voi/1069樱花千代王/',filename)
    return rec

voi_1070_folder = R.get('uma_voi/voi/1070天狼星象征/').path
def get_1070_folder():
    files = os.listdir(voi_1070_folder)
    filename = random.choice(files)
    rec = R.get('uma_voi/voi/1070天狼星象征/',filename)
    return rec

voi_1071_folder = R.get('uma_voi/voi/1071目白阿尔丹/').path
def get_1071_folder():
    files = os.listdir(voi_1071_folder)
    filename = random.choice(files)
    rec = R.get('uma_voi/voi/1071目白阿尔丹/',filename)
    return rec

voi_1072_folder = R.get('uma_voi/voi/1072八重无敌/').path
def get_1072_folder():
    files = os.listdir(voi_1072_folder)
    filename = random.choice(files)
    rec = R.get('uma_voi/voi/1072八重无敌/',filename)
    return rec

voi_1073_folder = R.get('uma_voi/voi/1073鹤丸刚志/').path
def get_1073_folder():
    files = os.listdir(voi_1073_folder)
    filename = random.choice(files)
    rec = R.get('uma_voi/voi/1073鹤丸刚志/',filename)
    return rec

voi_1074_folder = R.get('uma_voi/voi/1074目白光明/').path
def get_1074_folder():
    files = os.listdir(voi_1074_folder)
    filename = random.choice(files)
    rec = R.get('uma_voi/voi/1074目白光明/',filename)
    return rec

voi_1077_folder = R.get('uma_voi/voi/1077成田路/').path
def get_1077_folder():
    files = os.listdir(voi_1077_folder)
    filename = random.choice(files)
    rec = R.get('uma_voi/voi/1077成田路/',filename)
    return rec

voi_1098_folder = R.get('uma_voi/voi/1098小林历奇/').path
def get_1098_folder():
    files = os.listdir(voi_1098_folder)
    filename = random.choice(files)
    rec = R.get('uma_voi/voi/1098小林历奇/',filename)
    return rec

voi_2001_folder = R.get('uma_voi/voi/2001快乐米可/').path
def get_2001_folder():
    files = os.listdir(voi_2001_folder)
    filename = random.choice(files)
    rec = R.get('uma_voi/voi/2001快乐米可/',filename)
    return rec

#亚达随机发送
@sv.on_keyword('亚达','yada','鸭蛋','鸭达')
async def yada(bot,ev) -> MessageSegment:
    file = get_yada_folder()
    try:
        rec = MessageSegment.record(f'file:///{os.path.abspath(file.path)}')
        await bot.send(ev,rec)
    except CQHttpError:
        sv.logger.erro("发送失败喵")

#口八随机发送
@sv.on_keyword('口八','koba')
async def koba(bot,ev) -> MessageSegment:
    file = get_koba_folder()
    try:
        rec = MessageSegment.record(f'file:///{os.path.abspath(file.path)}')
        await bot.send(ev,rec)
    except CQHttpError:
        sv.logger.erro("发送失败喵")

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

#稻荷一1034
@sv.on_fullmatch('牡蛎稻荷一','稻荷一牡蛎')
async def muli(bot,ev) -> MessageSegment:
    muli_33 = R.get('uma_voi/muli/snd_voi_race_103400_8 -.wav')
    try:
        rec = MessageSegment.record(f'file:///{os.path.abspath(muli_33.path)}')
        await bot.send(ev,rec)
    except CQHttpError:
        sv.logger.erro("发送失败喵")

#空中神宫1036
@sv.on_fullmatch('牡蛎神宫','神宫牡蛎')
async def muli(bot,ev) -> MessageSegment:
    muli_36 = R.get('uma_voi/muli/snd_voi_race_103600_8 -.wav')
    try:
        rec = MessageSegment.record(f'file:///{os.path.abspath(muli_36.path)}')
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

#东商变革1044
@sv.on_fullmatch('牡蛎小魔女','小魔女牡蛎')
async def muli(bot,ev) -> MessageSegment:
    muli_39 = R.get('uma_voi/muli/snd_voi_race_104400_8 -.wav')
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

#青竹回忆1053
@sv.on_fullmatch('牡蛎青竹','青竹牡蛎')
async def muli(bot,ev) -> MessageSegment:
    muli_53 = R.get('uma_voi/muli/snd_voi_race_105300_8 -.wav')
    try:
        rec = MessageSegment.record(f'file:///{os.path.abspath(muli_53.path)}')
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

#目白善信1064
@sv.on_fullmatch('牡蛎善信','善信牡蛎')
async def muli(bot,ev) -> MessageSegment:
    muli_39 = R.get('uma_voi/muli/snd_voi_race_106400_8 -.wav')
    try:
        rec = MessageSegment.record(f'file:///{os.path.abspath(muli_39.path)}')
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

#小林历奇1098
@sv.on_fullmatch('牡蛎小林','小林牡蛎')
async def muli(bot,ev) -> MessageSegment:
    muli_98 = R.get('uma_voi/muli/snd_voi_race_109800_8 -.wav')
    try:
        rec = MessageSegment.record(f'file:///{os.path.abspath(muli_98.path)}')
        await bot.send(ev,rec)
    except CQHttpError:
        sv.logger.erro("发送失败喵")

@sv.on_keyword("特别周","特别渣", "特别肥", "特别胖", "特别能吃", "小特", "斯佩酱", "斯佩夏尔维特")
async def voisend(bot,ev) -> MessageSegment:
    try:
        rec = MessageSegment.record(f'file:///{os.path.abspath(get_1001_folder().path)}')
        await bot.send(ev,rec)
    except CQHttpError:
        sv.logger.erro("发送失败喵")

@sv.on_keyword("无声铃鹿","铃鹿","B71","识字卡")
async def voisend(bot,ev) -> MessageSegment:
    try:
        rec = MessageSegment.record(f'file:///{os.path.abspath(get_1002_folder().path)}')
        await bot.send(ev,rec)
    except CQHttpError:
        sv.logger.erro("发送失败喵")

@sv.on_keyword("东海帝王", "帝王", "帝皇", "痛快铁奥", "铁奥", "帝宝",)
async def voisend(bot,ev) -> MessageSegment:
    try:
        rec = MessageSegment.record(f'file:///{os.path.abspath(get_1003_folder().path)}')
        await bot.send(ev,rec)
    except CQHttpError:
        sv.logger.erro("发送失败喵")

@sv.on_keyword("司机", "姥爷", "老阿姨", "丸善斯基", "水司机")
async def voisend(bot,ev) -> MessageSegment:
    try:
        rec = MessageSegment.record(f'file:///{os.path.abspath(get_1004_folder().path)}')
        await bot.send(ev,rec)
    except CQHttpError:
        sv.logger.erro("发送失败喵")

@sv.on_keyword("富士", "奇迹", "富士奇石", "富士奇迹")
async def voisend(bot,ev) -> MessageSegment:
    try:
        rec = MessageSegment.record(f'file:///{os.path.abspath(get_1005_folder().path)}')
        await bot.send(ev,rec)
    except CQHttpError:
        sv.logger.erro("发送失败喵")

@sv.on_keyword("历战王", "帽子", "欧鼓励", "小礼帽", "圣诞帽", "小栗帽", "帽宝")
async def voisend(bot,ev) -> MessageSegment:
    try:
        rec = MessageSegment.record(f'file:///{os.path.abspath(get_1006_folder().path)}')
        await bot.send(ev,rec)
    except CQHttpError:
        sv.logger.erro("发送失败喵")

@sv.on_keyword("皮皮船", "船", "啊船", "阿船", "船宝", "黄金船")
async def voisend(bot,ev) -> MessageSegment:
    try:
        rec = MessageSegment.record(f'file:///{os.path.abspath(get_1007_folder().path)}')
        await bot.send(ev,rec)
    except CQHttpError:
        sv.logger.erro("发送失败喵")

@sv.on_keyword("伏特加")
async def voisend(bot,ev) -> MessageSegment:
    try:
        rec = MessageSegment.record(f'file:///{os.path.abspath(get_1008_folder().path)}')
        await bot.send(ev,rec)
    except CQHttpError:
        sv.logger.erro("发送失败喵")

@sv.on_keyword("大和", "红字白字", "大和赤骥", "斯卡雷特")
async def voisend(bot,ev) -> MessageSegment:
    try:
        rec = MessageSegment.record(f'file:///{os.path.abspath(get_1009_folder().path)}')
        await bot.send(ev,rec)
    except CQHttpError:
        sv.logger.erro("发送失败喵")

@sv.on_keyword("大树", "大树慢车", "小树慢车", "树宝", "大树快车")
async def voisend(bot,ev) -> MessageSegment:
    try:
        rec = MessageSegment.record(f'file:///{os.path.abspath(get_1010_folder().path)}')
        await bot.send(ev,rec)
    except CQHttpError:
        sv.logger.erro("发送失败喵")

@sv.on_keyword("草女士", "那我呢", "今天的小特不是我的对手", "草上飞", "啊草", "阿草")
async def voisend(bot,ev) -> MessageSegment:
    try:
        rec = MessageSegment.record(f'file:///{os.path.abspath(get_1011_folder().path)}')
        await bot.send(ev,rec)
    except CQHttpError:
        sv.logger.erro("发送失败喵")

@sv.on_keyword("亚马逊", "终点牌", "菱亚马逊")
async def voisend(bot,ev) -> MessageSegment:
    try:
        rec = MessageSegment.record(f'file:///{os.path.abspath(get_1012_folder().path)}')
        await bot.send(ev,rec)
    except CQHttpError:
        sv.logger.erro("发送失败喵")

@sv.on_keyword("麦昆","昆宝","目白麦昆")
async def voisend(bot,ev) -> MessageSegment:
    try:
        rec = MessageSegment.record(f'file:///{os.path.abspath(get_1013_folder().path)}')
        await bot.send(ev,rec)
    except CQHttpError:
        sv.logger.erro("发送失败喵")

@sv.on_keyword("神鹰","诶路")
async def voisend(bot,ev) -> MessageSegment:
    try:
        rec = MessageSegment.record(f'file:///{os.path.abspath(get_1014_folder().path)}')
        await bot.send(ev,rec)
    except CQHttpError:
        sv.logger.erro("发送失败喵")

@sv.on_keyword("好歌剧")
async def voisend(bot,ev) -> MessageSegment:
    try:
        rec = MessageSegment.record(f'file:///{os.path.abspath(get_1015_folder().path)}')
        await bot.send(ev,rec)
    except CQHttpError:
        sv.logger.erro("发送失败喵")

@sv.on_keyword("成田白仁","白仁")
async def voisend(bot,ev) -> MessageSegment:
    try:
        rec = MessageSegment.record(f'file:///{os.path.abspath(get_1016_folder().path)}')
        await bot.send(ev,rec)
    except CQHttpError:
        sv.logger.erro("发送失败喵")

@sv.on_keyword("鲁道夫", "豆腐", "会长", "露娜", "鲁道夫象征")
async def voisend(bot,ev) -> MessageSegment:
    try:
        rec = MessageSegment.record(f'file:///{os.path.abspath(get_1017_folder().path)}')
        await bot.send(ev,rec)
    except CQHttpError:
        sv.logger.erro("发送失败喵")

@sv.on_keyword("女帝", "副会长", "气槽")
async def voisend(bot,ev) -> MessageSegment:
    try:
        rec = MessageSegment.record(f'file:///{os.path.abspath(get_1018_folder().path)}')
        await bot.send(ev,rec)
    except CQHttpError:
        sv.logger.erro("发送失败喵")

@sv.on_keyword("数码", "dd", "爱丽数码", "尊", "尊死")
async def voisend(bot,ev) -> MessageSegment:
    try:
        rec = MessageSegment.record(f'file:///{os.path.abspath(get_1019_folder().path)}')
        await bot.send(ev,rec)
    except CQHttpError:
        sv.logger.erro("发送失败喵")

@sv.on_keyword("星云", "sky", "星宝", "星云天空")
async def voisend(bot,ev) -> MessageSegment:
    try:
        rec = MessageSegment.record(f'file:///{os.path.abspath(get_1020_folder().path)}')
        await bot.send(ev,rec)
    except CQHttpError:
        sv.logger.erro("发送失败喵")

@sv.on_keyword("tama", "玉藻","tm", "玉藻十字", "藻子哥")
async def voisend(bot,ev) -> MessageSegment:
    try:
        rec = MessageSegment.record(f'file:///{os.path.abspath(get_1021_folder().path)}')
        await bot.send(ev,rec)
    except CQHttpError:
        sv.logger.erro("发送失败喵")

@sv.on_keyword("美妙", "姿势","美妙姿势", "美味芝士")
async def voisend(bot,ev) -> MessageSegment:
    try:
        rec = MessageSegment.record(f'file:///{os.path.abspath(get_1022_folder().path)}')
        await bot.send(ev,rec)
    except CQHttpError:
        sv.logger.erro("发送失败喵")

@sv.on_keyword("大头","琵琶晨光")
async def voisend(bot,ev) -> MessageSegment:
    try:
        rec = MessageSegment.record(f'file:///{os.path.abspath(get_1023_folder().path)}')
        await bot.send(ev,rec)
    except CQHttpError:
        sv.logger.erro("发送失败喵")

@sv.on_keyword("玛雅", "maya", "小可爱", "玛雅诺冲锋枪", "重宝", "炮宝", "重炮")
async def voisend(bot,ev) -> MessageSegment:
    try:
        rec = MessageSegment.record(f'file:///{os.path.abspath(get_1024_folder().path)}')
        await bot.send(ev,rec)
    except CQHttpError:
        sv.logger.erro("发送失败喵")

@sv.on_keyword("茶座", "插座", "小仓唯", "曼哈顿咖啡", "xcw", "曼城茶座")
async def voisend(bot,ev) -> MessageSegment:
    try:
        rec = MessageSegment.record(f'file:///{os.path.abspath(get_1025_folder().path)}')
        await bot.send(ev,rec)
    except CQHttpError:
        sv.logger.erro("发送失败喵")

@sv.on_keyword("波旁", "赛博朋马", "亲啵", "情勃", "美浦波旁", "布鲁泵")
async def voisend(bot,ev) -> MessageSegment:
    try:
        rec = MessageSegment.record(f'file:///{os.path.abspath(get_1026_folder().path)}')
        await bot.send(ev,rec)
    except CQHttpError:
        sv.logger.erro("发送失败喵")

@sv.on_keyword("莱恩", "赖恩", "雷恩", "目白赖恩")
async def voisend(bot,ev) -> MessageSegment:
    try:
        rec = MessageSegment.record(f'file:///{os.path.abspath(get_1027_folder().path)}')
        await bot.send(ev,rec)
    except CQHttpError:
        sv.logger.erro("发送失败喵")

@sv.on_keyword("凌署", "凌曙", "菱署", "菱曙")
async def voisend(bot,ev) -> MessageSegment:
    try:
        rec = MessageSegment.record(f'file:///{os.path.abspath(get_1028_folder().path)}')
        await bot.send(ev,rec)
    except CQHttpError:
        sv.logger.erro("发送失败喵")

@sv.on_keyword("雪之美人")
async def voisend(bot,ev) -> MessageSegment:
    try:
        rec = MessageSegment.record(f'file:///{os.path.abspath(get_1029_folder().path)}')
        await bot.send(ev,rec)
    except CQHttpError:
        sv.logger.erro("发送失败喵")

@sv.on_keyword("大米洗澡", "小祖宗","米宝", "米浴")
async def voisend(bot,ev) -> MessageSegment:
    try:
        rec = MessageSegment.record(f'file:///{os.path.abspath(get_1030_folder().path)}')
        await bot.send(ev,rec)
    except CQHttpError:
        sv.logger.erro("发送失败喵")

@sv.on_keyword("风神", "艾尼斯风神")
async def voisend(bot,ev) -> MessageSegment:
    try:
        rec = MessageSegment.record(f'file:///{os.path.abspath(get_1031_folder().path)}')
        await bot.send(ev,rec)
    except CQHttpError:
        sv.logger.erro("发送失败喵")

@sv.on_keyword("速子", "爱丽速子")
async def voisend(bot,ev) -> MessageSegment:
    try:
        rec = MessageSegment.record(f'file:///{os.path.abspath(get_1032_folder().path)}')
        await bot.send(ev,rec)
    except CQHttpError:
        sv.logger.erro("发送失败喵")

@sv.on_keyword("织姬", "爱慕织姬")
async def voisend(bot,ev) -> MessageSegment:
    try:
        rec = MessageSegment.record(f'file:///{os.path.abspath(get_1033_folder().path)}')
        await bot.send(ev,rec)
    except CQHttpError:
        sv.logger.erro("发送失败喵")

@sv.on_keyword("稻荷一")
async def voisend(bot,ev) -> MessageSegment:
    try:
        rec = MessageSegment.record(f'file:///{os.path.abspath(get_1034_folder().path)}')
        await bot.send(ev,rec)
    except CQHttpError:
        sv.logger.erro("发送失败喵")

@sv.on_keyword("奖券", "胜利奖券", "小哭包")
async def voisend(bot,ev) -> MessageSegment:
    try:
        rec = MessageSegment.record(f'file:///{os.path.abspath(get_1035_folder().path)}')
        await bot.send(ev,rec)
    except CQHttpError:
        sv.logger.erro("发送失败喵")

@sv.on_keyword("神宫", "空中神宫")
async def voisend(bot,ev) -> MessageSegment:
    try:
        rec = MessageSegment.record(f'file:///{os.path.abspath(get_1036_folder().path)}')
        await bot.send(ev,rec)
    except CQHttpError:
        sv.logger.erro("发送失败喵")

@sv.on_keyword("荣进", "德国女仆", "阿荣", "啊荣", "荣耀闪进")
async def voisend(bot,ev) -> MessageSegment:
    try:
        rec = MessageSegment.record(f'file:///{os.path.abspath(get_1037_folder().path)}')
        await bot.send(ev,rec)
    except CQHttpError:
        sv.logger.erro("发送失败喵")

@sv.on_keyword("可怜酱", "可怜", "华恋", "真机灵", "真机伶", "怜宝")
async def voisend(bot,ev) -> MessageSegment:
    try:
        rec = MessageSegment.record(f'file:///{os.path.abspath(get_1038_folder().path)}')
        await bot.send(ev,rec)
    except CQHttpError:
        sv.logger.erro("发送失败喵")

@sv.on_keyword("川上", "川上公主")
async def voisend(bot,ev) -> MessageSegment:
    try:
        rec = MessageSegment.record(f'file:///{os.path.abspath(get_1039_folder().path)}')
        await bot.send(ev,rec)
    except CQHttpError:
        sv.logger.erro("发送失败喵")

@sv.on_keyword("黄金城市", "黄金城")
async def voisend(bot,ev) -> MessageSegment:
    try:
        rec = MessageSegment.record(f'file:///{os.path.abspath(get_1040_folder().path)}')
        await bot.send(ev,rec)
    except CQHttpError:
        sv.logger.erro("发送失败喵")

@sv.on_keyword("进王", "爆进", "暴进", "爆进王", "暴进王", "樱花暴进王", "樱花进王")
async def voisend(bot,ev) -> MessageSegment:
    try:
        rec = MessageSegment.record(f'file:///{os.path.abspath(get_1041_folder().path)}')
        await bot.send(ev,rec)
    except CQHttpError:
        sv.logger.erro("发送失败喵")

@sv.on_keyword("采珠")
async def voisend(bot,ev) -> MessageSegment:
    try:
        rec = MessageSegment.record(f'file:///{os.path.abspath(get_1042_folder().path)}')
        await bot.send(ev,rec)
    except CQHttpError:
        sv.logger.erro("发送失败喵")

@sv.on_keyword("新光风", "新风光")
async def voisend(bot,ev) -> MessageSegment:
    try:
        rec = MessageSegment.record(f'file:///{os.path.abspath(get_1043_folder().path)}')
        await bot.send(ev,rec)
    except CQHttpError:
        sv.logger.erro("发送失败喵")

@sv.on_keyword("东尚", "东商", "魔女", "小魔女", "东商变革", "小魔吕", )
async def voisend(bot,ev) -> MessageSegment:
    try:
        rec = MessageSegment.record(f'file:///{os.path.abspath(get_1044_folder().path)}')
        await bot.send(ev,rec)
    except CQHttpError:
        sv.logger.erro("发送失败喵")

@sv.on_keyword("小海湾", "海湾", "大海湾", "超级大海湾", "海湾妈妈", "超级小溪", "超级小海湾", "妈咪")
async def voisend(bot,ev) -> MessageSegment:
    try:
        rec = MessageSegment.record(f'file:///{os.path.abspath(get_1045_folder().path)}')
        await bot.send(ev,rec)
    except CQHttpError:
        sv.logger.erro("发送失败喵")

@sv.on_keyword("飞鹰", "飞鹰子", "寄", "寄寄子", "醒目飞鹰", "寄！")
async def voisend(bot,ev) -> MessageSegment:
    try:
        rec = MessageSegment.record(f'file:///{os.path.abspath(get_1046_folder().path)}')
        await bot.send(ev,rec)
    except CQHttpError:
        sv.logger.erro("发送失败喵")

@sv.on_keyword("荒漠", "荒漠英雄")
async def voisend(bot,ev) -> MessageSegment:
    try:
        rec = MessageSegment.record(f'file:///{os.path.abspath(get_1047_folder().path)}')
        await bot.send(ev,rec)
    except CQHttpError:
        sv.logger.erro("发送失败喵")

@sv.on_keyword("辣妹", "佐敦", "东瀛佐敦")
async def voisend(bot,ev) -> MessageSegment:
    try:
        rec = MessageSegment.record(f'file:///{os.path.abspath(get_1048_folder().path)}')
        await bot.send(ev,rec)
    except CQHttpError:
        sv.logger.erro("发送失败喵")

@sv.on_keyword("中山庆典")
async def voisend(bot,ev) -> MessageSegment:
    try:
        rec = MessageSegment.record(f'file:///{os.path.abspath(get_1049_folder().path)}')
        await bot.send(ev,rec)
    except CQHttpError:
        sv.logger.erro("发送失败喵")

@sv.on_keyword("大进", "成田小进", "小进", "迫影人", "迫影", "成田大进")
async def voisend(bot,ev) -> MessageSegment:
    try:
        rec = MessageSegment.record(f'file:///{os.path.abspath(get_1050_folder().path)}')
        await bot.send(ev,rec)
    except CQHttpError:
        sv.logger.erro("发送失败喵")

@sv.on_keyword("西野花")
async def voisend(bot,ev) -> MessageSegment:
    try:
        rec = MessageSegment.record(f'file:///{os.path.abspath(get_1051_folder().path)}')
        await bot.send(ev,rec)
    except CQHttpError:
        sv.logger.erro("发送失败喵")

@sv.on_keyword("乌拉拉", "春丽", "urara")
async def voisend(bot,ev) -> MessageSegment:
    try:
        rec = MessageSegment.record(f'file:///{os.path.abspath(get_1052_folder().path)}')
        await bot.send(ev,rec)
    except CQHttpError:
        sv.logger.erro("发送失败喵")

@sv.on_keyword("青竹回忆")
async def voisend(bot,ev) -> MessageSegment:
    try:
        rec = MessageSegment.record(f'file:///{os.path.abspath(get_1053_folder().path)}')
        await bot.send(ev,rec)
    except CQHttpError:
        sv.logger.erro("发送失败喵")

@sv.on_keyword("周日宁静", "周日")
async def voisend(bot,ev) -> MessageSegment:
    try:
        rec = MessageSegment.record(f'file:///{os.path.abspath(get_1054_folder().path)}')
        await bot.send(ev,rec)
    except CQHttpError:
        sv.logger.erro("发送失败喵")

@sv.on_keyword("微光", "飞驹", "微光飞驹")
async def voisend(bot,ev) -> MessageSegment:
    try:
        rec = MessageSegment.record(f'file:///{os.path.abspath(get_1055_folder().path)}')
        await bot.send(ev,rec)
    except CQHttpError:
        sv.logger.erro("发送失败喵")

@sv.on_keyword("福来", "神棍", "占卜师", "半仙", "待兼福来")
async def voisend(bot,ev) -> MessageSegment:
    try:
        rec = MessageSegment.record(f'file:///{os.path.abspath(get_1056_folder().path)}')
        await bot.send(ev,rec)
    except CQHttpError:
        sv.logger.erro("发送失败喵")

@sv.on_keyword('千明代表', "cb")
async def voisend(bot,ev) -> MessageSegment:
    try:
        rec = MessageSegment.record(f'file:///{os.path.abspath(get_1057_folder().path)}')
        await bot.send(ev,rec)
    except CQHttpError:
        sv.logger.erro("发送失败喵")

@sv.on_keyword("怒涛", "户仁", "名将怒涛")
async def voisend(bot,ev) -> MessageSegment:
    try:
        rec = MessageSegment.record(f'file:///{os.path.abspath(get_1058_folder().path)}')
        await bot.send(ev,rec)
    except CQHttpError:
        sv.logger.erro("发送失败喵")

@sv.on_keyword("多伯", "目白多伯", "多勃", "多啵")
async def voisend(bot,ev) -> MessageSegment:
    try:
        rec = MessageSegment.record(f'file:///{os.path.abspath(get_1059_folder().path)}')
        await bot.send(ev,rec)
    except CQHttpError:
        sv.logger.erro("发送失败喵")

@sv.on_keyword("好天资", "素质女士", "内恰", "内恰女士", "三着", "三着女士", "三角之外", "八方人", "素质极好", "今天也是开心的一天", "优秀素质", "好素质")
async def voisend(bot,ev) -> MessageSegment:
    try:
        rec = MessageSegment.record(f'file:///{os.path.abspath(get_1060_folder().path)}')
        await bot.send(ev,rec)
    except CQHttpError:
        sv.logger.erro("发送失败喵")

@sv.on_keyword("光辉", "帝王光环", "圣王光环", "圣王光辉", "king", "光环", "halo", "环环", "王环环", "帝王光辉")
async def voisend(bot,ev) -> MessageSegment:
    try:
        rec = MessageSegment.record(f'file:///{os.path.abspath(get_1061_folder().path)}')
        await bot.send(ev,rec)
    except CQHttpError:
        sv.logger.erro("发送失败喵")

@sv.on_keyword("诗宝", "AAO", "待兼诗歌剧", "咚啪嗯")
async def voisend(bot,ev) -> MessageSegment:
    try:
        rec = MessageSegment.record(f'file:///{os.path.abspath(get_1062_folder().path)}')
        await bot.send(ev,rec)
    except CQHttpError:
        sv.logger.erro("发送失败喵")

@sv.on_keyword('生野狄杜斯')
async def voisend(bot,ev) -> MessageSegment:
    try:
        rec = MessageSegment.record(f'file:///{os.path.abspath(get_1063_folder().path)}')
        await bot.send(ev,rec)
    except CQHttpError:
        sv.logger.erro("发送失败喵")

@sv.on_keyword('目白善信',"善信")
async def voisend(bot,ev) -> MessageSegment:
    try:
        rec = MessageSegment.record(f'file:///{os.path.abspath(get_1064_folder().path)}')
        await bot.send(ev,rec)
    except CQHttpError:
        sv.logger.erro("发送失败喵")

@sv.on_keyword('大拓太阳神',"太阳神")
async def voisend(bot,ev) -> MessageSegment:
    try:
        rec = MessageSegment.record(f'file:///{os.path.abspath(get_1065_folder().path)}')
        await bot.send(ev,rec)
    except CQHttpError:
        sv.logger.erro("发送失败喵")

@sv.on_keyword('双涡轮',"哒宝","双宝","挞宝")
async def voisend(bot,ev) -> MessageSegment:
    try:
        rec = MessageSegment.record(f'file:///{os.path.abspath(get_1066_folder().path)}')
        await bot.send(ev,rec)
    except CQHttpError:
        sv.logger.erro("发送失败喵")

@sv.on_keyword("光钻", "钻哥", "里见光钻", "钻宝")
async def voisend(bot,ev) -> MessageSegment:
    try:
        rec = MessageSegment.record(f'file:///{os.path.abspath(get_1067_folder().path)}')
        await bot.send(ev,rec)
    except CQHttpError:
        sv.logger.erro("发送失败喵")

@sv.on_keyword("北黑", "侑开始了", "悸动战士", "harikite", "小北", "北嗨", "北部玄驹")
async def voisend(bot,ev) -> MessageSegment:
    try:
        rec = MessageSegment.record(f'file:///{os.path.abspath(get_1068_folder().path)}')
        await bot.send(ev,rec)
    except CQHttpError:
        sv.logger.erro("发送失败喵")

@sv.on_keyword("千代王", "樱花千代王", "小千代")
async def voisend(bot,ev) -> MessageSegment:
    try:
        rec = MessageSegment.record(f'file:///{os.path.abspath(get_1069_folder().path)}')
        await bot.send(ev,rec)
    except CQHttpError:
        sv.logger.erro("发送失败喵")

@sv.on_keyword("天狼星象征")
async def voisend(bot,ev) -> MessageSegment:
    try:
        rec = MessageSegment.record(f'file:///{os.path.abspath(get_1070_folder().path)}')
        await bot.send(ev,rec)
    except CQHttpError:
        sv.logger.erro("发送失败喵")

@sv.on_keyword("阿尔丹", "中国媳妇", "目白阿尔丹", "中国媳妇儿")
async def voisend(bot,ev) -> MessageSegment:
    try:
        rec = MessageSegment.record(f'file:///{os.path.abspath(get_1071_folder().path)}')
        await bot.send(ev,rec)
    except CQHttpError:
        sv.logger.erro("发送失败喵")

@sv.on_keyword("八重", "八重无敌")
async def voisend(bot,ev) -> MessageSegment:
    try:
        rec = MessageSegment.record(f'file:///{os.path.abspath(get_1072_folder().path)}')
        await bot.send(ev,rec)
    except CQHttpError:
        sv.logger.erro("发送失败喵")

@sv.on_keyword("鹤丸刚志")
async def voisend(bot,ev) -> MessageSegment:
    try:
        rec = MessageSegment.record(f'file:///{os.path.abspath(get_1073_folder().path)}')
        await bot.send(ev,rec)
    except CQHttpError:
        sv.logger.erro("发送失败喵")

@sv.on_keyword("光明", "目白光明")
async def voisend(bot,ev) -> MessageSegment:
    try:
        rec = MessageSegment.record(f'file:///{os.path.abspath(get_1074_folder().path)}')
        await bot.send(ev,rec)
    except CQHttpError:
        sv.logger.erro("发送失败喵")

@sv.on_keyword("路哥", "成田路")
async def voisend(bot,ev) -> MessageSegment:
    try:
        rec = MessageSegment.record(f'file:///{os.path.abspath(get_1077_folder().path)}')
        await bot.send(ev,rec)
    except CQHttpError:
        sv.logger.erro("发送失败喵")

@sv.on_keyword("小林", "历奇")
async def voisend(bot,ev) -> MessageSegment:
    try:
        rec = MessageSegment.record(f'file:///{os.path.abspath(get_1098_folder().path)}')
        await bot.send(ev,rec)
    except CQHttpError:
        sv.logger.erro("发送失败喵")       

@sv.on_keyword("米可", "快乐温顺", "快乐米可", "happy milk", "嗨皮米可")
async def voisend(bot,ev) -> MessageSegment:
    try:
        rec = MessageSegment.record(f'file:///{os.path.abspath(get_2001_folder().path)}')
        await bot.send(ev,rec)
    except CQHttpError:
        sv.logger.erro("发送失败喵")
        