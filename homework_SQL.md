## Задача 1

Используя docker поднимите инстанс PostgreSQL (версию 12) c 2 volume, 
в который будут складываться данные БД и бэкапы.

Приведите получившуюся команду или docker-compose манифест.

### Ответ: 

```
(venv) georgijsivkov@MacBook-Pro-Georgij homework % docker pull postgres:12
...
(venv) georgijsivkov@MacBook-Pro-Georgij homework % docker run --rm --name homework -e POSTGRES_PASSWORD=admin -ti -p 5432:5432 -v vol1:/var/lib/docker/volumes/vol1/_data -v vol2:/var/lib/docker/volumes/vol2/_data postgres:12
...
(venv) georgijsivkov@MacBook-Pro-Georgij homework % docker volume ls
DRIVER    VOLUME NAME
local     95a53979a1fc2e712e188addf133904fe5da7bdd71bf03cb472b31dca00bb42b
local     vol1
local     vol2
(venv) georgijsivkov@MacBook-Pro-Georgij homework % docker ps  
CONTAINER ID   IMAGE         COMMAND                  CREATED              STATUS              PORTS                    NAMES
f17e48add5eb   postgres:12   "docker-entrypoint.s…"   About a minute ago   Up About a minute   0.0.0.0:5432->5432/tcp   homework
```
---
## Задача 2

В БД из задачи 1: 
- создайте пользователя test-admin-user и БД test_db
- в БД test_db создайте таблицу orders и clients (спeцификация таблиц ниже)
- предоставьте привилегии на все операции пользователю test-admin-user на таблицы БД test_db
- создайте пользователя test-simple-user  
- предоставьте пользователю test-simple-user права на SELECT/INSERT/UPDATE/DELETE данных таблиц БД test_db

Таблица orders:
- id (serial primary key)
- наименование (string)
- цена (integer)

Таблица clients:
- id (serial primary key)
- фамилия (string)
- страна проживания (string, index)
- заказ (foreign key orders)

Приведите:
- итоговый список БД после выполнения пунктов выше,
- описание таблиц (describe)
- SQL-запрос для выдачи списка пользователей с правами над таблицами test_db
- список пользователей с правами над таблицами test_db

### Ответ: 

- итоговый список БД после выполнения пунктов выше
```
postgres=# \l
                                 List of databases
   Name    |  Owner   | Encoding |  Collate   |   Ctype    |   Access privileges   
-----------+----------+----------+------------+------------+-----------------------
 postgres  | postgres | UTF8     | en_US.utf8 | en_US.utf8 | 
 template0 | postgres | UTF8     | en_US.utf8 | en_US.utf8 | =c/postgres          +
           |          |          |            |            | postgres=CTc/postgres
 template1 | postgres | UTF8     | en_US.utf8 | en_US.utf8 | =c/postgres          +
           |          |          |            |            | postgres=CTc/postgres
 test_db   | postgres | UTF8     | en_US.utf8 | en_US.utf8 | 
(4 rows)
```
- описание таблиц (describe)
```
postgres=# SELECT column_name, column_default, data_type FROM INFORMATION_SCHEMA.COLUMNS WHERE table_name = 'clients';
 column_name | column_default | data_type 
-------------+----------------+-----------
 id          |                | integer
 lastname    |                | text
 country     |                | text
 booking     |                | integer
(4 rows)

postgres=# SELECT column_name, column_default, data_type FROM INFORMATION_SCHEMA.COLUMNS WHERE table_name = 'orders';
 column_name | column_default | data_type 
-------------+----------------+-----------
 id          |                | integer
 name        |                | text
 price       |                | integer
(3 rows)

```
- SQL-запрос для выдачи списка пользователей с правами над таблицами test_db
```
postgres=# select * from information_schema.table_privileges where grantee in ('test-admin-user','test-simple-user');
```
- список пользователей с правами над таблицами test_db  
```
 grantor  |     grantee      | table_catalog | table_schema | table_name | privilege_type | is_grantable | with_hierarchy 
----------+------------------+---------------+--------------+------------+----------------+--------------+----------------
 postgres | test-simple-user | postgres      | public       | clients    | INSERT         | NO           | NO
 postgres | test-simple-user | postgres      | public       | clients    | SELECT         | NO           | YES
 postgres | test-simple-user | postgres      | public       | clients    | UPDATE         | NO           | NO
 postgres | test-simple-user | postgres      | public       | clients    | DELETE         | NO           | NO
 postgres | test-simple-user | postgres      | public       | orders     | INSERT         | NO           | NO
 postgres | test-simple-user | postgres      | public       | orders     | SELECT         | NO           | YES
 postgres | test-simple-user | postgres      | public       | orders     | UPDATE         | NO           | NO
 postgres | test-simple-user | postgres      | public       | orders     | DELETE         | NO           | NO
(8 rows)
```
---
## Задача 3

Используя SQL синтаксис - наполните таблицы следующими тестовыми данными:

Таблица orders

|Наименование|цена|
|------------|----|
|Шоколад| 10 |
|Принтер| 3000 |
|Книга| 500 |
|Монитор| 7000|
|Гитара| 4000|

Таблица clients

|ФИО|Страна проживания|
|------------|----|
|Иванов Иван Иванович| USA |
|Петров Петр Петрович| Canada |
|Иоганн Себастьян Бах| Japan |
|Ронни Джеймс Дио| Russia|
|Ritchie Blackmore| Russia|

