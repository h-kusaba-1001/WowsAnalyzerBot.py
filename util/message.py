"""
message.yamlを使用して、messageをセット
import configの後に読み込む
"""
import yaml
from os import path
import conf.config as config

class _message:

    def __init__(self):
        # config.LANGUAGEからyamlファイル名を作成
        yaml_path = 'util/message.{lang}.yaml'.format(lang=config.LANGUAGE)

        if(path.exists(yaml_path)):
            with open(yaml_path, 'r', encoding="utf-8_sig") as message_yaml:
                message = yaml.load(message_yaml, Loader=yaml.SafeLoader)

                for m in message:
                    self.__dict__[m] = message[m]

    class ConstError(TypeError):
        pass

import sys
sys.modules[__name__]=_message()