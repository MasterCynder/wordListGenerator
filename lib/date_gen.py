from datetime import datetime, timedelta

def get_years():
    """Returns a list of years from Current-100 to Current+30."""
    curr_y = datetime.now().year
    return [str(i) for i in range(curr_y - 100, curr_y + 31)]

def get_days_eu():
    """Generates all 366 possible days in ddmm format."""
    res = []
    d = datetime(2000, 1, 1) # Leap year to include Feb 29
    for _ in range(366):
        res.append(d.strftime("%d%m"))
        d += timedelta(days=1)
    return sorted(list(set(res)))

def get_days_us():
    """Generates all 366 possible days in mmdd format."""
    res = []
    d = datetime(2000, 1, 1)
    for _ in range(366):
        res.append(d.strftime("%m%d"))
        d += timedelta(days=1)
    return sorted(list(set(res)))

def get_dates_eu():
    """Generates full dates in ddmmyyyy format for the requested range."""
    res = []
    y_now = datetime.now().year
    for y in range(y_now - 100, y_now + 31):
        d = datetime(y, 1, 1)
        # Check leap year manually or use calendar
        days = 366 if (y % 4 == 0 and (y % 100 != 0 or y % 400 == 0)) else 365
        for _ in range(days):
            res.append(d.strftime("%d%m%Y"))
            d += timedelta(days=1)
    return res

def get_dates_us():
    """Generates full dates in mmddyyyy format for the requested range."""
    res = []
    y_now = datetime.now().year
    for y in range(y_now - 100, y_now + 31):
        d = datetime(y, 1, 1)
        days = 366 if (y % 4 == 0 and (y % 100 != 0 or y % 400 == 0)) else 365
        for _ in range(days):
            res.append(d.strftime("%m%d%Y"))
            d += timedelta(days=1)
    return res
