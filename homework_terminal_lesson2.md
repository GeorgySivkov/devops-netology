Какого типа команда cd? Попробуйте объяснить, почему она именно такого типа; опишите ход своих мыслей, если считаете что она могла бы быть другого типа.   

Ответ: ```cd is a shell builtin``` - встроенная команда. 

---

Какая альтернатива без pipe команде ```grep <some_string> <some_file> | wc -l? man grep``` поможет в ответе на этот вопрос. Ознакомьтесь с документом о других подобных некорректных вариантах использования pipe.   

Ответ: ```grep <some_string> <some_file> -c``` == ```grep <some_string> <some_file> | wc -l```

---

Какой процесс с PID 1 является родителем для всех процессов в вашей виртуальной машине Ubuntu 20.04?   

Ответ: ```1 root      20   0  102016  11232   8204 S   0.0   1.1   0:01.52 systemd ``` - systemd

---

Как будет выглядеть команда, которая перенаправит вывод ```stderr ls``` на другую сессию терминала?   

Ответ: ```ls -l /root 2>/dev/pts/1```

---

Получится ли одновременно передать команде файл на ```stdin``` и вывести ее ```stdout``` в другой файл? Приведите работающий пример.   

Ответ: ```cat <some_file >some_file_out```

---

Получится ли находясь в графическом режиме, вывести данные из PTY в какой-либо из эмуляторов TTY? Сможете ли вы наблюдать выводимые данные?   

Ответ: Можно, если перенаправим вывод: ```echo Some_text_for_example from pts1 to tty1 >/dev/tty1```. В графическом режиме наблюдать не получится, если только переключиться в TTY. 

---

Выполните команду bash ```5>&1```. К чему она приведет? Что будет, если вы выполните ```echo netology > /proc/$$/fd/5```? Почему так происходит?   

Ответ: 
- ```5>&1``` создает дескриптор и направляет в него ```stdout```
- ```echo netology > /proc/$$/fd/5``` - произойдет вывод в дескриптор под номером 5, перенаправленный в ```stdout```

---

Получится ли в качестве входного потока для ```pipe``` использовать только ```stderr``` команды, не потеряв при этом отображение ```stdout``` на ```pty```? Напоминаем: по умолчанию через ```pipe``` передается только ```stdout``` команды слева от ```|``` на ```stdin``` команды справа. Это можно сделать, поменяв стандартные потоки местами через промежуточный новый дескриптор, который вы научились создавать в предыдущем вопросе.   

Ответ: ```ls -l /root 6>&2 2>&1 1>&6 | grep <some_string> -c```

---

Что выведет команда cat ```/proc/$$/environ```? Как еще можно получить аналогичный по содержанию вывод?   

Ответ:   
- Выведет переменны окружения
```vagrant@vagrant:~$ cat /proc/$$/environ
LANG=en_US.UTF-8USER=vagrantLOGNAME=vagrantHOME=/home/vagrantPATH=/usr/local/sbin:/usr/local/bin:/usr/sbin:/usr/bin:/sbin:/bin:/usr/games:/usr/local/games:/snap/binSHELL=/bin/bashTERM=xterm-256colorXDG_SESSION_ID=6XDG_RUNTIME_DIR=/run/user/1000DBUS_SESSION_BUS_ADDRESS=unix:path=/run/user/1000/busXDG_SESSION_TYPE=ttyXDG_SESSION_CLASS=userMOTD_SHOWN=pamSSH_CLIENT=10.0.2.2 51616 22SSH_CONNECTION=10.0.2.2 51616 10.0.2.15 22SSH_TTY=/dev/pts/1vagrant@vagrant:~$ 
```
- Можно сделать то же самое, только с разделением по строкам с помощью ```env``` или ```printenv```.

---

Используя ```man```, опишите что доступно по адресам ```/proc/<PID>/cmdline```, ```/proc/<PID>/exe```.   

Ответ: 
- Путь до исполняемого файла процесса ```<PID>```
- Ссылка на файл, запущенный для процесса ```<PID>```

---

Узнайте, какую наиболее старшую версию набора инструкций ```SSE``` поддерживает ваш процессор с помощью /proc/cpuinfo.   

Ответ:```SSE 4.2```

---

При открытии нового окна терминала и ```vagrant ssh``` создается новая сессия и выделяется ```pty```. Это можно подтвердить командой ```tty```, которая упоминалась в лекции 3.2. Однако:
```
vagrant@netology1:~$ ssh localhost 'tty'   
not a tty
```
Почитайте, почему так происходит, и как изменить поведение.   

