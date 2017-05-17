from requests.structures import CaseInsensitiveDict
hosts = CaseInsensitiveDict()
hosts['A'] = CaseInsensitiveDict()
hosts['A'].update({'A': 'A'})
hosts['B'] = CaseInsensitiveDict()
hosts['B'].update({'B': 'B'})
print(hosts)
for h in hosts:
    print(hosts[h])
    for key in hosts[h].keys():
        print(hosts[h][key])
