def insert(table_name, **fields):
    sql = 'INSERT INTO %s (' % table_name
    for field in fields:
        sql += '%s, ' % field
    sql = sql[:-2] + ') VALUES (' # Remove trailing comma
    for field in fields:
        sql += '\'%s\', ' % fields[field]
    sql = sql[:-2] + ');'
    return sql
