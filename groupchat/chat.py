import random

from . import sv
from hoshino import R, Service, priv, util

@sv.on_rex('刷片')
async def ans_sp(bot, ev):
    if random.random() < 0.3:
        await bot.send(ev, '刷片死路一条')
        
