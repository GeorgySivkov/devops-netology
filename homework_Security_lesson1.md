Вопрос 1: Установите Bitwarden плагин для браузера. Зарегестрируйтесь и сохраните несколько паролей.

Ответ: Установил, зарегистрировался и сохранил пароли для рандомных сайтов. 

---
Вопрос 2: Установите Google authenticator на мобильный телефон. Настройте вход в Bitwarden акаунт через Google authenticator OTP.

Ответ: Настроил. 

---
Вопрос 3: Установите ```apache2```, сгенерируйте самоподписанный сертификат, настройте тестовый сайт для работы по ```HTTPS```.

Ответ: 

```
vagrant@vagrant:~$ sudo apt-get update
vagrant@vagrant:~$ sudo apt install apache2
vagrant@vagrant:~$ sudo a2enmod ssl
vagrant@vagrant:~$ sudo systemctl restart apache2
vagrant@vagrant:~$ sudo openssl req -x509 -nodes -days 365 -newkey rsa:2048 -keyout /etc/ssl/private/apache-selfsigned.key -out /etc/ssl/certs/apache-selfsigned.crt
vagrant@vagrant:~$ sudo nano /etc/apache2/sites-available/test_site.conf
...
<VirtualHost *:443>
   ServerName test_site
   DocumentRoot /var/www/test_site

   SSLEngine on
   SSLCertificateFile /etc/ssl/certs/apache-selfsigned.crt
   SSLCertificateKeyFile /etc/ssl/private/apache-selfsigned.key
</VirtualHost>
...
vagrant@vagrant:~$ sudo mkdir /var/www/test_site
vagrant@vagrant:~$ sudo nano /var/www/test_site/index.html
...
<h1>it worked!</h1>
...
vagrant@vagrant:~$ sudo a2ensite test_site.conf
Enabling site test_site.
To activate the new configuration, you need to run:
  systemctl reload apache2
vagrant@vagrant:~$ sudo apache2ctl configtest
AH00558: apache2: Could not reliably determine the server's fully qualified domain name, using 127.0.1.1. Set the 'ServerName' directive globally to suppress this message
Syntax OK
vagrant@vagrant:~$ sudo systemctl reload apache2

```

---
Вопрос 4: Проверьте на ```TLS``` уязвимости произвольный сайт в интернете (кроме сайтов МВД, ФСБ, МинОбр, НацБанк, РосКосмос, РосАтом, РосНАНО и любых госкомпаний, объектов КИИ, ВПК ... и тому подобное).

Ответ: 