Ответ: Насколько я понял stackoverflow.com и unix.stackexchange.com - shell ожидает, что подключается пользователь (человек), который вводит какие-то данные с какого-то устройства, следовательно, контролирует стандарт со стороны клиента. Поэтому ```tty``` не запускается.
Нашел два способа принудительно запустить ```tty```:
- Через атрибут ```-t``` - ```ssh -t localhost 'tty'```
- Добавить в конфиг ```ssh``` следующее: 
```
Host myserver.com
  User my-ssh-username
  RequestTTY Yes
  ```

---

Бывает, что есть необходимость переместить запущенный процесс из одной сессии в другую. Попробуйте сделать это, воспользовавшись reptyr. Например, так можно перенести в screen процесс, который вы запустили по ошибке в обычной SSH-сессии.

Ответ:
```
vagrant@vagrant:~$ sudo apt install reptyr
Reading package lists... Done
Building dependency tree       
Reading state information... Done
The following NEW packages will be installed:
  reptyr
0 upgraded, 1 newly installed, 0 to remove and 14 not upgraded.
Need to get 22.5 kB of archives.
After this operation, 67.6 kB of additional disk space will be used.
Get:1 http://us.archive.ubuntu.com/ubuntu focal/universe amd64 reptyr amd64 0.6.2-1.3 [22.5 kB]
Fetched 22.5 kB in 0s (50.6 kB/s) 
Selecting previously unselected package reptyr.
(Reading database ... 40620 files and directories currently installed.)
Preparing to unpack .../reptyr_0.6.2-1.3_amd64.deb ...
Unpacking reptyr (0.6.2-1.3) ...
Setting up reptyr (0.6.2-1.3) ...
Processing triggers for man-db (2.9.1-1) ...
vagrant@vagrant:~$ 
```

```
vagrant@vagrant:~$ sudo su - root
root@vagrant:~# nano /etc/sysctl.d/10-ptrace.conf
root@vagrant:~# cat /etc/sysctl.d/10-ptrace.conf
The PTRACE system is used for debugging.  With it, a single user process
can attach to any other dumpable process owned by the same user.  In the
case of malicious software, it is possible to use PTRACE to access
credentials that exist in memory (re-using existing SSH connections,
extracting GPG agent information, etc).

A PTRACE scope of "0" is the more permissive mode.  A scope of "1" limits
PTRACE only to direct child processes (e.g. "gdb name-of-program" and
"strace -f name-of-program" work, but gdb's "attach" and "strace -fp $PID"
do not).  The PTRACE scope is ignored when a user has CAP_SYS_PTRACE, so
"sudo strace -fp $PID" will work as before.  For more details see:
https://wiki.ubuntu.com/SecurityTeam/Roadmap/KernelHardening#ptrace

For applications launching crash handlers that need PTRACE, exceptions can
be registered by the debugee by declaring in the segfault handler
specifically which process will be using PTRACE on the debugee:
prctl(PR_SET_PTRACER, debugger_pid, 0, 0, 0);

In general, PTRACE is not needed for the average running Ubuntu system.
To that end, the default is to set the PTRACE scope to "1".  This value
may not be appropriate for developers or servers with only admin accounts.
kernel.yama.ptrace_scope = 0
```

```
root@vagrant:~# top
```
```
root@vagrant:~# bg
jobs -lgrant:~# 
jobs -l
[1]   1923 Stopped (signal)        top
[2]-  1924 Stopped (signal)        top
[3]+  1925 Stopped (signal)        top
```

```
root@vagrant:~# disown top
-bash: disown: top: ambiguous job spec
-bash: disown: top: no such job
```

```
root@vagrant:~# ps -a
    PID TTY          TIME CMD
   1891 pts/0    00:00:00 sudo
   1892 pts/0    00:00:00 su
   1893 pts/0    00:00:00 bash
   1923 pts/0    00:00:00 top
   1924 pts/0    00:00:00 top
   1925 pts/0    00:00:00 top
   1928 pts/0    00:00:00 ps
```

```
root@vagrant:~# reptyr 1925
   1982 root      20   0    2592   1880   1780 S   4.3   0.2   0:04.29 reptyr   
```

---

```sudo echo string > /root/new_file``` не даст выполнить перенаправление под обычным пользователем, так как перенаправлением занимается процесс ```shell'а```, который запущен без ```sudo``` под вашим пользователем. Для решения данной проблемы можно использовать конструкцию ```echo string | sudo tee /root/new_file```. Узнайте что делает команда ```tee``` и почему в отличие от ```sudo echo``` команда с ```sudo tee``` будет работать.   

Ответ:
- ```tee``` делает вывод в файл и в ```stdout```
- Потому, что сама команда ```tee``` запущена от ```sudo```, поэтому имеет право на запись в файл.

---