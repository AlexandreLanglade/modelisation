# Notes durant le développement du Plugin NetBox

## POSTGRESQL

- Invoquer le PostgreSQL shell as the system Postgres user : `sudo -u postgres psql`

- Création de DB + user :
    ```
    CREATE DATABASE netbox;
    CREATE USER netbox WITH PASSWORD 'J5brHrAXFLQSif0K';  
    GRANT ALL PRIVILEGES ON DATABASE netbox TO netbox;  
    ```
------------------------
- Connexion :
    ```
    psql --username netbox --password --host localhost netbox
    password :  J5brHrAXFLQSif0K
    ```
    > Connexion directe depuis /opt/netbox/ : `python netbox/manage.py dbshell`

- Quelques commandes POSTGRESQL utiles
    ```
    \conninfo
    \d nom_table
    ```

## REDIS

- Emplacement du fichier de configuration : `etc/redis/redis.conf`

- Commande pour ping-pong : `redis-cli ping`

## NETBOX

- Activer le venv de NetBox : `source /opt/netbox/venv/bin/activate`

- Rappel (username,password) de test : (netbox,netbox) (superuser)

- > Pour afficher le pannel de Debug :   
  > Mettre "DEBUG=True" dans le fichier configuration.py

- Pour lancer l'app NetBox : `python netbox/manage.py runserver`

- Ajout de Data dans la DB à la mano :
    ```
    python netbox/manage.py nbshell

    >>> from plugin.models import *
    >>> a = ModelA(truc='chose')
    >>> a.save()

    >>> ModelB(
    ...     modela=a,
    ...     truc='chose'
    ... ).save()

    ```

## DJANGO

**Migration**:  

> Mettre "DEVELOPER=True" dans le fichier configuration.py
```
python netbox/manage.py makemigrations nom_plugin --dry-run # simule 
python netbox/manage.py makemigrations nom_plugin           # fait
python netbox/manage.py migrate                             # migre
```

## Git

Tags et Releases :
```
git tag nom_du_tag
git push origin --tags
```
