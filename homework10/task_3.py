# Из набора тестов задания task_2 создайте один тест с параметрами, используя @pytest.mark.parametrize
# Промаркируйте 1 параметр из выборки как smokе, а 1 набор данных скипните


def all_division(*arg1):
    """Поочередное деление чисел из переданного списка"""
    division = arg1[0]
    for i in arg1[1:]:
        division /= i
    return division



