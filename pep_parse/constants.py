from pathlib import Path

import datetime as dt


BASE_DIR = Path(__file__).parents[1]
DATETIME_FORMAT = '%Y-%m-%d_%H-%M-%S'
RESULT_DIR = BASE_DIR / 'results'
now_format = dt.datetime.now().strftime(DATETIME_FORMAT)
FILENAME = f'status_summary_{now_format}.csv'
