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

\d nom_table


-------------------

python netbox/manage.py dbshell


## REDIS

etc/redis/redis.conf

redis-cli ping

## NETBOX

source /opt/netbox/venv/bin/activate

superuser : netbox netbox
DEBUG=True


python3 manage.py runserver 0.0.0.0:8000 --insecure

http://127.0.0.1:8000/

---------
```
python netbox/manage.py nbshell

>>> from netbox_access_lists.models import *
>>> acl = AccessList(name='MyACL1', default_action='deny')
>>> acl
<AccessList: MyACL1>
>>> acl.save()

>>> AccessListRule(
...     access_list=acl,
...     index=10,
...     protocol='tcp',
...     destination_prefix=prefix1,
...     destination_ports=[80, 443],
...     action='permit',
...     description='Web traffic'
... ).save()
>>> AccessListRule(
...     access_list=acl,
...     index=20,
...     protocol='udp',
...     destination_prefix=prefix2,
...     destination_ports=[53],
...     action='permit',
...     description='DNS'
... ).save()
>>> acl.rules.all()
<RestrictedQuerySet [<AccessListRule: MyACL1: Rule 10>, <AccessListRule: MyACL1: Rule 20>]>
```

## DJANGO

**Migration**:  

DEVELOPER=True

python netbox/manage.py makemigrations modelisation --dry-run

python netbox/manage.py makemigrations modelisation

python netbox/manage.py migrate