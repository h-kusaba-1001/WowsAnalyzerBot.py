"""
config.yamlを使用して、configをセット
"""
import yaml
from os import path
import datetime

class _config:

    def __init__(self):
        with open('conf/config.yaml', 'r', encoding="utf-8_sig") as config_yaml:
            config = yaml.load(config_yaml, Loader=yaml.SafeLoader)
            region = config['REGION']

            for c in config:
                if(not c.endswith('WOWS_API_URL')): # API URL以外
                    self.__dict__[c] = config[c]

                    if(c == 'TIMEZONE_HOURS'): # タイムゾーンを設定し、どこでも呼び出せるようにする
                        self.__dict__['TIME_ZONE_OBJECT'] = datetime.timezone(datetime.timedelta(hours=config[c]))

                else: # Wows APIのURLはRegion別に加工しておく

                    if(region != 'na'):
                        region_str = '.' + region
                    else:
                        region_str = '.com'
                    self.__dict__[c] = config[c].format(region_str = region_str)


    class ConstError(TypeError):
        pass

import sys
sys.modules[__name__]=_config()