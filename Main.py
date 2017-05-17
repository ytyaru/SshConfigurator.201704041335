import SshConfigurator

c = SshConfigurator.SshConfigurator()
print('Hosts-----------------------')
for hostname in c.Hosts.keys():
    print(hostname)
print('ditails-----------------------')
for host in c.Hosts:
    print(c.Hosts[host])
    print(c.Hosts[host]['host'])
    for key in c.Hosts[host].keys():
        print('  {0}={1}'.format(key, c.Hosts[host][key]))
# 大文字小文字を無視する
# sshのconfigファイルのキー名は大文字小文字の違いを無視する。しかし値は無視しない。
# よって、configはCaseInsensitiveDict型、Host名はdict型で実装する
#print(c.Hosts['github.com.YTYARU']['hoST'])
print(c.Hosts['github.com.ytyaru']['hoST'])
print(c.Hosts['github.com.ytyaru']['poRt'])
