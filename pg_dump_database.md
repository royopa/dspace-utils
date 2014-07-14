### The command build a pg_dump in database dspace

```shell
pg_dump -a dspace -S dspace -W --role=dspace --username=dspace > dspace_database.bkp


```shell
psql dspace -S dspace -W < dspace.bkp 
```
