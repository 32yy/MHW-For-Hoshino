import random

from hoshino import R, Service, priv, util
from hoshino.util import FreqLimiter, DailyNumberLimiter

from .. import chara
from . import sv

_max = 1
_nlmt = DailyNumberLimiter(_max)
EXCEED_NOTICE = "渣男，你今天已经抽过老婆啦！"

@sv.on_fullmatch('抽老婆')
async def random_waifu(bot, ev):
    uid = ev['user_id']
    if priv.check_priv(ev, priv.SUPERUSER):
        await bot.send(ev, "讨厌...猫猫就是达令的老婆啦！", at_sender=True)
        return
    if not _nlmt.check(uid):
        if not priv.check_priv(ev, priv.SUPERUSER):
            await bot.send(ev, EXCEED_NOTICE, at_sender=True)
            return
    _nlmt.increase(uid)
    
    monster = random.randint(3201,3275)
    while monster == 3211 or monster == 3244 or monster == 3256 or monster == 3262:
        monster = random.randint(3201,3275)
    #这四个没内容，写data时忘记怎么数数了
    
    name = ev['sender']['nickname']
    
    c1 = chara.fromid(monster)

    msg = ''
    msg += f'{c1.icon.cqcode}{name}さんがmhwで結婚するであろうヒロインは、\n【{c1.name}】です！'

    await bot.send(ev, msg)

    
    
    