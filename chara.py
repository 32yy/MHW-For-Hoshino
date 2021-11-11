import importlib
from io import BytesIO

import pygtrie
import requests
from fuzzywuzzy import fuzz, process
from PIL import Image

import hoshino
from hoshino import R, log, sucmd, util
from hoshino.typing import CommandSession

from . import _mhw_data

logger = log.new_logger('chara', hoshino.config.DEBUG)
UNKNOWN = 1000

try:
    unknown_chara_icon = R.img(f'mhw/icon/icon_unit_1000.png').open()
except Exception as e:
    logger.exception(e)


class Roster:

    def __init__(self):
        self._roster = pygtrie.CharTrie()
        self.update()
        
    
    def update(self):
        importlib.reload(_mhw_data)
        self._roster.clear()
        for idx, names in _mhw_data.CHARA_NAME.items():
            for n in names:
                n = util.normalize_str(n)
                if n not in self._roster:
                    self._roster[n] = idx
                else:
                    logger.warning(f'priconne.chara.Roster: 出现重名{n}于id{idx}与id{self._roster[n]}')
        self._all_name_list = self._roster.keys()
    
    
    def get_id(self, name):
        name = util.normalize_str(name)
        return self._roster[name] if name in self._roster else UNKNOWN


    def parse_team(self, namestr):
        """@return: List[ids], unknown_namestr"""
        namestr = util.normalize_str(namestr)
        team = []
        unknown = []
        while namestr:
            item = self._roster.longest_prefix(namestr)
            if not item:
                unknown.append(namestr[0])
                namestr = namestr[1:].lstrip()
            else:
                team.append(item.value)
                namestr = namestr[len(item.key):].lstrip()
        return team, ''.join(unknown)


roster = Roster()

def name2id(name):
    return roster.get_id(name)

def fromid(id_):
    return Chara(id_)

def fromname(name):
    id_ = name2id(name)
    return Chara(id_)


class Chara:

    def __init__(self, id_):
        self.id = id_
        
    def selfadd(self, num):
        self.id += num

    @property
    def name(self):
        return _mhw_data.CHARA_NAME[self.id][0] if self.id in _mhw_data.CHARA_NAME else _mhw_data.CHARA_NAME[UNKNOWN][0]

    @property
    def icon(self):
        res = R.img(f'mhw/icon/icon_unit_{self.id}.png')
        return res