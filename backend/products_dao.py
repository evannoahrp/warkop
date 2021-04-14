from sql_connection import get_sql_conncetion

def get_all_product(connection):

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

if __name__ == '__main__':
    connection = get_sql_conncetion()
    print(get_all_product(connection))