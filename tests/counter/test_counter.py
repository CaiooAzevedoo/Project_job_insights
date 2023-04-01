from src.pre_built.counter import count_ocurrences


def test_counter():
    test_counter_js = count_ocurrences('data/jobs.csv', r'/javascript/')
    test_counter_py = count_ocurrences('data/jobs.csv', r'/python/')
    assert test_counter_js != 0 and test_counter_py != 0
