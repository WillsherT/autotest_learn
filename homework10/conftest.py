import datetime
import time
import pytest


@pytest.fixture
def start_time():
    """Выводим время начала и завершения теста"""
    time_start = datetime.datetime.now()
    print(time_start.strftime('\n Тест запустился в %H:%M:%S'))
    yield
    time_end = datetime.datetime.now()
    print(time_end.strftime('\n Тест завершился в %H:%M:%S'))


@pytest.fixture
def running_time():
    """Выводим время выполнения теста"""
    start = time.time()
    yield
    end = time.time()
    print(f'\n Тест прошел за {end - start}')
