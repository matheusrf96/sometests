
def example_dict():
    return {
        'foo': 5,
        'bar': True,
        'hello': 'world',
    }


def test_key_in_dict():
    assert 'foo' in example_dict()


def test_dict_values():
    x = {
        'foo': 5,
        'bar': True,
        'hello': 'world',
    }

    assert x == example_dict()