```
vagrant@vagrant:~$ git clone --depth 1 https://github.com/drwetter/testssl.sh.git
Cloning into 'testssl.sh'...
remote: Enumerating objects: 100, done.
remote: Counting objects: 100% (100/100), done.
remote: Compressing objects: 100% (93/93), done.
remote: Total 100 (delta 13), reused 26 (delta 6), pack-reused 0
Receiving objects: 100% (100/100), 8.62 MiB | 5.93 MiB/s, done.
Resolving deltas: 100% (13/13), done.
vagrant@vagrant:~$ cd testssl.sh
vagrant@vagrant:~/testssl.sh$ ./testssl.sh -U --sneaky https://projapan.ru/
...
 Testing vulnerabilities 

 Heartbleed (CVE-2014-0160)                not vulnerable (OK), timed out
 CCS (CVE-2014-0224)                       not vulnerable (OK)
 Ticketbleed (CVE-2016-9244), experiment.  not vulnerable (OK)
 ROBOT                                     not vulnerable (OK)
 Secure Renegotiation (RFC 5746)           supported (OK)
 Secure Client-Initiated Renegotiation     not vulnerable (OK)
 CRIME, TLS (CVE-2012-4929)                not vulnerable (OK)
 BREACH (CVE-2013-3587)                    potentially NOT ok, "gzip" HTTP compression detected. - only supplied "/" tested
                                           Can be ignored for static pages or if no secrets in the page
 POODLE, SSL (CVE-2014-3566)               not vulnerable (OK)
 TLS_FALLBACK_SCSV (RFC 7507)              Downgrade attack prevention supported (OK)
 SWEET32 (CVE-2016-2183, CVE-2016-6329)    VULNERABLE, uses 64 bit block ciphers
 FREAK (CVE-2015-0204)                     not vulnerable (OK)
 DROWN (CVE-2016-0800, CVE-2016-0703)      not vulnerable on this host and port (OK)
                                           make sure you don't use this certificate elsewhere with SSLv2 enabled services
                                           https://censys.io/ipv4?q=A18E90BBF4A9AFA457057FDCEFDB0E866718874516920CA49EDCEB12534CDAD0 could help you to find out
 LOGJAM (CVE-2015-4000), experimental      not vulnerable (OK): no DH EXPORT ciphers, no DH key detected with <= TLS 1.2
 BEAST (CVE-2011-3389)                     TLS1: ECDHE-RSA-AES256-SHA AES256-SHA ECDHE-RSA-AES128-SHA AES128-SHA ECDHE-RSA-DES-CBC3-SHA DES-CBC3-SHA 
                                           VULNERABLE -- but also supports higher protocols  TLSv1.1 TLSv1.2 (likely mitigated)
 LUCKY13 (CVE-2013-0169), experimental     potentially VULNERABLE, uses cipher block chaining (CBC) ciphers with TLS. Check patches
 Winshock (CVE-2014-6321), experimental    not vulnerable (OK) - CAMELLIA or ECDHE_RSA GCM ciphers found
 RC4 (CVE-2013-2566, CVE-2015-2808)        no RC4 ciphers detected (OK)


 Done 2022-01-31 22:49:55 [  48s] -->> 212.109.222.156:443 (projapan.ru) <<--
```

---
Вопрос 5: Установите на ```Ubuntu``` ```ssh сервер```, сгенерируйте новый приватный ключ. Скопируйте свой публичный ключ на другой сервер. Подключитесь к серверу по ```SSH-ключу```.

Ответ: 

