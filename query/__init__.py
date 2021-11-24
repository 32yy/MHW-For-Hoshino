from hoshino import Service

sv_help = '''
mhw相关查询
[xxx图标]怪物/武器图标
[xxx怒后补正]怪物怒后补正
'''.strip()

sv = Service('mhw-query', help_=sv_help, bundle='mhw')

from .mhwho import *
from .angry import *