from sql_connection import get_sql_conncetion

def get_all_products(connection):

    cursor = connection.cursor()

    query = ("SELECT products.product_id, products.name, "
            "units.unit_name, products.price_per_unit "
            "FROM warkop_db.products INNER JOIN "
            "warkop_db.units ON products.unit_id "
            "= units.unit_id;")

    cursor.execute(query)

    response = []

    for (product_id, name, unit_name, price_per_unit) in cursor:
        response.append(
            {'product_id': product_id,
            'name': name,
            'unit_name': unit_name,
            'price_per_unit': price_per_unit
            }
        )

    return response

def insert_new_product (connection, product):
    cursor = connection.cursor()
    query = ("INSERT INTO products "
    "(name, unit_id, price_per_unit) "
    "VALUES (%s, %s, %s)")
    data = (product['product_name'], product['unit_id'], product['price_per_unit'])
    cursor.execute(query, data)
    connection.commit()

    return cursor.lastrowid

def delete_product(connection, product_id):
    cursor = connection.cursor()
    query = ("DELETE From products WHERE product_id = " + str(product_id))
    cursor.execute(query)
    connection.commit()

if __name__ == '__main__':
    connection = get_sql_conncetion()
    print(get_all_products(connection))
    #print(insert_new_product(connection, {
    #    'product_name': 'jahe',
    #    'unit_id': '2',
    #    'price_per_unit': '5000'
    #}))
    # print(delete_product(connection, 14))