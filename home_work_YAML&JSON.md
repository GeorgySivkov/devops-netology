## Обязательная задача 1
Мы выгрузили JSON, который получили через API запрос к нашему сервису:
```
    { "info" : "Sample JSON output from our service\t",
        "elements" :[
            { "name" : "first",
            "type" : "server",
            "ip" : 7175 
            }
            { "name" : "second",
            "type" : "proxy",
            "ip : 71.78.22.43
            }
        ]
    }
```
  Нужно найти и исправить все ошибки, которые допускает наш сервис

### Ваш JSON

```
    { "info" : "Sample JSON output from our service\t",
        "elements" :[
            { "name" : "first",
            "type" : "server",
            "ip" : 7175 
            }
            { "name" : "second",
            "type" : "proxy",
            "ip" : "71.78.22.43"
            }
        ]
    }
```

## Обязательная задача 2
В прошлый рабочий день мы создавали скрипт, позволяющий опрашивать веб-сервисы и получать их IP. К уже реализованному функционалу нам нужно добавить возможность записи JSON и YAML файлов, описывающих наши сервисы. Формат записи JSON по одному сервису: `{ "имя сервиса" : "его IP"}`. Формат записи YAML по одному сервису: `- имя сервиса: его IP`. Если в момент исполнения скрипта меняется IP у сервиса - он должен так же поменяться в yml и json файле.

### Ваш скрипт:
```python
#!/usr/bin/env python3

import socket as s
import time as t
import datetime as dt
import json
import yaml

i = 1
delay = 2  # Delay between checks in seconds
srv = {'drive.google.com': '0.0.0.0', 'mail.google.com': '0.0.0.0', 'google.com': '0.0.0.0'}
init = 0
fpath = "/Users/georgijsivkov/PycharmProjects/Devops/devops-netology/configs/"  # path to configurations files
flog = "/Users/georgijsivkov/PycharmProjects/Devops/devops-netology/logs/error.log"  # path to log files

# start script workflow
print('Script started')
print(srv)
print('==============')

while 1 == 1:
    for host in srv:
        is_error = False
        ip = s.gethostbyname(host)
        if ip != srv[host]:
            if i == 1 and init != 1:
                is_error = True
                with open(flog, 'a') as fl:
                    print(str(dt.datetime.now().strftime("%Y-%m-%d %H:%M:%S")) + ' [ERROR] ' + str(
                        host) + ' IP mistmatch: ' + srv[host] + ' ' + ip, file=fl)
                with open(fpath + host + ".json", 'w') as jsf:
                    json_data = json.dumps({host: ip})
                    jsf.write(json_data)
                with open(fpath + host + ".yaml", 'w') as ymf:
                    yaml_data = yaml.dump([{host: ip}])
                    ymf.write(yaml_data)
            srv[host] = ip
    # print(i) # print 1st step for test
    # For test 50 iterations
    #  i+=1
    #  if i >= 50 :
    #    break
    #  t.sleep(delay)

```

### Вывод скрипта при запуске при тестировании:
```
georgijsivkov@MacBook-Pro-Georgij py_lessons % /Users/georgijsivkov/PycharmProjects/Devops/devops-netology/py_lessons/take_ip.py
Script started
{'drive.google.com': '0.0.0.0', 'mail.google.com': '0.0.0.0', 'google.com': '0.0.0.0'}
==============
```

### json-файл(ы), который(е) записал ваш скрипт:
```json
drive.google.com.json: {"drive.google.com": "64.233.165.194"}

google.com.json: {"google.com": "142.251.1.101"}

mail.google.com.json: {"mail.google.com": "64.233.165.19"}
```

### yml-файл(ы), который(е) записал ваш скрипт:
```yaml
drive.google.com.yaml: - drive.google.com: 64.233.165.194

google.com.yaml: - google.com: 142.251.1.101

mail.google.com.yaml: - mail.google.com: 64.233.165.19
```