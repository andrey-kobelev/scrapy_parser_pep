import datetime as dt

import csv
from collections import defaultdict
from pathlib import Path

from pep_parse.settings import RESULTS_DIR

DATETIME_FORMAT = '%Y-%m-%d_%H-%M-%S'
STATUS_SUMMARY_FILE_NAME = 'status_summary_{date}.csv'
STATUS_NUM_HEAD = ('Статус', 'Количество')
TOTAL_NUMBERS = 'Total'
BASE_DIR = Path(__file__).parent


class PepParsePipeline:
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
            RESULTS_DIR / STATUS_SUMMARY_FILE_NAME.format(date=datetime_now),
            'w', encoding='utf-8'
        ) as results_file:
            csv.writer(
                results_file, dialect=csv.unix_dialect
            ).writerows(
                [
                    STATUS_NUM_HEAD,
                    *self.statuses_nums.items(),
                    (TOTAL_NUMBERS, sum(self.statuses_nums.values()))
                ]
            )
