import sys
from stats import parse_record, average_by_city

lines = sys.stdin.read().splitlines()
valid_records = []
parsed_count = 0
skipped_count = 0

for line in lines:
    if not line.strip():
        continue
try:
    record = parse_record(line)
    valid_records.append(record)
    parsed_count += 1
except ValueError:
    skipped_count += 1

print(parsed_count)
print(skipped_count)

if valid_records:
    averages = average_by_city(valid_records)
    max_avg_temp = max(averages.values())
    print(f"{max_avg_temp:.1f}")
else:
    print("0.0")
