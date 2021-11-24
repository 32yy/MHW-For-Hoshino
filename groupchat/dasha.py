from hoshino.typing import CQEvent, MessageSegment
from hoshino.util import FreqLimiter

from .. import chara
from . import sv
import random

@sv.on_fullmatch('今天打什么')
async def dasha(bot, ev: CQEvent):
    
    monster = random.randint(3201,3275)
    while monster == 3211 or monster == 3244 or monster == 3256 or monster == 3262:
        monster = random.randint(3201,3275)
    #这四个没内容，写data时忘记怎么数数了
    weapon = random.randint(3286,3299)
    
    c1 = chara.fromid(monster)
    c2 = chara.fromid(weapon)
    
    msg = ''
    msg += f'{c1.icon.cqcode} {c2.icon.cqcode} {c2.name} {c1.name}'
    ta = random.random()
    if ta > 0.5:
        msg += ' TA'
    msg += ' 打完记得艾特猫猫查看完成情况！'
    await bot.send(ev, msg, at_sender=True)
