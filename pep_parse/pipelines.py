import csv
from collections import defaultdict
from datetime import datetime as dt
from pathlib import Path

BASE_DIR = Path(__file__).parent.parent


class PepParsePipeline:
    def open_spider(self, spider):
        self.results_dir = BASE_DIR / 'results'
        self.results_dir.mkdir(exist_ok=True)
        self.status_summary = defaultdict(int)

    def process_item(self, item, spider):
        self.status_summary[item['status']] += 1
        return item

    def close_spider(self, spider):
        pep_total = sum(self.status_summary.values())
        time_stamp = dt.now().strftime('%Y-%m-%d_%H-%M-%S')
        filename = f'status_summary_{time_stamp}.csv'
        filepath = f'{self.results_dir}/{filename}'

        with open(filepath, mode='w', encoding='utf-8', newline='') as f:
            headers = ('Статус', 'Количество')
            writer = csv.writer(f)
            writer.writerow(headers)
            writer.writerows(sorted(self.status_summary.items()))
            writer.writerow(('Total', pep_total))
