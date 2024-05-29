from PyQt5.QtSql import QSqlQuery
import db.ColumnNames

operators = ['*.*', '*!*', '..*', '*..', '==', '!=', '>=', '<=', '>', '<']
res = []


def get_project_data(value, dbase):
    query = QSqlQuery(db=dbase)
    sql_command = "SELECT * FROM tblProjects WHERE projectID = :search_value "
    query.prepare(sql_command)
    query.bindValue(":search_value", value)
    res.clear()
    query.exec_()
    while query.next():
        res.append(query.value('projectID'))
        res.append(query.value('projectSapNo'))
        res.append(query.value('projectTask'))

    if len(res) > 0:
        return res
    else:
        return False


def get_related_field_value(table, column, where, value, dbase):
    query = QSqlQuery(db=dbase)
    sql_command = "SELECT " + column + " FROM " + table + " WHERE " + where + " LIKE '%' || :search_value || '%' "
    return execute_sql_command(sql_command, query, value, column)


def get_projectID(table, field, operator, value, dbase):
    query = QSqlQuery(db=dbase)
    sql_command = query_prepare(table, field, operator)
    return execute_sql_command(sql_command, query, value)


def get_data(dbase, sql_command, field_count):
    result = []
    query = QSqlQuery(db=dbase)
    query.prepare(sql_command)

    query.exec_()
    _tuple = ()
    _list = list(_tuple)
    while query.next():

        for i in range(field_count):
            _list.append(query.value(i))
        _tuple = tuple(_list)
        result.append(_tuple)
        _list.clear()
    if len(result) > 0:
        return result
    else:
        return False


def get_field_list(table, column, dbase, sql_command_type='select'):
    query = QSqlQuery(db=dbase)

    if sql_command_type == 'count':
        sql_command = "SELECT " + column + ", COUNT(" + column + ") " \
                                                                 "FROM " + table + " " \
                                                                                   "GROUP BY " + column + " " \
                                                                                                          "ORDER BY " + column
    elif sql_command_type == 'distinct':
        sql_command = "SELECT DISTINCT " + column + " FROM " + table
    else:
        sql_command = "SELECT " + column + " FROM " + table

    query.prepare(sql_command)
    res.clear()
    query.exec_()
    if sql_command_type == 'count':
        while query.next():
            res.append((query.value(0), str(query.value(1))))
    else:
        while query.next():
            res.append(query.value(0))
    if len(res) > 0:
        return res
    else:
        return False


def execute_sql_command(sql_command, query, value, column='projectID'):
    query.prepare(sql_command)
    query.bindValue(":search_value", value)
    res.clear()
    query.exec_()
    while query.next():
        res.append(query.value(column))

    if len(res) > 0:
        return res
    else:
        return False


