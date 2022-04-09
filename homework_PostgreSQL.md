## Задача 1

Используя docker поднимите инстанс PostgreSQL (версию 13). Данные БД сохраните в volume.

Подключитесь к БД PostgreSQL используя `psql`.

Воспользуйтесь командой `\?` для вывода подсказки по имеющимся в `psql` управляющим командам.

**Найдите и приведите** управляющие команды для:
- вывода списка БД
- подключения к БД
- вывода списка таблиц
- вывода описания содержимого таблиц
- выхода из psql

## Ответ 

```
(venv) georgijsivkov@MacBook-Pro-Georgij devops-netology % docker pull postgres:13
...
(venv) georgijsivkov@MacBook-Pro-Georgij devops-netology % docker volume create vol_postgres
vol_postgres
(venv) georgijsivkov@MacBook-Pro-Georgij devops-netology % docker run --rm --name pg-docker -e POSTGRES_PASSWORD=postgres -ti -p 5432:5432 -v vol_postgres:/var/lib/postgresql/data postgres:13
...
(venv) georgijsivkov@MacBook-Pro-Georgij devops-netology % docker exec -it pg-docker bash
root@ecbde283b634:/# psql -h localhost -p 5432 -U postgres -W
Password: 
psql (13.6 (Debian 13.6-1.pgdg110+1))
Type "help" for help.
```
(Список БД)
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
(3 rows)
```
(Подключение к БД)
```
postgres=# \c postgres 
Password: 
You are now connected to database "postgres" as user "postgres".
```
(вывод списка таблиц)
```
postgres=# \dt 
Did not find any relations.
```
(вывод списка таблиц с системными объектами)
```
postgres=# \dtS 
                    List of relations
   Schema   |          Name           | Type  |  Owner   
------------+-------------------------+-------+----------
 pg_catalog | pg_aggregate            | table | postgres
 pg_catalog | pg_am                   | table | postgres
...
```
(вывод описания содержимого таблиц)
```
postgres=# \dS+ pg_index 
                                      Table "pg_catalog.pg_index"
     Column     |     Type     | Collation | Nullable | Default | Storage  | Stats target | Description 
----------------+--------------+-----------+----------+---------+----------+--------------+-------------
 indexrelid     | oid          |           | not null |         | plain    |              | 
 indrelid       | oid          |           | not null |         | plain    |              | 
 indnatts       | smallint     |           | not null |         | plain    |              | 
...
```
(выход из psql)
```
postgres=# \q 

```
---
## Задача 2

Используя `psql` создайте БД `test_database`.

Изучите [бэкап БД](https://github.com/netology-code/virt-homeworks/tree/master/06-db-04-postgresql/test_data).

Восстановите бэкап БД в `test_database`.

Перейдите в управляющую консоль `psql` внутри контейнера.

Подключитесь к восстановленной БД и проведите операцию ANALYZE для сбора статистики по таблице.

Используя таблицу [pg_stats](https://postgrespro.ru/docs/postgresql/12/view-pg-stats), найдите столбец таблицы `orders` 
с наибольшим средним значением размера элементов в байтах.

**Приведите в ответе** команду, которую вы использовали для вычисления и полученный результат.

## Ответ 

```
postgres=# CREATE DATABASE test_database;
CREATE DATABASE
postgres=# 
\q
root@ecbde283b634:/var/lib/postgresql/data# psql -U postgres -f ./test_dumb.sql test_database
root@ecbde283b634:/var/lib/postgresql/data# psql -h localhost -p 5432 -U postgres -W
Password: 
psql (13.6 (Debian 13.6-1.pgdg110+1))
Type "help" for help.
postgres=# \c test_database
Password: 
You are now connected to database "test_database" as user "postgres".
test_database=# \dt
         List of relations
 Schema |  Name  | Type  |  Owner   
--------+--------+-------+----------
 public | orders | table | postgres
(1 row)
test_database=# ANALYZE VERBOSE public.orders;
INFO:  analyzing "public.orders"
INFO:  "orders": scanned 1 of 1 pages, containing 8 live rows and 0 dead rows; 8 rows in sample, 8 estimated total rows
ANALYZE
test_database=# select avg_width from pg_stats where tablename='orders';
 avg_width 
-----------
         4
        16
         4
(3 rows)
```
---
## Задача 3

Архитектор и администратор БД выяснили, что ваша таблица orders разрослась до невиданных размеров и
поиск по ней занимает долгое время. Вам, как успешному выпускнику курсов DevOps в нетологии предложили
провести разбиение таблицы на 2 (шардировать на orders_1 - price>499 и orders_2 - price<=499).

Предложите SQL-транзакцию для проведения данной операции.

Можно ли было изначально исключить "ручное" разбиение при проектировании таблицы orders?

## Ответ 

Переименовываем старую таблицу, создаем новую, переносим данные из старой в новую. 
```
test_database=# alter table orders rename to orders_simple;
ALTER TABLE
test_database=# create table orders (id integer, title varchar(80), price integer) partition by range(price);
CREATE TABLE
test_database=# create table orders_less499 partition of orders for values from (0) to (499);
CREATE TABLE
test_database=# create table orders_more499 partition of orders for values from (499) to (999999999);
CREATE TABLE
test_database=# insert into orders (id, title, price) select * from orders_simple;
INSERT 0 8
```
Да, изначально можно было сделать таблицу секционированной.  

---
## Задача 4

Используя утилиту `pg_dump` создайте бекап БД `test_database`.

Как бы вы доработали бэкап-файл, чтобы добавить уникальность значения столбца `title` для таблиц `test_database`?

## Ответ 

```
root@ecbde283b634:/var/lib/postgresql/data# pg_dump -U postgres -d test_database >test_database_dump.sql
root@ecbde283b634:/var/lib/postgresql/data# ls
base    pg_commit_ts  pg_hba.conf    pg_logical    pg_notify    pg_serial     pg_stat      pg_subtrans  pg_twophase  pg_wal   postgresql.auto.conf  postmaster.opts  test_database_dump.sql
global  pg_dynshmem   pg_ident.conf  pg_multixact  pg_replslot  pg_snapshots  pg_stat_tmp  pg_tblspc    PG_VERSION   pg_xact  postgresql.conf       postmaster.pid   test_dumb.sql
```
Для уникальности можно добавить индекс или первичный ключ
```
CREATE INDEX ON orders ((lower(title)));
```