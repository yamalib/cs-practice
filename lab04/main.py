import sys
from stats import average_by_city, read_valid, warmest_city

lines = sys.stdin.read().splitlines()

valid_records = read_valid(lines)
skipped_count = len(lines) - len(valid_records)

print(len(valid_records))
print(skipped_count)
print(average_by_city(valid_records)[warmest_city(valid_records)])
