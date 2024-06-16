import argparse

parser = argparse.ArgumentParser()
periods = ['day', 'week', 'month', 'year']
for p in periods:
    parser.add_argument(f'--per-{p}', type=int)
    
parser.add_argument('--get-by', choices=['day', 'month', 'year'], default='day')
args = parser.parse_args()

total = 0

if args.per_day is not None:
    total += args.per_day
if args.per_week is not None:
    total += args.per_week/7
if args.per_month is not None:
    total += args.per_month/30
if args.per_year is not None:
    total += args.per_year/360

match args.get_by:
    case 'day':
        print(int(total))
    case 'month':
        print(int(total*30))
    case 'year':
        print(int(total*360))