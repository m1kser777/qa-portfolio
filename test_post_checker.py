import pytest
from post_checker import check_post


def test_period_at_end():
    text = "Хлеб, который не съели\nТеперь он светит."
    assert len(check_post(text)) == 1


def test_too_long():
    text = "а" * 2201
    assert len(check_post(text)) == 1


def test_banned_phrase():
    text = "Светильник готов\nЗаказ — Пишите в Телеграм"
    assert len(check_post(text)) == 1


@pytest.mark.parametrize("text", [
    "Хлеб, который не съели\nТеперь он светит",
    "Хлеб, который не съели…\nТеперь он светит",
    "Хлеб, который не съели...\nТеперь он светит",
    "а" * 2200,
    "Нас читают в телеграме",
], ids=["clean", "ellipsis_char", "three_dots", "exactly_2200", "telegram_word"])
def test_clean_posts(text):
    assert check_post(text) == []