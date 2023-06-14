import csv
from datetime import datetime as dt
from collections import defaultdict

from scrapy.exceptions import DropItem

from pep_parse.settings import BASE_DIR


class PepParsePipeline:
    def __init__(self):
        self.statuses = defaultdict(int)

    def open_spider(self, spider):
        self.statuses.clear()

    def process_item(self, item, spider):
        try:
            key = item['status']
            self.statuses[key] += 1
        except DropItem:
            raise DropItem('Drop item')
        return item

    def close_spider(self, spider):
        time = dt.now().strftime('%Y-%m-%d_%H-%M-%S')
        path = BASE_DIR / 'results' / f'status_summary_{time}.csv'
        with open(path, mode='w', encoding='utf-8') as file:
            writer = csv.writer(
                file, dialect='unix', quoting=csv.QUOTE_NONE, escapechar=',')
            writer.writerows(
                (
                    ('Статус', 'Количество'),
                    *self.statuses.items(),
                    ('Total', sum(self.statuses.values()))
                ))
        self.statuses.clear()
