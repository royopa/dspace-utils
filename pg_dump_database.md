### The command build a pg_dump in database dspace

```
pg_dump -a dspace -S dspace -W --role=dspace --username=dspace > dspace_database.bkp
```

```
psql --host=localhost --dbname=dspace --echo-all --file=dspace.bkp --username=dspace
```

```
/usr/bin/pg_restore --host localhost --port 5432 --username "dspace" --dbname "dspace" --role "dspace" --no-password  --list "/vagrant_data/bkp_postgresql_01102015"
```