def query_prepare(table, field, operator):
    sql_command = ''

    if not table == "tblProjects":

        match operator:
            case '*.*':
                sql_command = "SELECT " + db.ColumnNames.task_db_fields + " FROM tblProjects " \
                                                                          "INNER JOIN " + table + " ON tblProjects.projectID = " + table + ".projectID " \
                                                                                                                                           "WHERE " + table + "." + field + " LIKE '%' || :search_value || '%' "
            case '*!*':
                sql_command = "SELECT " + db.ColumnNames.task_db_fields + " FROM tblProjects " \
                                                                          "INNER JOIN " + table + " ON tblProjects.projectID = " + table + ".projectID " \
                                                                                                                                           "WHERE " + table + "." + field + " NOT LIKE '%' || :search_value || '%' "
            case '..*':
                sql_command = "SELECT " + db.ColumnNames.task_db_fields + " FROM tblProjects " \
                                                                          "INNER JOIN " + table + " ON tblProjects.projectID = " + table + ".projectID " \
                                                                                                                                           "WHERE " + table + "." + field + " LIKE :search_value || '%' "
            case '*..':
                sql_command = "SELECT " + db.ColumnNames.task_db_fields + " FROM tblProjects " \
                                                                          "INNER JOIN " + table + " ON tblProjects.projectID = " + table + ".projectID " \
                                                                                                                                           "WHERE " + table + "." + field + " LIKE '%' || :search_value"
            case '==':
                sql_command = "SELECT " + db.ColumnNames.task_db_fields + " FROM tblProjects " \
                                                                          "INNER JOIN " + table + " ON tblProjects.projectID = " + table + ".projectID " \
                                                                                                                                           "WHERE " + table + "." + field + " = :search_value"
            case '!=':
                sql_command = "SELECT " + db.ColumnNames.task_db_fields + " FROM tblProjects " \
                                                                          "INNER JOIN " + table + " ON tblProjects.projectID = " + table + ".projectID " \
                                                                                                                                           "WHERE " + table + "." + field + " != :search_value"
            case '>=':
                sql_command = "SELECT " + db.ColumnNames.task_db_fields + " FROM tblProjects " \
                                                                          "INNER JOIN " + table + " ON tblProjects.projectID = " + table + ".projectID " \
                                                                                                                                           "WHERE " + table + "." + field + " >=  :search_value"
            case '<=':
                sql_command = "SELECT " + db.ColumnNames.task_db_fields + " FROM tblProjects " \
                                                                          "INNER JOIN " + table + " ON tblProjects.projectID = " + table + ".projectID " \
                                                                                                                                           "WHERE " + table + "." + field + " <= :search_value"
            case '>':
                sql_command = "SELECT " + db.ColumnNames.task_db_fields + " FROM tblProjects " \
                                                                          "INNER JOIN " + table + " ON tblProjects.projectID = " + table + ".projectID " \
                                                                                                                                           "WHERE " + table + "." + field + " >  :search_value"
            case '<':
                sql_command = "SELECT " + db.ColumnNames.task_db_fields + " FROM tblProjects " \
                                                                          "INNER JOIN " + table + " ON tblProjects.projectID = " + table + ".projectID " \
                                                                                                                                           "WHERE " + table + "." + field + " < :search_value"
    else:
        match operator:
            case '*.*':
                sql_command = "SELECT " + db.ColumnNames.task_db_fields + " FROM tblProjects WHERE " + field + " LIKE '%' || :search_value || '%' "
            case '*!*':
                sql_command = "SELECT " + db.ColumnNames.task_db_fields + " FROM tblProjects WHERE " + field + " NOT LIKE '%' || :search_value || '%' "
            case '..*':
                sql_command = "SELECT " + db.ColumnNames.task_db_fields + " FROM tblProjects WHERE " + field + " LIKE :search_value || '%' "
            case '*..':
                sql_command = "SELECT " + db.ColumnNames.task_db_fields + " FROM tblProjects WHERE " + field + " LIKE '%' || :search_value "
            case '==':
                sql_command = "SELECT " + db.ColumnNames.task_db_fields + " FROM tblProjects WHERE " + field + " = :search_value "
            case '!=':
                sql_command = "SELECT " + db.ColumnNames.task_db_fields + " FROM tblProjects WHERE " + field + " != :search_value "
            case '>=':
                sql_command = "SELECT " + db.ColumnNames.task_db_fields + " FROM tblProjects WHERE " + field + " >= :search_value"
            case '<=':
                sql_command = "SELECT " + db.ColumnNames.task_db_fields + " FROM tblProjects WHERE " + field + " <= :search_value"
            case '>':
                sql_command = "SELECT " + db.ColumnNames.task_db_fields + " FROM tblProjects WHERE " + field + " > :search_value"
            case '<':
                sql_command = "SELECT " + db.ColumnNames.task_db_fields + " FROM tblProjects WHERE " + field + " < :search_value"

    return sql_command


def get_seq_value(dbase, table):
    sql_command = "SELECT seq FROM SQLITE_SEQUENCE WHERE name = '" + table + "' LIMIT 1"
    query = QSqlQuery(db=dbase)
    query.prepare(sql_command)
    query.exec_()
    query.next()
    return query.value(0)


def get_max_id_value(dbase, table, column):
    sql_command = "SELECT MAX(" + column + ") FROM " + table
    query = QSqlQuery(db=dbase)
    query.prepare(sql_command)
    query.exec_()
    query.next()
    return query.value(0)


def delete_records(dbase, table, column, _id):
    sql_command = f'DELETE FROM {table} WHERE {column} = {int(_id)}'
    query = QSqlQuery(db=dbase)
    query.prepare(sql_command)
    return query.exec_()


def find_id_by_value(dbase, table, column, value):
    sql_command = f"SELECT * FROM {table} WHERE {column} = '{value}'"
    query = QSqlQuery(db=dbase)
    query.prepare(sql_command)
    query.exec_()
    query.next()
    return query.value(0)


def are_related_records(dbase, table, column, _id):
    sql_command = f"SELECT COUNT({column}) FROM {table} WHERE {column} = {_id}"
    query = QSqlQuery(db=dbase)
    query.prepare(sql_command)
    query.exec_()
    query.next()
    return query.value(0)


def add_value(dbase, sql_command):
    query = QSqlQuery(db=dbase)
    query.prepare(sql_command)
    return query.exec_()


def update_value(dbase, table, column, value, column_id, _id):
    sql_command = f"UPDATE {table} SET {column} = '{value}' WHERE {column_id} = {_id}"
    query = QSqlQuery(db=dbase)
    query.prepare(sql_command)
    return query.exec_()


def get_rows(dbase, sql_command, columns):
    result = []
    query = QSqlQuery(db=dbase)
    query.prepare(sql_command)

    query.exec_()

    while query.next():
        row = {}
        for col in columns:
            row[col] = query.value(col)
        result.append(row)

    if len(result) > 0:
        return result
    else:
        return False