from hoshino import Service

sv_help = '''
这是mh的查询help
'''.strip()

sv = Service('mhw-query', help_=sv_help, bundle='mhw查询')

from .mhwho import *
from .dasha import *