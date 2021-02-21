from collections import defaultdict
import csv
from io import TextIOWrapper
from urllib.request import urlopen

holidays = defaultdict(list)
with urlopen('https://www8.cao.go.jp/chosei/shukujitsu/syukujitsu.csv') as f:
    if f.status == 200:
        for row in csv.DictReader(TextIOWrapper(f, encoding='cp932', newline='')):
            holidays[row['国民の祝日・休日名称']].append(row['国民の祝日・休日月日'])
    else:
        raise 'Something was wrong'

print('---')
print('events:')
for name, days in holidays.items():
    times = [f'start: {d.replace("/", "-")}' for d in days]
    print(f'  "{name}": {{ color: "red", times: [{", ".join(times)}] }}')
print('---')
