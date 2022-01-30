Вопрос 1: Подключитесь к публичному маршрутизатору в интернет. Найдите маршрут к вашему публичному IP

```
telnet route-views.routeviews.org
Username: rviews
show ip route x.x.x.x/32
show bgp x.x.x.x/32
```

Ответ: 

```
route-views>show ip route 5.18.159.103 
Routing entry for 5.18.156.0/22
  Known via "bgp 6447", distance 20, metric 0
  Tag 6939, type external
  Last update from 64.71.137.241 6d02h ago
  Routing Descriptor Blocks:
  * 64.71.137.241, from 64.71.137.241, 6d02h ago
      Route metric is 0, traffic share count is 1
      AS Hops 3
      Route tag 6939
      MPLS label: none
```

```
route-views>show ip route 5.18.159.103 255.255.255.255
% Subnet not in table
```

```
route-views>show ip route 192.168.0.255/32             
                                       ^
% Invalid input detected at '^' marker.
```

```
route-views>show bgp 5.18.159.103 
BGP routing table entry for 5.18.156.0/22, version 6194
Paths: (23 available, best #23, table default)
  Not advertised to any peer
  Refresh Epoch 1
  57866 1299 9049 41733
    37.139.139.17 from 37.139.139.17 (37.139.139.17)
      Origin IGP, metric 0, localpref 100, valid, external
      Community: 1299:30000 57866:100 57866:101 57866:501
      path 7FE170382E08 RPKI State not found
      rx pathid: 0, tx pathid: 0
  Refresh Epoch 1
  3561 209 3356 1299 9049 41733
    206.24.210.80 from 206.24.210.80 (206.24.210.80)
      Origin IGP, localpref 100, valid, external
      path 7FE130F62C08 RPKI State not found
      rx pathid: 0, tx pathid: 0
  Refresh Epoch 1
  3333 1103 20562 9049 41733
    193.0.0.56 from 193.0.0.56 (193.0.0.56)
      Origin IGP, localpref 100, valid, external
      Community: 20562:45 20562:4001
      path 7FE13B378888 RPKI State not found
      rx pathid: 0, tx pathid: 0
  Refresh Epoch 1
  1351 6939 9049 41733
    132.198.255.253 from 132.198.255.253 (132.198.255.253)
      Origin IGP, localpref 100, valid, external
      path 7FE133939978 RPKI State not found
      rx pathid: 0, tx pathid: 0
  Refresh Epoch 1
  8283 1299 9049 41733
    94.142.247.3 from 94.142.247.3 (94.142.247.3)
      Origin incomplete, metric 0, localpref 100, valid, external
      Community: 1299:30000 8283:1 8283:101
      unknown transitive attribute: flag 0xE0 type 0x20 length 0x18
        value 0000 205B 0000 0000 0000 0001 0000 205B
              0000 0005 0000 0001 
      path 7FE08BE4E5E8 RPKI State not found
      rx pathid: 0, tx pathid: 0
  Refresh Epoch 1
  852 1299 9049 41733
    154.11.12.212 from 154.11.12.212 (96.1.209.43)
      Origin IGP, metric 0, localpref 100, valid, external
      path 7FE0B5E52AD0 RPKI State not found
      rx pathid: 0, tx pathid: 0
  Refresh Epoch 1
  20130 6939 9049 41733
    140.192.8.16 from 140.192.8.16 (140.192.8.16)
      Origin IGP, localpref 100, valid, external
      path 7FE01B5B9820 RPKI State not found
      rx pathid: 0, tx pathid: 0
  Refresh Epoch 1
  7018 1299 9049 41733
    12.0.1.63 from 12.0.1.63 (12.0.1.63)
      Origin incomplete, localpref 100, valid, external
      Community: 7018:5000 7018:37232
      path 7FE0FC964808 RPKI State not found
      rx pathid: 0, tx pathid: 0
  Refresh Epoch 3
  3303 6939 9049 41733
    217.192.89.50 from 217.192.89.50 (138.187.128.158)
      Origin IGP, localpref 100, valid, external
      Community: 3303:1006 3303:1021 3303:1030 3303:3067 6939:7040 6939:8752 6939:9002
      path 7FE144366288 RPKI State not found
      rx pathid: 0, tx pathid: 0
  Refresh Epoch 1
  4901 6079 1299 9049 41733
    162.250.137.254 from 162.250.137.254 (162.250.137.254)
      Origin incomplete, localpref 100, valid, external
      Community: 65000:10100 65000:10300 65000:10400
      path 7FE0E022E650 RPKI State not found
      rx pathid: 0, tx pathid: 0
  Refresh Epoch 1
  53767 174 174 1299 9049 41733
    162.251.163.2 from 162.251.163.2 (162.251.162.3)
      Origin incomplete, localpref 100, valid, external
      Community: 174:21000 174:22013 53767:5000
      path 7FE12667B378 RPKI State not found
      rx pathid: 0, tx pathid: 0
  Refresh Epoch 1
  20912 3257 1299 9049 41733
    212.66.96.126 from 212.66.96.126 (212.66.96.126)
      Origin incomplete, localpref 100, valid, external
      Community: 3257:8101 3257:30055 3257:50001 3257:53900 3257:53902 20912:65004
      path 7FE159BC64F0 RPKI State not found
      rx pathid: 0, tx pathid: 0
  Refresh Epoch 1
  3356 1299 9049 41733
    4.68.4.46 from 4.68.4.46 (4.69.184.201)
      Origin IGP, metric 0, localpref 100, valid, external
      Community: 3356:3 3356:22 3356:86 3356:575 3356:666 3356:903 3356:2012
      path 7FE0020138C0 RPKI State not found
      rx pathid: 0, tx pathid: 0
  Refresh Epoch 1
  3549 3356 1299 9049 41733
    208.51.134.254 from 208.51.134.254 (67.16.168.191)
      Origin IGP, metric 0, localpref 100, valid, external
      Community: 3356:3 3356:22 3356:86 3356:575 3356:666 3356:903 3356:2011 3549:2581 3549:30840
      path 7FE16D97A828 RPKI State not found
      rx pathid: 0, tx pathid: 0
  Refresh Epoch 1
  101 3356 1299 9049 41733
    209.124.176.223 from 209.124.176.223 (209.124.176.223)
      Origin IGP, localpref 100, valid, external
      Community: 101:20100 101:20110 101:22100 3356:3 3356:22 3356:86 3356:575 3356:666 3356:903 3356:2012
      Extended Community: RT:101:22100
      path 7FE121EAAE00 RPKI State not found
      rx pathid: 0, tx pathid: 0
  Refresh Epoch 1
  7660 2516 1299 9049 41733
    203.181.248.168 from 203.181.248.168 (203.181.248.168)
      Origin incomplete, localpref 100, valid, external
      Community: 2516:1030 7660:9003
      path 7FE16BA6DFC8 RPKI State not found
      rx pathid: 0, tx pathid: 0
  Refresh Epoch 1
  2497 1299 9049 41733
    202.232.0.2 from 202.232.0.2 (58.138.96.254)
      Origin incomplete, localpref 100, valid, external
      path 7FE142A475B0 RPKI State not found
      rx pathid: 0, tx pathid: 0
  Refresh Epoch 1
  49788 1299 9049 41733
    91.218.184.60 from 91.218.184.60 (91.218.184.60)
      Origin incomplete, localpref 100, valid, external
      Community: 1299:30000
      Extended Community: 0x43:100:1
      path 7FE17CAF8448 RPKI State not found
      rx pathid: 0, tx pathid: 0
  Refresh Epoch 1
  1221 4637 1299 9049 41733
    203.62.252.83 from 203.62.252.83 (203.62.252.83)
      Origin incomplete, localpref 100, valid, external
      path 7FE034E4DD50 RPKI State not found
      rx pathid: 0, tx pathid: 0
  Refresh Epoch 1
  701 1299 9049 41733
    137.39.3.55 from 137.39.3.55 (137.39.3.55)
      Origin incomplete, localpref 100, valid, external
      path 7FE16FE9FBA0 RPKI State not found
      rx pathid: 0, tx pathid: 0
  Refresh Epoch 1
  3257 1299 9049 41733
    89.149.178.10 from 89.149.178.10 (213.200.83.26)
      Origin incomplete, metric 10, localpref 100, valid, external
      Community: 3257:8794 3257:30052 3257:50001 3257:54900 3257:54901
      path 7FE179B389E8 RPKI State not found
      rx pathid: 0, tx pathid: 0
  Refresh Epoch 1
  19214 174 1299 9049 41733
    208.74.64.40 from 208.74.64.40 (208.74.64.40)
      Origin incomplete, localpref 100, valid, external
      Community: 174:21000 174:22013
      path 7FE0FE2365F8 RPKI State not found
      rx pathid: 0, tx pathid: 0
  Refresh Epoch 1
  6939 9049 41733
    64.71.137.241 from 64.71.137.241 (216.218.252.164)
      Origin IGP, localpref 100, valid, external, best
      path 7FE16C9F32C8 RPKI State not found
      rx pathid: 0, tx pathid: 0x0
```

