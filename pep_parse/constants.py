from pathlib import Path
import datetime as dt

BASE_DIR = Path(__file__).parents[2]
RESULTS_DIR = BASE_DIR / 'results'

DATETIME_FORMAT = '%Y-%m-%d_%H-%M-%S'
TIME_NOW = dt.datetime.now().strftime(DATETIME_FORMAT)

PEP_NAME = f'status_summary_{TIME_NOW}.csv'
FILE_PATH = RESULTS_DIR / PEP_NAME
