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
        self.pep_total = 0

    def process_item(self, item, spider):
        self.status_summary[item['status']] += 1
        self.pep_total += 1
        return item

    def close_spider(self, spider):
        time_stamp = dt.now().strftime("%Y-%m-%d_%H-%M-%S")
        filename = f'status_summary_{time_stamp}.csv'
        filepath = f'{self.results_dir}/{filename}'

        with open(filepath, mode='w', encoding='utf-8', newline='') as f:
            fieldnames = ['Статус', 'Количество']
            writer = csv.DictWriter(f, fieldnames=fieldnames)
            writer.writeheader()
            for status, amount in self.status_summary.items():
                writer.writerow({'Статус': status, 'Количество': amount})
            f.write(f'Total,{self.pep_total}\n')
