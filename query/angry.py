from hoshino import R, Service, priv, util
from hoshino.util import FreqLimiter, DailyNumberLimiter

from .. import chara
from . import sv

correction = [
    ("冰咒龙", 0.83), 
    ("雾瘴尸套龙", 0.95), 
    ("麒麟", 0.90), 
    ("钢龙", 0.90), 
    ("炎王龙", 0.83), 
    ("炎妃龙", 0.83), 
    ("溟波龙", 1.10), 
    ("惶怒恐暴龙", 0.83), 
    ("红莲爆鳞龙", 0.90), 
    ("天地煌啼龙", 0.95), 
    ("歼世灭尽龙", 1.00), 
    ("猛爆碎龙", 0.95), 
    ("狱狼龙", 1.00), 
    ("金狮子", 1.00), 
    ("激昂金狮子", 1.00), 
    ("金火龙", 0.83), 
    ("银火龙", 0.83), 
    ("爆锤龙", 0.83), 
    ("雷颚龙", 1.00), 
    ("雷狼龙", 1.00), 
    ("迅龙", 0.90), 
    ("熔岩龙", 1.10), 
    ("惨爪龙", 1.00), 
    ("凶爪龙", 1.00), 
    ("角龙", 0.90), 
    ("黑角龙", 0.90), 
    ("碎龙", 1.05), 
    ("冰牙龙", 0.95), 
    ("樱火龙", 0.90), 
    ("苍火龙", 0.90), 
    ("火龙", 0.90), 
    ("风漂龙", 0.90), 
    ("霜翼风漂龙", 0.90), 
    ("轰龙", 0.90), 
    ("黑轰龙", 0.90), 
    ("黑狼鸟", 0.90), 
    ("战痕黑狼鸟", 0.90), 
    ("斩龙", 1.00), 
    ("硫斩龙", 1.00), 
]
correction = dict(correction)

@sv.on_suffix("怒后补正")
async def angry_correction(bot, ev):
    name = ev.message.extract_plain_text().strip()
    
    id_ = chara.name2id(name)
    c = chara.fromid(id_)
    
    msg = ''
    try:
        msg += f'{c.name}的怒后防御补正为{correction[c.name]}'
    except:
        msg += '呜呜，出错了，可能数据库里没有它的数据呢'
    
    await bot.send(ev, msg, at_sender = True)