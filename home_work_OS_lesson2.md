Вопрос 1: На лекции мы познакомились с ```node_exporter```. 
В демонстрации его исполняемый файл запускался в ```background```. 
Этого достаточно для демо, но не для настоящей production-системы, 
где процессы должны находиться под внешним управлением. 
Используя знания из лекции по ```systemd```, 
создайте самостоятельно простой ```unit-фай``` для ```node_exporter```:
- поместите его в автозагрузку,
- предусмотрите возможность добавления опций к запускаемому процессу через внешний файл 
(посмотрите, например, на ```systemctl cat cron```),
- удостоверьтесь, что с помощью ```systemctl``` процесс корректно стартует, 
завершается, а после перезагрузки автоматически поднимается.

Ответ: Вагран запустился, выводит на хостовую машину информацию, но через другой порт (```http://0.0.0.0:9999/metrics```) - 9100 был занят. 

Конфигурационный файл:

```
root@vagrant:~# cat /etc/systemd/system/node_exporter.service
[Unit]
Description=Node Exporter Service
After=network.target

[Service]
User=nodeusr
Group=nodeusr
Type=simple
ExecStart=/usr/local/bin/node_exporter
ExecReload=/bin/kill -HUP $MAINPID
Restart=on-failure

[Install]
WantedBy=multi-user.target

```

Проверка:

```
root@vagrant:~# ps -e | grep node_exporter
    641 ?        00:00:00 node_exporter
root@vagrant:~# systemctl stop node_exporter
root@vagrant:~# ps -e | grep node_exporter
root@vagrant:~# systemctl start node_exporter
root@vagrant:~# ps -e | grep node_exporter
   1253 ?        00:00:00 node_exporter
```



Перезагрузил виртуалку - экспортер запустился автоматически. Аналогично и при тушении виртуалки. 

---

Вопрос 2: Ознакомьтесь с опциями node_exporter и выводом ```/metrics``` по-умолчанию. 
Приведите несколько опций, которые вы бы выбрали для базового мониторинга хоста по CPU, 
памяти, диску и сети.

Ответ: 

CPU:

```
node_cpu_seconds_total{cpu="0",mode="idle"} 40.35
node_cpu_seconds_total{cpu="0",mode="system"} 6.78
node_cpu_seconds_total{cpu="0",mode="user"} 3.49
process_cpu_seconds_total 0.05
```

Memory:

```
node_memory_MemAvailable_bytes 7.43022592e+08
node_memory_MemFree_bytes 5.50825984e+08
```

Disk:

```
node_disk_io_time_seconds_total{device="sda"} 8.024000000000001
node_disk_read_bytes_total{device="sda"} 2.27887104e+08
node_disk_read_time_seconds_total{device="sda"} 10.883000000000001
node_disk_write_time_seconds_total{device="sda"} 0.842
```

Network:

```
node_network_receive_errs_total{device="eth0"} 0
node_network_receive_bytes_total{device="eth0"} 48707
node_network_transmit_bytes_total{device="eth0"} 46138
node_network_transmit_errs_total{device="eth0"} 0
```


---

Вопрос 3: Установите в свою виртуальную машину ```Netdata```. 
Воспользуйтесь готовыми пакетами для установки (```sudo apt install -y netdata```). 
После успешной установки:
- в конфигурационном файле ```/etc/netdata/netdata.conf``` 
в секции ```[web]``` замените значение с ```localhost``` на ```bind to = 0.0.0.0```,
- добавьте в ```Vagrantfile``` проброс порта ```Netdata```
на свой локальный компьютер и сделайте ```vagrant reload```:
```
config.vm.network "forwarded_port", guest: 19999, host: 19999
```
После успешной перезагрузки в браузере на своем ПК (не в виртуальной машине) 
вы должны суметь зайти на ```localhost:19999```. 
Ознакомьтесь с метриками, 
которые по умолчанию собираются ```Netdata``` и с комментариями, 
которые даны к этим метрикам.

Ответ: Установил ```netdata```. Посмотрел, ознакомился. 

