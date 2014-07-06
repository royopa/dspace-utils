Remove items in collection 
====

This script is used to remove items directly in database postgresql without to use DSpace interface.
The parameter is the collection handle of the collection that you want to remove the items


```sql
CREATE OR REPLACE FUNCTION deleteItensByHandleCollection(handle_parameter text) RETURNS text AS $$
DECLARE
	affected_rows      int;
	item_collection_id int;
	text_return        text;
BEGIN
	SELECT INTO item_collection_id 
		resource_id 
	FROM 
		handle
	WHERE
		handle = handle_parameter AND resource_type_id = 3;
	
	RAISE NOTICE 'collection_id = %', item_collection_id;

	IF item_collection_id IS NULL THEN 
		RAISE NOTICE 'Erro, nenhuma coleção encontrada com o handle %', handle_parameter;
		text_return := 'No collection found with handle informed.';
	ELSE
		RAISE NOTICE 'removing items from table metadatavalue';

		DELETE FROM 
			metadatavalue
		WHERE
			item_id IN (
				SELECT
					item_id
				FROM
					collection2item
				WHERE
					collection_id = item_collection_id
			);

		RAISE NOTICE 'removing items from table communities2item';
			
		DELETE FROM 
			communities2item
		WHERE
			item_id IN (
				SELECT
					item_id
				FROM
					collection2item
				WHERE
					collection_id = item_collection_id
			);

		RAISE NOTICE 'removing items from table collection2item';

		DELETE FROM 
			collection2item
		WHERE
			item_id IN (
				SELECT
					item_id
				FROM
					collection2item
				WHERE
					collection_id = item_collection_id
			);

		RAISE NOTICE 'removing itens from table workspaceitem';

		DELETE FROM 
			workspaceitem
		WHERE
			item_id IN (
				SELECT
					item_id
				FROM
					collection2item
				WHERE
					collection_id = item_collection_id
			);

		RAISE NOTICE 'removing items from table item2bundle';

		DELETE FROM 
			item2bundle 
		WHERE
			item_id IN (
				SELECT
					item_id
				FROM
					collection2item
				WHERE
					collection_id = item_collection_id
				)
		;

		DELETE FROM 
			item
		WHERE
			item_id IN (
				SELECT
					item_id
				FROM
					collection2item
				WHERE
					collection_id = item_collection_id
				)
		;		

		text_return := 'Success. Now execute the command "[dspace]/bin/dspace index-discovery -b"';
	END IF;
RETURN 
	text_return;
END;
$$ LANGUAGE plpgsql;
```

Examples of use
-----

```sql
SELECT deleteItensByHandleCollection('10673/92');

SELECT deleteItensByHandleCollection('123456789/1289');
```
