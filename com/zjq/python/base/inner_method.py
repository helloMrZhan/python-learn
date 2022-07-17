

# 内置方法
if __name__ == '__main__':

    # assert abs(-1) == 1
    # assert max(10, 100) == 100
    # assert min(10, 100) == 10
    # assert round(3.5) == 3
    # assert pow(2, 4) == 16
    # assert float(1) == 1.0

    assert 'count' in dir([])
    assert hash("a") == hash(chr(97))
    assert type({}) == type({'a': 1})

    assert all([True, True]) == True
    assert any([True, False]) == True
    assert bool({}) == False
    assert callable(abs) == True

    seasons = ['Spring', 'Summer', 'Fall', 'Winter']
    assert len(seasons) == 4

    shortcut = list(map(lambda s: s[0], seasons))
    assert shortcut == ['S', 'S', 'F', 'W']