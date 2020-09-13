# download_113_57_190_228
从 http://113.57.190.228:8001/web/Report/RiverReport 下载水情报表

### install postgres

```
sudo -u postgres psql
create role ロール名 with createdb login password 'パスワード';
create database データベース名;
```

```
sudo apt install libpq-dev
sudo pip3 install -U psycopg2
```

```
export DATABASE_URL=postgresql://{username}:{password}@localhsot:5432/{database}
```

### tips
- rename table `alter table dyna2 rename to dyna;`


```
  table pos       位置表
    STCD    text  pk
    RVNM    text  河名
    STNM    text  站名
    FRZ     text  设防水位
    GRZ     text  保证水位
    WRZ     text  警戒水位
    MAXZ    text  大概是历史最高水位

CREATE TABLE if not exists dyna (
              STCD  text,               -- PK 水文站编码
              DATE  text,               -- PK 数据检索日时 "yyyy-mm-dd hh:00"
              Y     char(4),            -- DATE分解版检索用
              M     char(2),            -- DATE分解版检索用
              D     char(2),            -- DATE分解版检索用
              H     char(2),            -- DATE分解版检索用
              Q     decimal(9,2),       -- 流量。数字以外被删除，出入都有时放出
              QIN   decimal(9,2),       -- Q分解版。出入都有时放入，其他时候空
              YZ    decimal(9,2),       -- 比昨日+涨-落
              Z     decimal(9,2),       -- 水位
              WPTN  char(1),            -- 水势。4降，5升，6平
              PRIMARY KEY(STCD, DATE)
              );

  注意
    数字位置还可以是空，--，带有(入)(出)和<br>，缺测
```

```sql
CREATE TABLE if not exists pos (
              STCD text PRIMARY KEY,
              RVNM text,
              STNM text,
              FRZ text,
              GRZ text,
              WRZ text,
              MAXZ text);
```

csv抽出
```
psql -c "select left(date,10),q,qin,z from dyna where stcd='60106980' and h='08' order by date;" --csv -t >t.csv
```


### ref
- mysql or postgres https://www.enterprisedb.com/blog/postgresql-vs-mysql-360-degree-comparison-syntax-performance-scalability-and-features
- download and install postgres https://www.postgresql.org/download/linux/ubuntu/
- python https://qiita.com/hoto17296/items/0ca1569d6fa54c7c4732
