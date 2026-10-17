from post_checker import check_post

def test_clean_post():
    text = "Хлеб, который не съели\nТеперь он светит"
    assert check_post(text) == []
def test_period_at_end():
    text = "Хлеб, который не съели\nТеперь он светит."
    assert check_post(text) == []


def test_period_at_end():
    text = "Хлеб, который не съели\nТеперь он светит."
    assert len(check_post(text)) == 1


def test_ellipsis_symbol_allowed():
    text = "Хлеб, который не съели…\nТеперь он светит"
    assert check_post(text) == []


def test_ellipsis_three_dots_allowed():
    text = "Хлеб, который не съели...\nТеперь он светит"
    assert check_post(text) == []


def test_exactly_limit_ok():
    text = "а" * 2200
    assert check_post(text) == []

def test_too_long():
    text = "а" * 2201
    assert len(check_post(text)) == 1