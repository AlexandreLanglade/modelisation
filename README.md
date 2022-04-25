# MEMO

## POSTGRESQL

invoking the PostgreSQL shell as the system Postgres user :
sudo -u postgres psql

CREATE DATABASE netbox;
CREATE USER netbox WITH PASSWORD 'J5brHrAXFLQSif0K';
GRANT ALL PRIVILEGES ON DATABASE netbox TO netbox;

psql --username netbox –-password --host localhost netbox
pwd :  J5brHrAXFLQSif0K

\conninfo

## REDIS

etc/redis/redis.conf

redis-cli ping

## NETBOX

source /opt/netbox/venv/bin/activate

superuser : netbox netbox



python3 manage.py runserver 0.0.0.0:8000 --insecure

http://127.0.0.1:8000/