```
route-views>show bgp 5.18.159.103/32        
% Network not in table
```

```
route-views>show bgp 5.18.159.103 255.255.255.255
% Network not in table
```

---

Вопрос 2: Создайте dummy0 интерфейс в Ubuntu. Добавьте несколько статических маршрутов. Проверьте таблицу маршрутизации.

Ответ: 

```
vagrant@vagrant:~$ sudo -i
root@vagrant:~# ip link add dummy0 type dummy
root@vagrant:~# ip link set dummy0 up
root@vagrant:~# ip a
1: lo: <LOOPBACK,UP,LOWER_UP> mtu 65536 qdisc noqueue state UNKNOWN group default qlen 1000
    link/loopback 00:00:00:00:00:00 brd 00:00:00:00:00:00
    inet 127.0.0.1/8 scope host lo
       valid_lft forever preferred_lft forever
    inet6 ::1/128 scope host 
       valid_lft forever preferred_lft forever
2: eth0: <BROADCAST,MULTICAST,UP,LOWER_UP> mtu 1500 qdisc fq_codel state UP group default qlen 1000
    link/ether 08:00:27:b1:28:5d brd ff:ff:ff:ff:ff:ff
    inet 10.0.2.15/24 brd 10.0.2.255 scope global dynamic eth0
       valid_lft 85703sec preferred_lft 85703sec
    inet6 fe80::a00:27ff:feb1:285d/64 scope link 
       valid_lft forever preferred_lft forever
3: dummy0: <BROADCAST,NOARP,UP,LOWER_UP> mtu 1500 qdisc noqueue state UNKNOWN group default qlen 1000
    link/ether 9e:1d:0e:64:f0:61 brd ff:ff:ff:ff:ff:ff
    inet6 fe80::9c1d:eff:fe64:f061/64 scope link 
       valid_lft forever preferred_lft forever
root@vagrant:~# ip ro add 10.0.2.1 via 10.0.2.2
root@vagrant:~# ip ro add 10.0.2.3 via 10.0.2.2
root@vagrant:~# ip ro add 10.0.2.4 via 10.0.2.2
root@vagrant:~# ip route
default via 10.0.2.2 dev eth0 proto dhcp src 10.0.2.15 metric 100 
10.0.2.0/24 dev eth0 proto kernel scope link src 10.0.2.15 
10.0.2.1 via 10.0.2.2 dev eth0 
10.0.2.2 dev eth0 proto dhcp scope link src 10.0.2.15 metric 100 
10.0.2.3 via 10.0.2.2 dev eth0 
10.0.2.4 via 10.0.2.2 dev eth0 
```

