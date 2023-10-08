from datetime import datetime, timedelta


def generate_schedule(days, work_days, rest_days, start_date):
    try:
        schedule = []
        current_date = start_date

        for _ in range(days):
            if len(schedule) % (work_days + rest_days) < work_days:
                schedule.append(current_date)
            else:
                schedule.append(current_date + timedelta(days=1))

            current_date += timedelta(days=1)

        return schedule
    except Exception as e:
        return None
