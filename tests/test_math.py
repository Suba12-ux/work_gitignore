import pytest


def add_sum(a, b):
    return a + b


# маркируем как смоук-тест
@pytest.mark.smoke
def test_add():
    assert add_sum(2, 3) == 5, 'сумма не равна ожидаемой'


# маркируем как регрессионный тест
@pytest.mark.regression
def test_type_result():
    assert isinstance(add_sum(2, 3), int), \
        'не соответствует ожидаемому типу данных'


@pytest.mark.skip(reason="Тест устарел и требует переработки")
def test_old_functionality():
    assert False  # Этот тест не будет выполняться


@pytest.mark.xfail(reason="Баг в API, исправят в версии 2.5")
def test_broken_feature():
    assert add_sum(2, 3) == 6, 'сумма не равна ожидаемой'  # Сейчас падает