SQL Utils
====

Various portions of SQL code in the DSpace's database


##pega o handle e o id da coleção

```sql
SELECT 
	handle_id, 
	handle, 
	resource_type_id, 
	resource_id, 
	resource_id AS collection_id
FROM
	handle
WHERE
	handle = '123456789/1289' AND
	resource_type_id = 3
;
```

##pega os itens que estão relacionados a coleção
```sql
SELECT
	item_id
FROM
	collection2item
WHERE
	collection_id = 2
;
```

##pega os itens que estão relacionados a coleção
```sql
SELECT
	item_id
FROM
	item
WHERE 
	item_id IN (
		SELECT
			item_id
		FROM
			collection2item
		WHERE
			collection_id = 2
	)
;
```

##basic select to get tables where the items area located
```sql
SELECT * FROM metadatavalue;
SELECT * FROM communities2item;
SELECT * FROM collection2item;
SELECT * FROM workspaceitem;
SELECT * FROM item2bundle;
SELECT * FROM item;
```
