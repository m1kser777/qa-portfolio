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