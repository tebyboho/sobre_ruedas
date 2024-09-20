from datetime import datetime

def get_current_year():
    return datetime.now().year

def get_years_tuple():
    current_year = get_current_year()
    return [(year, year) for year in range(current_year - 15, current_year + 1)]


