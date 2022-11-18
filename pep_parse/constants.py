import datetime as dt


DATETIME_FORMAT = '%Y-%m-%d_%H-%M-%S'
TIME_NOW = dt.datetime.now().strftime(DATETIME_FORMAT)
FILENAME = f'status_summary_{TIME_NOW}.csv'
