Вопрос 1: Дайте письменые ответы на следующие вопросы:

Ответ:
- В чём отличие режимов работы сервисов в Docker Swarm кластере: replication и global?   
```
Replication - Мы самостоятельно указываем какое количество сервисов мы хотим запустить. 
Т.е. мы можем хотим запустить сервис только на 3 нодах из 6. 

Global - Сервис будет запущен на каждой ноде. 
Оркестратор самостоятельно будет запускать сервис на новой ноде. 
```
- Какой алгоритм выбора лидера используется в Docker Swarm кластере?   
```
Используется алгоритм поддержания распределенного консенсуса Raft
```
- Что такое Overlay Network?   
```
Сеть, созданная поверх другой сети. Яркий пример - VPN. 
```

---
Вопрос 2:
Создать ваш первый Docker Swarm кластер в Яндекс.Облаке   
Для получения зачета, вам необходимо предоставить скриншот из терминала (консоли), с выводом команды:   

Ответ: [Скриншот](https://github.com/GeorgySivkov/devops-netology/blob/main/src/%D0%A1%D0%BD%D0%B8%D0%BC%D0%BE%D0%BA%20%D1%8D%D0%BA%D1%80%D0%B0%D0%BD%D0%B0%202022-03-29%20%D0%B2%2021.05.02.png)
```
[root@node01 ~]# docker node ls
ID                            HOSTNAME             STATUS    AVAILABILITY   MANAGER STATUS   ENGINE VERSION
fkyd12175ppphy42xinod04tg *   node01.netology.yc   Ready     Active         Leader           20.10.14
uime8akunprmymwi7smj19oyq     node02.netology.yc   Ready     Active         Reachable        20.10.14
n2w7rs3c7pd6q09dst80kw0jn     node03.netology.yc   Ready     Active         Reachable        20.10.14
zrgck4575ndejii5eygi2zmx1     node04.netology.yc   Ready     Active                          20.10.14
yrym54whdettuhggbnjpixly7     node05.netology.yc   Ready     Active                          20.10.14
udbzsceb86xntnpvttdoaqv2q     node06.netology.yc   Ready     Active                          20.10.14
```
---
Вопрос 3: 
Создать ваш первый, готовый к боевой эксплуатации кластер мониторинга, состоящий из стека микросервисов.   
Для получения зачета, вам необходимо предоставить скриншот из терминала (консоли), с выводом команды:   

Ответ: [Скриншот](https://github.com/GeorgySivkov/devops-netology/blob/main/src/%D0%A1%D0%BD%D0%B8%D0%BC%D0%BE%D0%BA%20%D1%8D%D0%BA%D1%80%D0%B0%D0%BD%D0%B0%202022-03-29%20%D0%B2%2021.05.02.png)
```
[root@node01 ~]# docker service ls
ID             NAME                                MODE         REPLICAS   IMAGE                                          PORTS
l95xzgx2hjpe   swarm_monitoring_alertmanager       replicated   1/1        stefanprodan/swarmprom-alertmanager:v0.14.0    
ln1ckz07reqa   swarm_monitoring_caddy              replicated   1/1        stefanprodan/caddy:latest                      *:3000->3000/tcp, *:9090->9090/tcp, *:9093-9094->9093-9094/tcp
u3l26rij60r6   swarm_monitoring_cadvisor           global       6/6        google/cadvisor:latest                         
0gj5ep2nbmkg   swarm_monitoring_dockerd-exporter   global       6/6        stefanprodan/caddy:latest                      
q0bwiyq8bfdm   swarm_monitoring_grafana            replicated   1/1        stefanprodan/swarmprom-grafana:5.3.4           
f0rrwfrp151q   swarm_monitoring_node-exporter      global       6/6        stefanprodan/swarmprom-node-exporter:v0.16.0   
w3ptdzob8f1z   swarm_monitoring_prometheus         replicated   1/1        stefanprodan/swarmprom-prometheus:v2.5.0       
nkdu27a8988b   swarm_monitoring_unsee              replicated   1/1        cloudflare/unsee:v0.8.0   
```