```
# Устанавливаю public_network и две машины в Vagrant
georgijsivkov@MacBook-Pro-Georgij Vagrant % nano Vagrantfile
Vagrant.configure("2") do |config|
  config.vm.provision "shell", inline: "echo Hello"
  config.vm.network "public_network"

  config.vm.define "ubuntu" do |ubuntu|
    ubuntu.vm.box = "bento/ubuntu-20.04"
  end

  config.vm.define "ubuntu2" do |ubuntu|
    ubuntu.vm.box = "bento/ubuntu-20.04"
  end
end
# Первая машина Vagrant_ubuntu_1643909924949_39553 IP 192.168.0.119
# Вторая машина Vagrant_ubuntu2_1643909987982_90016 IP 192.168.0.120

# Устанавливаем sshd-сервер (предустановлен) на первую машину.
georgijsivkov@MacBook-Pro-Georgij Vagrant % vagrant ssh ubuntu                            
Welcome to Ubuntu 20.04.3 LTS (GNU/Linux 5.4.0-91-generic x86_64)

 * Documentation:  https://help.ubuntu.com
 * Management:     https://landscape.canonical.com
 * Support:        https://ubuntu.com/advantage

  System information as of Thu 03 Feb 2022 05:44:30 PM UTC

  System load:  0.03               Processes:             123
  Usage of /:   11.6% of 30.88GB   Users logged in:       0
  Memory usage: 21%                IPv4 address for eth0: 10.0.2.15
  Swap usage:   0%                 IPv4 address for eth1: 192.168.0.119


This system is built by the Bento project by Chef Software
More information can be found at https://github.com/chef/bento
vagrant@vagrant:~$ sudo -i
root@vagrant:~# apt install openssh-server
Reading package lists... Done
Building dependency tree       
Reading state information... Done
openssh-server is already the newest version (1:8.2p1-4ubuntu0.3).
0 upgraded, 0 newly installed, 0 to remove and 0 not upgraded.

# На второй машине генерируем ключ
georgijsivkov@MacBook-Pro-Georgij Vagrant % vagrant ssh ubuntu2
Welcome to Ubuntu 20.04.3 LTS (GNU/Linux 5.4.0-91-generic x86_64)

 * Documentation:  https://help.ubuntu.com
 * Management:     https://landscape.canonical.com
 * Support:        https://ubuntu.com/advantage

  System information as of Thu 03 Feb 2022 05:46:34 PM UTC

  System load:  0.01               Processes:             116
  Usage of /:   11.6% of 30.88GB   Users logged in:       0
  Memory usage: 21%                IPv4 address for eth0: 10.0.2.15
  Swap usage:   0%                 IPv4 address for eth1: 192.168.0.120


This system is built by the Bento project by Chef Software
More information can be found at https://github.com/chef/bento

vagrant@vagrant:~$ ssh-keygen
Generating public/private rsa key pair.
Enter file in which to save the key (/home/vagrant/.ssh/id_rsa): 
Enter passphrase (empty for no passphrase): 
Enter same passphrase again: 
Your identification has been saved in /home/vagrant/.ssh/id_rsa
Your public key has been saved in /home/vagrant/.ssh/id_rsa.pub
The key fingerprint is:
SHA256:FB1fg1JgLKourknfPKbC5TKxBTLmPs60tFxDJuyksbg vagrant@vagrant
The key's randomart image is:
+---[RSA 3072]----+
|        .o++..o  |
|        .o+... . |
|       ... ..    |
|+o    ..         |
|==.o .  S        |
|==+o.            |
|*=*+             |
|*@*.=o           |
|EO*+oo.          |
+----[SHA256]-----+

# Копируем ключ со второй машины на первую, коннектимся. 
vagrant@vagrant:~$ ssh-copy-id vagrant@192.168.0.119
/usr/bin/ssh-copy-id: INFO: Source of key(s) to be installed: "/home/vagrant/.ssh/id_rsa.pub"
/usr/bin/ssh-copy-id: INFO: attempting to log in with the new key(s), to filter out any that are already installed
/usr/bin/ssh-copy-id: INFO: 1 key(s) remain to be installed -- if you are prompted now it is to install the new keys
vagrant@192.168.0.119's password: 

Number of key(s) added: 1

Now try logging into the machine, with:   "ssh 'vagrant@192.168.0.119'"
and check to make sure that only the key(s) you wanted were added.

vagrant@vagrant:~$ ssh 'vagrant@192.168.0.119'
vagrant@192.168.0.119's password: 
Welcome to Ubuntu 20.04.3 LTS (GNU/Linux 5.4.0-91-generic x86_64)

 * Documentation:  https://help.ubuntu.com
 * Management:     https://landscape.canonical.com
 * Support:        https://ubuntu.com/advantage

  System information as of Thu 03 Feb 2022 06:02:59 PM UTC

  System load:  0.0                Processes:             119
  Usage of /:   11.8% of 30.88GB   Users logged in:       1
  Memory usage: 21%                IPv4 address for eth0: 10.0.2.15
  Swap usage:   0%                 IPv4 address for eth1: 192.168.0.119


This system is built by the Bento project by Chef Software
More information can be found at https://github.com/chef/bento
Last login: Thu Feb  3 17:44:30 2022 from 10.0.2.2
vagrant@vagrant:~$ logout
Connection to 192.168.0.119 closed.
```

---
Вопрос 6: Переименуйте файлы ключей из задания 5. Настройте файл конфигурации ```SSH клиента```, так чтобы вход на удаленный сервер осуществлялся по имени сервера.

Ответ: 

