
Вопрос 1: Какой системный вызов делает команда ```cd```? 
В прошлом ДЗ мы выяснили, что ```cd``` не является самостоятельной программой, 
это ```shell builtin```, поэтому запустить ```strace``` непосредственно на ```cd```
не получится. Тем не менее вы можете запустить ```strace``` на ```/bin/bash -c 'cd /tmp'```.
В этом случае вы увидите полный список системных вызовов, которые делает сам ```bash``` при 
старте. Вам нужно найти тот единственный, который относится именно к ```cd```. 
Обратите внимание, что ```strace``` выдаёт результат своей работы в поток ```stderr```, 
а не в ```stdout```.

Ответ: ```chdir("/tmp")```

---

Вопрос 2: Попробуйте использовать команду ```file``` на объекты разных типов на файловой системе. Например:

```
vagrant@netology1:~$ file /dev/tty
/dev/tty: character special (5/0)
vagrant@netology1:~$ file /dev/sda
/dev/sda: block special (8/0)
vagrant@netology1:~$ file /bin/bash
/bin/bash: ELF 64-bit LSB shared object, x86-64
```

Используя ```strace``` выясните, 
где находится база данных ```file``` на основании которой она делает свои догадки.

Ответ: ```openat(AT_FDCWD, "/usr/share/misc/magic.mgc", O_RDONLY) = 3``` - /usr/share/misc/magic.mgc

---

Вопрос 3: Предположим, приложение пишет лог в текстовый файл. 
Этот файл оказался удален (```deleted``` в ```lsof```), 
однако возможности сигналом сказать приложению 
переоткрыть файлы или просто перезапустить приложение – нет. 
Так как приложение продолжает писать в удаленный файл, 
место на диске постепенно заканчивается. 
Основываясь на знаниях о перенаправлении потоков предложите 
способ обнуления открытого удаленного файла 
(чтобы освободить место на файловой системе).

Ответ: Перенаправить echo в дескриптор файла. 

```
vagrant@vagrant:~$ echo '' >/proc/<PID>/fd/<number_of_descriptor>
```

Гугл рекомендует 
```
vagrant@vagrant:~$ : > /proc/<PID>/fd/<number_of_descriptor>
```
```
vagrant@vagrant:~$ > /proc/<PID>/fd/<number_of_descriptor>
```
```
vagrant@vagrant:~$ truncate -s 0 /proc/<PID>/fd/<number_of_descriptor>
```

---

Вопрос 4: Занимают ли зомби-процессы какие-то ресурсы в ОС (CPU, RAM, IO)?

Ответ: Нет, зомби процессы не занимают ресурсы ОС, но они занимают место в таблице процессов. 

---

Вопрос 5: В iovisor BCC есть утилита ```opensnoop```:

```
root@vagrant:~# dpkg -L bpfcc-tools | grep sbin/opensnoop
/usr/sbin/opensnoop-bpfcc
```

На какие файлы вы увидели вызовы группы ```open``` за первую секунду работы утилиты? 
Воспользуйтесь пакетом ```bpfcc-tools``` для Ubuntu 20.04. 
Дополнительные сведения по установке.

Ответ: Не совсем понял вопрос.

```
vagrant@vagrant:~$ sudo /usr/sbin/opensnoop-bpfcc
PID    COMM               FD ERR PATH
637    irqbalance          6   0 /proc/interrupts
637    irqbalance          6   0 /proc/stat
637    irqbalance          6   0 /proc/irq/20/smp_affinity
637    irqbalance          6   0 /proc/irq/0/smp_affinity
637    irqbalance          6   0 /proc/irq/1/smp_affinity
637    irqbalance          6   0 /proc/irq/8/smp_affinity
637    irqbalance          6   0 /proc/irq/12/smp_affinity
637    irqbalance          6   0 /proc/irq/14/smp_affinity
637    irqbalance          6   0 /proc/irq/15/smp_affinity
829    vminfo              4   0 /var/run/utmp
632    dbus-daemon        -1   2 /usr/local/share/dbus-1/system-services
632    dbus-daemon        20   0 /usr/share/dbus-1/system-services
632    dbus-daemon        -1   2 /lib/dbus-1/system-services
632    dbus-daemon        20   0 /var/lib/snapd/dbus-1/system-services/
384    systemd-udevd      14   0 /sys/fs/cgroup/unified/system.slice/systemd-udevd.service/cgroup.procs
384    systemd-udevd      14   0 /sys/fs/cgroup/unified/system.slice/systemd-udevd.service/cgroup.threads
829    vminfo              4   0 /var/run/utmp
632    dbus-daemon        -1   2 /usr/local/share/dbus-1/system-services
632    dbus-daemon        20   0 /usr/share/dbus-1/system-services
632    dbus-daemon        -1   2 /lib/dbus-1/system-services
632    dbus-daemon        20   0 /var/lib/snapd/dbus-1/system-services/
```

---

Вопрос 6: Какой системный вызов использует ```uname -a```? 
Приведите цитату из ```man``` по этому системному вызову, 
где описывается альтернативное местоположение в ```/proc```, 
где можно узнать версию ядра и релиз ОС.

Ответ: uname()   
Цитата:

```Part  of  the utsname information is also accessible via /proc/sys/kernel/{ostype, hostname, osrelease, version, domainname}.```

---

Вопрос 7: Чем отличается последовательность команд через ```;``` и через ```&&```
в bash? Например:

```
root@netology1:~# test -d /tmp/some_dir; echo Hi
Hi
root@netology1:~# test -d /tmp/some_dir && echo Hi
root@netology1:~#
```
Есть ли смысл использовать в bash ```&&```, если применить ```set -e```?

Ответ: 

- ```;``` разделитель для последовательных команды
- ```&&``` условный оператор логического И   
В примере, в первом варианте ```echo``` отработает в любом случае, во втором варианте, только если команда ```test``` успешно завершится
- ```set -e``` обрывает выполнение команд при любом завершении команд в конвеере с кодом не 0, кроме последней. Кмк не имеет смысла, т.к. выполнение команд прекратиться при ошибке (код не 0) 

---

Вопрос 8: Из каких опций состоит режим ```bash set -euxo pipefail```
и почему его хорошо было бы использовать в сценариях?

Ответ:

- ```e``` прерывает выполнение команд при возврате не последней командой любого кода, кроме 0. 
- ```u``` выводит в stderr неустановленные параметры и переменные
- ```x``` выводит трейс команд и их аргументов по мере их выполнения
- ```o pipefall``` возвращает в значении статус (код) последней команды, которая завершилась с ненулевым кодом или 0, если все команды, кроме последней завершились с кодом 0

Хорошо использовать для траблшутинга - детализация вывода ошибок и собственно остановит выполнение команд при ошибке в одной из них. 

---

Вопрос 9: Используя ```-o stat``` для ```ps```, определите, 
какой наиболее часто встречающийся статус у процессов в системе. 
В ```man ps``` ознакомьтесь (```/PROCESS STATE CODES```) что значат 
дополнительные к основной заглавной буквы статуса процессов. 
Его можно не учитывать при расчете (считать ```S```, ```Ss``` или ```Ssl```
равнозначными).

Ответ:

- ```Ss``` - Ожидают завершения, спящие с прерыванием сна. 
- ```R+``` - Выполняются или в очереди на выполнение. В группе процессов переднего плана. 

---

