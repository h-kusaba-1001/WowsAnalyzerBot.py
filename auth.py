"""
トークン系の値をauth.yamlから取得する
本番環境(heroku) で環境変数が設定されている場合は、そちらを取得する
"""
import yaml
from os import path, environ

class _auth:

    def __init__(self):
        if(path.exists("auth.yaml")):
            with open('auth.yaml', 'r') as auth_yaml:
                auth = yaml.load(auth_yaml, Loader=yaml.SafeLoader)

                for a in auth:
                    if(a in environ):
                        # 本番環境の環境変数をセット
                        self.__dict__[a] = environ[a]
                    else:
                        # 本番環境でない場合は、auth.yamlのものをセット
                        self.__dict__[a] = auth[a]
                auth_yaml.close()

    class ConstError(TypeError):
        pass

import sys
sys.modules[__name__]=_auth()