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


### ref
- mysql or postgres https://www.enterprisedb.com/blog/postgresql-vs-mysql-360-degree-comparison-syntax-performance-scalability-and-features
- download and install postgres https://www.postgresql.org/download/linux/ubuntu/
- python https://qiita.com/hoto17296/items/0ca1569d6fa54c7c4732
