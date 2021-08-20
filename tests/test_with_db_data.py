
from db.connection import get_connection

connection = get_connection()
cursor = connection.cursor()


def item_example():
    return {
        'id': 1,
        'name': 'Item 1',
        'description': 'Este é o item #1',
        'active': True,
    }


def format_data(data, fetchone=False):
    def create_dict(item):
        return {
            'id': item[0],
            'name': item[1],
            'description': item[2],
            'active': item[3],
        }

    if fetchone:
        return [create_dict(data)]

    return [create_dict(item) for item in data]


def test_select():
    cursor.execute('SELECT * FROM items ORDER BY id')
    data = format_data(cursor.fetchone(), fetchone=True)
    first_item = data[0]
    example = item_example()

    assert first_item.get('id') == example.get('id')
    assert first_item.get('name') == example.get('name')
    assert first_item.get('description') == example.get('description')
    assert first_item.get('active') == example.get('active')
    assert first_item == example
