Задача 1:   
Сценарий выполения задачи:
- создайте свой репозиторий на https://hub.docker.com; 
- выберете любой образ, который содержит веб-сервер Nginx; 
- создайте свой fork образа; 
- реализуйте функциональность: запуск веб-сервера в фоне с индекс-страницей, содержащей HTML-код ниже:
```
<html>
<head>
Hey, Netology
</head>
<body>
<h1>I’m DevOps Engineer!</h1>
</body>
</html>
```

Опубликуйте созданный форк в своем репозитории и предоставьте ответ в виде ссылки на https://hub.docker.com/username_repo.

Ответ:
```
https://hub.docker.com/repository/docker/edr1an/homework
```

---
Задача 2:   
Посмотрите на сценарий ниже и ответьте на вопрос: "Подходит ли в этом сценарии использование Docker контейнеров или лучше подойдет виртуальная машина, физическая машина? Может быть возможны разные варианты?"

Детально опишите и обоснуйте свой выбор.

--

Сценарий:

- Высоконагруженное монолитное java веб-приложение; 
- Nodejs веб-приложение; 
- Мобильное приложение c версиями для Android и iOS; 
- Шина данных на базе Apache Kafka; 
- Elasticsearch кластер для реализации логирования продуктивного веб-приложения - три ноды elasticsearch, два logstash и две ноды kibana; 
- Мониторинг-стек на базе Prometheus и Grafana; 
- MongoDB, как основное хранилище данных для java-приложения; 
- Gitlab сервер для реализации CI/CD процессов и приватный (закрытый) Docker Registry.

Ответ:
- ```Высоконагруженное монолитное java веб-приложение.```    
В целом, можно спользовать докер, если оно небольшое. Но в идеале для него использовать физический сервер - у нас высокая нагрузка, к тому же на монолитной архитектуре придется столкнуться с трудностями с разворачиванием в контейнерах. 
- ```Nodejs веб-приложение.```   
Вполне подойдет контейнеризация докером, каких-то проблем не должно быть. 
- ```Мобильное приложение c версиями для Android и iOS.```   
У докера нет интерфейса, он тут не подойдет. 
- ```Шина данных на базе Apache Kafka.```   
Если для нас некритичны данные, которые пропадут в случае потери контейнера, можно использовать Docker. В противном случае я бы использовал виртуальную машну. 
- ```Elasticsearch кластер для реализации логирования продуктивного веб-приложения - три ноды elasticsearch, два logstash и две ноды kibana.```   
Подойдет и докер, и виртуальные машины - нашел несколько решений. По ощущению - Elasticsearch я бы точно оставил бы на виртуальной машине, для отказоустойчивости. А logstash и kibana оставил бы в docker.
- ```Мониторинг-стек на базе Prometheus и Grafana.```   
Мы не храним никаких данных - я бы развернул в докере. 
- ```MongoDB, как основное хранилище данных для java-приложения.```   
Если высоконагруженная - железный сервер, если нет - виртуальная машина. Докер не подойдет потому, что можем потерять данные при потере контейнера.
- ```Gitlab сервер для реализации CI/CD процессов и приватный (закрытый) Docker Registry.```   
Идеально подойдет Docker, данных не храним, нужна только реализация процессов. 


---
Задача 3:   
- Запустите первый контейнер из образа centos c любым тэгом в фоновом режиме, подключив папку /data из текущей рабочей директории на хостовой машине в /data контейнера; 
- Запустите второй контейнер из образа debian в фоновом режиме, подключив папку /data из текущей рабочей директории на хостовой машине в /data контейнера; 
- Подключитесь к первому контейнеру с помощью docker exec и создайте текстовый файл любого содержания в /data; 
- Добавьте еще один файл в папку /data на хостовой машине; 
- Подключитесь во второй контейнер и отобразите листинг и содержание файлов в /data контейнера.

Ответ:
```
#Скачал образы
georgijsivkov@MacBook-Pro-Georgij devops-netology % docker pull centos
...
georgijsivkov@MacBook-Pro-Georgij devops-netology % docker pull debian
...

# Создал контейнеры со связкой на директорию /data на хостовой машине
georgijsivkov@MacBook-Pro-Georgij devops-netology % docker run -v /Users/georgijsivkov/PycharmProjects/Devops/devops-netology/data:/data --name my_centos -t -d centos
0a8dc07c730569e6b32e7d37d97829c394f76654696369d554d53515d7ceeed4
georgijsivkov@MacBook-Pro-Georgij devops-netology % docker run -v /Users/georgijsivkov/PycharmProjects/Devops/devops-netology/data:/data --name my_debian -t -d debian
a5fa820fc2465e11eaa688ea4a9de7fe68bc9ea20208b8c2fc67c41d49f4cca7
georgijsivkov@MacBook-Pro-Georgij devops-netology % docker ps
CONTAINER ID   IMAGE     COMMAND       CREATED          STATUS          PORTS     NAMES
a5fa820fc246   debian    "bash"        3 seconds ago    Up 2 seconds              my_debian
0a8dc07c7305   centos    "/bin/bash"   15 seconds ago   Up 14 seconds             my_centos

#Подключился к первому контейнеру и создал текстовый файл в директории /data
georgijsivkov@MacBook-Pro-Georgij devops-netology % docker exec -it my_centos /bin/bash
[root@0a8dc07c7305 /]# ls
bin  data  dev  etc  home  lib  lib64  lost+found  media  mnt  opt  proc  root  run  sbin  srv  sys  tmp  usr  var
[root@0a8dc07c7305 /]# cd data
[root@0a8dc07c7305 data]# echo Hello_world>new_file.txt
[root@0a8dc07c7305 data]# ls
new_file.txt
[root@0a8dc07c7305 data]# cat new_file.txt
Hello_world
[root@0a8dc07c7305 data]# exit

#Создал еще один файл в директории /data на хостовой машине
georgijsivkov@MacBook-Pro-Georgij devops-netology % cd data
georgijsivkov@MacBook-Pro-Georgij data % echo The_new_hello_world>one_more_new_file.txt
georgijsivkov@MacBook-Pro-Georgij data % ls
new_file.txt            one_more_new_file.txt
georgijsivkov@MacBook-Pro-Georgij data % 

#Подключился ко второму контейнеру и вывел листинг и содержание
georgijsivkov@MacBook-Pro-Georgij devops-netology % docker exec -it my_debian bash     
root@a5fa820fc246:/# cd data
root@a5fa820fc246:/data# ls
new_file.txt  one_more_new_file.txt
root@a5fa820fc246:/data# cat new_file.txt
Hello_world
root@a5fa820fc246:/data# cat one_more_new_file.txt
The_new_hello_world
root@a5fa820fc246:/data# 
exit
```

---