Используя SQL синтаксис:
- вычислите количество записей для каждой таблицы 
- приведите в ответе:
    - запросы 
    - результаты их выполнения.

### Ответ: 

```
postgres=# insert into orders VALUES (1, 'Шоколад', 10), (2, 'Принтер', 3000), (3, 'Книга', 500), (4, 'Монитор', 7000), (5, 'Гитара', 4000);
INSERT 0 5
postgres=# insert into clients VALUES (1, 'Иванов Иван Иванович', 'USA'), (2, 'Петров Петр Петрович', 'Canada'), (3, 'Иоганн Себастьян Бах', 'Japan'), (4, 'Ронни Джеймс Дио', 'Russia'), (5, 'Ritchie Blackmore', 'Russia');
INSERT 0 5
postgres=# select count (*) from orders;
 count 
-------
     5
(1 row)

postgres=# select count (*) from clients;
 count 
-------
     5
(1 row)
```

---
## Задача 4

Часть пользователей из таблицы clients решили оформить заказы из таблицы orders.

Используя foreign keys свяжите записи из таблиц, согласно таблице:

|ФИО|Заказ|
|------------|----|
|Иванов Иван Иванович| Книга |
|Петров Петр Петрович| Монитор |
|Иоганн Себастьян Бах| Гитара |

Приведите SQL-запросы для выполнения данных операций.

Приведите SQL-запрос для выдачи всех пользователей, которые совершили заказ, а также вывод данного запроса.
 
Подсказк - используйте директиву `UPDATE`.

### Ответ: 

```
postgres=# update  clients set booking = 3 where id = 1;
UPDATE 1
postgres=# update  clients set booking = 4 where id = 2;
UPDATE 1
postgres=# update  clients set booking = 5 where id = 3;
UPDATE 1
postgres=# select * from clients as c where  exists (select id from orders as o where c.booking = o.id) ;
 id |       lastname       | country | booking 
----+----------------------+---------+---------
  1 | Иванов Иван Иванович | USA     |       3
  2 | Петров Петр Петрович | Canada  |       4
  3 | Иоганн Себастьян Бах | Japan   |       5
(3 rows)

```
---
## Задача 5

Получите полную информацию по выполнению запроса выдачи всех пользователей из задачи 4 
(используя директиву EXPLAIN).

Приведите получившийся результат и объясните что значат полученные значения.

### Ответ:

- Показывает нагрузку на исполнение запроса. Показывает шаги, связи, сбор, сканирование таблиц после связи. 
```
postgres=# explain select * from clients as c where exists (select id from orders as o where c.booking = o.id);
                               QUERY PLAN                               
------------------------------------------------------------------------
 Hash Join  (cost=37.00..57.24 rows=810 width=72)
   Hash Cond: (c.booking = o.id)
   ->  Seq Scan on clients c  (cost=0.00..18.10 rows=810 width=72)
   ->  Hash  (cost=22.00..22.00 rows=1200 width=4)
         ->  Seq Scan on orders o  (cost=0.00..22.00 rows=1200 width=4)
(5 rows)
```
- Показывает стоимость запроса и фильтрацию по полю `booking` для выборки.
```
postgres=# explain select * from clients where booking is not null;
                        QUERY PLAN                         
-----------------------------------------------------------
 Seq Scan on clients  (cost=0.00..18.10 rows=806 width=72)
   Filter: (booking IS NOT NULL)
(2 rows)
```

---
## Задача 6

Создайте бэкап БД test_db и поместите его в volume, предназначенный для бэкапов (см. Задачу 1).

Остановите контейнер с PostgreSQL (но не удаляйте volumes).

Поднимите новый пустой контейнер с PostgreSQL.

Восстановите БД test_db в новом контейнере.

Приведите список операций, который вы применяли для бэкапа данных и восстановления. 

### Ответ: 

```
(venv) georgijsivkov@MacBook-Pro-Georgij homework % docker exec -t homework pg_dump -U postgres test_db -f /var/lib/docker/volumes/vol2/_data/dumb_test.sql
...
(venv) georgijsivkov@MacBook-Pro-Georgij homework % docker exec -i homework2 psql -U postgres -d test_db -f /var/lib/docker/volumes/vol2/_data/dumb_test.sql
(venv) georgijsivkov@MacBook-Pro-Georgij homework % docker exec -it 78031dc3572e bash                                                                          
root@78031dc3572e:/# psql -h localhost -p 5432 -U postgres -W
Password: 
psql (12.10 (Debian 12.10-1.pgdg110+1))
Type "help" for help.

postgres=# SELECT column_name, column_default, data_type FROM INFORMATION_SCHEMA.COLUMNS WHERE table_name = 'clients';

postgres=# SELECT column_name, column_default, data_type FROM INFORMATION_SCHEMA.COLUMNS WHERE table_name = 'clients';
 column_name | column_default | data_type 
-------------+----------------+-----------
 id          |                | integer
 lastname    |                | text
 country     |                | text
 booking     |                | integer
(4 rows)

postgres=# SELECT column_name, column_default, data_type FROM INFORMATION_SCHEMA.COLUMNS WHERE table_name = 'orders';
 column_name | column_default | data_type 
-------------+----------------+-----------
 id          |                | integer
 name        |                | text
 price       |                | integer
(3 rows)
```
---