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
                # вывод ошибок в файл
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
