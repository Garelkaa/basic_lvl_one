from days_generator import generate_schedule
from datetime import datetime


def test_generate_schedule():
    start_date = datetime(2020, 1, 30)
    schedule = generate_schedule(4, 2, 1, start_date)

    assert schedule == [
        datetime(2020, 1, 30, 0, 0),
        datetime(2020, 1, 31, 0, 0),
        datetime(2020, 2, 1, 0, 0),
        datetime(2020, 2, 2, 0, 0)
    ]


test_generate_schedule()
