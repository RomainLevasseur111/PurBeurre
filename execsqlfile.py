def execsqlfile(cursor, sql_file):
    statement = ""
    for line in open(sql_file):
        if line.endswith(';') :
            statement = statement + line
            try :
                cursor.execute(statement)
            statement = ""
        else :
            statement = statement + line