---

Вопрос 3: Проверьте открытые TCP порты в Ubuntu, какие протоколы и приложения используют эти порты? Приведите несколько примеров. 

Ответ: 

```
root@vagrant:~# lsof -nP -i | grep TCP | grep LISTEN
systemd-r   600 systemd-resolve   13u  IPv4  20943      0t0  TCP 127.0.0.53:53 (LISTEN)
sshd        819            root    3u  IPv4  24963      0t0  TCP *:22 (LISTEN)
sshd        819            root    4u  IPv6  24965      0t0  TCP *:22 (LISTEN)
...
root@vagrant:~# lsof -nP -i | grep TCP
systemd-r   600 systemd-resolve   13u  IPv4  20943      0t0  TCP 127.0.0.53:53 (LISTEN)
sshd        819            root    3u  IPv4  24963      0t0  TCP *:22 (LISTEN)
sshd        819            root    4u  IPv6  24965      0t0  TCP *:22 (LISTEN)
sshd      13923            root    4u  IPv4  43924      0t0  TCP 10.0.2.15:22->10.0.2.2:63147 (ESTABLISHED)
sshd      13970         vagrant    4u  IPv4  43924      0t0  TCP 10.0.2.15:22->10.0.2.2:63147 (ESTABLISHED)
```

---

Вопрос 4: Проверьте используемые UDP сокеты в Ubuntu, какие протоколы и приложения используют эти порты?

Ответ: 

```
root@vagrant:~# lsof -nP -i | grep UDP | grep LISTEN 
root@vagrant:~# lsof -nP -i | grep UDP
systemd-n   598 systemd-network   19u  IPv4  20923      0t0  UDP 10.0.2.15:68 
systemd-r   600 systemd-resolve   12u  IPv4  20942      0t0  UDP 127.0.0.53:53 
```

---

Вопрос 5: Используя diagrams.net, создайте L3 диаграмму вашей домашней сети или любой другой сети, с которой вы работали.

Ответ: схема во вложении. 