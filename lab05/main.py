from logstats import count_levels, top_errors, format_report

filename = input().strip()

log_lines = []
with open(filename, encoding="utf-8") as log:
    for line in log:
        log_lines.append(line)

counts = count_levels(log_lines)
errors = top_errors(log_lines, 3)

total = sum(counts.values())
error_count = counts.get("ERROR", 0)
broken_count = counts.get("BROKEN", 0)

print(total, error_count, broken_count, sep='\n')

report = format_report(counts, errors)

with open("report.txt", "w", encoding="utf-8") as out:
    out.write(report)
