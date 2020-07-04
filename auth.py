"""
トークン系の値をauth.yamlから取得する
本番環境(heroku) で環境変数が設定し、auth.yamlを使用しない
"""
import yaml
from os import path, environ

class _auth:

    def __init__(self):
        # auth.yamlから認証情報を読み込む (テスト環境の場合)
        if(path.exists("auth.yaml")):
            with open('auth.yaml', 'r') as auth_yaml:
                auth = yaml.load(auth_yaml, Loader=yaml.SafeLoader)

                for a in auth:
                    # 本番環境でない場合は、auth.yamlのものをセット
                    self.__dict__[a] = auth[a]
                auth_yaml.close()

        else: # 本番環境の場合
            AUTH_VALIABLE_NAMES = [
                'DISCORD_TOKEN',
                'WARGAMING_APP_TOKEN'
            ]
            for A in AUTH_VALIABLE_NAMES:
                if(a in environ): # 環境変数にある場合
                    # 本番環境の環境変数をセット
                    self.__dict__[a] = environ[a]

    class ConstError(TypeError):
        pass

import sys
sys.modules[__name__]=_auth()