```
# Переименовываем файл ключей на второй машине
vagrant@vagrant:~$ cd /home/vagrant/.ssh
vagrant@vagrant:~/.ssh$ ls
authorized_keys  id_rsa  id_rsa.pub  known_hosts
vagrant@vagrant:~/.ssh$ mv id_rsa id_rrssaa
vagrant@vagrant:~/.ssh$ mv id_rsa.pub id_rrssaa.pub
vagrant@vagrant:~/.ssh$ ls
authorized_keys  id_rrssaa  id_rrssaa.pub  known_hosts

# Создаем файл конфига
vagrant@vagrant:~/.ssh$ cd ~
vagrant@vagrant:~$ mkdir -p ~/.ssh && chmod 700 ~/.ssh
vagrant@vagrant:~$ touch ~/.ssh/config && chmod 600 ~/.ssh/config
vagrant@vagrant:~$ cd ~/.ssh
vagrant@vagrant:~/.ssh$ ls
authorized_keys  config  id_rrssaa  id_rrssaa.pub  known_hosts
vagrant@vagrant:~/.ssh$ nano config
vagrant@vagrant:~/.ssh$ cat config
Host my_server
	HostName 192.168.1.119
	IdentityFile ~/.ssh/id_rrssaa
	User vagrant
	Port 2222
	StrictHostKeyChecking no
	

```

---
Вопрос 7: Соберите дамп трафика утилитой ```tcpdump``` в формате ```pcap```, 100 пакетов. Откройте файл pcap в Wireshark.

Ответ: 

