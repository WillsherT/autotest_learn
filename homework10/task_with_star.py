# Есть маркер @pytest.mark.id_check(1, 2, 3), нужно вывести на печать, то что в него передано
#
# >>> 1, 2, 3

import pytest


@pytest.fixture(autouse=True)
def test_2(request):
    """Выводим переданные в маркер аргументы в консоль"""
    mark = request.node.get_closest_marker("id_check")
    print(f"\nВ маркер {mark.name} переданы аргументы {', '.join([str(i) for i in mark.args])}\n")


@pytest.mark.id_check(1, 2, 3)
def test():
    """Просто тест с маркером имеющим аргументы"""
    pass



