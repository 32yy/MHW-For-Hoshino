from hoshino import Service

sv_help = '''
mhw相关基本聊天
[猫猫今天打什么] 随机给你个题材玩
[抽老婆] 随机抽个老婆
'''.strip()

sv = Service('mhw-groupchat', help_=sv_help, bundle='mhw')

from .chat import *
from .waifu import *
from .dasha import *
