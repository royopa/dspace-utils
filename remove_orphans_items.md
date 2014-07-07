Remove orphans items
====

This script is used to remove orphan items directly in database postgresql without to use DSpace interface.

Orphans items are those items which are not tied to any collection.


```sql
CREATE OR REPLACE FUNCTION deleteOrphanItens() RETURNS text AS $$
DECLARE
    text_return        text;
BEGIN

        RAISE NOTICE 'removing items from table metadatavalue';

        DELETE FROM
            metadatavalue
        WHERE
            item_id IN (
        SELECT item_id FROM item WHERE owning_collection IS NULL
            );

        RAISE NOTICE 'removing items from table communities2item';

        DELETE FROM
            communities2item
        WHERE
            item_id IN (
        SELECT item_id FROM item WHERE owning_collection IS NULL
            );

        RAISE NOTICE 'removing items from table collection2item';

        DELETE FROM
            collection2item
        WHERE
            item_id IN (
        SELECT item_id FROM item WHERE owning_collection IS NULL
            );

        RAISE NOTICE 'removing itens from table workspaceitem';

        DELETE FROM
            workspaceitem
        WHERE
            item_id IN (
        SELECT item_id FROM item WHERE owning_collection IS NULL
            );

        RAISE NOTICE 'removing items from table item2bundle';

        DELETE FROM
            item2bundle
        WHERE
            item_id IN (
        SELECT item_id FROM item WHERE owning_collection IS NULL
                )
        ;

        DELETE FROM
            item
        WHERE
            item_id IN (
        SELECT item_id FROM item WHERE owning_collection IS NULL
                )
        ;

        text_return := 'Success. Now execute the command "[dspace]/bin/dspace index-discovery -b"';
RETURN
    text_return;
END;
$$ LANGUAGE plpgsql;
```

Example of use
-----

```sql
SELECT deleteOrphanItens();
```