```
vagrant@vagrant:~$ sudo -i
root@vagrant:~# apt install tcpdump
Reading package lists... Done
Building dependency tree       
Reading state information... Done
tcpdump is already the newest version (4.9.3-4).
0 upgraded, 0 newly installed, 0 to remove and 0 not upgraded.
root@vagrant:~# tcpdump -D
1.eth0 [Up, Running]
2.lo [Up, Running, Loopback]
3.any (Pseudo-device that captures on all interfaces) [Up, Running]
4.bluetooth-monitor (Bluetooth Linux Monitor) [none]
5.nflog (Linux netfilter log (NFLOG) interface) [none]
6.nfqueue (Linux netfilter queue (NFQUEUE) interface) [none]
root@vagrant:~# tcpdump -i eth0 -c 100 -w icmp.pcap
tcpdump: listening on eth0, link-type EN10MB (Ethernet), capture size 262144 bytes
root@vagrant:~# tcpdump -r icmp.pcap
reading from file icmp.pcap, link-type EN10MB (Ethernet)
18:28:20.371260 IP vagrant.ssh > _gateway.59012: Flags [P.], seq 3005316595:3005316703, ack 19601255, win 62780, length 108
18:28:20.371610 IP _gateway.59012 > vagrant.ssh: Flags [.], ack 108, win 65535, length 0
18:28:22.922779 IP _gateway.59012 > vagrant.ssh: Flags [P.], seq 1:37, ack 108, win 65535, length 36
18:28:22.922924 IP vagrant.ssh > _gateway.59012: Flags [P.], seq 108:144, ack 37, win 62780, length 36
18:28:22.923110 IP _gateway.59012 > vagrant.ssh: Flags [.], ack 144, win 65535, length 0
18:28:23.004374 IP _gateway.59012 > vagrant.ssh: Flags [P.], seq 37:73, ack 144, win 65535, length 36
18:28:23.004496 IP vagrant.ssh > _gateway.59012: Flags [P.], seq 144:180, ack 73, win 62780, length 36
18:28:23.004602 IP _gateway.59012 > vagrant.ssh: Flags [.], ack 180, win 65535, length 0
18:28:23.192685 IP _gateway.59012 > vagrant.ssh: Flags [P.], seq 73:109, ack 180, win 65535, length 36
18:28:23.192795 IP vagrant.ssh > _gateway.59012: Flags [P.], seq 180:216, ack 109, win 62780, length 36
18:28:23.192982 IP _gateway.59012 > vagrant.ssh: Flags [.], ack 216, win 65535, length 0
18:28:24.014366 IP _gateway.59012 > vagrant.ssh: Flags [P.], seq 109:145, ack 216, win 65535, length 36
18:28:24.014494 IP vagrant.ssh > _gateway.59012: Flags [P.], seq 216:252, ack 145, win 62780, length 36
18:28:24.014677 IP _gateway.59012 > vagrant.ssh: Flags [.], ack 252, win 65535, length 0
18:28:25.767082 IP _gateway.59012 > vagrant.ssh: Flags [P.], seq 145:181, ack 252, win 65535, length 36
18:28:25.767231 IP vagrant.ssh > _gateway.59012: Flags [P.], seq 252:288, ack 181, win 62780, length 36
18:28:25.767486 IP _gateway.59012 > vagrant.ssh: Flags [.], ack 288, win 65535, length 0
18:28:26.595279 IP _gateway.59012 > vagrant.ssh: Flags [P.], seq 181:217, ack 288, win 65535, length 36
18:28:26.595407 IP vagrant.ssh > _gateway.59012: Flags [P.], seq 288:324, ack 217, win 62780, length 36
18:28:26.595597 IP _gateway.59012 > vagrant.ssh: Flags [.], ack 324, win 65535, length 0
18:28:27.166809 IP _gateway.59012 > vagrant.ssh: Flags [P.], seq 217:253, ack 324, win 65535, length 36
18:28:27.166954 IP vagrant.ssh > _gateway.59012: Flags [P.], seq 324:360, ack 253, win 62780, length 36
18:28:27.167283 IP _gateway.59012 > vagrant.ssh: Flags [.], ack 360, win 65535, length 0
18:28:27.445420 IP _gateway.59012 > vagrant.ssh: Flags [P.], seq 253:289, ack 360, win 65535, length 36
18:28:27.445545 IP vagrant.ssh > _gateway.59012: Flags [P.], seq 360:396, ack 289, win 62780, length 36
18:28:27.445687 IP _gateway.59012 > vagrant.ssh: Flags [.], ack 396, win 65535, length 0
18:28:28.034246 IP _gateway.59012 > vagrant.ssh: Flags [P.], seq 289:325, ack 396, win 65535, length 36
18:28:28.034402 IP vagrant.ssh > _gateway.59012: Flags [P.], seq 396:432, ack 325, win 62780, length 36
18:28:28.034574 IP _gateway.59012 > vagrant.ssh: Flags [.], ack 432, win 65535, length 0
18:28:29.542991 IP _gateway.59012 > vagrant.ssh: Flags [P.], seq 325:361, ack 432, win 65535, length 36
18:28:29.543169 IP vagrant.ssh > _gateway.59012: Flags [P.], seq 432:468, ack 361, win 62780, length 36
18:28:29.543449 IP _gateway.59012 > vagrant.ssh: Flags [.], ack 468, win 65535, length 0
18:28:29.826495 IP _gateway.59012 > vagrant.ssh: Flags [P.], seq 361:397, ack 468, win 65535, length 36
18:28:29.826647 IP vagrant.ssh > _gateway.59012: Flags [P.], seq 468:504, ack 397, win 62780, length 36
18:28:29.826916 IP _gateway.59012 > vagrant.ssh: Flags [.], ack 504, win 65535, length 0
18:28:29.926782 IP _gateway.59012 > vagrant.ssh: Flags [P.], seq 397:433, ack 504, win 65535, length 36
18:28:29.926904 IP vagrant.ssh > _gateway.59012: Flags [P.], seq 504:540, ack 433, win 62780, length 36
18:28:29.927070 IP _gateway.59012 > vagrant.ssh: Flags [.], ack 540, win 65535, length 0
18:28:30.296413 IP _gateway.59012 > vagrant.ssh: Flags [P.], seq 433:469, ack 540, win 65535, length 36
18:28:30.296715 IP vagrant.ssh > _gateway.59012: Flags [P.], seq 540:576, ack 469, win 62780, length 36
18:28:30.296902 IP _gateway.59012 > vagrant.ssh: Flags [.], ack 576, win 65535, length 0
18:28:30.440121 IP _gateway.59012 > vagrant.ssh: Flags [P.], seq 469:505, ack 576, win 65535, length 36
18:28:30.440243 IP vagrant.ssh > _gateway.59012: Flags [P.], seq 576:612, ack 505, win 62780, length 36
18:28:30.440502 IP _gateway.59012 > vagrant.ssh: Flags [.], ack 612, win 65535, length 0
18:28:30.601106 IP _gateway.59012 > vagrant.ssh: Flags [P.], seq 505:541, ack 612, win 65535, length 36
18:28:30.601237 IP vagrant.ssh > _gateway.59012: Flags [P.], seq 612:648, ack 541, win 62780, length 36
18:28:30.601460 IP _gateway.59012 > vagrant.ssh: Flags [.], ack 648, win 65535, length 0
18:28:30.807300 IP _gateway.59012 > vagrant.ssh: Flags [P.], seq 541:577, ack 648, win 65535, length 36
18:28:30.807419 IP vagrant.ssh > _gateway.59012: Flags [P.], seq 648:684, ack 577, win 62780, length 36
18:28:30.807589 IP _gateway.59012 > vagrant.ssh: Flags [.], ack 684, win 65535, length 0
18:28:30.922426 IP _gateway.59012 > vagrant.ssh: Flags [P.], seq 577:613, ack 684, win 65535, length 36
18:28:30.922571 IP vagrant.ssh > _gateway.59012: Flags [P.], seq 684:720, ack 613, win 62780, length 36
18:28:30.922774 IP _gateway.59012 > vagrant.ssh: Flags [.], ack 720, win 65535, length 0
18:28:31.007864 IP _gateway.59012 > vagrant.ssh: Flags [P.], seq 613:649, ack 720, win 65535, length 36
18:28:31.007981 IP vagrant.ssh > _gateway.59012: Flags [P.], seq 720:756, ack 649, win 62780, length 36
18:28:31.008121 IP _gateway.59012 > vagrant.ssh: Flags [.], ack 756, win 65535, length 0
18:28:31.638662 IP _gateway.59012 > vagrant.ssh: Flags [P.], seq 649:685, ack 756, win 65535, length 36
18:28:31.638816 IP vagrant.ssh > _gateway.59012: Flags [P.], seq 756:792, ack 685, win 62780, length 36
18:28:31.638980 IP _gateway.59012 > vagrant.ssh: Flags [.], ack 792, win 65535, length 0
18:28:32.114690 IP _gateway.59012 > vagrant.ssh: Flags [P.], seq 685:721, ack 792, win 65535, length 36
18:28:32.114915 IP vagrant.ssh > _gateway.59012: Flags [P.], seq 792:828, ack 721, win 62780, length 36
18:28:32.115122 IP _gateway.59012 > vagrant.ssh: Flags [.], ack 828, win 65535, length 0
18:28:55.224871 IP6 vagrant > ip6-allrouters: ICMP6, router solicitation, length 16
18:30:38.107355 IP _gateway.59012 > vagrant.ssh: Flags [P.], seq 721:757, ack 828, win 65535, length 36
18:30:38.156820 IP vagrant.ssh > _gateway.59012: Flags [.], ack 757, win 62780, length 0
18:30:43.287649 ARP, Request who-has _gateway tell vagrant, length 28
18:30:43.287891 ARP, Reply _gateway is-at 52:54:00:12:35:02 (oui Unknown), length 46
18:30:45.826545 IP _gateway.59487 > vagrant.ssh: Flags [S], seq 67840001, win 65535, options [mss 1460], length 0
18:30:45.826574 IP vagrant.ssh > _gateway.59487: Flags [S.], seq 1218737834, ack 67840002, win 64240, options [mss 1460], length 0
18:30:45.826714 IP _gateway.59487 > vagrant.ssh: Flags [.], ack 1, win 65535, length 0
18:30:45.827220 IP _gateway.59487 > vagrant.ssh: Flags [P.], seq 1:22, ack 1, win 65535, length 21
18:30:45.827228 IP vagrant.ssh > _gateway.59487: Flags [.], ack 22, win 64219, length 0
18:30:45.835005 IP vagrant.ssh > _gateway.59487: Flags [P.], seq 1:42, ack 22, win 64219, length 41
18:30:45.835184 IP _gateway.59487 > vagrant.ssh: Flags [.], ack 42, win 65535, length 0
18:30:45.835671 IP _gateway.59487 > vagrant.ssh: Flags [P.], seq 22:1534, ack 42, win 65535, length 1512
18:30:45.835679 IP vagrant.ssh > _gateway.59487: Flags [.], ack 1534, win 62780, length 0
18:30:45.836130 IP vagrant.ssh > _gateway.59487: Flags [P.], seq 42:1098, ack 1534, win 62780, length 1056
18:30:45.836269 IP _gateway.59487 > vagrant.ssh: Flags [.], ack 1098, win 65535, length 0
18:30:45.838191 IP _gateway.59487 > vagrant.ssh: Flags [P.], seq 1534:1582, ack 1098, win 65535, length 48
18:30:45.838196 IP vagrant.ssh > _gateway.59487: Flags [.], ack 1582, win 62780, length 0
18:30:45.843237 IP vagrant.ssh > _gateway.59487: Flags [P.], seq 1098:1534, ack 1582, win 62780, length 436
18:30:45.843385 IP _gateway.59487 > vagrant.ssh: Flags [.], ack 1534, win 65535, length 0
18:30:45.846875 IP _gateway.59487 > vagrant.ssh: Flags [P.], seq 1582:1598, ack 1534, win 65535, length 16
18:30:45.846882 IP vagrant.ssh > _gateway.59487: Flags [.], ack 1598, win 62780, length 0
18:30:45.847074 IP _gateway.59487 > vagrant.ssh: Flags [P.], seq 1598:1642, ack 1534, win 65535, length 44
18:30:45.847079 IP vagrant.ssh > _gateway.59487: Flags [.], ack 1642, win 62780, length 0
18:30:45.847125 IP vagrant.ssh > _gateway.59487: Flags [P.], seq 1534:1578, ack 1642, win 62780, length 44
18:30:45.847277 IP _gateway.59487 > vagrant.ssh: Flags [.], ack 1578, win 65535, length 0
18:30:45.847375 IP _gateway.59487 > vagrant.ssh: Flags [P.], seq 1642:1710, ack 1578, win 65535, length 68
18:30:45.854806 IP vagrant.ssh > _gateway.59487: Flags [P.], seq 1578:1630, ack 1710, win 62780, length 52
18:30:45.855092 IP _gateway.59487 > vagrant.ssh: Flags [.], ack 1630, win 65535, length 0
18:30:45.857888 IP _gateway.59487 > vagrant.ssh: Flags [P.], seq 1710:2362, ack 1630, win 65535, length 652
18:30:45.865739 IP vagrant.ssh > _gateway.59487: Flags [P.], seq 1630:1658, ack 2362, win 62780, length 28
18:30:45.866132 IP _gateway.59487 > vagrant.ssh: Flags [.], ack 1658, win 65535, length 0
18:30:45.866623 IP _gateway.59487 > vagrant.ssh: Flags [P.], seq 2362:2474, ack 1658, win 65535, length 112
18:30:45.907757 IP vagrant.ssh > _gateway.59487: Flags [.], ack 2474, win 62780, length 0
18:30:46.163364 IP vagrant.ssh > _gateway.59487: Flags [P.], seq 1658:2418, ack 2474, win 62780, length 760
18:30:46.163553 IP _gateway.59487 > vagrant.ssh: Flags [.], ack 2418, win 65535, length 0
18:30:46.163585 IP vagrant.ssh > _gateway.59487: Flags [P.], seq 2418:2454, ack 2474, win 62780, length 36
18:30:46.163730 IP _gateway.59487 > vagrant.ssh: Flags [.], ack 2454, win 65535, length 0
```