```
vagrant@vagrant:~$ sudo lsof -i :19999
COMMAND PID    USER   FD   TYPE DEVICE SIZE/OFF NODE NAME
netdata 636 netdata    4u  IPv4  23311      0t0  TCP *:19999 (LISTEN)
netdata 636 netdata   21u  IPv4  29289      0t0  TCP vagrant:19999->_gateway:63639 (ESTABLISHED)
netdata 636 netdata   22u  IPv4  29760      0t0  TCP vagrant:19999->_gateway:63641 (ESTABLISHED)
netdata 636 netdata   27u  IPv4  29291      0t0  TCP vagrant:19999->_gateway:63645 (ESTABLISHED)
netdata 636 netdata   31u  IPv4  29764      0t0  TCP vagrant:19999->_gateway:63651 (ESTABLISHED)
netdata 636 netdata   32u  IPv4  29762      0t0  TCP vagrant:19999->_gateway:63643 (ESTABLISHED)
netdata 636 netdata   33u  IPv4  29765      0t0  TCP vagrant:19999->_gateway:63652 (ESTABLISHED)
```

---

Вопрос 4: Можно ли по выводу ```dmesg``` понять, осознает ли ОС, 
что загружена не на настоящем оборудовании, а на системе виртуализации?

Ответ: Да.

```
vagrant@vagrant:~$ dmesg | grep virtual
[    0.005787] CPU MTRRs all blank - virtualized system.
[    0.144499] Booting paravirtualized kernel on KVM
[    3.260808] systemd[1]: Detected virtualization oracle.
```

---

Вопрос 5: Как настроен ```sysctl fs.nr_open``` на системе по-умолчанию? 
Узнайте, что означает этот параметр. 
Какой другой существующий лимит не позволит достичь такого числа (```ulimit --help```)?

Ответ:

- Максимальное количество открытых дескрипторов для системы:
```
root@vagrant:~# /sbin/sysctl -n fs.nr_open
1048576
```

Не позволит достичь такого числа:
- софт лимит:
```
root@vagrant:~# ulimit -Sn
1024

```

- хард лимит:
```
root@vagrant:~# ulimit -Hn
1048576

```

---

Вопрос 6: Запустите любой долгоживущий процесс 
(не ```ls```, который отработает мгновенно, а, например, ```sleep 1h```) 
в отдельном неймспейсе процессов; покажите, 
что ваш процесс работает под ```PID 1``` через ```nsenter```. 
Для простоты работайте в данном задании под root (```sudo -i```). 
Под обычным пользователем требуются дополнительные опции (```--map-root-user```) и т.д.

Ответ:

```
root@vagrant:/# ps -e | grep sleep
  15888 pts/0    00:00:00 sleep
root@vagrant:/# nsenter --target 15888 --pid --mount
root@vagrant:/# ps
    PID TTY          TIME CMD
  15944 pts/1    00:00:00 sudo
  15946 pts/1    00:00:00 nsenter
  15947 pts/1    00:00:00 bash
  15966 pts/1    00:00:00 nsenter
  15967 pts/1    00:00:00 bash
  15978 pts/1    00:00:00 ps
root@vagrant:/# 
```

---

Вопрос 7: Найдите информацию о том, что такое ```:(){ :|:& };:```. 
Запустите эту команду в своей виртуальной машине Vagrant с Ubuntu 20.04 
(это важно, поведение в других ОС не проверялось). 
Некоторое время все будет "плохо", 
после чего (минуты) – ОС должна стабилизироваться. 
Вызов ```dmesg``` расскажет, какой механизм помог автоматической стабилизации. 
Как настроен этот механизм по-умолчанию, 
и как изменить число процессов, которое можно создать в сессии?

Ответ: Нашел название ```fork-бомба```

Можно упростить заменив ```:``` на ```f``` и привести в читаемый вид:

```
f() {
  f | f &
}
f
```

Эта функция, которая параллельно запускает два своих экземпляра, каждый из которых пускает еще два и т.д. 
При отсутствии лимита на число процессов машина быстро исчерпывает физическую память и уходит в своп. После 20 итераций процессов будет больше миллиона. 

Останавливает похоже вот это:

```
[   82.143184] cgroup: fork rejected by pids controller in /user.slice/user-1000.slice/session-3.scope
```

Система имеет ограничения на создаваемые ресурсы в сессии, после превышения которых начинает блокировать создание новых. 
Можно изменить через ```ulimit -u <number>```