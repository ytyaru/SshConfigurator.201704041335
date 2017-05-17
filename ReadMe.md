# このソフトウェアについて

PythonでSSHのconfigファイルからHost情報を読み取る。

# 開発環境

* Linux Mint 17.3 MATE 32bit
* [Python 3.4.3](https://www.python.org/downloads/release/python-343/)
* [SQLite3](https://www.sqlite.org/index.html) 3.8.2

## WebService

* [GitHub](https://github.com/)
    * [アカウント](https://github.com/join)
    * [AccessToken](https://github.com/settings/tokens)
    * [Two-Factor認証](https://github.com/settings/two_factor_authentication/intro)
    * [API v3](https://developer.github.com/v3/)

# 準備

* `~/.ssh/config`のディレクトリとファイルを作成しておく
* たとえば以下のようにHost定義をしておく

```
Host github.com.user1
  User git
  Port 22
  HostName github.com
  IdentityFile ~/.ssh/rsa_user1
  TCPKeepAlive yes
  IdentitiesOnly yes
```

# 実行

```sh
python3 Main.py
```

# 結果

* `~/.ssh/config`のHost設定が標準出力される

# ライセンス #

このソフトウェアはCC0ライセンスである。

[![CC0](http://i.creativecommons.org/p/zero/1.0/88x31.png "CC0")](http://creativecommons.org/publicdomain/zero/1.0/deed.ja)
