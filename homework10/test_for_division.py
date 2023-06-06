import pytest
from task_2 import all_division
from task_3 import all_division


@pytest.mark.smoke
@pytest.mark.parametrize('args, result',
                         [
                          pytest.param([1, 2], 0.5, marks=pytest.mark.smoke),
                          pytest.param([15, 5, 1], 3, marks=pytest.mark.skip('not now')),
                          ([999, 111, 2], 4.5),
                          ([12, 2, 2, 2], 1.5),
                          ([1], 1)
                         ])
def test_positive(args, result):
    """Позитивные кейсы деления переданных чисел"""
    assert all_division(*args) == result


@pytest.mark.acceptance
@pytest.mark.negative
@pytest.mark.parametrize('args, exception',
                         [
                          ((1, 0), ZeroDivisionError),
                          ((2, '1'), TypeError),
                          ((2, [2, 3]), TypeError),
                          ((), IndexError)
                         ])
def test_exceptions(args, exception):
    """Проверяем наличие исключений при передаче данных отличных от чисел/пустой ввод/деление на 0"""
    with pytest.raises(exception):
        all_division(*args)
