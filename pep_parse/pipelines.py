import csv
from collections import defaultdict
from pathlib import Path

from pep_parse.constants import FILENAME, RESULT_DIR

BASE_DIR = Path(__file__).parents[1]


class PepParsePipeline:
    def __init__(self):
        self.result_dir = RESULT_DIR
        self.result_dir.mkdir(exist_ok=True)

    def open_spider(self, spider):
        self.results = defaultdict(int)

    def process_item(self, item, spider):
        self.results[item['status']] += 1
        return item

    def close_spider(self, spider):
        file_path = self.result_dir / FILENAME
        with open(file_path, 'w', encoding='utf-8') as csvfile:
            writer = csv.writer(
                csvfile,
                dialect=csv.unix_dialect,
                quoting=csv.QUOTE_MINIMAL
            )
            writer.writerows([
                ('Статус', 'Количество'),
                *self.results.items(),
                ('Total', sum(self.results.values()))
            ])
