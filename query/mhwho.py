from hoshino.typing import CQEvent, MessageSegment
from hoshino.util import FreqLimiter

from .. import chara
from . import sv

lmt = FreqLimiter(5)

@sv.on_suffix('图标')
async def mhwho(bot, ev: CQEvent):
    uid = ev.user_id
    if not lmt.check(uid):
        await bot.send(ev, f'mh花名册冷却中(剩余 {int(lmt.left_time(uid)) + 1}秒)', at_sender=True)
        return
    lmt.start_cd(uid)
    
    name = ev.message.extract_plain_text().strip()
    
    sp = 0
    if "历战王" in name:
        sp = 2
        name = name.strip("历战王")
        
    elif "历战" in name:
        sp = 1
        name = name.strip("历战")
    #sp用来标志需要图标是否历战
    print(sp)
    if not name:
        await bot.send(ev, '？')
        return  
    id_ = chara.name2id(name)
    c = chara.fromid(id_)
    
    msg = ''
    msg += f'{c.name} '

    c.selfadd(sp * 1000)
    msg += f'{c.icon.cqcode}'
    msg += '没有图片就是没资源，有了记得给猫猫一份'
    
    await bot.send(ev, msg, at_sender=True)
