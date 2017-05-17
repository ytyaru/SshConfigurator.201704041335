import re
line = 'Host github.com.user1'
#line = 'Host '
#line = '  Host github.com.user1'

# 大文字小文字を無視したdict型
# http://qiita.com/seizans/items/d50b5d08f20777deff03
# https://github.com/tivvit/python-case-insensitive-dict/blob/master/CaseInsensitiveDict/CaseInsensitiveDict.py

# インデントされた行
print(re.compile(' +', re.IGNORECASE).match('      ab cd'))
print(re.compile(r'[ \t]+', re.IGNORECASE).match(' ab'))
print(re.compile(r'[ \t]+', re.IGNORECASE).match('      ab'))
print(re.compile(r'[ \t]+', re.IGNORECASE).match('	ab'))
print(re.compile(r'[ \t]+', re.IGNORECASE).match('	 ab'))
print(re.compile('[ \t]+', re.IGNORECASE).match(' 	ab  bd'))

# split引数省略時は空白文字で区切る（間にいくつあろうが1つとみなす。空要素は作らない）
key, value = '  ab       cd '.split()
print(key)
print(value)

# 部分一致
#print(re.compile('host', re.IGNORECASE).findall(line))
#print(re.compile('host', re.IGNORECASE).finditer(line))
#print(re.compile('host', re.IGNORECASE).search(line))

print(re.compile('host ', re.IGNORECASE).match(line))
#print(re.compile('*host*', re.IGNORECASE).match(line)) # エラー。部分一致はfindall関数を使う
print(re.compile('host ', re.IGNORECASE).match(line))
print(re.compile('host +', re.IGNORECASE).match(line))
print(re.compile('host *', re.IGNORECASE).match(line))
print(re.compile('HOST *', re.IGNORECASE).match(line))
print(re.compile('Host *', re.IGNORECASE).match(line))
print(re.compile('HOOO *', re.IGNORECASE).match(line))
print(re.compile('^host ', re.IGNORECASE).match(line))
print(re.compile(r'^host ', re.IGNORECASE).match(line))
print(re.compile('\Ahost ', re.IGNORECASE).match(line))
print(re.compile('\Ahost \Z', re.IGNORECASE).match(line)) # 正規表現では行の先頭と末尾は^と$だが、Pythonでは\A,\Zで表す。さもないと無視される
print(re.compile('\Ahost github.com.user1\Z', re.IGNORECASE).match(line))
print(re.compile('\Ahost *\Z', re.IGNORECASE).match(line)) # 一致しない。なぜ？
if None != re.compile('host ', re.IGNORECASE).match(line):
#if None != re.compile(r'^host ', re.IGNORECASE).match(line):
#if None != re.compile(line, re.IGNORECASE).match(r'host *'):
    print('match!')
else:
    print('no match...')
    
# http://qiita.com/wanwanland/items/ce272419dde2f95cdabc
# match: 先頭一致
# search: 一致位置
# findall: 部分一致
# finditer: 部分一致
