# Домашнее задание к занятию "08.01 Введение в Ansible"

## Подготовка к выполнению
1. Установите ansible версии 2.10 или выше.
2. Создайте свой собственный публичный репозиторий на github с произвольным именем.
3. Скачайте [playbook](./playbook/) из репозитория с домашним заданием и перенесите его в свой репозиторий.

## Основная часть
1. Попробуйте запустить playbook на окружении из `test.yml`, зафиксируйте какое значение имеет факт `some_fact` для указанного хоста при выполнении playbook'a.   
Ответ:
```commandline
(venv) georgijsivkov@MacBook-Pro-Georgij devops-netology % cd playbook
(venv) georgijsivkov@MacBook-Pro-Georgij playbook % ansible-playbook -i inventory/test.yml site.yml           

PLAY [Print os facts] *********************************************************************************************************************************************************************************************************************

TASK [Gathering Facts] ********************************************************************************************************************************************************************************************************************
[WARNING]: Platform darwin on host localhost is using the discovered Python interpreter at /Library/Frameworks/Python.framework/Versions/3.10/bin/python3.10, but future installation of another Python interpreter could change the
meaning of that path. See https://docs.ansible.com/ansible-core/2.13/reference_appendices/interpreter_discovery.html for more information.
ok: [localhost]

TASK [Print OS] ***************************************************************************************************************************************************************************************************************************
ok: [localhost] => {
    "msg": "MacOSX"
}

TASK [Print fact] *************************************************************************************************************************************************************************************************************************
ok: [localhost] => {
    "msg": 12
}

PLAY RECAP ********************************************************************************************************************************************************************************************************************************
localhost                  : ok=3    changed=0    unreachable=0    failed=0    skipped=0    rescued=0    ignored=0
```
2. Найдите файл с переменными (group_vars) в котором задаётся найденное в первом пункте значение и поменяйте его на 'all default fact'.    
Ответ:
```commandline
(venv) georgijsivkov@MacBook-Pro-Georgij playbook % nano group_vars/all/examp.yml
(venv) georgijsivkov@MacBook-Pro-Georgij playbook % cat group_vars/all/examp.yml 
---
  some_fact: "all default fact"
  
(venv) georgijsivkov@MacBook-Pro-Georgij playbook % ansible-playbook -i inventory/test.yml site.yml 

PLAY [Print os facts] *********************************************************************************************************************************************************************************************************************

TASK [Gathering Facts] ********************************************************************************************************************************************************************************************************************
[WARNING]: Platform darwin on host localhost is using the discovered Python interpreter at /Library/Frameworks/Python.framework/Versions/3.10/bin/python3.10, but future installation of another Python interpreter could change the
meaning of that path. See https://docs.ansible.com/ansible-core/2.13/reference_appendices/interpreter_discovery.html for more information.
ok: [localhost]

TASK [Print OS] ***************************************************************************************************************************************************************************************************************************
ok: [localhost] => {
    "msg": "MacOSX"
}

TASK [Print fact] *************************************************************************************************************************************************************************************************************************
ok: [localhost] => {
    "msg": "all default fact"
}

PLAY RECAP ********************************************************************************************************************************************************************************************************************************
localhost                  : ok=3    changed=0    unreachable=0    failed=0    skipped=0    rescued=0    ignored=0 
```
3. Воспользуйтесь подготовленным (используется `docker`) или создайте собственное окружение для проведения дальнейших испытаний.   
Ответ:
```commandline

```
4. Проведите запуск playbook на окружении из `prod.yml`. Зафиксируйте полученные значения `some_fact` для каждого из `managed host`.   
Ответ:
```commandline

```
5. Добавьте факты в `group_vars` каждой из групп хостов так, чтобы для `some_fact` получились следующие значения: для `deb` - 'deb default fact', для `el` - 'el default fact'.   
Ответ:
```commandline

```
6. Повторите запуск playbook на окружении `prod.yml`. Убедитесь, что выдаются корректные значения для всех хостов.   
Ответ:
```commandline

```
7. При помощи `ansible-vault` зашифруйте факты в `group_vars/deb` и `group_vars/el` с паролем `netology`.   
Ответ:
```commandline

```
8. Запустите playbook на окружении `prod.yml`. При запуске `ansible` должен запросить у вас пароль. Убедитесь в работоспособности.   
Ответ:
```commandline

```
9. Посмотрите при помощи `ansible-doc` список плагинов для подключения. Выберите подходящий для работы на `control node`.   
Ответ:
```commandline

```
10. В `prod.yml` добавьте новую группу хостов с именем  `local`, в ней разместите localhost с необходимым типом подключения.   
Ответ:
```commandline

```
11. Запустите playbook на окружении `prod.yml`. При запуске `ansible` должен запросить у вас пароль. Убедитесь что факты `some_fact` для каждого из хостов определены из верных `group_vars`.   
Ответ:
```commandline

```
12. Заполните `README.md` ответами на вопросы. Сделайте `git push` в ветку `master`. В ответе отправьте ссылку на ваш открытый репозиторий с изменённым `playbook` и заполненным `README.md`.   
Ответ:
```commandline

```

## Необязательная часть

1. При помощи `ansible-vault` расшифруйте все зашифрованные файлы с переменными.
2. Зашифруйте отдельное значение `PaSSw0rd` для переменной `some_fact` паролем `netology`. Добавьте полученное значение в `group_vars/all/exmp.yml`.
3. Запустите `playbook`, убедитесь, что для нужных хостов применился новый `fact`.
4. Добавьте новую группу хостов `fedora`, самостоятельно придумайте для неё переменную. В качестве образа можно использовать [этот](https://hub.docker.com/r/pycontribs/fedora).
5. Напишите скрипт на bash: автоматизируйте поднятие необходимых контейнеров, запуск ansible-playbook и остановку контейнеров.
6. Все изменения должны быть зафиксированы и отправлены в вашей личный репозиторий.

---

### Как оформить ДЗ?

Выполненное домашнее задание пришлите ссылкой на .md-файл в вашем репозитории.

---
