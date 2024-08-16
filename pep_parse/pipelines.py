import datetime as dt

import csv
from collections import defaultdict

from pep_parse.settings import BASE_DIR, RESULTS_DIR_NAME, RESULTS_DIR

DATETIME_FORMAT = '%Y-%m-%d_%H-%M-%S'
STATUS_SUMMARY_FILE_NAME = 'status_summary_{date}.csv'
STATUS_NUM_HEAD = ('Статус', 'Количество')
TOTAL_NUMBERS = 'Общее количество'


class PepParsePipeline:

    def __init__(self):
        if RESULTS_DIR_NAME not in [
            directory.name for directory in BASE_DIR.iterdir()
        ]:
            RESULTS_DIR.mkdir(exist_ok=True)

    def open_spider(self, spider):
        self.statuses_nums = defaultdict(int)

    def process_item(self, item, spider):
        self.statuses_nums[item['status']] += 1
        return item

    def close_spider(self, spider):
        datetime_now = dt.datetime.now().strftime(
            DATETIME_FORMAT
        )
        with open(
            BASE_DIR / RESULTS_DIR_NAME / (
                STATUS_SUMMARY_FILE_NAME.format(date=datetime_now)
            ),
            'w', encoding='utf-8'
        ) as results_file:
            csv.writer(
                results_file,
                dialect=csv.unix_dialect,
                quoting=csv.QUOTE_MINIMAL
            ).writerows((
                STATUS_NUM_HEAD,
                *self.statuses_nums.items(),
                (TOTAL_NUMBERS, sum(self.statuses_nums.values()))
            ))
