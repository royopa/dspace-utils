### The command build a pg_dump in database dspace

```
pg_dump -a dspace -S dspace -W --role=dspace --username=dspace > dspace_database.bkp
```

```
psql -S -W --host=localhost --dbname=dspace --echo-all --file=dspace.bkp --username=dspace
```
