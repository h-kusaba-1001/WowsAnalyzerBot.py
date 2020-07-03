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
                for c in config:
                    self.__dict__[c] = config[c]

    class ConstError(TypeError):
        pass

import sys
sys.modules[__name__]=_config()