### 大人気PC海戦ゲーム「World of Warships」の検索ができるdiscordのbotです。
##### discord.pyとWargaming社の公式APIを使用しています。

※ WoWS Legendには対応していません。

***

### botの使い方

* playerコマンド `-player, -p`
プレイヤーの戦績を検索します。

```
-player [プレイヤー名]
-p [プレイヤー名]
```

他にも、艦艇情報の装甲・隠蔽値を表示するコマンドを実装予定です。

***

### config

`conf/config.yaml`内の値を変更することによって、細微な設定を変更することができます。

* コマンドprefix
`COMMAND_PREFIX: '-'`

初期状態では、`COMMAND_PREFIX`には`'-'`が設定されており、`-player`などでdiscord botに呼びかけが可能です。
こちらを任意の記号等に置き換えることで、コマンド前置詞の変更が可能です。

* Wargaming APIのリージョン設定
`REGION: 'asia' # ru, eu, na, asia`

初期状態では、Wargamingのasiaリージョンにアクセスを行います。
こちらをコメントアウトされているリージョン記入例のいずれかに置き換えることで、アクセスするAPIのリージョンの変更が可能です。

* タイムゾーン設定
`TIMEZONE_HOURS: 9`

初期状態では、UTC+0900を設定しています。
`conf.config.py`内でタイムゾーンをconf内のdictに設定し、`util/util.py`内のメソッド`timestamp_format`で使用しています。
`TIMEZONE_STR`も同様のメソッド内で文字列結合に使用しています。

* **(WIP)** 言語設定
`LANGUAGE: 'ja'`

読み込むmessage.yamlの変更を可能とする予定です。
現在は日本語のみの対応で、`util/message.ja.yaml`を読み込むようにしています。

***

### auth.yamlについて

ローカル環境等で実行する場合は、discordトークンとWargaming API トークンは、`conf/auth.yaml`にセットしてください。
`conf/auth_example.yaml`をコピーして設置できます。

heroku等にデプロイする場合は、auth.yamlを使用せずに、直接環境変数にそれらをセットしてください。

