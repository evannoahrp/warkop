def get_units(connection):
    cursor = connection.cursor()
    query = ("SELECT * FROM units")
    cursor.execute(query)

    response = []
    for (unit_id, unit_name) in cursor:
        response.append({
            'unit_id': unit_id,
            'unit_name': unit_name
        })
    return response

if __name__ == '__main__':
    from sql_connection import  get_sql_conncetion

    connection = get_sql_conncetion()

    print(get_units(connection))