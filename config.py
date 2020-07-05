"""
config.yamlを使用して、configをセット
"""
import yaml
from os import path

class _config:

    def __init__(self):
        if(path.exists("config.yaml")):
            with open('config.yaml', 'r') as config_yaml:
                config = yaml.load(config_yaml, Loader=yaml.SafeLoader)
                region = config['REGION']

                for c in config:
                    if(not c.endswith('WOWS_API_URL')): # API URL以外
                        self.__dict__[c] = config[c]

                    else: # Wows APIのURLはRegion別に加工しておく

                        if(region is not 'na'):
                            region_str = '.' + region
                        else:
                            region_str = '.com'
                        self.__dict__[c] = config[c].format(region_str = region_str)


    class ConstError(TypeError):
        pass

import sys
sys.modules[__name__]=_config()