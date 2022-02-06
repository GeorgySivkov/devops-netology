#!/usr/bin/env python3

import os

bash_command = ["cd /Users/georgijsivkov/PycharmProjects/Devops/devops-netology", "git status"]
result_os = os.popen(' && '.join(bash_command)).read()
print(result_os)
for result in result_os.split('\n'):
    print(result, result_os)
    if result.find('modified') != -1:
        prepare_result = result.replace('\tmodified:   ', '')
        print(prepare_result)