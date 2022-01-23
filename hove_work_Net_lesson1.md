Вопрос 1: Работа c HTTP через телнет.

- Подключитесь утилитой телнет к сайту stackoverflow.com telnet stackoverflow.com 80 
- отправьте HTTP запрос:

```
GET /questions HTTP/1.0
HOST: stackoverflow.com
[press enter]
[press enter]
```

- В ответе укажите полученный HTTP код, что он означает?

Ответ:

- Подключился
```
vagrant@vagrant:~$ telnet stackoverflow.com 80
Trying 151.101.129.69...
Connected to stackoverflow.com.
Escape character is '^]'.
```

- Отправил запрос. 

```
HTTP/1.1 301 Moved Permanently
cache-control: no-cache, no-store, must-revalidate
location: https://stackoverflow.com/questions
x-request-guid: 88ed4c63-e0a6-4867-9521-78375277d20d
feature-policy: microphone 'none'; speaker 'none'
content-security-policy: upgrade-insecure-requests; frame-ancestors 'self' https://stackexchange.com
Accept-Ranges: bytes
Date: Sun, 23 Jan 2022 15:43:35 GMT
Via: 1.1 varnish
Connection: close
X-Served-By: cache-hel1410029-HEL
X-Cache: MISS
X-Cache-Hits: 0
X-Timer: S1642952615.313697,VS0,VE109
Vary: Fastly-SSL
X-DNS-Prefetch-Control: off
Set-Cookie: prov=5ca84598-b145-27a5-7ffa-c219071ad059; domain=.stackoverflow.com; expires=Fri, 01-Jan-2055 00:00:00 GMT; path=/; HttpOnly

Connection closed by foreign host.
```
- В ответе 301 код - показывает, что запрошенный ресурс был окончательно перемещён в URL, указанный в заголовке Location

---
Вопрос 2: Повторите задание 1 в браузере, используя консоль разработчика F12. 
- откройте вкладку ```Network``` 
- отправьте запрос ```http://stackoverflow.com```
- найдите первый ответ ```HTTP сервера```, откройте вкладку ```Headers``` 
- укажите в ответе полученный ```HTTP код```. 
- проверьте время загрузки страницы, какой запрос обрабатывался дольше всего? 
- приложите скриншот консоли браузера в ответ.

Ответ:

- Первый ответ сервера - 307 Internal Redirect
- Полное время загрузки страницы 1.9 секунды. Самый долгий запрос beacon.js. 
- Скриншот в отдельном вложении (скриншот 1)

---
Вопрос 3: Какой IP адрес у вас в интернете?

Ответ:

```
5.18.159.103 
```

---
Вопрос 4: Какому провайдеру принадлежит ваш IP адрес? Какой автономной системе AS? Воспользуйтесь утилитой ```whois```

Ответ:

```
georgijsivkov@MacBook-Pro-Georgij ~ % whois 5.18.159.103    
...
role:           ER-Telecom ISP Contact Role
...
route:          5.18.0.0/16
descr:          Z-Telecom
origin:         AS41733
```

---
Вопрос 5: Через какие сети проходит пакет, отправленный с вашего компьютера на адрес 8.8.8.8? Через какие AS? Воспользуйтесь утилитой ```traceroute```

Ответ:

```
georgijsivkov@MacBook-Pro-Georgij ~ % traceroute 8.8.8.8
traceroute to 8.8.8.8 (8.8.8.8), 64 hops max, 52 byte packets
 1  192.168.0.1 (192.168.0.1)  3.053 ms  1.085 ms  1.110 ms
 2  10.93.58.1 (10.93.58.1)  2.815 ms  2.058 ms  2.040 ms
 3  5x19x2x250.static-business.spb.ertelecom.ru (5.19.2.250)  3.673 ms  5.362 ms  2.666 ms
 4  net131.234.188-158.ertelecom.ru (188.234.131.158)  3.037 ms  3.568 ms  3.525 ms
 5  net131.234.188-159.ertelecom.ru (188.234.131.159)  3.032 ms
    72.14.214.138 (72.14.214.138)  2.962 ms
    net131.234.188-159.ertelecom.ru (188.234.131.159)  4.733 ms
 6  * * *
 7  74.125.244.129 (74.125.244.129)  15.458 ms  4.914 ms
    209.85.245.238 (209.85.245.238)  2.933 ms
 8  74.125.244.180 (74.125.244.180)  3.863 ms
    74.125.244.181 (74.125.244.181)  3.783 ms
    74.125.244.133 (74.125.244.133)  5.231 ms
 9  72.14.232.84 (72.14.232.84)  3.539 ms
    72.14.232.85 (72.14.232.85)  3.279 ms
    142.251.51.187 (142.251.51.187)  7.925 ms
10  142.251.61.221 (142.251.61.221)  19.989 ms
    216.239.48.163 (216.239.48.163)  6.656 ms
    172.253.64.53 (172.253.64.53)  11.133 ms
11  142.250.208.23 (142.250.208.23)  8.425 ms * *
12  * * *
13  * * *
14  * * *
15  * * *
16  * * *
17  * * *
18  * * *
19  * * *
20  * * dns.google (8.8.8.8)  6.989 ms
```

```
georgijsivkov@MacBook-Pro-Georgij ~ % traceroute -an 8.8.8.8
traceroute to 8.8.8.8 (8.8.8.8), 64 hops max, 52 byte packets
 1  [AS0] 192.168.0.1  4.187 ms  15.813 ms  1.223 ms
 2  [AS0] 10.93.58.1  2.772 ms  3.287 ms  3.397 ms
 3  [AS41733] 5.19.2.250  2.963 ms  3.425 ms  3.637 ms
 4  [AS9049] 188.234.131.158  4.063 ms  3.241 ms  3.142 ms
 5  [AS15169] 72.14.214.138  3.821 ms
    [AS9049] 188.234.131.159  3.706 ms  3.004 ms
 6  * * *
 7  [AS15169] 74.125.244.129  4.968 ms
    [AS15169] 74.125.37.218  3.327 ms
    [AS15169] 74.125.244.129  4.488 ms
 8  [AS15169] 74.125.244.132  7.648 ms
    [AS15169] 74.125.244.181  9.243 ms
    [AS15169] 74.125.244.180  5.212 ms
 9  [AS15169] 142.251.61.219  34.914 ms
    [AS15169] 72.14.232.85  4.309 ms
    [AS15169] 142.251.61.219  9.338 ms
10  [AS15169] 142.251.61.221  8.604 ms
    [AS15169] 72.14.235.193  9.515 ms
    [AS15169] 142.250.56.221  8.911 ms
11  [AS15169] 216.239.49.3  8.475 ms
    [AS15169] 172.253.51.245  18.807 ms
    [AS15169] 172.253.51.247  8.493 ms
12  * * *
13  * * *
14  * * *
15  * * *
16  * * *
17  * * *
18  * * *
19  * * *
20  * * [AS0] 8.8.8.8  11.559 ms
```

---
Вопрос 6: Повторите задание 5 в утилите ```mtr```. На каком участке наибольшая задержка - ```delay```?

Ответ:

```
Keys:  Help   Display mode   Restart statistics   Order of fields   quit
                                                                   Packets               Pings
 Host                                                            Loss%   Snt   Last   Avg  Best  Wrst StDev
 1. AS???    10.0.2.2                                             0.0%    83    0.4   0.5   0.1   3.3   0.6
 2. AS???    192.168.0.1                                          0.0%    83    3.0   9.4   1.2  71.6  17.9
 3. AS???    10.93.58.1                                           1.2%    83    3.9   9.8   2.2  91.2  14.8
 4. AS41733  5.19.2.250                                           1.2%    83    8.2   6.2   2.9 129.4  14.2
 5. AS9049   188.234.131.158                                      2.4%    83    3.3  10.5   3.1 304.9  34.7
 6. AS15169  72.14.214.138                                        3.7%    83    3.1  14.6   3.0 304.5  51.1
 7. AS15169  74.125.244.129                                       1.2%    82   11.1  16.8   3.9 244.9  41.8
 8. AS15169  74.125.244.133                                       0.0%    82    3.4  16.0   3.0 262.9  39.9
 9. AS15169  142.251.61.221                                       0.0%    82    8.7  15.3   7.3 202.9  26.2
10. AS15169  142.250.209.171                                      1.2%    82    8.4  13.0   7.6 143.7  16.4
11. (waiting for reply)
12. (waiting for reply)
13. (waiting for reply)
14. (waiting for reply)
15. (waiting for reply)
16. (waiting for reply)
17. AS15169  8.8.8.8                                             65.9%    82    7.9  12.8   6.5  81.2  17.1
```

Большая задержка на этом AS
```
7. AS15169  74.125.244.129                                       1.2%    82   11.1  16.8   3.9 244.9  41.8
```

---
Вопрос 7: Какие DNS сервера отвечают за доменное имя ```dns.google```? Какие A записи? воспользуйтесь утилитой ```dig```

Ответ:

```
...
.			51983	IN	NS	m.root-servers.net.
.			51983	IN	NS	b.root-servers.net.
.			51983	IN	NS	c.root-servers.net.
.			51983	IN	NS	d.root-servers.net.
.			51983	IN	NS	e.root-servers.net.
.			51983	IN	NS	f.root-servers.net.
.			51983	IN	NS	g.root-servers.net.
.			51983	IN	NS	h.root-servers.net.
.			51983	IN	NS	a.root-servers.net.
.			51983	IN	NS	i.root-servers.net.
.			51983	IN	NS	j.root-servers.net.
.			51983	IN	NS	k.root-servers.net.
.			51983	IN	NS	l.root-servers.net.
...
google.			172800	IN	NS	ns-tld1.charlestonroadregistry.com.
google.			172800	IN	NS	ns-tld2.charlestonroadregistry.com.
google.			172800	IN	NS	ns-tld3.charlestonroadregistry.com.
google.			172800	IN	NS	ns-tld4.charlestonroadregistry.com.
google.			172800	IN	NS	ns-tld5.charlestonroadregistry.com.
...
dns.google.		10800	IN	NS	ns4.zdns.google.
dns.google.		10800	IN	NS	ns2.zdns.google.
dns.google.		10800	IN	NS	ns1.zdns.google.
dns.google.		10800	IN	NS	ns3.zdns.google
...
dns.google.		900	IN	A	8.8.4.4
dns.google.		900	IN	A	8.8.8.8
```

---
Вопрос 8: Проверьте PTR записи для IP адресов из задания 7. Какое доменное имя привязано к IP? воспользуйтесь утилитой ```dig```

Ответ:

```
vagrant@vagrant:~$ dig PTR @8.8.8.8 dns.google

; <<>> DiG 9.16.1-Ubuntu <<>> PTR @8.8.8.8 dns.google
; (1 server found)
;; global options: +cmd
;; Got answer:
;; ->>HEADER<<- opcode: QUERY, status: NOERROR, id: 61359
;; flags: qr rd ra ad; QUERY: 1, ANSWER: 0, AUTHORITY: 1, ADDITIONAL: 1

;; OPT PSEUDOSECTION:
; EDNS: version: 0, flags:; udp: 512
;; QUESTION SECTION:
;dns.google.			IN	PTR

;; AUTHORITY SECTION:
dns.google.		53	IN	SOA	ns1.zdns.google. cloud-dns-hostmaster.google.com. 1 21600 3600 259200 300

;; Query time: 12 msec
;; SERVER: 8.8.8.8#53(8.8.8.8)
;; WHEN: Sun Jan 23 17:09:25 UTC 2022
;; MSG SIZE  rcvd: 115
```

---
